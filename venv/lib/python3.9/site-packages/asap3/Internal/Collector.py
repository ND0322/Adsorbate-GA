"""Asap module Collector.

Defines a filter collecting all information about parallel atoms on the master.
"""

import asap3
import numpy as np

class Collector:
    "Atoms-like filter collecting information on the master node."
    _is_asap_collector_object=True

    def __init__(self, atoms, master=None, allow_forces=False, noconstraints=True):
        self.atoms = atoms
        self.comm = atoms.get_comm()
        self.allow_forces = allow_forces
        if master is None:
            master = (self.comm.rank == 0)
        self.master = master
        if noconstraints:
            self.constraints = []
        else:
            self.constraints = self.atoms.constraints
        self.reset_collector()
        
    def reset_collector(self):
        """Cache some stuff so Trajectory does not block."""
        self._n = self.atoms.get_global_number_of_atoms()
        try:
            del self.numbers
        except AttributeError:
            pass
        self.numbers = self.get_atomic_numbers()

    def __len__(self):
        if self.master:
            return self._n
        else:
            return 0

    def get_global_number_of_atoms(self):
        return self.atoms.get_global_number_of_atoms()

    # Compatibility with ASE 3.18.0 and earlier
    get_number_of_atoms = get_global_number_of_atoms

    def get_positions(self):
        return self.collect(self.atoms.get_positions)

    def get_forces(self):
        return self.collect(self.atoms.get_forces)

    def get_momenta(self):
        return self.collect(self.atoms.get_momenta)

    def get_atomic_numbers(self):
        if hasattr(self, "numbers"):
            return self.numbers
        else:
            return self.collect(self.atoms.get_atomic_numbers)
    
    def get_tags(self):
        return self.collect(self.atoms.get_tags)

    def get_potential_energy(self):
        return self.atoms.get_potential_energy()

    def get_cell(self):
        return self.atoms.get_cell()

    def get_calculator(self):
        """Return a fake calculator that makes Trajectory work when it calls calculation_required."""
        return CollectorCalculator(self.atoms.calc, self.allow_forces)

    @property
    def calc(self):
        """Calculator object."""
        return self.get_calculator()
    
    def get_stress(self):
        return self.atoms.get_stress()

    def get_pbc(self):
        return self.atoms.get_pbc()
    
    def get_info(self):
        return self.atoms.info
    
    def get_charges(self):
        raise asap3.PropertyNotImplementedError
    
    def get_array(self, label):
        return self.collect(lambda a=self.atoms, l=label: a.get_array(l))

    def has(self, name):
        """Check for existance of array.

        name must be one of: 'tags', 'momenta', 'masses', 'magmoms',
        'charges'.
        """
        if name in ['positions', 'tags', 'momenta', 'numbers']:
            return self.atoms.has(name) 
        else:
            return False

    def iterimages(self):
        """An atom is also a list of images."""
        yield self

    def collect(self, method):
        "Collect data from all cpus onto the master."
        ids = self.atoms.get_ids()
        data = method()
        n = self.atoms.get_global_number_of_atoms()
        if self.master:
            shape = (n,) + data.shape[1:]
            result = np.zeros(shape, data.dtype)
            for cpu in range(self.comm.size):
                if cpu != 0:
                    # Receive from cpu
                    nrecv = np.zeros(1, int)
                    self.comm.receive(nrecv, cpu)
                    nrecv = nrecv[0]
                    ids = np.zeros(nrecv, int)
                    data = np.zeros((nrecv,) + result.shape[1:], result.dtype)
                    self.comm.receive(ids, cpu)
                    self.comm.receive(data, cpu)
                result[ids] = data
            return result
        else:
            assert(len(data) == len(ids))
            nsend = np.array([len(ids)])
            self.comm.send(nsend, 0)
            self.comm.send(ids, 0)
            self.comm.send(data, 0)
            return np.zeros((0,)+data.shape[1:], dtype=data.dtype)

    def _cant_set_pbc(self, pbc):
        "Fake set_pbc method."
        raise NotImplementedError("Cannot change PBC of a Collector instance.")
    
    pbc = property(get_pbc, _cant_set_pbc, "The boundary conditions attribute")
    
    def _cant_set_numbers(self, z):
        "Fake set_atomic_numbers method."
        raise NotImplementedError(
            "Cannot change atomic numbers of a Collector instance.")
   
    def _cant_set_info(self, info):
        "Cannot set info attribute of Collector instance"
        raise NotImplementedError("Cannot set info attribute of Collector instance")
    
    info = property(get_info, _cant_set_info, "The info dictionary")
    
class CollectorCalculator:
    """Fake calculator object returned by Collector.
    
    This object implements the minimal interface Trajectory needs when it
    tries to write the Collector object as if it were an Atoms object, and
    needs to test which quantities are available.  The calls are forwarded to
    the real potential acting on the real atoms.
    """
    def __init__(self, calc, allow_forces):
        try:
            self.name = calc.name
        except AttributeError:
            try:
                self.name = "asap3." + calc._get_name()
            except AttributeError:
                self.name = calc.__class__.__name__
        self.allow_forces = allow_forces
        
    def calculation_required(self, atoms, props):
        if not self.allow_forces and 'forces' in props:
            return True
        assert isinstance(atoms, Collector)
        realcalc = atoms.atoms.calc
        x = realcalc.calculation_required(atoms.atoms, props)
        return x
    
    # def get_potential_energy(self, atoms):
    #     return atoms.atoms.get_potential_energy()
    
    # def get_forces(self, atoms):
    #     return atoms.atoms.get_forces()

    def get_property(self, prop, atoms, allow_calculation=True):
        assert isinstance(atoms, Collector)
        try:
            if (not allow_calculation and
                self.calculation_required(atoms, [prop])):
                return None
        except AttributeError:
            pass

        method = 'get_' + {'energy': 'potential_energy'}.get(prop, prop)
        try:
            result = getattr(atoms, method)()
        except AttributeError:
            raise asap3.PropertyNotImplementedError
        return result
    
                     
            
