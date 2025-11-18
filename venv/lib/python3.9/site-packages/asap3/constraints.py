from ase.constraints import FixAtoms as ASE_FixAtoms
from ase.filters import Filter as ASE_Filter
import numpy as np

class ConstraintMixin:
    """Mixin class FixAtoms and Filter"""
         
    def start_asap_dynamics(self, atoms):
        """Prepare this constraint for optimized Asap dynamics
        
        This function must be called when parallel dynamics start running for
        all dynamics supporting parallel MD.
        """
        # Store the arrays of the atoms, not the atoms, to prevent cyclic references.
        if getattr(atoms, "parallel", False):
            assert not self.asap_ready
            self.atoms_arrays = atoms.arrays
            assert self.indexname not in self.atoms_arrays
            idx = self.index   # Reads constraint from this object
            self.asap_ready = True
            self.storable = False
            self.index = idx   # Stores constraint on atoms object
            del self._index
            assert self.indexname in self.atoms_arrays

    def end_asap_dynamics(self, atoms):
        """Undo what start_asap_dynamics() did.

        This function must be called when parallel dynamics stop running.
        """
        if getattr(atoms, "parallel", False):
            assert self.asap_ready
            assert self.indexname in self.atoms_arrays
            idx = self.index   # Reads constraint from atoms
            self.asap_ready = False
            del self.atoms_arrays[self.indexname]
            self.index = idx   # Stores constraint in this object
            assert hasattr(self, '_index')
        
    def set_index(self, idx):
        if self.asap_ready:
            natoms = len(self.atoms_arrays['positions'])
            if idx.dtype == bool:
                # Boolean - must be a mask
                assert len(idx) == natoms
            else:
                # Must be a list of indices.  Convert to a mask
                idx2 = np.zeros(natoms, bool)
                idx2[idx] = True
                idx = idx2
            self.atoms_arrays[self.indexname] = idx
        else:
            self._index = idx
            
    def get_index(self):
        if self.asap_ready:
            return self.atoms_arrays[self.indexname]
        else:
            return self._index

    def todict(self):
        "Convert to dictionary for storage in e.g. a Trajectory object."
        if not self.storable:
            raise RuntimeError(
                f"Cannot store asap3.{self.dictname} constraint in parallel simulations.")
        idx = self.index
        if idx.dtype == bool:
            return {'name': self.dictname,
                    'kwargs': {'mask': idx}}
        else:
            return {'name': self.dictname,
                    'kwargs': {'indices': idx}}
                
class FixAtoms(ConstraintMixin, ASE_FixAtoms):
    dictname = 'FixAtoms'  # Name used when converting to dictionary.
    def __init__(self, indices=None, mask=None):
        self.pre_init()
        ASE_FixAtoms.__init__(self, indices=indices, mask=mask)
        
    def pre_init(self):
        self.indexname = "FixAtoms_index"
        self.asap_ready = False
        self.storable = True
        
    def copy(self):
        if self.index.dtype == bool:
            return FixAtoms(mask=self.index.copy())
        else:
            return FixAtoms(indices=self.index.copy())

    def get_removed_dof(self, atoms):
        if self.index.dtype == bool:
            return 3 * (len(self.index) - self.index.sum())
        else:
            return 3 * len(self.index)
        
    def __get_state__(self):
        return {'data': self.index,
                'version': 1}
        
    def __set_state__(self, state):
        try:
            assert(state['version'] == 1)
        except KeyError:
            print(state)
            raise
        self.pre_init()
        self.index = state['data']
        
    index = property(ConstraintMixin.get_index, ConstraintMixin.set_index)
    
    
class Filter(ASE_Filter):
    dictname = 'Filter'  # Name used when converting to dictionary.
    def __init__(self, atoms, indices=None, mask=None):
        """Filter atoms.

        This filter can be used to hide degrees of freedom in an Atoms
        object.

        Parameters
        ----------
        indices : list of int
           Indices for those atoms that should remain visible.
        mask : list of bool
           One boolean per atom indicating if the atom should remain
           visible or not.
        """

        self.indexname = "Filter_index"
        if getattr(atoms, "parallel", False):
            assert self.indexname not in atoms.arrays
            self.asap_ready = True
            self.storable = False
        ASE_Filter.__init__(self, atoms, indices, mask)
        
    def set_index(self, idx):
        if self.asap_ready:
            natoms = len(self.atoms.arrays['positions'])
            if idx.dtype == bool:
                # Boolean - must be a mask
                assert len(idx) == natoms
            else:
                # Must be a list of indices.  Convert to a mask
                idx2 = np.zeros(natoms, bool)
                idx2[idx] = True
                idx = idx2
            self.atoms.arrays[self.indexname] = idx
        else:
            self._index = idx

    def get_index(self):
        if self.asap_ready:
            return self.atoms.arrays[self.indexname]
        else:
            return self._index

    index = property(get_index, set_index)
    
def check_asap_constraints(atoms, allowed=None):
    """Check that atoms only have allowed constraints.  Return True if so, otherwise False.
    
    An optional second parameter can be a tuple of allowed constraints.
    """
    if allowed is None:
        allowed = (FixAtoms,)
        
    if len(atoms.constraints) == 0:
        return True
    if len(atoms.constraints) > 1:
        return False
    return isinstance(atoms.constraints[0], allowed)

