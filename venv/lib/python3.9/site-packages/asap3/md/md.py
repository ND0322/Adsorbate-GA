"""Molecular Dynamics."""

import numpy as np

try:
    from ase.optimize.optimize import Dynamics
except ImportError:
    # Fallback to old placement
    from ase.optimize import Dynamics
from ase.data import atomic_masses
from ase.md import MDLogger
import asap3

_counter = 0  # Prevents identical prefixes


class ParallelMolDynMixinNoData:
    def before_run(self):
        # Identify FixAtoms constraint
        if self.atoms.constraints and getattr(self.atoms, "parallel", False):
            # Parallel simulation with constraints
            if len(self.atoms.constraints) != 1:
                raise RuntimeError("Asap can only do parallel dynamics with a single constraint.")
            constraint = self.atoms.constraints[0]
            if not  isinstance(constraint, asap3.constraints.FixAtoms):
                raise RuntimeError("Asap only supports constrained dynamics with the ASAP FixAtoms constraint.")
            constraint.start_asap_dynamics(self.atoms)

    def after_run(self):
        if self.atoms.constraints and getattr(self.atoms, "parallel", False):
            assert len(self.atoms.constraints) == 1
            self.atoms.constraints[0].end_asap_dynamics(self.atoms)


class ParallelMolDynMixin(ParallelMolDynMixinNoData):
    def __init__(self, prefix, atoms):
        global _counter
        self.prefix = prefix+str(_counter)+"_"
        _counter += 1
        self._uselocaldata = not getattr(atoms, "parallel", False)
        self._localdata = {}
        
    def set(self, name, var):
        """Set a local variable.

        If the local variable is a scalar, it is stored locally.  If
        it is an array it is stored on the atoms.  This allows for
        parallel Asap simulations, where such arrays will have to
        migrate among processors along with all other data for the
        atoms.
        """
        if self._uselocaldata or getattr(var, "shape", ()) == ():
            self._localdata[name] = var
        else:
            if name in self._localdata:
                del self._localdata[name]
            self.atoms.set_array(self.prefix+name, var)

    def get(self, name):
        try:
            return self._localdata[name]
        except KeyError:
            return self.atoms.get_array(self.prefix+name, copy=False)

