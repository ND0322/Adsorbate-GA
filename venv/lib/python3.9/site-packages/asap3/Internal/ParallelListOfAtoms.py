"""Asap module ParallelListOfAtoms.

Defines the parallel list of atoms object (`ParallelAtoms`), and a factory
method for creating them (`MakeParallelAtoms`).

Importing this module also installs a Python exit function causing
MPI_Abort to be called if an uncaught exception occurs.
"""


__docformat__ = "restructuredtext en"

import ase
import ase.units
try:
    from ase.geometry.cell import Cell
except ImportError:
    # Cell was introduced in ASE in April 2019.
    Cell = None
from asap3 import _asap
from asap3.Internal.BuiltinPotentials import AsapPotential
import asap3.mpi
import numpy as np
import pickle
import sys, time
import ase.parallel
import numbers
from ase.utils import deprecated
import copy


class BorrowedNeighborLocator:
    """A front for a neighbor locator borrowed from a parallel potential.

    In a parallel simulation, borrowing a neighbor locator from a 
    potential and then updating it will corrupt the potential as
    a migration may be triggered without the potentials knowledge.

    This front for the borrowed neighbor list solves that problem
    by asking the potential to do the update.
    """
    def __init__(self, nblist, potential):
        self._nblist = nblist
        self._potential = potential

    def check_and_update(self, atoms):
        self._potential.check_update_neighborlist(atoms)

    # All other methods are passed onto the neighbor list
    def __getattr__(self, name):
        return getattr(self._nblist, name)


class ParallelPotential(_asap.ParallelPotential, AsapPotential):
    def __init__(self, potential, *args, **kwargs):
        super().__init__(potential, *args, **kwargs)
        self._calc = potential
        
    def get_stress(self, atoms):
        stress = self.get_virial(atoms)
        if not getattr(atoms, "_ase_handles_dynamic_stress", False):
            p = atoms.get_momenta()
            masses = atoms.get_masses()
            invmass = 1.0 / masses
            dynstress = np.zeros_like(stress)
            for alpha in range(3):
                for beta in range(alpha, 3):
                    dynstress[self._stresscomp[alpha,beta]] = -(p[:,alpha] * p[:,beta] * invmass).sum()
            asap3.mpi.world.sum(dynstress)
            stress += dynstress
        stress /= atoms.get_volume()
        return stress

    def get_neighborlist(self):
        nbl = self._calc.get_neighborlist()
        return BorrowedNeighborLocator(nblist=nbl, potential=self)

    # Some Potentials may have non-standard methods and attributes.
    # In those cases, pass through to the original Potential.
    def __getattr__(self, name):
        return getattr(self._calc, name)

class NoCalculatorWrapper:
    """Object proxy hiding the calculator of an Atoms object."""
    def __init__(self, wrappee):
        self._wrappee = wrappee

    def get_calculator(self):
        return None

    def __getattr__(self, attr):
        return getattr(self._wrappee, attr)

    @property
    def calc(self):
        """Calculator object."""
        return None



class ParallelAtoms(ase.Atoms):
    """Atoms class for parallel Asap simulations.

    It is recommended to create ParallelAtoms objects using
    `MakeParallelAtoms`.
    """
    parallel = 1
    def __init__(self, nCells, comm, atoms, cell=None, pbc=None,
                 distribute=True):
        """Create a ParallelAtoms object.

        WARNING: ParallelAtoms object should normally not be created
        explicitly.  Use MakeParallelAtoms instead.
        """
        # Initialize the atoms.  Hide the calculator: Often there will
        # be a SinglePointCalculator (or anothter calculator) on the
        # master but nothing on the slaves, causing a deadlock.  And a
        # ParallelPotential cannot be reused on a new ParallelAtoms
        # object.
        super().__init__(NoCalculatorWrapper(atoms), cell=cell, pbc=pbc, constraint=None)

        # Sanity checks
        assert self.arrays["positions"].dtype == np.dtype(float)
        assert self.arrays["positions"].shape == (len(atoms), 3)
        assert self.arrays["numbers"].shape ==  (len(atoms),)

        # The initializer of the parent class (ase.Atoms) only copies
        # known arrays.  Copy the rest.
        for k, v in atoms.arrays.items():
            if k not in self.arrays:
                self.arrays[k] = v.copy()

        self.nCells = np.array(nCells, int)
        if self.nCells.shape != (3,):
            raise ValueError("ParallelAtoms: nCells must be 3 integers.")
        self.comm = comm

        self.ghosts = {}
        self.ghosts["positions"] = np.zeros((0,3), float)
        self.ghosts["numbers"] = np.zeros(0, self.arrays["numbers"].dtype)

        # Now make the IDs
        mynatoms = np.array([len(self)])
        natoms_all = np.zeros(self.comm.size, int)
        self.comm.all_gather(mynatoms, natoms_all)
        if "ID" not in self.arrays:
            firstID = sum(natoms_all[:self.comm.rank])
            self.arrays["ID"] = np.arange(firstID, firstID+len(atoms))
        self.total_number_of_atoms = sum(natoms_all)

        if distribute:
            self.distribute()

    def distribute(self, verbose=None):
        if verbose is None:
            verbose = _asap.verbose
        _asap.DistributeAtoms(self, verbose)

    def get_global_number_of_atoms(self):
        n = len(self)
        return self.comm.sum(n)

    def get_number_of_degrees_of_freedom(self):
        n = super().get_number_of_degrees_of_freedom()
        return self.comm.sum(n)
    
    def get_list_of_elements(self):
        """Get a list of elements.

        The list is cached to prevent unnecessary communication.
        """
        try:
            return self.listofelements
        except AttributeError:
            z = self.get_atomic_numbers()
            present = np.zeros(100, int)
            if len(z):
                zmax = z.max()
                zmin = z.min()
                present[zmin] = present[zmax] = 1
                for i in range(zmin+1, zmax):
                    if np.equal(z, i).any():
                        present[i] = 1
            self.comm.sum(present)
            self.listofelements = []
            for i, p in enumerate(present):
                if p:
                    self.listofelements.append(i)
            return self.listofelements

    def set_atomic_numbers(self, numbers):
        """Set the atomic numbers."""
        try:
            # Discard the cached list of elements
            del self.listofelements
        except AttributeError:
            pass
        ase.Atoms.set_atomic_numbers(self, numbers)

    def get_ids(self):
        """Get the atom IDs in a parallel simulation."""
        return self.arrays["ID"].copy()

    def is_master(self):
        """Return 1 on the master node, 0 on all other nodes."""
        return (self.comm.rank == 0)

    def get_comm(self):
        return self.comm
    
    def wrap_calculator(self, calc):
        "Make an ASAP calculator compatible with parallel simulations."
        try:
            parallelOK = calc.supports_parallel()
        except AttributeError:
            parallelOK = False
        if not parallelOK:
            raise ValueError("The calculator does not support parallel ASAP calculations.")
        try:
            verbose = calc.verbose
        except AttributeError:
            verbose = _asap.verbose
        return ParallelPotential(calc, verbose)

    def set_calculator(self, calc, wrap=True):
        """Sets the calculator in a way compatible with parallel simulations.
        
        calc: 
            The Calculator to be used.  Normally only Asap calculators will work.
            
        wrap (optional, default=True):
            Indicates if a calculator should be wrapped in a ParallelCalculator object.  
            Wrapping is the default, and should almost always be used, the only exception
            being if the Calculator is implemented as a Python object wrapping an Asap
            calculator, in which case the Asap calculator should first be wrapped in
            a ParallelCalculator object (use atoms.wrap_calculator) and this one should then
            be used by the Python calculator.  The Python calculator is then attached
            without being wrapped again.
        """
        if wrap and calc is not None:
            parcalc = self.wrap_calculator(calc)
        else:
            parcalc = calc
        ase.Atoms.calc.fset(self, parcalc)

    def copy(self):
        """Return a copy."""
        atoms = self.__class__(self.nCells, self.comm, self)
        atoms.constraints = copy.deepcopy(self.constraints)
        return atoms

    @property
    def calc(self):
        """Calculator object."""
        return ase.Atoms.calc.fget(self)
    
    @calc.setter
    def calc(self, calc):
        self.set_calculator(calc)

    @calc.deleter  # type: ignore
    @deprecated(DeprecationWarning('Please use atoms.calc = None'))
    def calc(self):
        self.set_calculator(None)

    def get_kinetic_energy(self):
        local_ekin = ase.Atoms.get_kinetic_energy(self)
        return self.comm.sum(local_ekin)
    
    def get_temperature(self):
        """Get the temperature. in Kelvin"""
        dof = 3 * self.get_global_number_of_atoms()
        removed_dof = 0
        for c in self.constraints:
            removed_dof += c.get_removed_dof(self)
        removed_dof = self.comm.sum(int(removed_dof))
        ekin_per_dof = self.get_kinetic_energy() / (dof - removed_dof)
        return ekin_per_dof / (0.5 * ase.units.kB)

    def get_ghost_positions(self):
        return self.ghosts['positions'].copy()
    
    def get_ghost_atomic_numbers(self):
        return self.ghosts['numbers'].copy()
    
    def get_center_of_mass(self, scaled=False):
        """Get the center of mass.

        If scaled=True the center of mass in scaled coordinates
        is returned."""
        m = self.get_masses()
        rsum = np.dot(m, self.arrays['positions'])
        msum = m.sum()
        data = np.zeros(4)
        data[:3] = rsum
        data[3] = msum
        self.comm.sum(data)
        com = data[:3] / data[3]
        if scaled:
            return np.linalg.solve(self._cell.T, com)
        else:
            return com


    def get_moments_of_inertia(self, vectors=False):
        """Get the moments of inertia along the principal axes.

        The three principal moments of inertia are computed from the
        eigenvalues of the symmetric inertial tensor. Periodic boundary
        conditions are ignored. Units of the moments of inertia are
        amu*angstrom**2.
        """
        com = self.get_center_of_mass()
        positions = self.get_positions()
        positions -= com  # translate center of mass to origin
        masses = self.get_masses()

        # Initialize elements of the inertial tensor
        I11 = I22 = I33 = I12 = I13 = I23 = 0.0
        for i in range(len(self)):
            x, y, z = positions[i]
            m = masses[i]

            I11 += m * (y ** 2 + z ** 2)
            I22 += m * (x ** 2 + z ** 2)
            I33 += m * (x ** 2 + y ** 2)
            I12 += -m * x * y
            I13 += -m * x * z
            I23 += -m * y * z

        I = np.array([[I11, I12, I13],
                      [I12, I22, I23],
                      [I13, I23, I33]])
        self.comm.sum(I)

        evals, evecs = np.linalg.eigh(I)
        if vectors:
            return evals, evecs.transpose()
        else:
            return evals

    def get_angular_momentum(self):
        """Get total angular momentum with respect to the center of mass."""
        data = super().get_angular_momentum()
        self.comm.sum(data)
        return data
    
    def get_stress(self, voigt=True, apply_constraint=True, include_ideal_gas=False):
        """Calculate stress tensor.

        Returns an array of the six independent components of the
        symmetric stress tensor, in the traditional Voigt order
        (xx, yy, zz, yz, xz, xy) or as a 3x3 matrix.  Default is Voigt
        order.

        The ideal gas contribution to the stresses is added if the 
        atoms have momenta, unless it is explicitly disabled.
        """

        if self._calc is None:
            raise RuntimeError('Atoms object has no calculator.')

        stress = self._calc.get_stress(self)
        assert stress.shape == (6,)

        if apply_constraint:
            for constraint in self.constraints:
                if hasattr(constraint, 'adjust_stress'):
                    constraint.adjust_stress(self, stress)

        # Add ideal gas contribution, if applicable
        if getattr(self, "_ase_handles_dynamic_stress", False) and include_ideal_gas and self.has('momenta'):
            stresscomp = np.array([[0, 5, 4], [5, 1, 3], [4, 3, 2]])
            invvol = 1.0 / self.get_volume()
            p = self.get_momenta()
            masses = self.get_masses()
            invmass = 1.0 / masses
            dynstress = np.zeros_like(stress)
            for alpha in range(3):
                for beta in range(alpha, 3):
                    dynstress[stresscomp[alpha,beta]] -= (p[:,alpha] * p[:,beta] * invmass).sum() * invvol
            asap3.mpi.world.sum(dynstress)
            stress += dynstress

        if voigt:
            return stress
        else:
            xx, yy, zz, yz, xz, xy = stress
            return np.array([(xx, xy, xz),
                             (xy, yy, yz),
                             (xz, yz, zz)])

    def delete_atoms_globally(self, local_indices=None, global_indices=None):
        """Delete atoms from a parallel simulation.

        local_indices: Remove atoms with these indices on the local MPI task.

        global_indices: Remove atoms with these global IDs.  The atoms
        may reside on this or on another MPI task.

        Both parameters should be sequences, or a single int.  Both can
        be specified simultaneously, if need be, although that may be
        confusing.

        This method must be called simultaneously by all MPI tasks, but
        the lists of indices may be diffent on the different tasks.  An
        atom is deleted if it is specified in at least one task.
        Duplicates are allowed.
        """
        for c in self.constraints:
            # Constraint must have data stored on atoms.
            c.start_asap_dynamics(self)
        indices = []
        if isinstance(local_indices, int):
            local_indices = [local_indices]
        if isinstance(global_indices, int):
            global_indices = [global_indices]
        if local_indices is not None and len(local_indices):
            # Convert to global indices
            ids = self.get_ids()
            indices += [ids[i] for i in local_indices]
        if global_indices is not None and len(global_indices):
            indices += list(global_indices)
        # Now merge all these lists.  They may be empty on most MPI tasks.
        number = len(indices)
        number = self.comm.max(number)
        if number == 0:
            # Not deleting anything is valid.
            return
        natoms = self.get_global_number_of_atoms()
        indices_array = -np.ones(number, int)  # Array of the value -1
        indices_array[:len(indices)] = indices
        merged_indices = np.zeros(number * self.comm.size, int)
        self.comm.all_gather(indices_array, merged_indices)
        # Now all tasks have a list of the global indices of all atoms
        # to delete, polluted by elements with value -1 and by
        # duplicates.  Clean it up.
        merged_indices = np.unique(merged_indices[merged_indices != -1])

        # Ready to delete.  We need to "prune" the arrays on some tasks,
        # and to make sure that the IDs remain contiguous.  We start by
        # swapping IDs between the atoms being removed, and the ones
        # with the largest IDs.  Then we remove the ones with the
        # largest IDs.  It is possible that some atoms to be removed
        # have so large IDs that they do not need an ID swap.
        remove_above = natoms - len(merged_indices)
        to_be_swapped = list(range(remove_above, natoms))
        print(merged_indices, remove_above, to_be_swapped)
        for idx in merged_indices:
            if idx in to_be_swapped:
                to_be_swapped.remove(idx)
        swp = {}
        for idx in merged_indices:
            if idx < remove_above:
                swp[idx] = to_be_swapped.pop()
        assert len(to_be_swapped) == 0
        ids = self.arrays["ID"]
        for k, v in swp.items():
            # Now swap k and v in arrays["ID"].   They may or may not be present.
            k_idx = np.nonzero(ids == k)
            v_idx = np.nonzero(ids == v)
            if len(k_idx) == 1:
                ids[k_idx[0]] = v
            if len(v_idx) == 1:
                ids[v_idx[0]] = k
        # Now the atoms to be removed have ids of remove_above or higher
        keep = ids < remove_above
        if keep.sum() < len(keep):
            for k, v in self.arrays.items():
                self.arrays[k] = v[keep]
        assert self.get_global_number_of_atoms() == natoms - len(merged_indices)

        # Ghost atoms are now incorrect.  Better delete them, so accessing them cause a visible error
        self._asap_invalidghosts = True
        for k, v in self.ghosts.items():
            self.ghosts[k] = np.zeros((0,) + v.shape[1:], v.dtype)

        # Final sanity check: Any constraint must have its data on the atoms, otherwise
        # it will now be corrupt.
        for constraint in self.constraints:
            if not getattr(constraint, 'asap_ready', False):
                raise ValueError("Deleting atoms has corrupted contraint "+str(constraint))
        for c in self.constraints:
            c.end_asap_dynamics(self)

    # It is not possible to delete atoms with __delitem__ as that cannot sync correctly.
    def __delitem__(self, *args, **kwargs):
        raise NotImplementedError("Cannot delete parallel atoms with del.  Use atoms.delete_atoms_globally()")
        
    # We need to redefine __getitem__ since __init__ does not
    # take the expected arguments.
    def __getitem__(self, i):
        """Return a subset of the atoms.

        i -- scalar integer, list of integers, or slice object
        describing which atoms to return.

        If i is a scalar, return an Atom object. If i is a list or a
        slice, return an Atoms object with the same cell, pbc, and
        other associated info as the original Atoms object. The
        indices of the constraints will be shuffled so that they match
        the indexing in the subset returned.

        The returned object is an ordinary Atoms object, not a
        ParallelAtoms object.
        """
        if isinstance(i, numbers.Integral):
            natoms = len(self)
            if i < -natoms or i >= natoms:
                raise IndexError('Index out of range.')

            return ase.Atom(atoms=self, index=i)

        import copy
        from ase.constraints import FixConstraint, FixBondLengths

        atoms = ase.Atoms(cell=self._cell, pbc=self._pbc, info=self.info)

        atoms.arrays = {}
        for name, a in self.arrays.items():
            atoms.arrays[name] = a[i].copy()

        # Constraints need to be deepcopied, since we need to shuffle
        # the indices
        atoms.constraints = copy.deepcopy(self.constraints)
        condel = []
        for con in atoms.constraints:
            if isinstance(con, (FixConstraint, FixBondLengths)):
                try:
                    con.index_shuffle(self, i)
                except IndexError:
                    condel.append(con)
        for con in condel:
            atoms.constraints.remove(con)
        return atoms

def MakeParallelAtoms(atoms, nCells, cell=None, pbc=None,
                      distribute=True):
    """Build parallel simulation from serial lists of atoms.

    Call simultaneously on all processors.  Each processor having
    atoms should pass a list of atoms as the first argument, or None
    if this processor does not contribute with any atoms.  If the
    cell and/or pbc arguments are given, they must be given on
    all processors, and be identical.  If it is not given, a supercell
    is attempted to be extracted from the atoms on the processor with
    lowest rank.

    Any atoms object passed to this method cannot have a calculator or a
    contraint attached.

    This is the preferred method for creating parallel simulations.
    """
    mpi = asap3.mpi
    #comm = mpi.world.duplicate()
    comm = mpi.world

    # Sanity check: No contraint.
    if atoms is not None:
        if getattr(atoms, "contraints", None):
            raise ValueError("The atoms on node {} have contraints: {}".format(
                comm.rank, str(atoms.constraints)))

    # Sanity check: is the node layout reasonable
    nNodes = nCells[0] * nCells[1] * nCells[2]
    if nNodes != comm.size:
        raise RuntimeError("Wrong number of CPUs: %d != %d*%d*%d" %
                           (comm.size, nCells[0], nCells[1], nCells[2]))
    t1 = np.zeros((3,))
    t2 = np.zeros((3,))
    comm.min(t1)
    comm.max(t2)
    if (t1[0] != t2[0] or t1[1] != t2[1] or t1[2] != t2[2]):
        raise RuntimeError("CPU layout inconsistent.")

    # If pbc and/or cell are given, they may be shorthands in need of
    # expansion.
    if pbc:
        try:
            plen = len(pbc)
        except TypeError:
            # It is a scalar, interpret as a boolean.
            if pbc:
                pbc = (1,1,1)
            else:
                pbc = (0,0,0)
        else:
            if plen != 3:
                raise ValueError("pbc must be a scalar or a 3-sequence.")
    if cell:
        cell = array(cell)  # Make sure it is a numeric array.
        if cell.shape == (3,):
            cell = array([[cell[0], 0, 0],
                          [0, cell[1], 0],
                          [0, 0, cell[2]]])
        elif cell.shape != (3,3):
            raise ValueError("Unit cell must be a 3x3 matrix or a 3-vector.")

    # Find the lowest CPU with atoms, and let that one distribute
    # which data it has.  All other CPUs check for consistency.
    if atoms is None:
        hasdata = None
        mynum = comm.size
    else:
        hasdata = {}
        for name in atoms.arrays.keys():
            datatype = atoms.arrays[name].dtype.char
            shape = atoms.arrays[name].shape[1:]
            hasdata[name] = (datatype, shape)
        mynum = comm.rank
        if pbc is None:
            pbc = atoms.get_pbc()
        if cell is None:
            cell = np.array(atoms.get_cell())
    root = comm.min(mynum)   # The first CPU with atoms
    # Now send hasdata, cell and pbc to all other CPUs
    package = pickle.dumps((hasdata, cell, pbc), 2)
    package = comm.broadcast_string(package, root)
    rootdata, rootcell, rootpbc = pickle.loads(package)
    if rootdata is None or len(rootdata) == 0:
        raise ValueError("No data from 'root' atoms.  Empty atoms?!?")
    
    # Check for consistent cell and pbc arguments
    if cell is not None:
        if rootcell is None:
            raise TypeError("Cell given on another processor than the atoms.")
        if (cell.ravel() - rootcell.ravel()).max() > 1e-12:
            raise ValueError("Inconsistent cell specification.")
    else:
        cell = rootcell   # May still be None
    if pbc is not None:
        if rootpbc is None:
            raise TypeError("PBC given on another processor than the atoms.")
        if (pbc != rootpbc).any():
            raise ValueError("Inconsistent pbc specification.")
    else:
        pbc = rootpbc

    # Check for consistent atoms data
    if hasdata is not None:
        if hasdata != rootdata:
            raise ValueError("Atoms do not contain the sama data on different processors.")
    if "positions" not in rootdata:
        raise ValueError("Atoms do not have positions!")
    
    # Create empty atoms
    if atoms is None:
        atoms = ase.Atoms(cell=cell, pbc=pbc)
        for name in rootdata.keys():
            if name in atoms.arrays:
                assert atoms.arrays[name].dtype.char == rootdata[name][0]
                assert len(atoms.arrays[name]) == 0
            else:
                shape = (0,) + rootdata[name][1]
                atoms.arrays[name] = np.zeros(shape, rootdata[name][0])
        
    return ParallelAtoms(nCells, comm, atoms, cell=cell, pbc=pbc, 
                         distribute=distribute)



# A cleanup function should call MPI_Abort if python crashes to
# terminate the processes on the other nodes.
ase.parallel.register_parallel_cleanup_function()

# _oldexitfunc = getattr(sys, "exitfunc", None)
# def _asap_cleanup(lastexit = _oldexitfunc, sys=sys, time=time,
#                   comm = asap3.mpi.world):
#     error = getattr(sys, "last_type", None)
#     if error:
#         sys.stdout.flush()
#         sys.stderr.write("ASAP CLEANUP (node " + str(comm.rank) +
#                          "): " + str(error) +
#                          " occurred.  Calling MPI_Abort!\n")
#         sys.stderr.flush()
#         # Give other nodes a moment to crash by themselves (perhaps
#         # producing helpful error messages).
#         time.sleep(3)
#         comm.abort(42)
#     if lastexit:
#         lastexit()
# sys.exitfunc = _asap_cleanup
        
# END OF PARALLEL STUFF
