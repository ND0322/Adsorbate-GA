from ase.md.nose_hoover_chain import NoseHooverChainNVT as _NoseHooverChainNVT
from ase.md.nose_hoover_chain import NoseHooverChainThermostat as _NoseHooverChainThermostat
from ase.md.nose_hoover_chain import IsotropicMTKNPT as _IsotropicMTKNPT

import asap3.mpi
import ase
import numpy as np

class NoseHooverChainNVT(_NoseHooverChainNVT):
    def __init__(
        self,
        atoms: ase.Atoms,
        timestep: float,
        temperature_K: float,
        tdamp: float,
        tchain: int = 3,
        tloop: int = 1,
        communicator = asap3.mpi.world,
        **kwargs,
    ):
        # Replace parent's __init__, but chain to grandparent.
        super(_NoseHooverChainNVT, self).__init__(
            atoms=atoms, 
            timestep=timestep,
            **kwargs
        )
        self.comm = communicator
        if ase.__version__ < '3.25.0':
            raise RuntimeError('ASE too old.  NoseHooverChainNVT requires ASE 3.23.0.')
        
        num_atoms = self.atoms.get_global_number_of_atoms()
        self._thermostat = Asap_NoseHooverChainThermostat(
            num_atoms_global=num_atoms,
            communicator=communicator,
            masses=self.masses,
            temperature_K=temperature_K,
            tdamp=tdamp,
            tchain=tchain,
            tloop=tloop,
        )
        

        # The following variables are updated during self.step()
        # and synced with atoms before/after each force calculation.
        self._q = self.atoms.get_positions()
        self._p = self.atoms.get_momenta()

    def _get_forces(self) -> np.ndarray:
        f = super()._get_forces()
        # Sync internal variables as atoms may have migrated.
        self._p = self.atoms.get_momenta()
        self._q = self.atoms.get_positions()
        self.masses = self.atoms.get_masses()
        self.masses.shape = (-1, 1)
        self._thermostat.set_masses(self.masses)
        return f

class Asap_NoseHooverChainThermostat(_NoseHooverChainThermostat):
    def __init__(self, communicator, **kwargs):
        super().__init__(**kwargs)
        self.comm = communicator

    def set_masses(self, m):
        self._masses = m

    def _integrate_p_eta_j(self, p: np.ndarray, j: int, 
                           delta2: float, delta4: float) -> None:
        if j < self._tchain - 1:
            self._p_eta[j] *= np.exp(
                -delta4 * self._p_eta[j + 1] / self._Q[j + 1]
            )

        if j == 0:
            # Change compared to ASE
            p2overmass = np.sum(p**2 / self._masses)
            p2overmass = self.comm.sum(p2overmass)
            g_j = p2overmass - 3 * self._num_atoms_global * self._kT
        else:
            g_j = self._p_eta[j - 1] ** 2 / self._Q[j - 1] - self._kT
        self._p_eta[j] += delta2 * g_j

        if j < self._tchain - 1:
            self._p_eta[j] *= np.exp(
                -delta4 * self._p_eta[j + 1] / self._Q[j + 1]
            )

class IsotropicMTKNPT(_IsotropicMTKNPT):
    def __init__(
        self,
        atoms: ase.Atoms,
        timestep: float,
        temperature_K: float,
        pressure_au: float,
        tdamp: float,
        pdamp: float,
        tchain: int = 3,
        pchain: int = 3,
        tloop: int = 1,
        ploop: int = 1,
        communicator = asap3.mpi.world,
        **kwargs,
    ):
        """
        Parameters
        ----------
        atoms: ase.Atoms
            The atoms object.
        timestep: float
            The time step in ASE time units.
        temperature_K: float
            The target temperature in K.
        pressure_au: float
            The external pressure in eV/Å^3.
        tdamp: float
            The characteristic time scale for the thermostat in ASE time units.
            Typically, it is set to 100 times of `timestep`.
        pdamp: float
            The characteristic time scale for the barostat in ASE time units.
            Typically, it is set to 1000 times of `timestep`.
        tchain: int
            The number of thermostat variables in the Nose-Hoover thermostat.
        pchain: int
            The number of barostat variables in the MTK barostat.
        tloop: int
            The number of sub-steps in thermostat integration.
        ploop: int
            The number of sub-steps in barostat integration.
        **kwargs : dict, optional
            Additional arguments passed to :class:~ase.md.md.MolecularDynamics
            base class.
        """
        super().__init__(
            atoms=atoms,
            timestep=timestep,
            temperature_K=temperature_K,
            pressure_au=pressure_au,
            tdamp=tdamp,
            pdamp=pdamp,
            tchain=tchain,
            pchain=pchain,
            tloop=tloop,
            ploop=ploop,
            **kwargs,
        )
        self.comm = communicator

        # Replace the thermostat with Asap version.  The barostat is OK.
        num_atoms_global = self.atoms.get_global_number_of_atoms()
        self._thermostat = Asap_NoseHooverChainThermostat(
            communicator=communicator,
            num_atoms_global=num_atoms_global,
            masses=self.masses,
            temperature_K=temperature_K,
            tdamp=tdamp,
            tchain=tchain,
            tloop=tloop,
        )

    def _get_forces(self) -> np.ndarray:
        f = super()._get_forces()
        # Sync internal variables as atoms may have migrated.
        self._p = self.atoms.get_momenta()
        self._q = self.atoms.get_positions()
        self.masses = self.atoms.get_masses()
        self.masses.shape = (-1, 1)
        self._thermostat.set_masses(self.masses)
        return f

    def _integrate_p_cell(self, delta: float) -> None:
        """Integrate exp(i * L_(epsilon, 2) * delta)"""
        pressure = self._get_pressure()
        volume = self._get_volume()
        p2overmass = np.sum(self._p**2 / self.masses)
        p2overmass = self.comm.sum(p2overmass)
        G = (
            3 * volume * (pressure - self._pressure_au)
            + p2overmass / self.atoms.get_global_number_of_atoms()
        )
        self._p_eps += delta * G
