from ase.optimize.fire import FIRE as _FIRE
from asap3.optimize.optimize import asap_Optimizer_mixin
from asap3.mpi import world
import numpy as np

class FIRE(asap_Optimizer_mixin, _FIRE):
    vtag = "fire_v"

    def initialize(self):
        if self.atoms.has(self.vtag):
            self.atoms.set_array(self.vtag, None)

    def read(self):
        if world.size > 1:
            raise NotImplementedError("Restarting is not implemented for FIRE in parallel mode (ASAP).")
        v, self.dt = self.load()
        self.atoms.set_array(self.vtag, v)
       
    def step(self,f=None):
        atoms = self.atoms
        if f is None:
            f = atoms.get_forces()
        if not atoms.has(self.vtag):
            v = np.zeros((len(atoms), 3))
        else:
            v = atoms.get_array(self.vtag)
            vf = np.vdot(f, v)
            if world.size > 1:
                vf = world.sum(vf)
            if vf > 0.0:
                vv = np.vdot(v, v)
                ff = np.vdot(f, f)
                if world.size > 1:
                    vv = world.sum(vv)
                    ff = world.sum(ff)
                v = (1.0 - self.a) * v + self.a * f / np.sqrt(
                    ff) * np.sqrt(vv)
                if self.Nsteps > self.Nmin:
                    self.dt = min(self.dt * self.finc, self.dtmax)
                    self.a *= self.fa
                self.Nsteps += 1
            else:
                v[:] *= 0.0
                self.a = self.astart
                self.dt *= self.fdec
                self.Nsteps = 0

        v += self.dt * f
        dr = self.dt * v
        drdr = np.vdot(dr, dr)
        if world.size > 1:
            drdr = world.sum(drdr)
        normdr = np.sqrt(drdr)
        try:
            maxstep = self.maxstep
        except AttributeError:
            maxstep = self.maxmove
        if normdr > maxstep:
            dr = maxstep * dr / normdr
        r = atoms.get_positions()
        atoms.set_positions(r + dr)
        atoms.set_array(self.vtag, v)
        self.dump((v, self.dt))
        
    def dump(self, data):
        # Can only restart in serial mode
        if world.size == 1:
            _FIRE.dump(self, data)
