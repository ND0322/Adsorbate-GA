import numpy as npy

from asap3.optimize.optimize import Optimizer


class MDMin(Optimizer):
    def __init__(self, atoms, restart=None, logfile='-', trajectory=None,
                 dt=None):
        Optimizer.__init__(self, atoms, restart, logfile, trajectory)

        if dt is not None:
            self.dt = dt

    def initialize(self):
        self.dt = 0.1

    def read(self):
        v, self.dt = self.load()
        atoms.set_velocities(v)
        
    def step(self, f=None):
        atoms = self.atoms
        if f is None:
            f = atoms.get_forces()
            
        v = atoms.get_velocities()
        if v is None:
            v = npy.zeros((len(atoms), 3))
        else:
            v += 0.5 * self.dt * f
            # Correct velocities:
            vf = npy.vdot(v, f)
            if vf < 0.0:
                v[:] = 0.0
            else:
                v[:] = f * vf / npy.vdot(f, f)

        v += 0.5 * self.dt * f
        r = atoms.get_positions()
        atoms.set_positions(r + self.dt * v)
        atoms.set_velocities(v)
        self.dump((v, self.dt))
