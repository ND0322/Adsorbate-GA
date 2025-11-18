from ase.lattice.cubic import FaceCenteredCubic
from asap3.setup.multidislocation import random_dislocations
from asap3.setup.dislocation import Dislocation
import ase.data
from .helpers import create_atoms
import numpy as np

def make_dislocated_nanocrystal(size, centres, rotations, 
                                dislocationdensity,
                                symbol, latticeconstant=None,
                                min_dist=2.0,
                                multiproc=False):
    """Create a nanocrystalline sample with pre-existing dislocation density.

    Parameters:
      size:      Size of the system, in Angstrom (either a number or three numbers).
      centres:   Positions of grains in scaled coordinates.
      rotations: Rotation matrices for the grains.
      dislocationdensity:
                 Dislocation density in m^-2
      symbol:    Chemical symbol or atomic number.
      latticeconstant (optional):
                 Overrides the default lattice constant.
      min_dist (optional):
                 If two atoms are closer than this distance, one of them is removed
                 (default: 2.0).
      multiproc: Use all cores to calculate dislocation strain fields (default: False).
    """

    assert type(size) == float or type(size) == list
    if type(size) == float:
        size = np.array([size, size, size])
    elif type(size) == list:
        size = np.array(size)
    assert size.shape == (3,)
    assert len(centres) == len(rotations)
    centres *= size
    if latticeconstant is None:
        # Get lattice constant from the element
        if isinstance(symbol, int):
            z = symbol
        else:
            z = ase.data.atomic_numbers[symbol]
        if ase.data.reference_states[z]['symmetry'] != 'fcc':
            raise ValueError(f"Cannot extract FCC lattice constant from non-fcc element ({symbol})")
        latticeconstant = ase.data.reference_states[z]['a']
    unit = FaceCenteredCubic(symbol=symbol, size=(1,1,1), pbc=True,
                             latticeconstant=latticeconstant)
    # Create a dislocation field for each grain.  The radius of the dislocation
    # field should be half the sidelength of the overall system
    dislocationfields = []
    for i in range(len(centres)):
        disloc_params = random_dislocations(max(size)/2.0, dislocationdensity)
        n_dislocs = len(disloc_params)
        dislocs = [Dislocation(point, line, latticeconstant * burgers)
                   for point, burgers, line in disloc_params]
        dislocationfields.append(dislocs)

    return create_atoms(centres, rotations, unit, size, min_dist,
                        dislocations=dislocationfields, multiproc=multiproc)

