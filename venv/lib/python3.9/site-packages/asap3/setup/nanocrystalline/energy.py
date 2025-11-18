from asap3.optimize import FIRE
from asap3.md.nptberendsen import Inhomogeneous_NPTBerendsen
from ase import units


def minimize_energy(atoms, nstep, pressure_interval=10, bulkmodulus = 140e9/1e5):
    """Helper function for minimizing the energy of a nanocrystalline structure.

    It minimizes the energy while eliminating the diagonal components of the stress.
    The atomic positions are optimized using the FIRE algorithm and the stress
    is minimized using the Inhomogeneous_Berendsen algorithm.

    Parameters:

    atoms: The atoms object to be energy-minimized.

    nsteps: Number of time steps in the FIRE algorithm

    pressure_interval=10: (optional) How often to call the stress minimizer.

    bulkmodulus=1.4e6: (optional).  The bulk modulus (in bar !!!) used by the
    stress optimizer.  This value is for Cu and is useful for all metals.
    The value is uncritical, but the order of magnitude should be reasonable. 
    """
    dyn = FIRE(atoms)
    unstress = Inhomogeneous_NPTBerendsen(atoms, 50*units.fs, 0,
                                          taup=5000*units.fs,
                                          compressibility=1/bulkmodulus)
    dyn.attach(unstress.scale_positions_and_cell, interval=10)
    dyn.run(steps=nstep)


