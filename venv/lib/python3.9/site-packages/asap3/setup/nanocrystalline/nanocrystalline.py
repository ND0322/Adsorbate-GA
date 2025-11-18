from ase.lattice.cubic import FaceCenteredCubic
from .helpers import create_atoms
import numpy as np


def make_nanocrystal(size, centres, rotations, min_dist=2.0, unit=None,
                     symbol=None, latticeconstant=None):
    """Create a nanocrystalline sample.

    Parameters:
      size:      Size of the system, in Angstrom (either a number or three numbers).
      centres:   Positions of grains in scaled coordinates.
      rotations: Rotation matrices for the grains.

      min_dist (optional):
                 If two atoms are closer than this distance, one of them is removed
                 (default: 2.0).

    In addition, either the 'unit' or the 'symbol' parameter must be specified.
      unit (optional):
                 A unit cell for building the crystals (Atoms object).
                 MUST be orthorhombic!
      symbol (optional):
                 If unit is None, then an FCC crystal of this element is used.
      latticeconstant (optional):
                 If symbol is specified, this overrides the default lattice constant.
    """

    assert type(size) == float or type(size) == list
    if type(size) == float:
        size = np.array([size, size, size])
    elif type(size) == list:
        size = np.array(size)
    assert size.shape == (3,)
    assert len(centres) == len(rotations)
    centres *= size
    if unit is None:
        unit = FaceCenteredCubic(symbol=symbol, size=(1,1,1), pbc=True,
                                 latticeconstant=latticeconstant)

    return create_atoms(centres, rotations, unit, size, min_dist)

