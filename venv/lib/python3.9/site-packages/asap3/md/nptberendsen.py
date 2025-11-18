from ase.md.nptberendsen import NPTBerendsen as _NPTBerendsen
from ase.md.nptberendsen import Inhomogeneous_NPTBerendsen as _Inhomogeneous_NPTBerendsen
from asap3.md.md import ParallelMolDynMixinNoData

class NPTBerendsen(_NPTBerendsen, ParallelMolDynMixinNoData):
    def __init__(self, atoms, timestep, temperature=None,
                 *, fixcm=False, **kwargs):
        """Berendsen (constant N, P, T) molecular dynamics.

        This dynamics scale the velocities and volumes to maintain a constant
        pressure and temperature.  The shape of the simulation cell is not
        altered, if that is desired use Inhomogenous_NPTBerendsen.

        Parameters:

        atoms: Atoms object
            The list of atoms.

        timestep: float
            The time step in ASE time units.

        temperature: float
            The desired temperature, in Kelvin.

        temperature_K: float
            Alias for ``temperature``.

        pressure: float (deprecated)
            The desired pressure, in bar (1 bar = 1e5 Pa).  Deprecated,
            use ``pressure_au`` instead.

        pressure: float
            The desired pressure, in atomic units (eV/Å^3).

        taut: float
            Time constant for Berendsen temperature coupling in ASE
            time units.  Default: 0.5 ps.

        taup: float
            Time constant for Berendsen pressure coupling.  Default: 1 ps.

        compressibility: float (deprecated)
            The compressibility of the material, in bar-1.  Deprecated,
            use ``compressibility_au`` instead.

        compressibility_au: float
            The compressibility of the material, in atomic units (Å^3/eV).

        fixcm: bool (optional)
            If True, the position and momentum of the center of mass is
            kept unperturbed.  Default: False.   This is not supported in
            parallel simulations, and should in general be unnecessary unless
            a global non-zero center-of-mass momentum needs to be preserved,
            as a zero center-of-mass momentum will remain zero.

        trajectory: Trajectory object or str (optional)
            Attach trajectory object.  If *trajectory* is a string a
            Trajectory will be constructed.  Use *None* for no
            trajectory.

        logfile: file object or str (optional)
            If *logfile* is a string, a file with that name will be opened.
            Use '-' for stdout.

        loginterval: int (optional)
            Only write a log line for every *loginterval* time steps.  
            Default: 1

        append_trajectory: boolean (optional)
            Defaults to False, which causes the trajectory file to be
            overwriten each time the dynamics is restarted from scratch.
            If True, the new structures are appended to the trajectory
            file instead.

        """
        if (fixcm and getattr(atoms, 'parallel', False)):
            raise NotImplementedError("NVTBerendsen does not support fixcm=True for parallel simulations.")
        super().__init__(atoms, timestep, temperature, fixcm=fixcm, **kwargs)

    def run(self, steps):
        self.before_run()
        super().run(steps)
        self.after_run()


class Inhomogeneous_NPTBerendsen(_Inhomogeneous_NPTBerendsen, ParallelMolDynMixinNoData):
    def __init__(self, atoms, timestep, temperature=None,
                 *, fixcm=False, **kwargs):
        if (fixcm and getattr(atoms, 'parallel', False)):
            raise NotImplementedError("NVTBerendsen does not support fixcm=True for parallel simulations.")
        super().__init__(atoms, timestep, temperature, fixcm=fixcm, **kwargs)

    def run(self, steps):
        self.before_run()
        super().run(steps)
        self.after_run()
