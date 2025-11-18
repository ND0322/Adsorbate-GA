'''
Created on Mar 16, 2011

@author: schiotz
'''

from ase.md.md import MolecularDynamics
from ase.md.verlet import VelocityVerlet as _VelocityVerlet
from asap3.md.md import ParallelMolDynMixinNoData
import ase
import asap3
from ase.parallel import world
import numpy as np
import sys

class VelocityVerlet_Asap(MolecularDynamics, ParallelMolDynMixinNoData):
    def __init__(self, atoms, timestep, trajectory=None, logfile=None,
                 loginterval=1):
        MolecularDynamics.__init__(self, atoms, timestep, trajectory, logfile,
                                   loginterval)
        if not atoms.has('momenta'):
            atoms.set_momenta(np.zeros((len(atoms), 3), float))
        self.calculator = atoms.calc
        self.asap_md = asap3._asap.VelocityVerlet(atoms, self.calculator, timestep)
            
    def run(self, steps):
        assert(self.calculator is self.atoms.calc)
        self.before_run()
        # Extra stuff needs to be done for FixAtoms constraint.
        if self.atoms.constraints:
            if len(self.atoms.constraints) != 1:
                raise RuntimeError("AASAP Verlet can only do parallel dynamics with a single constraint.")
            constraint = self.atoms.constraints[0]
            if not  isinstance(constraint, asap3.constraints.FixAtoms):
                raise RuntimeError("ASAP Verlet only supports constrained dynamics with the ASAP FixAtoms constraint.")
            mask = constraint.index
            if not mask.dtype == bool:
                mask2 = np.zeros(len(self.atoms), bool)
                mask2[mask] = True
                mask = mask2
            assert mask.shape == (len(self.atoms),) and mask.dtype == bool
            mult = np.logical_not(mask).astype(float)
            self.atoms.arrays["FixAtoms_mult_double"] = mult
            del mask, mult
        self.asap_md.run(steps, self.observers, self)
        self.after_run()
        if self.atoms.constraints:
            del self.atoms.arrays["FixAtoms_mult_double"]

class VelocityVerlet_ASE(_VelocityVerlet, ParallelMolDynMixinNoData):
    def run(self, steps):
        self.before_run()
        super().run(steps)
        self.after_run()
        
def VelocityVerlet(atoms, timestep, trajectory=None, logfile=None, loginterval=1):
    if isinstance(atoms, ase.Atoms) and asap3.constraints.check_asap_constraints(atoms):
        if world.rank == 0:
            sys.stderr.write("Using Asap-optimized Verlet algorithm\n")
        return VelocityVerlet_Asap(atoms, timestep, trajectory, logfile, loginterval)
    else:
        if world.rank == 0:
            sys.stderr.write("Using ASE Verlet algorithm\n")
        return VelocityVerlet_ASE(atoms, timestep, trajectory, logfile, loginterval)

