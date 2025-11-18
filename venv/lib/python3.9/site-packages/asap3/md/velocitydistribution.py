# VelocityDistributions.py -- set up a velocity distribution

"""Module for setting up e.g. Maxwell-Boltzmann velocity distributions.

Currently, only one function is defined, MaxwellBoltzmannDistribution,
which sets the momenta of a list of atoms according to a
Maxwell-Boltzmann distribution at a given temperature.
"""

import numpy as np
import asap3.mpi
from ase.md.velocitydistribution import _maxwellboltzmanndistribution
from ase.md.velocitydistribution import ZeroRotation as _ZeroRotation
from ase.md.md import process_temperature
from ase import units

def MaxwellBoltzmannDistribution(atoms, temp=None, *, temperature_K=None,
                                     force_temp=False, rng=None):
    """Sets the momenta to a Maxwell-Boltzmann distribution.

    Parameters:

    atoms: Atoms object
        The atoms.  Their momenta will be modified.

    temp: float (deprecated)
        The temperature in eV.  Deprecated, used temperature_K instead.

    temperature_K: float
        The temperature in Kelvin.

    force_temp: bool (optinal, default: False)
        If True, random the momenta are rescaled so the kinetic energy is 
        exactly 3/2 N k T.  This is a slight deviation from the correct
        Maxwell-Boltzmann distribution.

    rng: Numpy RNG (optional)
        Random number generator.  Default: numpy.random
    """
    temp = units.kB * process_temperature(temp, temperature_K, 'eV')

    momenta = _maxwellboltzmanndistribution(atoms.get_masses(),
                                                temp=temp,
                                                communicator='serial',
                                                rng=rng)
    atoms.set_momenta(momenta)
    if force_temp:
        force_temperature(atoms, temp, 'eV')

def Stationary(atoms, preserve_temperature=True):
    "Sets the center-of-mass momentum to zero."

    # Save initial temperature
    temp0 = atoms.get_temperature()

    p = atoms.get_momenta()
    p0 = np.sum(p, 0)
    # We should add a constant velocity, not momentum, to the atoms
    m = atoms.get_masses()
    mtot = np.sum(m)
    if getattr(atoms, "parallel", False):
        data = np.zeros(4, float)
        data[:3] = p0
        data[3] = mtot
        asap3.mpi.world.sum(data)
        p0 = data[:3]
        mtot = data[3]
    v0 = p0/mtot
    p -= v0*m[:,np.newaxis]
    atoms.set_momenta(p)

    if preserve_temperature:
        force_temperature(atoms, temp0)

# We cannot just use the ASE version of ZeroTemperature, as it is calling force_temperature,
# which would then be the ASE version and not the Asap version.
def ZeroRotation(atoms, preserve_temperature=True):
    "Sets the total angular momentum to zero by counteracting rigid rotations."

    # Save initial temperature
    temp0 = atoms.get_temperature()
    _ZeroRotation(atoms, preserve_temperature=False)
    if preserve_temperature:
        force_temperature(atoms, temp0)

def force_temperature(atoms, temperature, unit="K"):
    """ force (nucl.) temperature to have a precise value

    Parameters:
    atoms: ase.Atoms
        the structure
    temperature: float
        nuclear temperature to set
    unit: str
        'K' or 'eV' as unit for the temperature
    """

    eps_temp = 1e-12  # define a ``zero'' temperature to avoid divisions by zero

    if unit == "K":
        E_temp = temperature * units.kB
    elif unit == "eV":
        E_temp = temperature
    else:
        raise ValueError(f"Unit '{unit}' is not supported, use 'K' or 'eV'.")

    if temperature > eps_temp:
        E_kin0 = atoms.get_kinetic_energy() / atoms.get_global_number_of_atoms() / 1.5
        gamma = E_temp / E_kin0
    else:
        gamma = 0.0
    atoms.set_momenta(atoms.get_momenta() * np.sqrt(gamma))

