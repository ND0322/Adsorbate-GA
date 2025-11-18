"""
Module potential_simple_module


Defined at Potential_simple.fpp lines 145-1509

The Potential_simple module handles the first-level selection of the
desidered force field(tight-binding \texttt{TB_type}, empirical potential \texttt{IP_type} or
hybrid description \texttt{FilePot_type}).
It contains the interfaces \texttt{Initialise}, \texttt{Finalise}, \texttt{cutoff},
\texttt{Calc}, \texttt{Print}, which have the only role to
re-addressing the calls to the corresponding
modules.
A Potential object simply contains a pointer to the desired force field type
(only one of the three can be selected).
It is initialised with
>    call Initialise(pot,arg_str,io_obj,[mpi_obj])
where, \texttt{arg_str} is a string defining the potential type and
possible some additional options.
For interatomic potentials \texttt{arg_str} will start with 'IP'; there are several different IPs defined:
see documentation for the 'IP_module' module. For tight binding, 'arg_str' should start with 'TB';
see docuementation for 'TB_module' for more details.
"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy
from quippy.tb_module import TB_type

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("quippy.Potential_Simple")
class Potential_Simple(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=potential_simple)
    
    
    Defined at Potential_simple.fpp lines 169-181
    
    """
    def __init__(self, args_str, filename, no_parallel=None, error=None, handle=None):
        """
        self = Potential_Simple(args_str, filename[, no_parallel, error])
        
        
        Defined at Potential_simple.fpp lines 223-236
        
        Parameters
        ----------
        args_str : str
        filename : str
        no_parallel : bool
        error : int
        
        Returns
        -------
        this : Potential_Simple
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_potential_simple_filename_initialise(args_str=args_str, filename=filename, \
            no_parallel=no_parallel, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Potential_Simple
        
        
        Defined at Potential_simple.fpp lines 345-365
        
        Parameters
        ----------
        this : Potential_Simple
        error : int
        
        Finalise the Potential_Simple object
        """
        if self._alloc:
            quippy._quippy.f90wrap_potential_simple_finalise(this=self._handle, error=error)
    
    def print(self, file=None, dict=None, error=None):
        """
        print(self[, file, dict, error])
        
        
        Defined at Potential_simple.fpp lines 1403-1423
        
        Parameters
        ----------
        this : Potential_Simple
        file : Inoutput
        dict : Dictionary
        error : int
        
        Print potential details
        """
        quippy._quippy.f90wrap_potential_simple_print(this=self._handle, file=None if file is None else file._handle, dict=None \
            if dict is None else dict._handle, error=error)
    
    def cutoff(self):
        """
        potential_simple_cutoff = cutoff(self)
        
        
        Defined at Potential_simple.fpp lines 367-382
        
        Parameters
        ----------
        this : Potential_Simple
        
        Returns
        -------
        potential_simple_cutoff : float
        
        Set potential cutoff
        """
        potential_simple_cutoff = quippy._quippy.f90wrap_potential_simple_cutoff(this=self._handle)
        return potential_simple_cutoff
    
    def calc(self, at, args_str=None, error=None):
        """
        calc(self, at[, args_str, error])
        
        
        Defined at Potential_simple.fpp lines 384-1385
        
        Parameters
        ----------
        this : Potential_Simple
        at : Atoms
        	The atoms structure to compute energy and forces
        
        args_str : str
        error : int
        
        Potential_Simple calculator for energy, forces and virial
        
        .. rubric:: args_str options
        
        ======================== ===== ====== =================================================================
        Name                     Type  Value  Doc                                                              
        ======================== ===== ====== =================================================================
        single_cluster           bool  F      If true, calculate all active/transition atoms with a single big 
                                              cluster                                                          
        run_suffix               None         suffix to append to hybrid_mark field used                       
        carve_cluster            bool  T      If true, calculate active region atoms by carving out a cluster  
        little_clusters          bool  F      If true, calculate forces(only) by doing each atom separately    
                                              surrounded by a little buffer cluster                            
        partition_k_clusters     int   0      If given and K > 1, partition QM core region into K sub-clusters 
                                              using partition_qm_list() routine                                
        partition_nneightol      float 0.0    If given override at%nneightol used to generate connectivity     
                                              matrix for partitioning                                          
        partition_do_ripening    bool  F      If true, enable digestive ripening to refine the METIS-generated 
                                              K-way partitioning(not yet implemented)                          
        cluster_box_buffer       float 0.0    If present, quickly cut out atoms in box within                  
                                              cluster_box_radius of any active atoms, rather than doing it     
                                              properly                                                         
        r_scale                  float 1.0    rescale calculated positions(and correspondingly forces) by this 
                                              factor                                                           
        E_scale                  float 1.0    rescale calculate energies(and correspondingly forces) by this   
                                              factor                                                           
        use_ridders              bool  F      If true and using numerical derivatives, use the Ridders method. 
        force_using_fd           bool  F      If true, and if 'force' is also present in the argument list,    
                                              calculate forces using finite difference.                        
        force_fd_delta           float 1.0e-4 Displacement to use with finite difference force calculation     
        virial_using_fd          bool  F      If true, and if 'virial' is also present in the argument list,   
                                              calculate virial using finite difference.                        
        virial_fd_delta          float 1.0e-4 Displacement to use with finite difference virial calculation    
        energy                   None         If present, calculate energy and put it in field with this       
                                              string as name                                                   
        force                    None         If present, calculate force and put it in field with this string 
                                              as name                                                          
        local_energy             None         If present, calculate local_energy and put it in field with this 
                                              string as name                                                   
        virial                   None         If present, calculate virial and put it in field with this       
                                              string as name                                                   
        local_virial             None         If present, calculate local_virial and put it in field with this 
                                              string as name                                                   
        read_extra_param_list    None         if single_cluster=T and carve_cluster=T, extra params to copy    
                                              back from cluster                                                
        read_extra_property_list None         if single_cluster=T and carve_cluster=T, extra properties to     
                                              copy back from cluster                                           
        ======================== ===== ====== =================================================================
        
        
        """
        quippy._quippy.f90wrap_potential_simple_calc(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    def setup_parallel(self, at, args_str, error=None):
        """
        setup_parallel(self, at, args_str[, error])
        
        
        Defined at Potential_simple.fpp lines 1425-1473
        
        Parameters
        ----------
        this : Potential_Simple
        at : Atoms
        	The atoms structure to compute energy and forces
        
        args_str : str
        error : int
        
        Set up what you need for parallel calculation
        
        .. rubric:: args_str options
        
        ====== ==== ===== =====================================================================================
        Name   Type Value Doc                                                                                  
        ====== ==== ===== =====================================================================================
        energy None       If present, calculate energy. Also name of parameter to put energy into              
        force  None       If present, calculate forces. Also name of property to put forces into               
        ====== ==== ===== =====================================================================================
        
        
        """
        quippy._quippy.f90wrap_potential_simple_setup_parallel(this=self._handle, at=at._handle, args_str=args_str, error=error)
    
    def calc_tb_matrices(self, at, args_str=None, hd=None, sd=None, hz=None, sz=None, dh=None, ds=None, index_bn=None, \
        error=None):
        """
        calc_tb_matrices(self, at[, args_str, hd, sd, hz, sz, dh, ds, index_bn, error])
        
        
        Defined at Potential_simple.fpp lines 1489-1509
        
        Parameters
        ----------
        this : Potential_Simple
        at : Atoms
        args_str : str
        hd : float array
        sd : float array
        hz : complex array
        sz : complex array
        dh : float array
        ds : float array
        index_bn : int
        error : int
        
        """
        quippy._quippy.f90wrap_potential_simple_calc_tb_matrices(this=self._handle, at=at._handle, args_str=args_str, hd=hd, \
            sd=sd, hz=hz, sz=sz, dh=dh, ds=ds, index_bn=index_bn, error=error)
    
    def _initialise_inoutput(self, args_str, io_obj, no_parallel=None, error=None):
        """
        _initialise_inoutput(self, args_str, io_obj[, no_parallel, error])
        
        
        Defined at Potential_simple.fpp lines 238-261
        
        Parameters
        ----------
        this : Potential_Simple
        args_str : str
        io_obj : Inoutput
        no_parallel : bool
        error : int
        
        """
        quippy._quippy.f90wrap_potential_simple_initialise_inoutput(this=self._handle, args_str=args_str, io_obj=io_obj._handle, \
            no_parallel=no_parallel, error=error)
    
    def _initialise_str(self, args_str, param_str=None, error=None):
        """
        _initialise_str(self, args_str[, param_str, error])
        
        
        Defined at Potential_simple.fpp lines 263-343
        
        Parameters
        ----------
        this : Potential_Simple
        args_str : str
        param_str : str
        error : int
        
        
        .. rubric:: args_str options
        
        =============== ==== ===== ============================================================================
        Name            Type Value Doc                                                                         
        =============== ==== ===== ============================================================================
        TB              None false If true, a tight-binding model                                              
        IP              None false If true, an interatomic potential model                                     
        FilePot         None false If true, a potential that interacts with another executable by              
                                   reading/writing files                                                       
        wrapper         None false If true, a hardcoded wrapper function                                       
        CallbackPot     None false If true, a callback potential(calls arbitrary passed by user)               
        SocketPot       None false If true, a socket potential that communicates via TCP/IP sockets            
        little_clusters None false If true, uses little cluster, calculate forces only                         
        force_using_fd  bool F     If true, and if 'force' is also present in the calc argument list,          
                                   calculate forces using finite difference.                                   
        virial_using_fd bool F     If true, and if 'virial' is also present in the calc argument list,         
                                   calculate virial using finite difference.                                   
        =============== ==== ===== ============================================================================
        
        
        """
        quippy._quippy.f90wrap_potential_simple_initialise_str(this=self._handle, args_str=args_str, param_str=param_str, \
            error=error)
    
    def initialise(*args, **kwargs):
        """
        initialise(*args, **kwargs)
        
        
        Defined at Potential_simple.fpp lines 186-187
        
        Overloaded interface containing the following procedures:
          _initialise_inoutput
          _initialise_str
        
        Initialise a Potential object(selecting the force field) and, if necessary, the input file for potential parameters.
        """
        for proc in [Potential_Simple._initialise_inoutput, Potential_Simple._initialise_str]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    @property
    def type_args_str(self):
        """
        Element type_args_str ftype=character(len=124) pytype=str
        
        
        Defined at Potential_simple.fpp line 171
        
        """
        return quippy._quippy.f90wrap_potential_simple__get__type_args_str(self._handle)
    
    @type_args_str.setter
    def type_args_str(self, type_args_str):
        quippy._quippy.f90wrap_potential_simple__set__type_args_str(self._handle, type_args_str)
    
    @property
    def tb(self):
        """
        Element tb ftype=type(tb_type) pytype=Tb_Type
        
        
        Defined at Potential_simple.fpp line 173
        
        """
        tb_handle = quippy._quippy.f90wrap_potential_simple__get__tb(self._handle)
        if tuple(tb_handle) in self._objs:
            tb = self._objs[tuple(tb_handle)]
        else:
            tb = TB_type.from_handle(tb_handle)
            self._objs[tuple(tb_handle)] = tb
        return tb
    
    @tb.setter
    def tb(self, tb):
        tb = tb._handle
        quippy._quippy.f90wrap_potential_simple__set__tb(self._handle, tb)
    
    @property
    def is_wrapper(self):
        """
        Element is_wrapper ftype=logical pytype=bool
        
        
        Defined at Potential_simple.fpp line 178
        
        """
        return quippy._quippy.f90wrap_potential_simple__get__is_wrapper(self._handle)
    
    @is_wrapper.setter
    def is_wrapper(self, is_wrapper):
        quippy._quippy.f90wrap_potential_simple__set__is_wrapper(self._handle, is_wrapper)
    
    @property
    def little_clusters(self):
        """
        Element little_clusters ftype=logical pytype=bool
        
        
        Defined at Potential_simple.fpp line 179
        
        """
        return quippy._quippy.f90wrap_potential_simple__get__little_clusters(self._handle)
    
    @little_clusters.setter
    def little_clusters(self, little_clusters):
        quippy._quippy.f90wrap_potential_simple__set__little_clusters(self._handle, little_clusters)
    
    @property
    def force_using_fd(self):
        """
        Element force_using_fd ftype=logical pytype=bool
        
        
        Defined at Potential_simple.fpp line 180
        
        """
        return quippy._quippy.f90wrap_potential_simple__get__force_using_fd(self._handle)
    
    @force_using_fd.setter
    def force_using_fd(self, force_using_fd):
        quippy._quippy.f90wrap_potential_simple__set__force_using_fd(self._handle, force_using_fd)
    
    @property
    def virial_using_fd(self):
        """
        Element virial_using_fd ftype=logical pytype=bool
        
        
        Defined at Potential_simple.fpp line 181
        
        """
        return quippy._quippy.f90wrap_potential_simple__get__virial_using_fd(self._handle)
    
    @virial_using_fd.setter
    def virial_using_fd(self, virial_using_fd):
        quippy._quippy.f90wrap_potential_simple__set__virial_using_fd(self._handle, virial_using_fd)
    
    def __str__(self):
        ret = ['<potential_simple>{\n']
        ret.append('    type_args_str : ')
        ret.append(repr(self.type_args_str))
        ret.append(',\n    tb : ')
        ret.append(repr(self.tb))
        ret.append(',\n    is_wrapper : ')
        ret.append(repr(self.is_wrapper))
        ret.append(',\n    little_clusters : ')
        ret.append(repr(self.little_clusters))
        ret.append(',\n    force_using_fd : ')
        ret.append(repr(self.force_using_fd))
        ret.append(',\n    virial_using_fd : ')
        ret.append(repr(self.virial_using_fd))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "potential_simple_module".')

for func in _dt_array_initialisers:
    func()
