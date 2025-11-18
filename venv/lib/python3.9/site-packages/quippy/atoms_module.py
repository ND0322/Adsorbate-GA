"""
Module atoms_module


Defined at Atoms.fpp lines 140-2958

An atoms object contains atomic numbers, all dynamical variables
and connectivity information for all the atoms in the simulation cell.
It is initialised like this:
>           call initialise(MyAtoms,N,lattice)
where 'N' is the number of atoms to allocate space for and 'lattice' is a $3\times3$
matrix of lattice vectors given as column vectors, so that lattice(:,i) is the i-th lattice vector.

Atoms also contains a Connection object, which stores distance information about
the atom neighbours after 'calc_connect' has been called. Rather than using a minimum
image convention, all neighbours are stored up to a radius of 'cutoff', including images.

"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy

_arrays = {}
_objs = {}

def copy_without_connect(self, from_, properties=None, properties_array=None, error=None):
    """
    copy_without_connect(self, from_[, properties, properties_array, error])
    
    
    Defined at Atoms.fpp lines 614-652
    
    Parameters
    ----------
    to : Atoms
    from_ : Atoms
    properties : str
    properties_array : str array
    error : int
    
    Make a copy of the atoms object 'from' without including
    connectivity information. Useful for saving the state of a
    dynamical simulation without incurring too great a memory
    cost.
    """
    quippy._quippy.f90wrap_atoms_copy_without_connect(to=self._handle, from_=from_._handle, properties=properties, \
        properties_array=properties_array, error=error)

def cosine(self, i, j, k, error=None):
    """
    cosine = cosine(self, i, j, k[, error])
    
    
    Defined at Atoms.fpp lines 1568-1580
    
    Parameters
    ----------
    this : Atoms
    i : int
    j : int
    k : int
    error : int
    
    Returns
    -------
    cosine : float
    
    Cosine of the angle j--i--k
    """
    cosine = quippy._quippy.f90wrap_cosine(this=self._handle, i=i, j=j, k=k, error=error)
    return cosine

def cosine_neighbour(self, i, n, m):
    """
    cosine_neighbour = cosine_neighbour(self, i, n, m)
    
    
    Defined at Atoms.fpp lines 1587-1599
    
    Parameters
    ----------
    this : Atoms
    i : int
    n : int
    m : int
    
    Returns
    -------
    cosine_neighbour : float
    
    Cosine of the angle n--i--m where {$n,m$} are the {$n$th, $m$th} neighbours of i
    """
    cosine_neighbour = quippy._quippy.f90wrap_cosine_neighbour(this=self._handle, i=i, n=n, m=m)
    return cosine_neighbour

def direction_cosines(self, i, j, shift):
    """
    direction_cosines = direction_cosines(self, i, j, shift)
    
    
    Defined at Atoms.fpp lines 1608-1613
    
    Parameters
    ----------
    this : Atoms
    i : int
    j : int
    shift : int array
    
    Returns
    -------
    direction_cosines : float array
    
    Given two atoms $i$ and $j$ and a shift returns the direction
    cosines of the differnece vector from $i$ to $j$.
    """
    direction_cosines = quippy._quippy.f90wrap_direction_cosines(this=self._handle, i=i, j=j, shift=shift)
    return direction_cosines

def direction_cosines_min_image(self, i, j, error=None):
    """
    direction_cosines_min_image = direction_cosines_min_image(self, i, j[, error])
    
    
    Defined at Atoms.fpp lines 1616-1626
    
    Parameters
    ----------
    this : Atoms
    i : int
    j : int
    error : int
    
    Returns
    -------
    direction_cosines_min_image : float array
    
    Direction cosines of the difference vector from $i$ to $j$
    """
    direction_cosines_min_image = quippy._quippy.f90wrap_direction_cosines_min_image(this=self._handle, i=i, j=j, \
        error=error)
    return direction_cosines_min_image

def set_map_shift(self, error=None):
    """
    set_map_shift(self[, error])
    
    
    Defined at Atoms.fpp lines 1628-1644
    
    Parameters
    ----------
    this : Atoms
    error : int
    
    """
    quippy._quippy.f90wrap_set_map_shift(this=self._handle, error=error)

def make_lattice(a, b=None, c=None, alpha=None, beta=None, gamma=None, error=None):
    """
    lattice = make_lattice(a[, b, c, alpha, beta, gamma, error])
    
    
    Defined at Atoms.fpp lines 1663-1713
    
    Parameters
    ----------
    a : float
    b : float
    c : float
    alpha : float
    beta : float
    gamma : float
    error : int
    
    Returns
    -------
    lattice : float array
    
    Make a matrix of lattice vectors from the lengths 'a','b','c'
    and the angles 'alpha', 'beta' and 'gamma'.
    One length must be supplied. Any missing angle is assumed to be 90 degrees
    and any missing length is assumed to be 'a'.
    The vectors are created in a right-handed order.
    """
    lattice = quippy._quippy.f90wrap_make_lattice(a=a, b=b, c=c, alpha=alpha, beta=beta, gamma=gamma, error=error)
    return lattice

def get_lattice_params(lattice, a=None, b=None, c=None, alpha=None, beta=None, gamma=None):
    """
    get_lattice_params(lattice[, a, b, c, alpha, beta, gamma])
    
    
    Defined at Atoms.fpp lines 1719-1732
    
    Parameters
    ----------
    lattice : float array
    a : float
    b : float
    c : float
    alpha : float
    beta : float
    gamma : float
    
    Opposite of Make_Lattice.
    Given a lattice, return a,b,c,alpha,beta and gamma(if needed)
    """
    quippy._quippy.f90wrap_get_lattice_params(lattice=lattice, a=a, b=b, c=c, alpha=alpha, beta=beta, gamma=gamma)

def centre_of_mass(self, index_list=None, mask=None, origin=None, error=None):
    """
    com = centre_of_mass(self[, index_list, mask, origin, error])
    
    
    Defined at Atoms.fpp lines 1744-1812
    
    Parameters
    ----------
    at : Atoms
    index_list : int array
    mask : bool array
    origin : int
    error : int
    
    Returns
    -------
    com : float array
    
    Calculate the centre of mass of an atoms object, using the closest images to the origin atom,
    or first atom if this is not specified.  If origin is zero, use actual position, not minimum image.
    If an 'index_list' is present, just calculate it for that subset of atoms(then the origin atom is
    the first in this list unless it is specified separately).
    
    Note: Because the origin can be specified separately it need not be one of the atoms in the
    calculation.
    """
    com = quippy._quippy.f90wrap_centre_of_mass(at=self._handle, index_list=index_list, mask=mask, origin=origin, \
        error=error)
    return com

def prop_names_string(self, with_types=None, error=None):
    """
    prop_names_string = prop_names_string(self[, with_types, error])
    
    
    Defined at Atoms.fpp lines 1988-1995
    
    Parameters
    ----------
    this : Atoms
    with_types : bool
    error : int
    
    Returns
    -------
    prop_names_string : str
    
    """
    prop_names_string = quippy._quippy.f90wrap_prop_names_string(this=self._handle, with_types=with_types, error=error)
    return prop_names_string

def termination_bond_rescale(z1, z2):
    """
    termination_bond_rescale = termination_bond_rescale(z1, z2)
    
    
    Defined at Atoms.fpp lines 2046-2050
    
    Parameters
    ----------
    z1 : int
    z2 : int
    
    Returns
    -------
    termination_bond_rescale : float
    
    Calculates the rescale ratio of a Z1--H bond
    generate from a Z1--Z2 bond.
    """
    termination_bond_rescale = quippy._quippy.f90wrap_termination_bond_rescale(z1=z1, z2=z2)
    return termination_bond_rescale

def coalesce_in_one_periodic_image(self, seed=None, is_periodic=None, error=None):
    """
    coalesce_in_one_periodic_image(self[, seed, is_periodic, error])
    
    
    Defined at Atoms.fpp lines 2197-2308
    
    Parameters
    ----------
    this : Atoms
    seed : int
    is_periodic : bool array
    error : int
    
    move atoms around following neighbor list bonds so that all are in the same periodic image
    (that of 'seed', if present)
    poorly tested, especially for situations where not all atoms are in one connected clump
    probably needs a better subroutine name
    """
    quippy._quippy.f90wrap_coalesce_in_one_periodic_image(this=self._handle, seed=seed, is_periodic=is_periodic, \
        error=error)

def closest_atom(self, r, cell_image_na, cell_image_nb, cell_image_nc, mask=None, dist=None, diff=None, error=None):
    """
    closest_atom = closest_atom(self, r, cell_image_na, cell_image_nb, cell_image_nc[, mask, dist, diff, error])
    
    
    Defined at Atoms.fpp lines 2310-2378
    
    Parameters
    ----------
    this : Atoms
    r : float array
    cell_image_na : int
    cell_image_nb : int
    cell_image_nc : int
    mask : bool array
    dist : float
    diff : float array
    error : int
    
    Returns
    -------
    closest_atom : int
    
    """
    closest_atom = quippy._quippy.f90wrap_closest_atom(this=self._handle, r=r, cell_image_na=cell_image_na, \
        cell_image_nb=cell_image_nb, cell_image_nc=cell_image_nc, mask=mask, dist=dist, diff=diff, error=error)
    return closest_atom

def is_nearest_neighbour_abs_index(self, i, j, alt_connect=None):
    """
    is_nearest_neighbour_abs_index = is_nearest_neighbour_abs_index(self, i, j[, alt_connect])
    
    
    Defined at Atoms.fpp lines 2673-2688
    
    Parameters
    ----------
    this : Atoms
    i : int
    j : int
    alt_connect : Connection
    
    Returns
    -------
    is_nearest_neighbour_abs_index : bool
    
    Test if an atom 'j' is one of 'i's nearest neighbours
    """
    is_nearest_neighbour_abs_index = quippy._quippy.f90wrap_is_nearest_neighbour_abs_index(this=self._handle, i=i, j=j, \
        alt_connect=None if alt_connect is None else alt_connect._handle)
    return is_nearest_neighbour_abs_index

def is_nearest_neighbour(self, i, n, alt_connect=None):
    """
    is_nearest_neighbour = is_nearest_neighbour(self, i, n[, alt_connect])
    
    
    Defined at Atoms.fpp lines 2691-2701
    
    Parameters
    ----------
    this : Atoms
    i : int
    n : int
    alt_connect : Connection
    
    Returns
    -------
    is_nearest_neighbour : bool
    
    Test if an atom's $n$th neighbour is one if its nearest neighbours
    """
    is_nearest_neighbour = quippy._quippy.f90wrap_is_nearest_neighbour(this=self._handle, i=i, n=n, alt_connect=None if \
        alt_connect is None else alt_connect._handle)
    return is_nearest_neighbour

def undo_pbc_jumps(self, persistent=None):
    """
    undo_pbc_jumps(self[, persistent])
    
    
    Defined at Atoms.fpp lines 2823-2846
    
    Parameters
    ----------
    at : Atoms
    persistent : bool
    
    undo pbc jumps, assuming nearest periodic image, with or without persistent atoms object
    without persistent atoms object, global storage is used, and calling on multiple trajcetories
    interspersed will not work
    """
    quippy._quippy.f90wrap_undo_pbc_jumps(at=self._handle, persistent=persistent)

def undo_com_motion(self, persistent=None):
    """
    undo_com_motion(self[, persistent])
    
    
    Defined at Atoms.fpp lines 2851-2883
    
    Parameters
    ----------
    at : Atoms
    persistent : bool
    
    undo center of mass motion, with or without persistent atoms object
    without persistent atoms object, global storage is used, and calling on multiple trajcetories
    interspersed will not work
    """
    quippy._quippy.f90wrap_undo_com_motion(at=self._handle, persistent=persistent)

def calc_msd(self, mask=None, reset_msd=None, persistent=None):
    """
    calc_msd(self[, mask, reset_msd, persistent])
    
    
    Defined at Atoms.fpp lines 2889-2926
    
    Parameters
    ----------
    at : Atoms
    mask : bool array
    reset_msd : bool
    persistent : bool
    
    calculate mean squared displacement, with or without persistent atoms object
    without persistent atoms object, global storage is used, and calling on multiple trajcetories
    interspersed will not work.
    usually desirable to call undo_pbc_jumps and undo_CoM_motion first
    """
    quippy._quippy.f90wrap_calc_msd(at=self._handle, mask=mask, reset_msd=reset_msd, persistent=persistent)

def fake_smooth_pos(self, mix, persistent=None):
    """
    fake_smooth_pos(self, mix[, persistent])
    
    
    Defined at Atoms.fpp lines 2928-2958
    
    Parameters
    ----------
    at : Atoms
    mix : float
    persistent : bool
    
    """
    quippy._quippy.f90wrap_fake_smooth_pos(at=self._handle, mix=mix, persistent=persistent)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "atoms_module".')

for func in _dt_array_initialisers:
    func()
