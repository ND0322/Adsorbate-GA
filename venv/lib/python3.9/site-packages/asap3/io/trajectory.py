import asap3
import ase.parallel
import ase.constraints as _ase_constraints
import asap3.constraints as _asap_constraints
#from ase.io.trajectory import PickleTrajectory as _PickleTrajectory
from ase.io import trajectory
from . import cpu_setup
import numpy as np
import ase.parallel


class _GetAtoms:
    "Mixin class implementing the get_atoms method."
    def get_atoms(self, n, cpus=None, extra=None):
        """Return Atoms object number n from the trajectory.

        traj.get_atoms(n) is very similar to traj[n], but with the following
        differences:

        In serial simulations are traj.get_atoms(n) and traj[n] equivalent.

        In parallel simulations:
        traj[n] returns all atoms on all processors

        traj.get_atoms(n) returns all atoms on the master, and None on
        all other processors.

        traj.get_atoms(n, cpus) returns a ParallelAtoms object with
        atoms distributed among the processors, and processor layout
        given by cpus (three integers).
        
        Optional parameters:
        extra (BundleTrajectory only): 
            A list of names of extra arrays that should be read from the 
            input file.  The data is available with atoms.get_array.
        """
        if self.master:
            atoms = self[n]
            if extra:
                for d in extra:
                    atoms.set_array(d, self.read_extra_data(d, n))
        else:
            atoms = None

        if cpus is None:
            return atoms
        elif cpus == 'auto':

            if self.master:
                num_cores = ase.parallel.world.size
                print("num cpus:", num_cores)
                print("cell:", np.diag(atoms.cell).tolist())
                cpus = cpu_setup.calculate_optimal_cpu_setup(num_cores, np.diag(atoms.cell).tolist())
                print("cpu setup:", cpus)
            else:
                cpus = np.zeros(3, int)

            cpus = ase.parallel.broadcast(cpus, 0)
            return asap3.MakeParallelAtoms(atoms, cpus)
        else:
            return asap3.MakeParallelAtoms(atoms, cpus)


class PickleTrajectory(trajectory.PickleTrajectory, _GetAtoms):
    write_forces = False
    write_charges = False
    write_magmoms = False

    def __init__(self, filename, mode='r', atoms=None, master=None,
                 *args, **kwargs):
        if master is not None:
            if atoms.get_comm().rank != 0:
                raise NotImplementedError("It is required that the cpu with rank 0 is the master")
        trajectory.PickleTrajectory.__init__(self, filename, mode, atoms, master, *args, **kwargs)

    def set_atoms(self, atoms=None):
        if atoms is not None and getattr(atoms, "parallel", False):
            atoms = asap3.Collector(atoms, self.master)
            self.sanitycheck = False
        trajectory.PickleTrajectory.set_atoms(self, atoms)
        
    def write(self, atoms=None):
        if atoms is not None and getattr(atoms, "parallel", False):
            atoms = asap3.Collector(atoms, self.master)
            self.sanitycheck = False
        trajectory.PickleTrajectory.write(self, atoms)



def Trajectory(filename, mode='r', atoms=None, master=None, 
               properties=['energy']):
    """A Trajectory can be created in read, write or append mode.

    Parameters:

    filename:
        The name of the parameter file.  Should end in .traj.

    mode='r':
        The mode.

        'r' is read mode, the file should already exist, and
        no atoms argument should be specified.

        'w' is write mode.  If the file already exists, it is
        renamed by appending .bak to the file name.  The atoms
        argument specifies the Atoms object to be written to the
        file, if not given it must instead be given as an argument
        to the write() method.

        'a' is append mode.  It acts a write mode, except that
        data is appended to a preexisting file.

    atoms=None:
        The Atoms object to be written in write or append mode.

    master=None:
        Controls which process does the actual writing. The
        default is that process number 0 does this.  If this
        argument is given, processes where it is True will write.

    properties=['energy']:
        List of properties that should be stored in the 
        Trajectory file.  Unlike the ASE version, the default 
        is to only store the energy, not forces, stress etc.  
        Allowed values are energy, forces, stress, dipole, charges,
        magmom and magmoms; but only the first three are meaningful
        in an Asap calcualtion. 

    The atoms, master and properties arguments are ignores in read
    mode.
    """
    if mode == 'r':
        return TrajectoryReader(filename)
    return TrajectoryWriter(filename, mode, atoms, master=master, properties=properties)


class TrajectoryReader(trajectory.TrajectoryReader, _GetAtoms):
    def __init__(self, filename):
        trajectory.TrajectoryReader.__init__(self, filename)
        self.master = ase.parallel.world.rank == 0

    def close(self):
        # Do nothing - fixes bug 99 in ASE
        pass
    
    def __getitem__(self, i=-1):
        atoms = trajectory.TrajectoryReader.__getitem__(self, i)
        constraints = atoms.constraints
        for i, c in enumerate(constraints):
            print("XXXX", c.__class__)
            if c.__class__ is _ase_constraints.FixAtoms:
                # Exact class match, not a subclass
                constraints[i] = _asap_constraints.FixAtoms(indices=c.index)
        return atoms

class TrajectoryWriter(trajectory.TrajectoryWriter):
    def __init__(self, filename, mode='w', atoms=None, properties=None,
                 master=None):
        self.allow_forces = properties is not None and 'forces' in properties
        if master is not None:
            if atoms.get_comm().rank != 0:
                raise NotImplementedError("It is required that the cpu with rank 0 is the master")
        else:
            if atoms and hasattr(atoms, 'get_comm'):
                rank = atoms.get_comm().rank
            else:
                rank = ase.parallel.world.rank
            master = (rank == 0)
        if atoms is not None and getattr(atoms, "parallel", False):
            atoms = asap3.Collector(atoms, master, self.allow_forces)        
        trajectory.TrajectoryWriter.__init__(self, filename, mode=mode, atoms=atoms, 
                                       properties=properties, master=master)
       
    def write(self, atoms=None, **kwargs):
        if atoms is not None and getattr(atoms, "parallel", False):
            atoms = asap3.Collector(atoms, self.master, self.allow_forces)
        elif hasattr(self.atoms, "_is_asap_collector_object"):
            self.atoms.reset_collector()
        trajectory.TrajectoryWriter.write(self, atoms, **kwargs)

