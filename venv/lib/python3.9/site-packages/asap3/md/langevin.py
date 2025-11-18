"""Langevin dynamics class."""

import numpy as np
from numpy.random import standard_normal, randint
import asap3
import ase
import ase.units
from asap3.md.md import ParallelMolDynMixin
from ase.md.md import MolecularDynamics
from ase.md.langevin import Langevin as _Langevin_ASE
import asap3.constraints
from ase.parallel import world
import sys
import numbers

class ASE_Langevin(_Langevin_ASE, ParallelMolDynMixin):
    def __init__(self, atoms, timestep, temperature=None, friction=None, fixcm=True,
                     *, temperature_K=None, **kwargs):
        ParallelMolDynMixin.__init__(self, "Langevin", atoms)
        _Langevin_ASE.__init__(self, atoms, timestep, temperature=temperature,
                               friction=friction, temperature_K=temperature_K,
                               fixcm=fixcm, communicator=None, **kwargs)

    def run(self, steps):
        self.before_run()
        super().run(steps)
        self.after_run()

    def _get_com_velocity(self, velocity=None):
        """Return the center of mass velocity."""
        if velocity is None:
            velocity = self.v  # Compatibility with older ASE
        if getattr(self.atoms, "parallel", False):
            data = np.zeros(4)
            data[:3] = np.dot(self.masses.flatten(), velocity)
            data[3] = self.masses.sum()
            self.atoms.comm.sum(data)
            return data[:3] / data[3]
        else:
            return np.dot(self.masses.flatten(), velocity) / self.masses.sum()

    temp = property(lambda s: s.get("temp"), lambda s, x: s.set("temp", x))
    fr = property(lambda s: s.get("fr"), lambda s, x: s.set("fr", x))
    masses = property(lambda s: s.get("masses"), lambda s, x: s.set("masses", x))
    c1 = property(lambda s: s.get("c1"), lambda s, x: s.set("c1", x))
    c2 = property(lambda s: s.get("c2"), lambda s, x: s.set("c2", x))
    c3 = property(lambda s: s.get("c3"), lambda s, x: s.set("c3", x))
    c4 = property(lambda s: s.get("c4"), lambda s, x: s.set("c4", x))
    c5 = property(lambda s: s.get("c5"), lambda s, x: s.set("c5", x))
    v = property(lambda s: s.get("v"), lambda s, x: s.set("v", x))
    rnd_pos = property(lambda s: s.get("rnd_pos"), lambda s, x: s.set("rnd_pos", x))
    rnd_vel = property(lambda s: s.get("rnd_vel"), lambda s, x: s.set("rnd_vel", x))

class Langevin_Fast(MolecularDynamics, ParallelMolDynMixin):
    def __init__(self, atoms, timestep, temperature=None, friction=None, fixcm=True,
                     *, temperature_K=None, 
                     trajectory=None, logfile=None, loginterval=1, seed=None):
        temperature = ase.units.kB * self._process_temperature(temperature, temperature_K, 'eV')
        ParallelMolDynMixin.__init__(self, "Langevin", atoms)
        self._uselocaldata = False # Need to store on atoms for serial simul too.
        self.calculator = atoms.calc
        if not atoms.has('momenta'):
            atoms.set_momenta(np.zeros((len(atoms), 3), float))
        self.atoms_have_constraints = len(atoms.constraints)
        if self.atoms_have_constraints:
            if len(atoms.constraints) != 1:
                raise RuntimeError("ASAP Langevin dynamics only support a single constraint.")
            constraint = atoms.constraints[0]
            if not isinstance(constraint, asap3.constraints.FixAtoms):
                raise RuntimeError("ASAP Langevin dynamics only support the ASAP FixAtoms constraint.")
            # Make all constants arrays by making friction an array
            friction = friction * np.ones(len(atoms))
            fixcm = False   # Unneccesary (and incompatible) when FixAtoms constraint used.
        if seed is None:
            seed = randint(1 << 30)
        elif isinstance(seed, np.random.SeedSequence):
            # Convert into a numeric seed for the Asap implementation.
            seed = seed.generate_state(1, dtype=np.uint64)
        assert isinstance(seed, numbers.Integral), "seed must be an int"
        self.asap_md = asap3._asap.Langevin(atoms, self.calculator, timestep,
                                            self.prefix+"sdpos", self.prefix+"sdmom",
                                            self.prefix+"c1", self.prefix+"c2",
                                            fixcm, seed)
        MolecularDynamics.__init__(self, atoms, timestep, trajectory,
                                   logfile, loginterval)
        self.temp = temperature
        self.frict = friction
        self.fixcm = fixcm  # will the center of mass be held fixed?
        self.communicator = None
        self.updatevars()

    def set_temperature(self, temperature=None, *, temperature_K=None):
        self.temp =  ase.units.kB * self._process_temperature(temperature, temperature_K, 'eV')
        self.updatevars()

    def set_friction(self, friction):
        self.frict = friction
        self.updatevars()

    def set_timestep(self, timestep):
        self.dt = timestep
        self.updatevars()

    def updatevars(self):
        dt = self.dt
        # If the friction is an array some other constants must be arrays too.
        self._localfrict = hasattr(self.frict, 'shape')
        lt = self.frict * dt
        masses = self.masses
        sdpos = dt * np.sqrt(self.temp / masses.reshape(-1) *
                             (2.0 / 3.0 - 0.5 * lt) * lt)
        sdpos.shape = (-1, 1)
        sdmom = np.sqrt(self.temp * masses.reshape(-1) * 2.0 * (1.0 - lt) * lt)
        sdmom.shape = (-1, 1)
        pmcor = np.sqrt(3.0) / 2.0 * (1.0 - 0.125 * lt)
        cnst = np.sqrt((1.0 - pmcor) * (1.0 + pmcor))

        act0 = 1.0 - lt + 0.5 * lt * lt
        act1 = (1.0 - 0.5 * lt + (1.0 / 6.0) * lt * lt)
        act2 = 0.5 - (1.0 / 6.0) * lt + (1.0 / 24.0) * lt * lt
        c1 = act1 * dt / masses.reshape(-1)
        c1.shape = (-1, 1)
        c2 = act2 * dt * dt / masses.reshape(-1)
        c2.shape = (-1, 1)
        c3 = (act1 - act2) * dt
        c4 = act2 * dt
        del act1, act2
        if self._localfrict:
            # If the friction is an array, so are these
            act0.shape = (-1, 1)
            c3.shape = (-1, 1)
            c4.shape = (-1, 1)
            pmcor.shape = (-1, 1)
            cnst.shape = (-1, 1)
        self.sdpos = sdpos
        self.sdmom = sdmom
        self.c1 = c1
        self.c2 = c2
        self.act0 = act0
        self.c3 = c3
        self.c4 = c4
        self.pmcor = pmcor
        self.cnst = cnst
        # Also works in parallel Asap:
        self.natoms = self.atoms.get_global_number_of_atoms() #GLOBAL number of atoms
        if len(self.atoms.constraints) == 1:
            # Process the FixAtoms constraint
            constr = self.atoms.constraints[0].index
            self.sdpos[constr] = 0.0
            self.sdmom[constr] = 0.0
            self.c1[constr] = 0.0
            self.c2[constr] = 0.0
            self.c3[constr] = 0.0
            self.c4[constr] = 0.0
            self.act0[constr] = 0.0
        if self._localfrict:
            self.asap_md.set_vector_constants(self.prefix+"act0", self.prefix+"c3",
                                              self.prefix+"c4", self.prefix+"pmcor",
                                              self.prefix+"cnst")
        else:
            self.asap_md.set_scalar_constants(self.act0, self.c3, self.c4,
                                              self.pmcor, self.cnst)

    def run(self, steps):
        assert(self.calculator is self.atoms.calc)
        if self.atoms.constraints or self.atoms_have_constraints:
            # Constraints may have been added, removed or changed
            self.updatevars()
        self.before_run()
        self.asap_md.run(steps, self.observers, self)
        self.after_run()
        self.atoms_have_constraints = len(self.atoms.constraints)

    def get_random(self, gaussian):
        return self.asap_md.get_random(gaussian)

    # Properties are not inherited, need to repeat them
    sdpos = property(lambda s: s.get("sdpos"), lambda s, x: s.set("sdpos", x))
    sdmom = property(lambda s: s.get("sdmom"), lambda s, x: s.set("sdmom", x))
    c1 = property(lambda s: s.get("c1"), lambda s, x: s.set("c1", x))
    c2 = property(lambda s: s.get("c2"), lambda s, x: s.set("c2", x))
    act0 = property(lambda s: s.get("act0"), lambda s, x: s.set("act0", x))
    c3 = property(lambda s: s.get("c3"), lambda s, x: s.set("c3", x))
    c4 = property(lambda s: s.get("c4"), lambda s, x: s.set("c4", x))
    pmcor = property(lambda s: s.get("pmcor"), lambda s, x: s.set("pmcor", x))
    cnst = property(lambda s: s.get("cnst"), lambda s, x: s.set("cnst", x))
    masses = property(lambda s: s.get("masses"), lambda s, x: s.set("masses", x))
    frict = property(lambda s: s.get("frict"), lambda s, x: s.set("frict", x))

def Langevin(atoms, *args, **kwargs):
    if (isinstance(atoms, ase.Atoms)
        and asap3.constraints.check_asap_constraints(atoms)
        and not kwargs.pop('forceASE', False)
       ):
        # Nothing prevents Asap optimization
        if world.rank == 0:
            sys.stderr.write("Using Asap-optimized C++-Langevin algorithm\n")
        return Langevin_Fast(atoms, *args, **kwargs)
    else:
        if world.rank == 0:
            sys.stderr.write("Using ASE-based Langevin algorithm\n")
        return ASE_Langevin(atoms, *args, **kwargs)
