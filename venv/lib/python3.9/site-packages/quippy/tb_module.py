"""
Module tb_module


Defined at TB.fpp lines 131-1984

General object which handles all the possible tight-binding potentials(TB), re-addressing
the calls to the right routines.

"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy
from quippy.atoms_types_module import Atoms

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("quippy.TB_type")
class TB_type(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=tb_type)
    
    
    Defined at TB.fpp lines 163-177
    
    """
    def tb_initialise_filename(self, args_str, filename, error=None):
        """
        tb_initialise_filename(self, args_str, filename[, error])
        
        
        Defined at TB.fpp lines 239-251
        
        Parameters
        ----------
        this : Tb_Type
        args_str : str
        filename : str
        error : int
        
        """
        quippy._quippy.f90wrap_tb_initialise_filename(this=self._handle, args_str=args_str, filename=filename, error=error)
    
    def tb_evals(self):
        """
        tb_evals = tb_evals(self)
        
        
        Defined at TB.fpp lines 1893-1900
        
        Parameters
        ----------
        this : Tb_Type
        
        Returns
        -------
        tb_evals : float array
        
        """
        tb_evals = quippy._quippy.f90wrap_tb_evals(this=self._handle)
        return tb_evals
    
    def absorption(self, polarization, freqs, gamma, a):
        """
        absorption(self, polarization, freqs, gamma, a)
        
        
        Defined at TB.fpp lines 1904-1956
        
        Parameters
        ----------
        this : Tb_Type
        polarization : complex array
        freqs : float array
        gamma : float
        a : float array
        
        """
        quippy._quippy.f90wrap_absorption(this=self._handle, polarization=polarization, freqs=freqs, gamma=gamma, a=a)
    
    def __del__(self):
        """
        Destructor for class Tb_Type
        
        
        Defined at TB.fpp lines 288-300
        
        Parameters
        ----------
        this : Tb_Type
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_tb_finalise(this=self._handle)
    
    def tb_cutoff(self):
        """
        tb_cutoff = tb_cutoff(self)
        
        
        Defined at TB.fpp lines 315-318
        
        Parameters
        ----------
        this : Tb_Type
        
        Returns
        -------
        tb_cutoff : float
        
        """
        tb_cutoff = quippy._quippy.f90wrap_tb_cutoff(this=self._handle)
        return tb_cutoff
    
    def tb_wipe(self):
        """
        tb_wipe(self)
        
        
        Defined at TB.fpp lines 302-313
        
        Parameters
        ----------
        this : Tb_Type
        
        """
        quippy._quippy.f90wrap_tb_wipe(this=self._handle)
    
    def tb_print(self, file=None):
        """
        tb_print(self[, file])
        
        
        Defined at TB.fpp lines 320-357
        
        Parameters
        ----------
        this : Tb_Type
        file : Inoutput
        
        """
        quippy._quippy.f90wrap_tb_print(this=self._handle, file=None if file is None else file._handle)
    
    def tb_setup_atoms(self, at, is_noncollinear=None, is_spinpol_no_scf=None, args_str=None, error=None):
        """
        tb_setup_atoms(self, at[, is_noncollinear, is_spinpol_no_scf, args_str, error])
        
        
        Defined at TB.fpp lines 366-378
        
        Parameters
        ----------
        this : Tb_Type
        at : Atoms
        is_noncollinear : bool
        is_spinpol_no_scf : bool
        args_str : str
        error : int
        
        """
        quippy._quippy.f90wrap_tb_setup_atoms(this=self._handle, at=at._handle, is_noncollinear=is_noncollinear, \
            is_spinpol_no_scf=is_spinpol_no_scf, args_str=args_str, error=error)
    
    def tb_calc(self, at, energy=None, local_e=None, forces=None, virial=None, local_virial=None, args_str=None, \
        use_fermi_e=None, fermi_e=None, fermi_t=None, band_width=None, dh=None, ds=None, index_bn=None, error=None):
        """
        tb_calc(self, at[, energy, local_e, forces, virial, local_virial, args_str, use_fermi_e, fermi_e, fermi_t, band_width, \
            dh, ds, index_bn, error])
        
        
        Defined at TB.fpp lines 552-679
        
        Parameters
        ----------
        this : Tb_Type
        at : Atoms
        energy : float
        local_e : float array
        forces : float array
        virial : float array
        local_virial : float array
        args_str : str
        use_fermi_e : bool
        fermi_e : float
        fermi_t : float
        band_width : float
        dh : float array
        ds : float array
        index_bn : int
        error : int
        
        
        .. rubric:: args_str options
        
        =============== ===== ===== ===========================================================================
        Name            Type  Value Doc                                                                        
        =============== ===== ===== ===========================================================================
        solver          None  DIAG  No help yet. This source file was $LastChangedBy$                          
        noncollinear    bool  F     No help yet. This source file was $LastChangedBy$                          
        spinpol_no_scf  bool  F     No help yet. This source file was $LastChangedBy$                          
        use_prev_charge bool  F     No help yet. This source file was $LastChangedBy$                          
        do_at_local_N   bool  F     No help yet. This source file was $LastChangedBy$                          
        do_evecs        bool  F     No help yet. This source file was $LastChangedBy$                          
        atom_mask_name  None  NONE  No help yet. This source file was $LastChangedBy$                          
        r_scale         float 1.0   Recaling factor for distances. Default 1.0.                                
        E_scale         float 1.0   Recaling factor for energy. Default 1.0.                                   
        =============== ===== ===== ===========================================================================
        
        
        """
        quippy._quippy.f90wrap_tb_calc(this=self._handle, at=at._handle, energy=energy, local_e=local_e, forces=forces, \
            virial=virial, local_virial=local_virial, args_str=args_str, use_fermi_e=use_fermi_e, fermi_e=fermi_e, \
            fermi_t=fermi_t, band_width=band_width, dh=dh, ds=ds, index_bn=index_bn, error=error)
    
    def tb_calc_diag(self, use_fermi_e=None, fermi_e=None, fermi_t=None, local_e=None, forces=None, virial=None, \
        use_prev_charge=None, do_evecs=None, dh=None, ds=None, index_bn=None, error=None):
        """
        tb_calc_diag = tb_calc_diag(self[, use_fermi_e, fermi_e, fermi_t, local_e, forces, virial, use_prev_charge, do_evecs, \
            dh, ds, index_bn, error])
        
        
        Defined at TB.fpp lines 710-885
        
        Parameters
        ----------
        this : Tb_Type
        use_fermi_e : bool
        fermi_e : float
        fermi_t : float
        local_e : float array
        forces : float array
        virial : float array
        use_prev_charge : bool
        do_evecs : bool
        dh : float array
        ds : float array
        index_bn : int
        error : int
        
        Returns
        -------
        tb_calc_diag : float
        
        
        .. rubric:: args_str options
        
        ================= ==== ========================== =====================================================
        Name              Type Value                      Doc                                                  
        ================= ==== ========================== =====================================================
        fermi_e_precision None ''//this%fermi_E_precision No help yet. This source file was $LastChangedBy$    
        ================= ==== ========================== =====================================================
        
        
        """
        tb_calc_diag = quippy._quippy.f90wrap_tb_calc_diag(this=self._handle, use_fermi_e=use_fermi_e, fermi_e=fermi_e, \
            fermi_t=fermi_t, local_e=local_e, forces=forces, virial=virial, use_prev_charge=use_prev_charge, do_evecs=do_evecs, \
            dh=dh, ds=ds, index_bn=index_bn, error=error)
        return tb_calc_diag
    
    def tb_calc_gf(self, use_fermi_e=None, fermi_e=None, fermi_t=None, band_width=None, local_e=None, forces=None):
        """
        tb_calc_gf = tb_calc_gf(self[, use_fermi_e, fermi_e, fermi_t, band_width, local_e, forces])
        
        
        Defined at TB.fpp lines 887-1037
        
        Parameters
        ----------
        this : Tb_Type
        use_fermi_e : bool
        fermi_e : float
        fermi_t : float
        band_width : float
        local_e : float array
        forces : float array
        
        Returns
        -------
        tb_calc_gf : float
        
        """
        tb_calc_gf = quippy._quippy.f90wrap_tb_calc_gf(this=self._handle, use_fermi_e=use_fermi_e, fermi_e=fermi_e, \
            fermi_t=fermi_t, band_width=band_width, local_e=local_e, forces=forces)
        return tb_calc_gf
    
    def tb_copy_matrices(self, hd=None, sd=None, hz=None, sz=None, index_bn=None):
        """
        tb_copy_matrices(self[, hd, sd, hz, sz, index_bn])
        
        
        Defined at TB.fpp lines 359-364
        
        Parameters
        ----------
        this : Tb_Type
        hd : float array
        sd : float array
        hz : complex array
        sz : complex array
        index_bn : int
        
        """
        quippy._quippy.f90wrap_tb_copy_matrices(this=self._handle, hd=hd, sd=sd, hz=hz, sz=sz, index_bn=index_bn)
    
    def __init__(self, handle=None):
        """
        self = Tb_Type()
        
        
        Defined at TB.fpp lines 163-177
        
        
        Returns
        -------
        this : Tb_Type
        	Object to be constructed
        
        
        Automatically generated constructor for tb_type
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_tb_type_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def _tb_initialise_inoutput(self, args_str, io_obj=None, error=None):
        """
        _tb_initialise_inoutput(self, args_str[, io_obj, error])
        
        
        Defined at TB.fpp lines 253-272
        
        Parameters
        ----------
        this : Tb_Type
        args_str : str
        io_obj : Inoutput
        error : int
        
        """
        quippy._quippy.f90wrap_tb_initialise_inoutput(this=self._handle, args_str=args_str, io_obj=None if io_obj is None else \
            io_obj._handle, error=error)
    
    def _tb_initialise_str(self, args_str, param_str, error=None):
        """
        _tb_initialise_str(self, args_str, param_str[, error])
        
        
        Defined at TB.fpp lines 274-286
        
        Parameters
        ----------
        this : Tb_Type
        args_str : str
        param_str : str
        error : int
        
        """
        quippy._quippy.f90wrap_tb_initialise_str(this=self._handle, args_str=args_str, param_str=param_str, error=error)
    
    def initialise(*args, **kwargs):
        """
        initialise(*args, **kwargs)
        
        
        Defined at TB.fpp lines 181-182
        
        Overloaded interface containing the following procedures:
          _tb_initialise_inoutput
          _tb_initialise_str
        
        """
        for proc in [TB_type._tb_initialise_inoutput, TB_type._tb_initialise_str]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    @property
    def at(self):
        """
        Element at ftype=type(atoms) pytype=Atoms
        
        
        Defined at TB.fpp line 165
        
        """
        at_handle = quippy._quippy.f90wrap_tb_type__get__at(self._handle)
        if tuple(at_handle) in self._objs:
            at = self._objs[tuple(at_handle)]
        else:
            at = Atoms.from_handle(at_handle)
            self._objs[tuple(at_handle)] = at
        return at
    
    @at.setter
    def at(self, at):
        at = at._handle
        quippy._quippy.f90wrap_tb_type__set__at(self._handle, at)
    
    @property
    def method(self):
        """
        Element method ftype=integer  pytype=int
        
        
        Defined at TB.fpp line 166
        
        """
        return quippy._quippy.f90wrap_tb_type__get__method(self._handle)
    
    @method.setter
    def method(self, method):
        quippy._quippy.f90wrap_tb_type__set__method(self._handle, method)
    
    @property
    def calc_done(self):
        """
        Element calc_done ftype=logical pytype=bool
        
        
        Defined at TB.fpp line 172
        
        """
        return quippy._quippy.f90wrap_tb_type__get__calc_done(self._handle)
    
    @calc_done.setter
    def calc_done(self, calc_done):
        quippy._quippy.f90wrap_tb_type__set__calc_done(self._handle, calc_done)
    
    @property
    def fermi_e(self):
        """
        Element fermi_e ftype=real(dp) pytype=float
        
        
        Defined at TB.fpp line 173
        
        """
        return quippy._quippy.f90wrap_tb_type__get__fermi_e(self._handle)
    
    @fermi_e.setter
    def fermi_e(self, fermi_e):
        quippy._quippy.f90wrap_tb_type__set__fermi_e(self._handle, fermi_e)
    
    @property
    def fermi_t(self):
        """
        Element fermi_t ftype=real(dp) pytype=float
        
        
        Defined at TB.fpp line 173
        
        """
        return quippy._quippy.f90wrap_tb_type__get__fermi_t(self._handle)
    
    @fermi_t.setter
    def fermi_t(self, fermi_t):
        quippy._quippy.f90wrap_tb_type__set__fermi_t(self._handle, fermi_t)
    
    @property
    def fermi_e_precision(self):
        """
        Element fermi_e_precision ftype=real(dp) pytype=float
        
        
        Defined at TB.fpp line 174
        
        """
        return quippy._quippy.f90wrap_tb_type__get__fermi_e_precision(self._handle)
    
    @fermi_e_precision.setter
    def fermi_e_precision(self, fermi_e_precision):
        quippy._quippy.f90wrap_tb_type__set__fermi_e_precision(self._handle, fermi_e_precision)
    
    @property
    def homo_e(self):
        """
        Element homo_e ftype=real(dp) pytype=float
        
        
        Defined at TB.fpp line 175
        
        """
        return quippy._quippy.f90wrap_tb_type__get__homo_e(self._handle)
    
    @homo_e.setter
    def homo_e(self, homo_e):
        quippy._quippy.f90wrap_tb_type__set__homo_e(self._handle, homo_e)
    
    @property
    def lumo_e(self):
        """
        Element lumo_e ftype=real(dp) pytype=float
        
        
        Defined at TB.fpp line 175
        
        """
        return quippy._quippy.f90wrap_tb_type__get__lumo_e(self._handle)
    
    @lumo_e.setter
    def lumo_e(self, lumo_e):
        quippy._quippy.f90wrap_tb_type__set__lumo_e(self._handle, lumo_e)
    
    @property
    def init_args_str(self):
        """
        Element init_args_str ftype=character(len=1024) pytype=str
        
        
        Defined at TB.fpp line 176
        
        """
        return quippy._quippy.f90wrap_tb_type__get__init_args_str(self._handle)
    
    @init_args_str.setter
    def init_args_str(self, init_args_str):
        quippy._quippy.f90wrap_tb_type__set__init_args_str(self._handle, init_args_str)
    
    @property
    def calc_args_str(self):
        """
        Element calc_args_str ftype=character(len=1024) pytype=str
        
        
        Defined at TB.fpp line 177
        
        """
        return quippy._quippy.f90wrap_tb_type__get__calc_args_str(self._handle)
    
    @calc_args_str.setter
    def calc_args_str(self, calc_args_str):
        quippy._quippy.f90wrap_tb_type__set__calc_args_str(self._handle, calc_args_str)
    
    def __str__(self):
        ret = ['<tb_type>{\n']
        ret.append('    at : ')
        ret.append(repr(self.at))
        ret.append(',\n    method : ')
        ret.append(repr(self.method))
        ret.append(',\n    calc_done : ')
        ret.append(repr(self.calc_done))
        ret.append(',\n    fermi_e : ')
        ret.append(repr(self.fermi_e))
        ret.append(',\n    fermi_t : ')
        ret.append(repr(self.fermi_t))
        ret.append(',\n    fermi_e_precision : ')
        ret.append(repr(self.fermi_e_precision))
        ret.append(',\n    homo_e : ')
        ret.append(repr(self.homo_e))
        ret.append(',\n    lumo_e : ')
        ret.append(repr(self.lumo_e))
        ret.append(',\n    init_args_str : ')
        ret.append(repr(self.init_args_str))
        ret.append(',\n    calc_args_str : ')
        ret.append(repr(self.calc_args_str))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "tb_module".')

for func in _dt_array_initialisers:
    func()
