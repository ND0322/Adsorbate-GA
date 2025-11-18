import os
import time
import sys
import numpy as np
import asap3
from asap3.mpi import world
from asap3.io.trajectory import _GetAtoms
from ase.io.bundletrajectory import BundleTrajectory as _BundleTrajectory
from ase.io.bundletrajectory import UlmBundleBackend
import ase.parallel
from asap3.io import cpu_setup

    
class BundleTrajectory(_BundleTrajectory, _GetAtoms):
    """Reads and writes atoms into a .bundle directory.

    The BundleTrajectory is an alternative way of storing
    trajectories, intended for large-scale molecular dynamics
    simulations, where a single flat file becomes unwieldy.  Instead,
    the data is stored in directory, a 'bundle' (the name bundle is
    inspired from bundles in Mac OS, which are really just directories
    the user is supposed to think of as a single file-like unit).

    Parameters:

    filename:
        The name of the directory.  Preferably ending in .bundle.

    mode (optional):
        The file opening mode.  'r' means open for reading, 'w' for
        writing and 'a' for appending.  Default: 'r'.  If opening in
        write mode, and the filename already exists, the old file is
        renamed to .bak (any old .bak file is deleted), except if the
        existing file is empty.

    atoms (optional):
        The atoms that will be written.  Can only be specified in
        write or append mode.  If not specified, the atoms must be
        given as an argument to the .write() method instead.

    backup (optional):
        Use backup=False to disable renaming of an existing file.

    split (optional):
        If set to True or False, determines whether a split file
        format is used instead of the normal one.  In the split
        format, each processor in a parallel simulation writes its own
        files inside the BundleTrajectory, instead of leaving all I/O
        to the master.  In not specified, a split format is used if
        more than one million atoms.  Ignored in serial simulations.

    iolimit (optional):
        Limits the number of MPI tasks performing I/O simultaneously,
        to prevent overloading the NFS server.  Only enforced if the
        number of tasks is somewhat larger than the limit.
        
    backend=None:
        Request a backend.  The only supported backend is 'ulm'.
        Only honored when writing.  

    singleprecision=True:
        Store floating point data in single precision (ulm backend only).
        Note that for ASAP, the default is True!
    
    """
    def __init__(self, filename, mode='r', atoms=None,
                 backup=True, split=None, iolimit=10,
                 backend=None, singleprecision=True):
        if split is None:
            # Decide if subtype should be split based on number of atoms
            split = (atoms is not None) and atoms.get_global_number_of_atoms() > 1000000
        # Never use subtype split for serial simulations
        if not getattr(atoms, "parallel", False):
            split = False
        if split:
            self.subtype = 'split'
        else:
            self.subtype = 'normal'
        # self.iolimit may be needed if reading a split bundle.
        if world.size < 1.5 * iolimit:
            self.iolimit = None
        else:
            self.iolimit = iolimit

        if backend is None:
            backend = 'ulm'
        _BundleTrajectory.__init__(self, filename, mode, atoms,
                                   backup=backup, backend=backend,
                                   singleprecision=singleprecision)
        if self.subtype == 'split':
            self.set_extra_data('ID')  # So the atoms can be sorted when read.
        
    def _set_defaults(self):
        subtype = self.subtype   # Preserve it
        _BundleTrajectory._set_defaults(self)
        self.subtype = subtype
        self.datatypes['forces'] = False

    def _open_write(self, atoms, *args, **kwargs):
        _BundleTrajectory._open_write(self, atoms, *args, **kwargs)
        # Use the collector object to join all data on master if subtype is normal
        # and the simulation is parallel.
        if self.subtype == 'normal' and atoms is not None and getattr(atoms, "parallel", False):
            self.atoms = asap3.Collector(atoms)

    def _open_append(self, atoms, backend=None):
        if backend is None:
            # Compatibility with ASE 3.23.0 and earlier.
            _BundleTrajectory._open_append(self, atoms)
        else:
            _BundleTrajectory._open_append(self, atoms, backend)
        if self.subtype == 'normal' and atoms is not None and getattr(atoms, "parallel", False):
            self.atoms = asap3.Collector(atoms)
        
    def _set_backend(self, backend=None):
        """Set the backed doing the actual I/O."""
        if backend is not None:
            self.backend_name = backend
        if self.backend_name == 'pickle':
            raise OSError('BundleTrajectory no longer suppports the unsafe pickle backend.')
        elif self.backend_name == 'ulm':
            if self.subtype == 'normal':
                # Use the standard ASE backend
                self.backend = UlmBundleBackend(self.master, self.singleprecision)
            elif self.subtype == 'split':
                self.backend = UlmSplitBundleBackend(self.master,
                                                     self.iolimit,
                                                     self.singleprecision)            
        else:
            raise NotImplementedError(
                "This version of ASE/Asap cannot use BundleTrajectory with backend '%s'"
                % self.backend_name)

    def write(self, atoms=None):
        if self.subtype == 'normal' and atoms is not None and getattr(atoms, "parallel", False):
            atoms = asap3.Collector(atoms)
        _BundleTrajectory.write(self, atoms)

    def _make_bundledir(self, filename):
        """Make the main bundle directory.

        Since all MPI tasks might write to it, all tasks must wait for
        the directory to appear.

        For performance reasons, the first frame directory is created immediately.
        """
        assert not os.path.isdir(filename)
        world.barrier()
        if self.master:
            self.log("Making directory "+filename)
            os.mkdir(filename)
            framedir = os.path.join(filename, "F0")
            self.log("Making directory "+ framedir)    
            os.mkdir(framedir)
            world.barrier()
        else:
            world.barrier()
            i = 0
            while not os.path.isdir(filename):
                time.sleep(1)
                i += 1
            if i > 10:
                self.log("Waiting %d seconds for %s to appear!"
                         % (i, filename))

    def _make_framedir(self, frame):
        """Make subdirectory for the frame.

        For a split bundle, all MPI tasks write to the frame
        directory.  The slaves must therefore wait until it becomes
        available.  To minimize the waiting time, frames are
        pre-created.
        """
        if self.subtype == 'split':
            numdirs = 10
        else:
            numdirs = 1
        if self.master:
            for i in range(frame, frame+numdirs):
                framedir = os.path.join(self.filename, "F"+str(i))
                if not os.path.exists(framedir):
                    self.log("Making directory " + framedir)
                    os.mkdir(framedir)
        framedir = os.path.join(self.filename, "F"+str(frame))
        # Wait for the directory to appear
        world.barrier()
        i = 0
        while not os.path.isdir(framedir):
            time.sleep(1)
            i += 1
        if i > 10:
            self.log("Waiting %d seconds for %s to appear!"
                     % (i, framedir))
        return framedir

    def close(self):
        """Clean up when closing."""
        if self.state == 'write' and self.master:
            i = self.nframes
            while True:
                fname = os.path.join(self.filename, "F" + str(i))
                if not os.path.exists(fname):
                    break
                self.log("Closing, removing empty directory "+fname)
                os.rmdir(fname)
                i += 1
        _BundleTrajectory.close(self)

    def __del__(self):
        if self.state != 'closed':
            self.close()

    def get_atoms_distributed(self, n, cpus='auto', extra=None, verbose=True):
        """Return Atoms object number n from the trajectory.

        traj.get_atoms_distributed(n) reads the atoms from a
        BundleTrajectory written in split mode without needing to store
        everything in RAM on the master.  The master reads each file
        in the bundle, and transmits it to the slaves.  At the end,
        a distribution is made.

        Parameters:

        n: Which frame to read.  Use -1 for the last one.
        
        Optional parameters:
        cpus (default: 'auto'):  CPU layout to use, or the keyword 'auto'
            to figure it out automatically.
        
        extra:
            A list of names of extra arrays that should be read from the 
            input file.  The data is available with atoms.get_array.

        verbose (default: True):  Whether log messages should be written.
        """
        if verbose and (world.rank == 0 or verbose >= 2):
            if verbose >= 2:
                verbfile = open(f"get_atoms_distributed_{world.rank}.log", "w", 1)
            else:
                verbfile = sys.stdout
            def printlog(txt, *args):
                if world.rank == 0:
                    print(f"{time.asctime()}: {txt}", *args, file=verbfile)
        else:
            def printlog(txt, *args, **kwargs):
                pass
        if self.state != 'read':
            raise OSError(f'Cannot read in {self.state} mode')
        if n < 0:
            n += self.nframes
        if n < 0 or n >= self.nframes:
            raise IndexError('Trajectory index %d out of range [0, %d['
                             % (n, self.nframes))

        printlog(f"Beginning distributed read of {self.filename} frame {n}")
        if self.subtype != 'split':
            raise RuntimeError("Distributed read only possible for subtype='split'")
        if world.rank == 0:
            framedir = os.path.join(self.filename, 'F' + str(n))
            framezero = os.path.join(self.filename, 'F0')
            smalldata = self.backend.read_small(framedir)
            data = {}
            data['pbc'] = smalldata['pbc']
            assert data['pbc'].shape == (3,)
            data['cell'] = smalldata['cell'].astype(np.float64)
            assert data['cell'].shape == (3,3)
            data['constraint'] = smalldata['constraints']
            if data['constraint']:
                raise RuntimeError("Distributed read not possible: constraints are present.")
            natoms = np.zeros(1, np.int64)
            natoms[0] = smalldata['natoms']
            # The following data is NOT distributed
            nfragments = smalldata['fragments']
            smalldata0 = self.backend.read_small(framezero)
            nfragments0 = smalldata0['fragments']
        else:
            data = {}
            data['pbc'] = np.zeros((3,), dtype=np.bool)
            data['cell'] = np.zeros((3,3), dtype=np.float64)
            data['constraint'] = []
            natoms = np.zeros(1, np.int64)
        world.broadcast(data['pbc'], 0)
        world.broadcast(data['cell'], 0)
        world.broadcast(natoms, 0)
        natoms = natoms[0]
        # Which atoms should this process keep?
        begin_atom = world.rank * natoms // world.size
        end_atom = (world.rank + 1) * natoms // world.size
        # Create the empty atoms object
        atoms = ase.Atoms(**data)
        printlog("Beginning distribution of data.")
        printinterval = 100
        # Find which datatypes to send, and in which order.
        arraynames = ['positions', 'numbers', 'tags', 'masses', 'momenta']
        if extra is not None:
            arraynames.extend(extra)
        my_idarray = None
        for name in arraynames:
            if world.rank == 0:
                # The master decides if we send, and from which frame
                use = self.datatypes.get(name)
                if use == 'once':
                    nframes = np.array([nfragments0,], dtype=int)
                elif use:
                    nframes = np.array([nfragments,], dtype=int)
                else:
                    nframes = np.array([0,], dtype=int)
            else:
                nframes = np.zeros(1, dtype=int)
            world.broadcast(nframes, 0)
            nframes = nframes[0]
            if nframes:
                printlog(f"Transmitting {name} in {nframes} blocks")
                myarray = None  # No data yet.
                for frame in range(nframes):
                    if world.rank == 0:
                        # Read the data for later broadcast.
                        if use == 'once':
                            dirname = framezero
                        else:
                            dirname = framedir
                        ids = self.backend.read(dirname, 'ID_'+str(frame))
                        data = self.backend.read(dirname, name + '_' + str(frame))
                        info = {'dtype': str(data.dtype), 'dtype_id': str(ids.dtype),
                                'shape': data.shape}
                        ase.parallel.broadcast(info, 0, world)
                    else:
                        info = ase.parallel.broadcast(None, 0, world)
                        info['dtype_id'] = getattr(np, info['dtype_id'])
                        info['dtype'] = getattr(np, info['dtype'])
                        ids = np.zeros(info['shape'][0], dtype=info['dtype_id'])
                        data = np.zeros(info['shape'], dtype=info['dtype'])
                    if frame % printinterval == 0:
                        printlog("   block {}, shape={}, dtype={}".format(frame,
                                                                             str(info['shape']),
                                                                             str(info['dtype'])))
                    world.broadcast(ids, 0)
                    world.broadcast(data, 0)
                    # Now all processes have this chunck of data.  Extract what we need.
                    if myarray is None:
                        myarrayshape = list(data.shape)
                        myarrayshape[0] = end_atom - begin_atom
                        myarray = np.zeros(tuple(myarrayshape), dtype=data.dtype)
                    if my_idarray is None:
                        # Create it as soon as we know know the dtype
                        my_idarray = np.arange(begin_atom, end_atom, dtype=ids.dtype)
                        atoms.arrays['ID'] = my_idarray
                        my_idarray_sanity = np.zeros(my_idarray.shape, dtype=my_idarray.dtype)
                    keep = np.logical_and(ids >= begin_atom, ids < end_atom)
                    ids = ids[keep]
                    idx = ids - begin_atom
                    assert (my_idarray[idx] == ids).all()
                    myarray[idx] = data[keep] # Assign the data to the relevant elements.
                    my_idarray_sanity[idx] = ids
                # We now have the whole array.
                # First check that we got all elements.
                assert (my_idarray == my_idarray_sanity).all()
                atoms.arrays[name] = myarray
            else:
                printlog("Not transmitting", name)
        printlog("All data distributed.")
        if cpus == 'auto':
            printlog("Calculating automatic CPU layout.")
            num_cores = world.size
            printlog("   num cpus:", num_cores)
            printlog("   cell:", np.diag(atoms.cell).tolist())
            cpus = cpu_setup.calculate_optimal_cpu_setup(num_cores, np.diag(atoms.cell).tolist())
            printlog("   cpu setup:", cpus)
            cpus = ase.parallel.broadcast(cpus, 0, world)
        printlog("Redistributing atoms according to positions.")
        atoms = asap3.MakeParallelAtoms(atoms, cpus)
        printlog("Redistribution done.")
        return atoms

class UlmSplitBundleBackend(UlmBundleBackend):
    """A special backend for writing split bundles (ASAP only)."""
    def __init__(self, master, iolimit, singleprecision):
        # Store if this backend will actually write anything
        UlmBundleBackend.__init__(self, master, singleprecision)
        self.writesmall = master
        self.writelarge = True
        self.writenonarray = master
        self.iolimit = iolimit
        if iolimit:
            self.iostart = np.round(
                np.linspace(0, world.size, iolimit+1)).astype(int)
            self.iotag = 797525
        self.lastwritedir = None

    def write_small(self, framedir, smalldata):
        "Write small data to be written jointly."
        smalldata['fragments'] = world.size
        UlmBundleBackend.write_small(self, framedir, smalldata)

    def write(self, framedir, name, data):
        "Write data to separate file."
        if hasattr(data, "shape"):
            # We need to store which kind of data was written in this frame 
            # so NFS synchronization is possible when closing file.
            if framedir != self.lastwritedir:
                self.lastwritedir = framedir
                self.writenames = []
            self.writenames.append(name)
            # As expected, we are writing a NumPy array
            self.iosync_start()
            name = "%s_%d" % (name, world.rank)
            UlmBundleBackend.write(self, framedir, name, data)
            self.iosync_end()
        elif self.writenonarray:
            # If the data is not a NumPy array, only the master writes.
            UlmBundleBackend.write(self, framedir, name, data)

    def read(self, framedir, name):
        "Read data from separate file."
        self.iosync_start()
        x = UlmBundleBackend.read(self, framedir, name)
        self.iosync_end()
        return x

    def iosync_start(self):
        "Prevents too many simultaneous IO tasks from trashing server."
        if self.iolimit and world.rank not in self.iostart:
            # I must wait.
            token = np.zeros(1, int)
            world.receive(token, world.rank-1, self.iotag)

    def iosync_end(self):
        if self.iolimit and world.rank+1 not in self.iostart:
            # Another task is waiting for me.
            token = np.zeros(1, int)
            world.send(token, world.rank+1, self.iotag)

    def close(self, log=None):
        """Make sure that all data is available on disk for all MPI tasks."""
        if self.lastwritedir:
            for name in self.writenames:
                for part in range(world.size):
                    fname = os.path.join(self.lastwritedir, "%s_%d.ulm" % (name, part))
                    if not os.path.exists(fname):
                        if log:
                            log.write("Task %i is waiting for '%s' to appear.\n" %
                                      (world.rank, fname))
                        for i in range(20):
                            time.sleep(5)
                            if os.path.exists(fname):
                                break
                        if not os.path.exists(fname) and log:
                            log.write("WARNING: Task %i gave up waiting for '%s'.\n" %
                                      (world.rank, fname))
        self.lastwritedir = None  # Do not repeat the above.
