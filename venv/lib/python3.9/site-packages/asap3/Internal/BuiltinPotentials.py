"""The potentials built into Asap."""

__docformat__ = "restructuredtext en"

from asap3.Internal.Builtins import _asap
from asap3.Internal.CheckArray import check_parameter_array, _ChkLJarray
import asap3

import numpy as np
import ase
import ase.calculators.emt
import ase.data
from ase.utils import basestring
from copy import copy
import sys

EMTParameters = _asap.EMTParameters
EMTDefaultParameters = _asap.EMTDefaultParameters
EMTRasmussenParameters = _asap.EMTRasmussenParameters
#EMTVariableParameters = _asap.EMTVariableParameters
#EMThcpParameters = _asap.EMThcpParameters

BrennerPotential = _asap.BrennerPotential

#IntVector = asap.IntVector
#DoubleVector = asap.DoubleVector


# class FullNeighborList(asap.NeighborList2):
#     "A full neighbor list object."
#     def __init__(self, atoms, *args):
#         asap.NeighborList2.__init__(self, atoms, *args)
#         self.EnableFullNeighborLists()
#         self.atoms = atoms  # Keep the atoms alive.
#         self.CheckAndUpdateNeighborList()

# class NeighborCellLocator(asap.NeighborCellLocator):
#     "A Neighbor list object."
#     def __init__(self, atoms, *args):
#         asap.NeighborCellLocator.__init__(self, atoms, *args)
#         self.atoms = atoms  # Keep the atoms alive.
#         self.CheckAndUpdateNeighborList()
    
# class NeighborList(asap.NeighborList2):
#     "A Neighbor list object."
#     def __init__(self, atoms, *args):
#         asap.NeighborList2.__init__(self, atoms, *args)
#         self.atoms = atoms  # Keep the atoms alive.
#         self.CheckAndUpdateNeighborList()

def get_cell_heights(atoms):
    "Get the heights of the unit cells (perpendicular to the surfaces)"
    heights = np.zeros(3)
    cell = atoms.get_cell()
    for i in range(3):
        direction = np.cross(cell[(i+1) % 3], cell[(i+2) % 3])
        heights[i] = abs(np.dot(cell[i], direction) / np.sqrt(np.dot(direction,direction)))
    return heights

def smallest_pbc_direction(atoms):
    smallest = 1.0e20  # Very big
    pbc = atoms.get_pbc()
    h = get_cell_heights(atoms)
    for i in range(3):
        if pbc[i] and h[i] < smallest:
            smallest = h[i]
    return smallest

class AsapPotential:
    """Mixin for all Asap potentials."""

    _stresscomp = np.array([[0, 5, 4], [5, 1, 3], [4, 3, 2]])

    def set_atoms_mixin(self, atoms):
        """Set the atoms.  This mixin fixes compatibility with ASE 3.18.0 and earlier."""
        if not hasattr(atoms, "get_global_number_of_atoms"):
            atoms.get_global_number_of_atoms = atoms.get_number_of_atoms

    def set_atoms(self, atoms, *args):
        """Set the atoms.  This default version fixes compatibility with ASE 3.18.0 and earlier."""
        self.set_atoms_mixin(atoms)
        # Now call the potential.
        super().set_atoms(atoms, *args)

    def get_stress(self, atoms):
        stress = self.get_virial(atoms)
        if not getattr(atoms, "_ase_handles_dynamic_stress", False):
            p = atoms.get_momenta()
            masses = atoms.get_masses()
            invmass = 1.0 / masses
            for alpha in range(3):
                for beta in range(alpha, 3):
                    stress[self._stresscomp[alpha,beta]] -= (p[:,alpha] * p[:,beta] * invmass).sum()
        stress /= atoms.get_volume()
        return stress

    def get_stresses(self, atoms):
        stresses = self.get_virials(atoms)
        if hasattr(self, 'get_atomic_volumes'):
            invvol = 1.0 / self.get_atomic_volumes()
        else:
            invvol = atoms.get_global_number_of_atoms() / atoms.get_volume()
        if not getattr(atoms, "_ase_handles_dynamic_stress", False):
            p = atoms.get_momenta()
            invmass = 1.0 / atoms.get_masses()
            for alpha in range(3):
                for beta in range(alpha, 3):
                    stresses[:,self._stresscomp[alpha,beta]] -= p[:,alpha] * p[:,beta] * invmass
        for i in range(6):
            stresses[:,i] *= invvol            
        return stresses

    def get_property(self, prop, atoms, allow_calculation=True):
        try:
            if (not allow_calculation and
                self.calculation_required(atoms, [prop])):
                return None
        except AttributeError:
            pass

        method = 'get_' + {'energy': 'potential_energy',
                           'magmom': 'magnetic_moment',
                           'magmoms': 'magnetic_moments',
                           'dipole': 'dipole_moment'}.get(prop, prop)
        try:
            result = getattr(self, method)(atoms)
        except AttributeError:
            raise asap3.PropertyNotImplementedError
        return result

    def get_name(self):
        return "asap3." + self._get_name()

    def get_neighborlist(self):
        """Return the neighbor locator"""
        return self._get_neighborlist()
    
    name = property(get_name, doc="Name of the potential")
    

class EMT(AsapPotential, _asap.EMT):
    """The Effective Medium Theory potential.

    Per default, the EMT potential uses standard parameters for the
    supported metals (Ni, Cu, Pd, Ag, Pt, Au).  If other parameters
    are desired, the relevant parameter provider can be provided as an
    optional argument.
    """
    def __init__(self, parameters=None, minimum_image=None, verbose=None):
        if parameters is None:
            parameters = EMTDefaultParameters()
        if verbose is None:
            verbose = _asap.verbose
        _asap.EMT.__init__(self, parameters, verbose)
        self.verbose = verbose
        self.absolute_max_cutoff = parameters.get_max_cutoff_beforeinit()
        self._set_atoms_called = False
        self.use_minimum_image = minimum_image
        
    def set_atoms(self, atoms, *args):
        self.set_atoms_mixin(atoms)
        if not self._set_atoms_called:
            if self.use_minimum_image is None:
                self.use_minimum_image = smallest_pbc_direction(atoms) >= 2.1 * self.absolute_max_cutoff
            if not self.use_minimum_image:
                #sys.stderr.write("Asap.EMT: Disabling minimum image convention.\n")
                self._use_imageatoms()
        self._set_atoms_called = True
        _asap.EMT.set_atoms(self, atoms, *args)

    def get_atomic_volumes(self):
        return self._get_atomic_volumes()

class MonteCarloEMT(AsapPotential, _asap.MonteCarloEMT):
    """The Effective Medium Theory potential optimized for Monte Carlo.

    Per default, the EMT potential uses standard parameters for the
    supported metals (Ni, Cu, Pd, Ag, Pt, Au).  If other parameters
    are desired, the relevant parameter provider can be provided as an
    optional argument.

    This version is optimized for Monte Carlo simulations, at the
    price of somewhat slower ordinary energy and force calculations
    and a larger memory footprint.  In addition, this version cannot
    be parallelized.
    """
    def __init__(self, parameters=None, verbose=None):
        if parameters is None:
            parameters = EMTDefaultParameters()
        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose
        _asap.MonteCarloEMT.__init__(self, parameters, verbose)

class EMT2013(AsapPotential, _asap.EMT2013):
    """The Effective Medium Theory version 2011 potential.
    
    Parameters must be provided as a dictionary, the keys are
    elements (atomic numbers or strings), the values are dictionaries
    with parameters.  The names of the parameters are 'eta2', 'lambda',
    'kappa', 'E0', 'V0', 'S0' and 'n0'.
    
    If no_new_elements is set to True, the user promises that no
    new elements are introduced after the first time the calculator
    is attached to an Atoms object.  Only elements present at that
    instance will be initialized.
    
    If no_new_elements is False (the default), all elements present
    in the parameters dictionary will be initialized.  This may cause
    a performance penalty as neighbor lists will be large enough to
    accommodate the largest atoms supported.
    """
    def __init__(self, parameters, no_new_elements=False, minimum_image=None, verbose=None):
        try:
            par_ver = parameters['Calculator']
        except KeyError:
            raise ValueError("Dictionary with parameters should contain a" +
                             " Calculator item - be careful not to use an " +
                             "obsolete parameter definition !!")
        if par_ver != "EMT2013_V1":
            raise ValueError("The parameters appear to be for a calculator " +
                             "of type " + par_ver + 
                             " (expected EMT2013_V1).")
        params = {}
        max_s0 = 0.0
        for k in parameters.keys():
            if k == "Calculator":
                continue  # Skip the version specification.
            if isinstance(k, basestring):
                z = ase.data.atomic_numbers[k]
            else:
                z = k
            params[z] = copy(parameters[k])
            params[z]['mass'] = ase.data.atomic_masses[z]
            s0 = params[z]['S0']
            if s0 > max_s0:
                max_s0 = s0
        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose
        _asap.EMT2013.__init__(self, params, no_new_elements, verbose)
        beta = 1.809399790563555  # ((16*pi/3)^(1./3.))/sqrt(2)
        self.maxcut = 0.5 * (np.sqrt(1.5) + np.sqrt(2.)) * np.sqrt(2.) * beta * max_s0 * 1.05
        self._set_atoms_called = False
        self.use_minimum_image = minimum_image
        
    def set_atoms(self, atoms, *args):
        self.set_atoms_mixin(atoms)
        if not self._set_atoms_called:
            if self.use_minimum_image is None:
                self.use_minimum_image = smallest_pbc_direction(atoms) >= 2.5 * self.maxcut
            if not self.use_minimum_image:
                #sys.stderr.write("Asap.EMT2013: Disabling minimum image convention.\n")
                self._use_imageatoms()
        self._set_atoms_called = True
        _asap.EMT2013.set_atoms(self, atoms, *args)

    def get_atomic_volumes(self):
        return self._get_atomic_volumes()


def EMT2011(parameters):
    """EMT2011 has been renamed EMT2013, please use the new version."""
    sys.stderr.write("\nASAP Warning: EMT2011 is deprecated, use EMT2013 instead.\n")
    return EMT2013(parameters)

class RGL(AsapPotential, _asap.RGL):
    """
    Calculator based on the RGL/Gupta semi empirical tight-binding potential.

    Parameters
    ----------
    elements: List of the elements that will be supported.

    The parameters can be given here as a dictionary with the form:
        {'Pt': [p, q, a, xi, r0], ('Pt','Y'): [...], ('Y','Y'): [...]}.

    p, q, a, xi, r0 (optional): The potential parameters listed in 2D arrays
    with each dimension equal to the number of elements. Only the upper
    triangular part is used. If there is only one element, then the
    parameters may be numbers.

    cutoff (optional): The distance at which the cutoff function should
    start given in nearest neighor distances. Default is 1.73.

    delta (optional): The length of the cutoff function given in nearest
    neighbor distances. Defauls is 0.15.

    The cutoff defaults are set to include the 3rd and not the 4th nearest
    neighors. The expected nearest neighbor distance is calculated based
    on the parameters.
    """

    def __init__(self, elements, p=None, q=None, a=None, xi=None, r0=None,
                 cutoff=1.73, delta=0.15, debug=False, verbose=None):
        # Check if parameters is given as a dictionary
        if isinstance(elements, dict):
            parameters = elements.copy()

            # Get elements
            elements = []
            elementmap = {}
            for key in parameters.keys():
                if isinstance(key, basestring):
                    symbols = [key]
                elif isinstance(key, tuple) and len(key) == 2:
                    symbols = list(key)
                else:
                    raise KeyError('Key must either be a string or a tuple with ' +
                                   'two elements.')
                for s in symbols:
                    if not s in elements:
                        elementmap[s] = len(elements)
                        elements.append(s)
            n = len(elements)

            # Get parameters
            p = np.zeros((n, n)) 
            q = np.zeros((n, n)) 
            a = np.zeros((n, n)) 
            xi = np.zeros((n, n)) 
            r0 = np.zeros((n, n)) 

            visit = np.zeros(n)
            for key in parameters.keys():
                if isinstance(key, basestring):
                    i = j = elementmap[key]
                elif isinstance(key, tuple) and len(key) == 2:
                    i = elementmap[key[0]]
                    j = elementmap[key[1]]
                else:
                    raise KeyError('Key must either be a string or a tuple with ' +
                                   'two elements.')

                visit[i] += 1
                visit[j] += 1

                p[i,j] = parameters[key][0]
                q[i,j] = parameters[key][1]
                a[i,j] = parameters[key][2]
                xi[i,j] = parameters[key][3]
                r0[i,j] = parameters[key][4]

            if np.any(visit != n + 1):
                raise ValueError('For some elements there are either too few or ' +
                                 'too many parameters.')

        # Interpret elements
        if not isinstance(elements, (tuple, list, np.ndarray)):
            elements = [elements]
        n = len(elements)

        for i, symbol in enumerate(elements):
            if isinstance(symbol, basestring):
                elements[i] = ase.data.atomic_numbers[symbol]
        elements = np.array(elements)


        # Interpret parameters
        p = check_parameter_array(n, "p", p)
        q = check_parameter_array(n, "q", q)
        a = check_parameter_array(n, "a", a)
        xi = check_parameter_array(n, "xi", xi)
        r0 = check_parameter_array(n, "r0", r0)

        # Calculate cutoff
        a1 = (np.log(np.sqrt(12) * a * p / (xi * q)) / (p - q) + 1) * r0

        if not np.all((1.0 < a1) & (a1 < 10.0)):
            raise ValueError('Unreasonable parameters - the nearest neighbor ' +
                             f'distance span [{a1.min():.3f}, {a1.max():.3f}]')

        rcs = cutoff * a1.max()
        rcd = delta * a1.max()
        rce = rcs + rcd
        #print "RGL cutoff: %.4f-%.4f" % (rcs, rcd)

        # Calculate parameters for the cutoff function
        qf = -xi * np.exp(-q * (rcs / r0 - 1)) / rcd**3
        qd = q / r0 * rcd
        q5 = (12.0*qf - 6.0*qf*qd + qf*qd*qd) / (2.0 * rcd**2)
        q4 = (15.0*qf - 7.0*qf*qd + qf*qd*qd) / rcd
        q3 = (20.0*qf - 8.0*qf*qd + qf*qd*qd) / 2.0

        pf = -a * np.exp(-p * (rcs / r0 - 1)) / rcd**3
        pd = p / r0 * rcd
        p5 = (12.0*pf - 6.0*pf*pd + pf*pd*pd) / (2.0 * rcd**2)
        p4 = (15.0*pf - 7.0*pf*pd + pf*pd*pd) / rcd
        p3 = (20.0*pf - 8.0*pf*pd + pf*pd*pd) / 2.0

        if debug:
            print("RGL potential parameters")
            print("p:", p)
            print("q:", q)
            print("a:", a)
            print("xi:", xi)
            print("r0:", r0)
            print("rcs:", rcs)
            print("rce:", rce)
            print("q5:", q5)
            print("q4:", q4)
            print("q3:", q3)
            print("p5:", p5)
            print("p4:", p4)
            print("p3:", p3)

        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose
        _asap.RGL.__init__(self, elements, p, q, a, xi * xi, r0, p3, p4, p5,
                           q3, q4, q5, rcs, rce, verbose)

Gupta = RGL

class LennardJones(AsapPotential, _asap.LennardJones):
    """Lennard-Jones potential.

    Parameters:
    
    elements:  Lists the elements that will be supported.
    
    epsilon and sigma: The LJ parameters.  2D arrays with each
    dimension equal to the number of elements.  Only the lower
    triangular part is used.  Or a 1D array obtained by flattening the
    corresponding 2D array (this possibility is deprecated, and incurs
    less runtime testing).  If there is only one element, then epsilon
    and sigma may be numbers.

    rCut:  The cutoff distance.  Default: XXX

    modified: Should the potential be shifted so no jump occurs at the
    cutoff.  Default: True.
    """
    def __init__(self, elements, epsilon, sigma, rCut=-1.0, modified=True, verbose=None):
        try:
            numelements = len(elements)
        except TypeError:
            numelements = 1
            elements = [elements]

        epsilon = _ChkLJarray(epsilon, numelements, "epsilon")
        sigma = _ChkLJarray(sigma, numelements, "sigma")
        masses = [ase.data.atomic_masses[z] for z in elements]

        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose
        _asap.LennardJones.__init__(self, numelements, elements, epsilon, sigma,
                                    masses, rCut, modified, verbose)

    # Atomic volumes disabled in the C code.
    #def get_atomic_volumes(self):
    #    return self._get_atomic_volumes()


class RahmanStillingerLemberg(AsapPotential, _asap.RahmanStillingerLemberg):
    """Rahman Stillinger Lemberg potential (RSL2).
    """
    def __init__(self, D0, R0, y, a1, b1, c1, a2, b2, c2, a3, b3, c3, 
                 elements, rCut=1.0, verbose=None):
        try:
            numelements = len(elements)
        except TypeError:
            numelements = 1
            elements = [elements]

        D0 = _ChkLJarray(D0, numelements, "D0")
        R0 = _ChkLJarray(R0, numelements, "R0")
        y = _ChkLJarray(y, numelements, "y")
        a1 = _ChkLJarray(a1, numelements, "a1")
        b1 = _ChkLJarray(b1, numelements, "b1")
        c1 = _ChkLJarray(c1, numelements, "c1")
        a2 = _ChkLJarray(a2, numelements, "a2")
        b2 = _ChkLJarray(b2, numelements, "b2")
        c2 = _ChkLJarray(c2, numelements, "c2")
        a3 = _ChkLJarray(a3, numelements, "a3")
        b3 = _ChkLJarray(b3, numelements, "b3")
        c3 = _ChkLJarray(c3, numelements, "c3")
        masses = [ase.data.atomic_masses[z] for z in elements]
        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose
        _asap.RahmanStillingerLemberg.__init__(self, numelements, 
                    D0, R0, y, a1, b1, c1, a2, b2, c2, a3, b3, c3, 
                    elements, masses, rCut, verbose)

# def Ewald(q, elements, rCut=1.0):
#     """Lennard-Jones potential.

#     Parameters:
    
#     elements:  Lists the elements that will be supported.
    
#     epsilon and sigma: The LJ parameters.  2D arrays with each
#     dimension equal to the number of elements.  Only the lower
#     triangular part is used.  Or a 1D array obtained by flattening the
#     corresponding 2D array (this possibility is deprecated, and incurs
#     less runtime testing).  If there is only one element, then epsilon
#     and sigma may be numbers.

#     rCut:  The cutoff distance.  Default: XXX

#     modified: Should the potential be shifted so no jump occurs at the
#     cutoff.  Default: True.
#     """
#     try:
#         numelements = len(elements)
#     except TypeError:
#         numelements = 1
#         elements = [elements]

#       q = _ChkLJarray(q, numelements, "q")
#     masses = [ase.data.atomic_masses[z] for z in elements]
    
#     return _asap.Ewald(numelements, q, elements, masses, rCut)

class MetalOxideInterface(AsapPotential, _asap.MetalOxideInterface):
    def __init__(self,
                 P, Q, A, xi, r0, RGL_cut, 
                 q, kappa, 
                 D, alpha, R0, 
                 a, b, f0, oxide_cut,
                 beta, gamma, interface_cut, verbose=None):
        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose
        _asap.MetalOxideInterface.__init__(self, 
            P, Q, A, xi, r0, RGL_cut, 
            q, kappa, 
            D, alpha, R0, 
            a, b, f0, oxide_cut,
            beta, gamma, interface_cut, verbose)
        
        self.max_cutoff = max(RGL_cut, oxide_cut, interface_cut)
        self.atoms_intialized = False
        self._set_atoms_called = False

    def set_atoms(self, atoms, *args):
        self.set_atoms_mixin(atoms)
        if not self._set_atoms_called:
            if smallest_pbc_direction(atoms) < 2.05 * self.max_cutoff:
                print('Using image atoms')
                self._use_imageatoms()
            self._set_atoms_called = True
            
        if hasattr(atoms, 'ghosts'):
            atoms.ghosts['assignment'] = np.zeros((0,),dtype=np.int32)
        if hasattr(atoms, 'ghosts'):
            atoms.ghosts['monolayer'] = np.zeros((0,),dtype=np.int32)
        
        _asap.MetalOxideInterface.set_atoms(self, atoms, *args)

class MetalOxideInterface2(AsapPotential, _asap.MetalOxideInterface2):
    def __init__(self,
                P, Q, A, xi, r0, RGL_cut, 
                q, kappa, 
                D, alpha, R0, 
                a, b, f0, oxide_cut,
                E, rho0, l0,
                B, C,
                interface_cut, verbose=None):
        if verbose is None:
            verbose =_asap.verbose
        self.verbose = verbose
        _asap.MetalOxideInterface2.__init__(self, 
            P, Q, A, xi, r0, RGL_cut, 
            q, kappa, 
            D, alpha, R0, 
            a, b, f0, oxide_cut,
            E, rho0, l0,
            B, C,
            interface_cut, verbose)
        
        self.max_cutoff = max(RGL_cut, oxide_cut, interface_cut)
        self.atoms_intialized = False
        self._set_atoms_called = False

    def set_atoms(self, atoms, *args):
        self.set_atoms_mixin(atoms)
        if not self._set_atoms_called:
            if smallest_pbc_direction(atoms) < 2.05 * self.max_cutoff:
                print('Using image atoms')
                self._use_imageatoms()
            self._set_atoms_called = True
            
        if hasattr(atoms, 'ghosts'):
            atoms.ghosts['assignment'] = np.zeros((0,),dtype=np.int32)
        if hasattr(atoms, 'ghosts'):
            atoms.ghosts['monolayer'] = np.zeros((0,),dtype=np.int32)

        _asap.MetalOxideInterface2.set_atoms(self, atoms, *args)

class Morse(AsapPotential, _asap.Morse):
    """Lennard-Jones potential.

    Parameters:
    
    elements:  Lists the elements that will be supported.
    
    epsilon, alpha and rmin: The Morse potential parameters.
    2D arrays with each  dimension equal to the number of elements.
    Only the lower triangular part is used.  Or a 1D array obtained by
    flattening the corresponding 2D array (this possibility is deprecated,
    and incurs less runtime testing).  If there is only one element,
    then epsilon and sigma may be numbers.

    rCut:  The cutoff distance.  Default: XXX

    modified: Should the potential be shifted so no jump occurs at the
    cutoff.  Default: True.
    """
    def __init__(self, elements, epsilon, alpha, rmin, rCut=-1.0, modified=True, verbose=None):
        try:
            numelements = len(elements)
        except TypeError:
            numelements = 1
            elements = [elements]
        epsilon = _ChkLJarray(epsilon, numelements, "epsilon", "Morse")
        alpha = _ChkLJarray(alpha, numelements, "alpha", "Morse")
        rmin = _ChkLJarray(rmin, numelements, "rmin", "Morse")
        if verbose is None:
            verbose = _asap.verbose
        self.verbose = verbose

        _asap.Morse.__init__(self, elements, epsilon, alpha,
                             rmin, rCut, modified, verbose)


# Disable ase.EMT to prevent catastrophic loss of performance.
ase.calculators.emt.EMT.disabled = "Disabled by loading asap3."

# Register if an OpenKIMcalculator is available
OpenKIMsupported = hasattr(_asap, 'OpenKIMcalculator')
