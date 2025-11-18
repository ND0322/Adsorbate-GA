"""
Module descriptors_module


Defined at descriptors.fpp lines 133-10207

"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("quippy.transfer_parameters_type")
class transfer_parameters_type(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=transfer_parameters_type)
    
    
    Defined at descriptors.fpp lines 190-192
    
    """
    def __init__(self, handle=None):
        """
        self = Transfer_Parameters_Type()
        
        
        Defined at descriptors.fpp lines 190-192
        
        
        Returns
        -------
        this : Transfer_Parameters_Type
        	Object to be constructed
        
        
        Automatically generated constructor for transfer_parameters_type
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_transfer_parameters_type_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Transfer_Parameters_Type
        
        
        Defined at descriptors.fpp lines 190-192
        
        Parameters
        ----------
        this : Transfer_Parameters_Type
        	Object to be destructed
        
        
        Automatically generated destructor for transfer_parameters_type
        """
        if self._alloc:
            quippy._quippy.f90wrap_transfer_parameters_type_finalise(this=self._handle)
    
    @property
    def do_transfer(self):
        """
        Element do_transfer ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 191
        
        """
        return quippy._quippy.f90wrap_transfer_parameters_type__get__do_transfer(self._handle)
    
    @do_transfer.setter
    def do_transfer(self, do_transfer):
        quippy._quippy.f90wrap_transfer_parameters_type__set__do_transfer(self._handle, do_transfer)
    
    @property
    def factor(self):
        """
        Element factor ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 192
        
        """
        return quippy._quippy.f90wrap_transfer_parameters_type__get__factor(self._handle)
    
    @factor.setter
    def factor(self, factor):
        quippy._quippy.f90wrap_transfer_parameters_type__set__factor(self._handle, factor)
    
    @property
    def r0(self):
        """
        Element r0 ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 192
        
        """
        return quippy._quippy.f90wrap_transfer_parameters_type__get__r0(self._handle)
    
    @r0.setter
    def r0(self, r0):
        quippy._quippy.f90wrap_transfer_parameters_type__set__r0(self._handle, r0)
    
    @property
    def width(self):
        """
        Element width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 192
        
        """
        return quippy._quippy.f90wrap_transfer_parameters_type__get__width(self._handle)
    
    @width.setter
    def width(self, width):
        quippy._quippy.f90wrap_transfer_parameters_type__set__width(self._handle, width)
    
    def __str__(self):
        ret = ['<transfer_parameters_type>{\n']
        ret.append('    do_transfer : ')
        ret.append(repr(self.do_transfer))
        ret.append(',\n    factor : ')
        ret.append(repr(self.factor))
        ret.append(',\n    r0 : ')
        ret.append(repr(self.r0))
        ret.append(',\n    width : ')
        ret.append(repr(self.width))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.descriptor_data_mono")
class descriptor_data_mono(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=descriptor_data_mono)
    
    
    Defined at descriptors.fpp lines 194-204
    
    """
    def __init__(self, handle=None):
        """
        self = Descriptor_Data_Mono()
        
        
        Defined at descriptors.fpp lines 194-204
        
        
        Returns
        -------
        this : Descriptor_Data_Mono
        	Object to be constructed
        
        
        Automatically generated constructor for descriptor_data_mono
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_descriptor_data_mono_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Descriptor_Data_Mono
        
        
        Defined at descriptors.fpp lines 194-204
        
        Parameters
        ----------
        this : Descriptor_Data_Mono
        	Object to be destructed
        
        
        Automatically generated destructor for descriptor_data_mono
        """
        if self._alloc:
            quippy._quippy.f90wrap_descriptor_data_mono_finalise(this=self._handle)
    
    @property
    def data(self):
        """
        Element data ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 195
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_descriptor_data_mono__array__data(self._handle)
        if array_handle in self._arrays:
            data = self._arrays[array_handle]
        else:
            data = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__data)
            self._arrays[array_handle] = data
        return data
    
    @data.setter
    def data(self, data):
        self.data[...] = data
    
    @property
    def grad_data(self):
        """
        Element grad_data ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 196
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_descriptor_data_mono__array__grad_data(self._handle)
        if array_handle in self._arrays:
            grad_data = self._arrays[array_handle]
        else:
            grad_data = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__grad_data)
            self._arrays[array_handle] = grad_data
        return grad_data
    
    @grad_data.setter
    def grad_data(self, grad_data):
        self.grad_data[...] = grad_data
    
    @property
    def ci(self):
        """
        Element ci ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 199
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_descriptor_data_mono__array__ci(self._handle)
        if array_handle in self._arrays:
            ci = self._arrays[array_handle]
        else:
            ci = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__ci)
            self._arrays[array_handle] = ci
        return ci
    
    @ci.setter
    def ci(self, ci):
        self.ci[...] = ci
    
    @property
    def ii(self):
        """
        Element ii ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 199
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_descriptor_data_mono__array__ii(self._handle)
        if array_handle in self._arrays:
            ii = self._arrays[array_handle]
        else:
            ii = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__ii)
            self._arrays[array_handle] = ii
        return ii
    
    @ii.setter
    def ii(self, ii):
        self.ii[...] = ii
    
    @property
    def pos(self):
        """
        Element pos ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 200
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_descriptor_data_mono__array__pos(self._handle)
        if array_handle in self._arrays:
            pos = self._arrays[array_handle]
        else:
            pos = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__pos)
            self._arrays[array_handle] = pos
        return pos
    
    @pos.setter
    def pos(self, pos):
        self.pos[...] = pos
    
    @property
    def has_data(self):
        """
        Element has_data ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 201
        
        """
        return quippy._quippy.f90wrap_descriptor_data_mono__get__has_data(self._handle)
    
    @has_data.setter
    def has_data(self, has_data):
        quippy._quippy.f90wrap_descriptor_data_mono__set__has_data(self._handle, has_data)
    
    @property
    def has_grad_data(self):
        """
        Element has_grad_data ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 202
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_descriptor_data_mono__array__has_grad_data(self._handle)
        if array_handle in self._arrays:
            has_grad_data = self._arrays[array_handle]
        else:
            has_grad_data = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__has_grad_data)
            self._arrays[array_handle] = has_grad_data
        return has_grad_data
    
    @has_grad_data.setter
    def has_grad_data(self, has_grad_data):
        self.has_grad_data[...] = has_grad_data
    
    @property
    def covariance_cutoff(self):
        """
        Element covariance_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 203
        
        """
        return quippy._quippy.f90wrap_descriptor_data_mono__get__covariance_cutoff(self._handle)
    
    @covariance_cutoff.setter
    def covariance_cutoff(self, covariance_cutoff):
        quippy._quippy.f90wrap_descriptor_data_mono__set__covariance_cutoff(self._handle, covariance_cutoff)
    
    @property
    def grad_covariance_cutoff(self):
        """
        Element grad_covariance_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 204
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_descriptor_data_mono__array__grad_covariance_cutoff(self._handle)
        if array_handle in self._arrays:
            grad_covariance_cutoff = self._arrays[array_handle]
        else:
            grad_covariance_cutoff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_descriptor_data_mono__array__grad_covariance_cutoff)
            self._arrays[array_handle] = grad_covariance_cutoff
        return grad_covariance_cutoff
    
    @grad_covariance_cutoff.setter
    def grad_covariance_cutoff(self, grad_covariance_cutoff):
        self.grad_covariance_cutoff[...] = grad_covariance_cutoff
    
    def __str__(self):
        ret = ['<descriptor_data_mono>{\n']
        ret.append('    data : ')
        ret.append(repr(self.data))
        ret.append(',\n    grad_data : ')
        ret.append(repr(self.grad_data))
        ret.append(',\n    ci : ')
        ret.append(repr(self.ci))
        ret.append(',\n    ii : ')
        ret.append(repr(self.ii))
        ret.append(',\n    pos : ')
        ret.append(repr(self.pos))
        ret.append(',\n    has_data : ')
        ret.append(repr(self.has_data))
        ret.append(',\n    has_grad_data : ')
        ret.append(repr(self.has_grad_data))
        ret.append(',\n    covariance_cutoff : ')
        ret.append(repr(self.covariance_cutoff))
        ret.append(',\n    grad_covariance_cutoff : ')
        ret.append(repr(self.grad_covariance_cutoff))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.cplx_2d")
class cplx_2d(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=cplx_2d)
    
    
    Defined at descriptors.fpp lines 206-207
    
    """
    def __init__(self, handle=None):
        """
        self = Cplx_2D()
        
        
        Defined at descriptors.fpp lines 206-207
        
        
        Returns
        -------
        this : Cplx_2D
        	Object to be constructed
        
        
        Automatically generated constructor for cplx_2d
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_cplx_2d_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Cplx_2D
        
        
        Defined at descriptors.fpp lines 206-207
        
        Parameters
        ----------
        this : Cplx_2D
        	Object to be destructed
        
        
        Automatically generated destructor for cplx_2d
        """
        if self._alloc:
            quippy._quippy.f90wrap_cplx_2d_finalise(this=self._handle)
    
    @property
    def mm(self):
        """
        Element mm ftype=complex(dp) pytype=complex
        
        
        Defined at descriptors.fpp line 207
        
        """
        array_ndim, array_type, array_shape, array_handle =     quippy._quippy.f90wrap_cplx_2d__array__mm(self._handle)
        if array_handle in self._arrays:
            mm = self._arrays[array_handle]
        else:
            mm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_cplx_2d__array__mm)
            self._arrays[array_handle] = mm
        return mm
    
    @mm.setter
    def mm(self, mm):
        self.mm[...] = mm
    
    def __str__(self):
        ret = ['<cplx_2d>{\n']
        ret.append('    mm : ')
        ret.append(repr(self.mm))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.RadialFunction_type")
class RadialFunction_type(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=radialfunction_type)
    
    
    Defined at descriptors.fpp lines 221-226
    
    """
    def __init__(self, n_max, cutoff, min_cutoff, error=None, handle=None):
        """
        self = Radialfunction_Type(n_max, cutoff, min_cutoff[, error])
        
        
        Defined at descriptors.fpp lines 889-915
        
        Parameters
        ----------
        n_max : int
        cutoff : float
        min_cutoff : float
        error : int
        
        Returns
        -------
        this : Radialfunction_Type
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_radialfunction_initialise(n_max=n_max, cutoff=cutoff, min_cutoff=min_cutoff, \
            error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Radialfunction_Type
        
        
        Defined at descriptors.fpp lines 917-927
        
        Parameters
        ----------
        this : Radialfunction_Type
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_radialfunction_finalise(this=self._handle, error=error)
    
    @property
    def n_max(self):
        """
        Element n_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 222
        
        """
        return quippy._quippy.f90wrap_radialfunction_type__get__n_max(self._handle)
    
    @n_max.setter
    def n_max(self, n_max):
        quippy._quippy.f90wrap_radialfunction_type__set__n_max(self._handle, n_max)
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 223
        
        """
        return quippy._quippy.f90wrap_radialfunction_type__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_radialfunction_type__set__cutoff(self._handle, cutoff)
    
    @property
    def min_cutoff(self):
        """
        Element min_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 223
        
        """
        return quippy._quippy.f90wrap_radialfunction_type__get__min_cutoff(self._handle)
    
    @min_cutoff.setter
    def min_cutoff(self, min_cutoff):
        quippy._quippy.f90wrap_radialfunction_type__set__min_cutoff(self._handle, min_cutoff)
    
    @property
    def radialtransform(self):
        """
        Element radialtransform ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 224
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_radialfunction_type__array__radialtransform(self._handle)
        if array_handle in self._arrays:
            radialtransform = self._arrays[array_handle]
        else:
            radialtransform = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_radialfunction_type__array__radialtransform)
            self._arrays[array_handle] = radialtransform
        return radialtransform
    
    @radialtransform.setter
    def radialtransform(self, radialtransform):
        self.radialtransform[...] = radialtransform
    
    @property
    def normfunction(self):
        """
        Element normfunction ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 225
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_radialfunction_type__array__normfunction(self._handle)
        if array_handle in self._arrays:
            normfunction = self._arrays[array_handle]
        else:
            normfunction = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_radialfunction_type__array__normfunction)
            self._arrays[array_handle] = normfunction
        return normfunction
    
    @normfunction.setter
    def normfunction(self, normfunction):
        self.normfunction[...] = normfunction
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 226
        
        """
        return quippy._quippy.f90wrap_radialfunction_type__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_radialfunction_type__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<radialfunction_type>{\n']
        ret.append('    n_max : ')
        ret.append(repr(self.n_max))
        ret.append(',\n    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    min_cutoff : ')
        ret.append(repr(self.min_cutoff))
        ret.append(',\n    radialtransform : ')
        ret.append(repr(self.radialtransform))
        ret.append(',\n    normfunction : ')
        ret.append(repr(self.normfunction))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.fourier_SO4_type")
class fourier_SO4_type(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=fourier_so4_type)
    
    
    Defined at descriptors.fpp lines 228-235
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Fourier_So4_Type(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1111-1143
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Fourier_So4_Type
        
        
        .. rubric:: args_str options
        
        =============== ===== =============== =================================================================
        Name            Type  Value           Doc                                                              
        =============== ===== =============== =================================================================
        cutoff          float 2.75            Cutoff for SO4 bispectrum                                        
        z0_ratio        float 0.0             Ratio of radius of 4D projection sphere times PI and the cutoff. 
        j_max           int   4               Max of expansion of bispectrum, i.e. resulution                  
        Z_center        int   0               Atomic number of central atom                                    
        n_Z_environment int   1               Number of species for the descriptor                             
        Z_environment   None  PARAM_MANDATORY Atomic number of species                                         
        w               None  PARAM_MANDATORY Weight associated to each atomic type                            
        =============== ===== =============== =================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_fourier_so4_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Fourier_So4_Type
        
        
        Defined at descriptors.fpp lines 1145-1157
        
        Parameters
        ----------
        this : Fourier_So4_Type
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_fourier_so4_finalise(this=self._handle, error=error)
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 229
        
        """
        return quippy._quippy.f90wrap_fourier_so4_type__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_fourier_so4_type__set__cutoff(self._handle, cutoff)
    
    @property
    def z0_ratio(self):
        """
        Element z0_ratio ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 230
        
        """
        return quippy._quippy.f90wrap_fourier_so4_type__get__z0_ratio(self._handle)
    
    @z0_ratio.setter
    def z0_ratio(self, z0_ratio):
        quippy._quippy.f90wrap_fourier_so4_type__set__z0_ratio(self._handle, z0_ratio)
    
    @property
    def z0(self):
        """
        Element z0 ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 231
        
        """
        return quippy._quippy.f90wrap_fourier_so4_type__get__z0(self._handle)
    
    @z0.setter
    def z0(self, z0):
        quippy._quippy.f90wrap_fourier_so4_type__set__z0(self._handle, z0)
    
    @property
    def j_max(self):
        """
        Element j_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 232
        
        """
        return quippy._quippy.f90wrap_fourier_so4_type__get__j_max(self._handle)
    
    @j_max.setter
    def j_max(self, j_max):
        quippy._quippy.f90wrap_fourier_so4_type__set__j_max(self._handle, j_max)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 232
        
        """
        return quippy._quippy.f90wrap_fourier_so4_type__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_fourier_so4_type__set__z(self._handle, z)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 233
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_fourier_so4_type__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_fourier_so4_type__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def w(self):
        """
        Element w ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 234
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_fourier_so4_type__array__w(self._handle)
        if array_handle in self._arrays:
            w = self._arrays[array_handle]
        else:
            w = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_fourier_so4_type__array__w)
            self._arrays[array_handle] = w
        return w
    
    @w.setter
    def w(self, w):
        self.w[...] = w
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 235
        
        """
        return quippy._quippy.f90wrap_fourier_so4_type__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_fourier_so4_type__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<fourier_so4_type>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    z0_ratio : ')
        ret.append(repr(self.z0_ratio))
        ret.append(',\n    z0 : ')
        ret.append(repr(self.z0))
        ret.append(',\n    j_max : ')
        ret.append(repr(self.j_max))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    w : ')
        ret.append(repr(self.w))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.bispectrum_SO4")
class bispectrum_SO4(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=bispectrum_so4)
    
    
    Defined at descriptors.fpp lines 237-245
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Bispectrum_So4(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1159-1174
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Bispectrum_So4
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_bispectrum_so4_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Bispectrum_So4
        
        
        Defined at descriptors.fpp lines 1176-1190
        
        Parameters
        ----------
        this : Bispectrum_So4
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_bispectrum_so4_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 2934-3168
        
        Parameters
        ----------
        this : Bispectrum_So4
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_bispectrum_so4_calc(this=self._handle, at=at._handle, \
            do_descriptor=do_descriptor, do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        bispectrum_so4_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8837-8845
        
        Parameters
        ----------
        this : Bispectrum_So4
        error : int
        
        Returns
        -------
        bispectrum_so4_cutoff : float
        
        """
        bispectrum_so4_cutoff = quippy._quippy.f90wrap_bispectrum_so4_cutoff(this=self._handle, error=error)
        return bispectrum_so4_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9150-9172
        
        Parameters
        ----------
        this : Bispectrum_So4
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_bispectrum_so4_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 238
        
        """
        return quippy._quippy.f90wrap_bispectrum_so4__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_bispectrum_so4__set__cutoff(self._handle, cutoff)
    
    @property
    def j_max(self):
        """
        Element j_max ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 239
        
        """
        return quippy._quippy.f90wrap_bispectrum_so4__get__j_max(self._handle)
    
    @j_max.setter
    def j_max(self, j_max):
        quippy._quippy.f90wrap_bispectrum_so4__set__j_max(self._handle, j_max)
    
    @property
    def z(self):
        """
        Element z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 239
        
        """
        return quippy._quippy.f90wrap_bispectrum_so4__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_bispectrum_so4__set__z(self._handle, z)
    
    @property
    def z0_ratio(self):
        """
        Element z0_ratio ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 240
        
        """
        return quippy._quippy.f90wrap_bispectrum_so4__get__z0_ratio(self._handle)
    
    @z0_ratio.setter
    def z0_ratio(self, z0_ratio):
        quippy._quippy.f90wrap_bispectrum_so4__set__z0_ratio(self._handle, z0_ratio)
    
    @property
    def z0(self):
        """
        Element z0 ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 241
        
        """
        return quippy._quippy.f90wrap_bispectrum_so4__get__z0(self._handle)
    
    @z0.setter
    def z0(self, z0):
        quippy._quippy.f90wrap_bispectrum_so4__set__z0(self._handle, z0)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 242
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_bispectrum_so4__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_bispectrum_so4__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def w(self):
        """
        Element w ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 243
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_bispectrum_so4__array__w(self._handle)
        if array_handle in self._arrays:
            w = self._arrays[array_handle]
        else:
            w = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_bispectrum_so4__array__w)
            self._arrays[array_handle] = w
        return w
    
    @w.setter
    def w(self, w):
        self.w[...] = w
    
    @property
    def fourier_so4(self):
        """
        Element fourier_so4 ftype=type(fourier_so4_type) pytype=Fourier_So4_Type
        
        
        Defined at descriptors.fpp line 244
        
        """
        fourier_so4_handle = quippy._quippy.f90wrap_bispectrum_so4__get__fourier_so4(self._handle)
        if tuple(fourier_so4_handle) in self._objs:
            fourier_so4 = self._objs[tuple(fourier_so4_handle)]
        else:
            fourier_so4 = fourier_SO4_type.from_handle(fourier_so4_handle)
            self._objs[tuple(fourier_so4_handle)] = fourier_so4
        return fourier_so4
    
    @fourier_so4.setter
    def fourier_so4(self, fourier_so4):
        fourier_so4 = fourier_so4._handle
        quippy._quippy.f90wrap_bispectrum_so4__set__fourier_so4(self._handle, fourier_so4)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 245
        
        """
        return quippy._quippy.f90wrap_bispectrum_so4__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_bispectrum_so4__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<bispectrum_so4>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    j_max : ')
        ret.append(repr(self.j_max))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    z0_ratio : ')
        ret.append(repr(self.z0_ratio))
        ret.append(',\n    z0 : ')
        ret.append(repr(self.z0))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    w : ')
        ret.append(repr(self.w))
        ret.append(',\n    fourier_so4 : ')
        ret.append(repr(self.fourier_so4))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.bispectrum_SO3")
class bispectrum_SO3(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=bispectrum_so3)
    
    
    Defined at descriptors.fpp lines 247-253
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Bispectrum_So3(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1192-1226
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Bispectrum_So3
        
        
        .. rubric:: args_str options
        
        =============== ===== =============== =================================================================
        Name            Type  Value           Doc                                                              
        =============== ===== =============== =================================================================
        cutoff          float 0.00            Cutoff for bispectrum_so3-type descriptors                       
        min_cutoff      float 0.00            Cutoff for minimal distances in bispectrum_so3-type descriptors  
        l_max           int   4               L_max for bispectrum_so3-type descriptors                        
        n_max           int   4               N_max for bispectrum_so3-type descriptors                        
        Z_center        int   0               Atomic number of central atom                                    
        n_Z_environment int   1               Number of species for the descriptor                             
        Z_environment   None  PARAM_MANDATORY Atomic number of species                                         
        w               None  PARAM_MANDATORY Weight associated to each atomic type                            
        =============== ===== =============== =================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_bispectrum_so3_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Bispectrum_So3
        
        
        Defined at descriptors.fpp lines 1228-1241
        
        Parameters
        ----------
        this : Bispectrum_So3
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_bispectrum_so3_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 3170-3423
        
        Parameters
        ----------
        this : Bispectrum_So3
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_bispectrum_so3_calc(this=self._handle, at=at._handle, \
            do_descriptor=do_descriptor, do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        bispectrum_so3_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8847-8855
        
        Parameters
        ----------
        this : Bispectrum_So3
        error : int
        
        Returns
        -------
        bispectrum_so3_cutoff : float
        
        """
        bispectrum_so3_cutoff = quippy._quippy.f90wrap_bispectrum_so3_cutoff(this=self._handle, error=error)
        return bispectrum_so3_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9174-9196
        
        Parameters
        ----------
        this : Bispectrum_So3
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_bispectrum_so3_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def l_max(self):
        """
        Element l_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 248
        
        """
        return quippy._quippy.f90wrap_bispectrum_so3__get__l_max(self._handle)
    
    @l_max.setter
    def l_max(self, l_max):
        quippy._quippy.f90wrap_bispectrum_so3__set__l_max(self._handle, l_max)
    
    @property
    def n_max(self):
        """
        Element n_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 248
        
        """
        return quippy._quippy.f90wrap_bispectrum_so3__get__n_max(self._handle)
    
    @n_max.setter
    def n_max(self, n_max):
        quippy._quippy.f90wrap_bispectrum_so3__set__n_max(self._handle, n_max)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 248
        
        """
        return quippy._quippy.f90wrap_bispectrum_so3__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_bispectrum_so3__set__z(self._handle, z)
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 249
        
        """
        return quippy._quippy.f90wrap_bispectrum_so3__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_bispectrum_so3__set__cutoff(self._handle, cutoff)
    
    @property
    def min_cutoff(self):
        """
        Element min_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 249
        
        """
        return quippy._quippy.f90wrap_bispectrum_so3__get__min_cutoff(self._handle)
    
    @min_cutoff.setter
    def min_cutoff(self, min_cutoff):
        quippy._quippy.f90wrap_bispectrum_so3__set__min_cutoff(self._handle, min_cutoff)
    
    @property
    def radial(self):
        """
        Element radial ftype=type(radialfunction_type) pytype=Radialfunction_Type
        
        
        Defined at descriptors.fpp line 250
        
        """
        radial_handle = quippy._quippy.f90wrap_bispectrum_so3__get__radial(self._handle)
        if tuple(radial_handle) in self._objs:
            radial = self._objs[tuple(radial_handle)]
        else:
            radial = RadialFunction_type.from_handle(radial_handle)
            self._objs[tuple(radial_handle)] = radial
        return radial
    
    @radial.setter
    def radial(self, radial):
        radial = radial._handle
        quippy._quippy.f90wrap_bispectrum_so3__set__radial(self._handle, radial)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 251
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_bispectrum_so3__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_bispectrum_so3__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def w(self):
        """
        Element w ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 252
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_bispectrum_so3__array__w(self._handle)
        if array_handle in self._arrays:
            w = self._arrays[array_handle]
        else:
            w = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_bispectrum_so3__array__w)
            self._arrays[array_handle] = w
        return w
    
    @w.setter
    def w(self, w):
        self.w[...] = w
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 253
        
        """
        return quippy._quippy.f90wrap_bispectrum_so3__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_bispectrum_so3__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<bispectrum_so3>{\n']
        ret.append('    l_max : ')
        ret.append(repr(self.l_max))
        ret.append(',\n    n_max : ')
        ret.append(repr(self.n_max))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    min_cutoff : ')
        ret.append(repr(self.min_cutoff))
        ret.append(',\n    radial : ')
        ret.append(repr(self.radial))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    w : ')
        ret.append(repr(self.w))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.behler_g2")
class behler_g2(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=behler_g2)
    
    
    Defined at descriptors.fpp lines 255-259
    
    """
    def __init__(self, handle=None):
        """
        self = Behler_G2()
        
        
        Defined at descriptors.fpp lines 255-259
        
        
        Returns
        -------
        this : Behler_G2
        	Object to be constructed
        
        
        Automatically generated constructor for behler_g2
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_behler_g2_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Behler_G2
        
        
        Defined at descriptors.fpp lines 255-259
        
        Parameters
        ----------
        this : Behler_G2
        	Object to be destructed
        
        
        Automatically generated destructor for behler_g2
        """
        if self._alloc:
            quippy._quippy.f90wrap_behler_g2_finalise(this=self._handle)
    
    @property
    def z_n(self):
        """
        Element z_n ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 256
        
        """
        return quippy._quippy.f90wrap_behler_g2__get__z_n(self._handle)
    
    @z_n.setter
    def z_n(self, z_n):
        quippy._quippy.f90wrap_behler_g2__set__z_n(self._handle, z_n)
    
    @property
    def eta(self):
        """
        Element eta ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 257
        
        """
        return quippy._quippy.f90wrap_behler_g2__get__eta(self._handle)
    
    @eta.setter
    def eta(self, eta):
        quippy._quippy.f90wrap_behler_g2__set__eta(self._handle, eta)
    
    @property
    def rs(self):
        """
        Element rs ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 258
        
        """
        return quippy._quippy.f90wrap_behler_g2__get__rs(self._handle)
    
    @rs.setter
    def rs(self, rs):
        quippy._quippy.f90wrap_behler_g2__set__rs(self._handle, rs)
    
    @property
    def rc(self):
        """
        Element rc ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 259
        
        """
        return quippy._quippy.f90wrap_behler_g2__get__rc(self._handle)
    
    @rc.setter
    def rc(self, rc):
        quippy._quippy.f90wrap_behler_g2__set__rc(self._handle, rc)
    
    def __str__(self):
        ret = ['<behler_g2>{\n']
        ret.append('    z_n : ')
        ret.append(repr(self.z_n))
        ret.append(',\n    eta : ')
        ret.append(repr(self.eta))
        ret.append(',\n    rs : ')
        ret.append(repr(self.rs))
        ret.append(',\n    rc : ')
        ret.append(repr(self.rc))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.behler_g3")
class behler_g3(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=behler_g3)
    
    
    Defined at descriptors.fpp lines 261-266
    
    """
    def __init__(self, handle=None):
        """
        self = Behler_G3()
        
        
        Defined at descriptors.fpp lines 261-266
        
        
        Returns
        -------
        this : Behler_G3
        	Object to be constructed
        
        
        Automatically generated constructor for behler_g3
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_behler_g3_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Behler_G3
        
        
        Defined at descriptors.fpp lines 261-266
        
        Parameters
        ----------
        this : Behler_G3
        	Object to be destructed
        
        
        Automatically generated destructor for behler_g3
        """
        if self._alloc:
            quippy._quippy.f90wrap_behler_g3_finalise(this=self._handle)
    
    @property
    def z_n(self):
        """
        Element z_n ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 262
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_behler_g3__array__z_n(self._handle)
        if array_handle in self._arrays:
            z_n = self._arrays[array_handle]
        else:
            z_n = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_behler_g3__array__z_n)
            self._arrays[array_handle] = z_n
        return z_n
    
    @z_n.setter
    def z_n(self, z_n):
        self.z_n[...] = z_n
    
    @property
    def eta(self):
        """
        Element eta ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 263
        
        """
        return quippy._quippy.f90wrap_behler_g3__get__eta(self._handle)
    
    @eta.setter
    def eta(self, eta):
        quippy._quippy.f90wrap_behler_g3__set__eta(self._handle, eta)
    
    @property
    def lambda_(self):
        """
        Element lambda_ ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 264
        
        """
        return quippy._quippy.f90wrap_behler_g3__get__lambda_(self._handle)
    
    @lambda_.setter
    def lambda_(self, lambda_):
        quippy._quippy.f90wrap_behler_g3__set__lambda_(self._handle, lambda_)
    
    @property
    def zeta(self):
        """
        Element zeta ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 265
        
        """
        return quippy._quippy.f90wrap_behler_g3__get__zeta(self._handle)
    
    @zeta.setter
    def zeta(self, zeta):
        quippy._quippy.f90wrap_behler_g3__set__zeta(self._handle, zeta)
    
    @property
    def rc(self):
        """
        Element rc ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 266
        
        """
        return quippy._quippy.f90wrap_behler_g3__get__rc(self._handle)
    
    @rc.setter
    def rc(self, rc):
        quippy._quippy.f90wrap_behler_g3__set__rc(self._handle, rc)
    
    def __str__(self):
        ret = ['<behler_g3>{\n']
        ret.append('    z_n : ')
        ret.append(repr(self.z_n))
        ret.append(',\n    eta : ')
        ret.append(repr(self.eta))
        ret.append(',\n    lambda_ : ')
        ret.append(repr(self.lambda_))
        ret.append(',\n    zeta : ')
        ret.append(repr(self.zeta))
        ret.append(',\n    rc : ')
        ret.append(repr(self.rc))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.behler")
class behler(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=behler)
    
    
    Defined at descriptors.fpp lines 268-274
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Behler(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1243-1386
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Behler
        
        
        .. rubric:: args_str options
        
        ================== ==== ===== =========================================================================
        Name               Type Value Doc                                                                      
        ================== ==== ===== =========================================================================
        Z                  int  0     Central atom                                                             
        specification      None       String to specify Parrinello-Behler descriptors                          
        specification_file None       File containing string to specify Parrinello-Behler descriptors          
        ================== ==== ===== =========================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_behler_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Behler
        
        
        Defined at descriptors.fpp lines 1388-1398
        
        Parameters
        ----------
        this : Behler
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_behler_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 3425-3612
        
        Parameters
        ----------
        this : Behler
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_behler_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        behler_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8857-8865
        
        Parameters
        ----------
        this : Behler
        error : int
        
        Returns
        -------
        behler_cutoff : float
        
        """
        behler_cutoff = quippy._quippy.f90wrap_behler_cutoff(this=self._handle, error=error)
        return behler_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9198-9220
        
        Parameters
        ----------
        this : Behler
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_behler_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 269
        
        """
        return quippy._quippy.f90wrap_behler__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_behler__set__cutoff(self._handle, cutoff)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 270
        
        """
        return quippy._quippy.f90wrap_behler__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_behler__set__initialised(self._handle, initialised)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 271
        
        """
        return quippy._quippy.f90wrap_behler__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_behler__set__z(self._handle, z)
    
    @property
    def n_g2(self):
        """
        Element n_g2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 272
        
        """
        return quippy._quippy.f90wrap_behler__get__n_g2(self._handle)
    
    @n_g2.setter
    def n_g2(self, n_g2):
        quippy._quippy.f90wrap_behler__set__n_g2(self._handle, n_g2)
    
    @property
    def n_g3(self):
        """
        Element n_g3 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 272
        
        """
        return quippy._quippy.f90wrap_behler__get__n_g3(self._handle)
    
    @n_g3.setter
    def n_g3(self, n_g3):
        quippy._quippy.f90wrap_behler__set__n_g3(self._handle, n_g3)
    
    def init_array_g2(self):
        self.g2 = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        quippy._quippy.f90wrap_behler__array_getitem__g2,
                                        quippy._quippy.f90wrap_behler__array_setitem__g2,
                                        quippy._quippy.f90wrap_behler__array_len__g2,
                                        """
        Element g2 ftype=type(behler_g2) pytype=Behler_G2
        
        
        Defined at descriptors.fpp line 273
        
        """, behler_g2)
        return self.g2
    
    def init_array_g3(self):
        self.g3 = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        quippy._quippy.f90wrap_behler__array_getitem__g3,
                                        quippy._quippy.f90wrap_behler__array_setitem__g3,
                                        quippy._quippy.f90wrap_behler__array_len__g3,
                                        """
        Element g3 ftype=type(behler_g3) pytype=Behler_G3
        
        
        Defined at descriptors.fpp line 274
        
        """, behler_g3)
        return self.g3
    
    def __str__(self):
        ret = ['<behler>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    n_g2 : ')
        ret.append(repr(self.n_g2))
        ret.append(',\n    n_g3 : ')
        ret.append(repr(self.n_g3))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = [init_array_g2, init_array_g3]
    

@f90wrap.runtime.register_class("quippy.distance_2b")
class distance_2b(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=distance_2b)
    
    
    Defined at descriptors.fpp lines 276-286
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Distance_2B(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1400-1449
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Distance_2B
        
        
        .. rubric:: args_str options
        
        ======================= ===== ============================== ==========================================
        Name                    Type  Value                          Doc                                       
        ======================= ===== ============================== ==========================================
        cutoff                  float 0.00                           Cutoff for distance_2b-type descriptors   
        cutoff_transition_width float 0.5                            Transition width of cutoff for            
                                                                     distance_2b-type descriptors              
        Z1                      int   0                              Atom type #1 in bond                      
        Z2                      int   0                              Atom type #2 in bond                      
        resid_name              None                                 Name of an integer property in the atoms  
                                                                     object giving the residue id of the       
                                                                     molecule to which the atom belongs.       
        only_intra              bool  F                              Only calculate INTRAmolecular pairs with  
                                                                     equal residue ids(bonds)                  
        only_inter              bool  F                              Only apply to INTERmolecular pairs with   
                                                                     different residue ids(non-bonded)         
        n_exponents             int   1                              Number of exponents                       
        tail_range              float 1.0                            Tail order                                
        tail_exponent           int   0                              Tail range                                
        exponents               None  repeat(" 1 ",this%n_exponents) Exponents                                 
        ======================= ===== ============================== ==========================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_distance_2b_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Distance_2B
        
        
        Defined at descriptors.fpp lines 1451-1468
        
        Parameters
        ----------
        this : Distance_2B
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_distance_2b_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 3614-3748
        
        Parameters
        ----------
        this : Distance_2B
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_distance_2b_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        distance_2b_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8867-8875
        
        Parameters
        ----------
        this : Distance_2B
        error : int
        
        Returns
        -------
        distance_2b_cutoff : float
        
        """
        distance_2b_cutoff = quippy._quippy.f90wrap_distance_2b_cutoff(this=self._handle, error=error)
        return distance_2b_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9222-9269
        
        Parameters
        ----------
        this : Distance_2B
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_distance_2b_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 277
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_distance_2b__set__cutoff(self._handle, cutoff)
    
    @property
    def cutoff_transition_width(self):
        """
        Element cutoff_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 278
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__cutoff_transition_width(self._handle)
    
    @cutoff_transition_width.setter
    def cutoff_transition_width(self, cutoff_transition_width):
        quippy._quippy.f90wrap_distance_2b__set__cutoff_transition_width(self._handle, cutoff_transition_width)
    
    @property
    def z1(self):
        """
        Element z1 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 279
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__z1(self._handle)
    
    @z1.setter
    def z1(self, z1):
        quippy._quippy.f90wrap_distance_2b__set__z1(self._handle, z1)
    
    @property
    def z2(self):
        """
        Element z2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 279
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__z2(self._handle)
    
    @z2.setter
    def z2(self, z2):
        quippy._quippy.f90wrap_distance_2b__set__z2(self._handle, z2)
    
    @property
    def resid_name(self):
        """
        Element resid_name ftype=character(string_length) pytype=str
        
        
        Defined at descriptors.fpp line 280
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__resid_name(self._handle)
    
    @resid_name.setter
    def resid_name(self, resid_name):
        quippy._quippy.f90wrap_distance_2b__set__resid_name(self._handle, resid_name)
    
    @property
    def only_intra(self):
        """
        Element only_intra ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 281
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__only_intra(self._handle)
    
    @only_intra.setter
    def only_intra(self, only_intra):
        quippy._quippy.f90wrap_distance_2b__set__only_intra(self._handle, only_intra)
    
    @property
    def only_inter(self):
        """
        Element only_inter ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 281
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__only_inter(self._handle)
    
    @only_inter.setter
    def only_inter(self, only_inter):
        quippy._quippy.f90wrap_distance_2b__set__only_inter(self._handle, only_inter)
    
    @property
    def n_exponents(self):
        """
        Element n_exponents ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 282
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__n_exponents(self._handle)
    
    @n_exponents.setter
    def n_exponents(self, n_exponents):
        quippy._quippy.f90wrap_distance_2b__set__n_exponents(self._handle, n_exponents)
    
    @property
    def tail_exponent(self):
        """
        Element tail_exponent ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 282
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__tail_exponent(self._handle)
    
    @tail_exponent.setter
    def tail_exponent(self, tail_exponent):
        quippy._quippy.f90wrap_distance_2b__set__tail_exponent(self._handle, tail_exponent)
    
    @property
    def tail_range(self):
        """
        Element tail_range ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 283
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__tail_range(self._handle)
    
    @tail_range.setter
    def tail_range(self, tail_range):
        quippy._quippy.f90wrap_distance_2b__set__tail_range(self._handle, tail_range)
    
    @property
    def exponents(self):
        """
        Element exponents ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 284
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_distance_2b__array__exponents(self._handle)
        if array_handle in self._arrays:
            exponents = self._arrays[array_handle]
        else:
            exponents = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_distance_2b__array__exponents)
            self._arrays[array_handle] = exponents
        return exponents
    
    @exponents.setter
    def exponents(self, exponents):
        self.exponents[...] = exponents
    
    @property
    def has_tail(self):
        """
        Element has_tail ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 285
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__has_tail(self._handle)
    
    @has_tail.setter
    def has_tail(self, has_tail):
        quippy._quippy.f90wrap_distance_2b__set__has_tail(self._handle, has_tail)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 286
        
        """
        return quippy._quippy.f90wrap_distance_2b__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_distance_2b__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<distance_2b>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    cutoff_transition_width : ')
        ret.append(repr(self.cutoff_transition_width))
        ret.append(',\n    z1 : ')
        ret.append(repr(self.z1))
        ret.append(',\n    z2 : ')
        ret.append(repr(self.z2))
        ret.append(',\n    resid_name : ')
        ret.append(repr(self.resid_name))
        ret.append(',\n    only_intra : ')
        ret.append(repr(self.only_intra))
        ret.append(',\n    only_inter : ')
        ret.append(repr(self.only_inter))
        ret.append(',\n    n_exponents : ')
        ret.append(repr(self.n_exponents))
        ret.append(',\n    tail_exponent : ')
        ret.append(repr(self.tail_exponent))
        ret.append(',\n    tail_range : ')
        ret.append(repr(self.tail_range))
        ret.append(',\n    exponents : ')
        ret.append(repr(self.exponents))
        ret.append(',\n    has_tail : ')
        ret.append(repr(self.has_tail))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.coordination")
class coordination(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=coordination)
    
    
    Defined at descriptors.fpp lines 288-292
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Coordination(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1470-1485
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Coordination
        
        
        .. rubric:: args_str options
        
        ================ ===== ===== ==========================================================================
        Name             Type  Value Doc                                                                       
        ================ ===== ===== ==========================================================================
        cutoff           float 0.00  Cutoff for coordination-type descriptors                                  
        transition_width float 0.20  Width of transition region from 1 to 0                                    
        Z_center         int   0     Atomic number of central atom                                             
        ================ ===== ===== ==========================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_coordination_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Coordination
        
        
        Defined at descriptors.fpp lines 1487-1495
        
        Parameters
        ----------
        this : Coordination
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_coordination_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 3750-3862
        
        Parameters
        ----------
        this : Coordination
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_coordination_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        coordination_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8887-8895
        
        Parameters
        ----------
        this : Coordination
        error : int
        
        Returns
        -------
        coordination_cutoff : float
        
        """
        coordination_cutoff = quippy._quippy.f90wrap_coordination_cutoff(this=self._handle, error=error)
        return coordination_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9271-9293
        
        Parameters
        ----------
        this : Coordination
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_coordination_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 289
        
        """
        return quippy._quippy.f90wrap_coordination__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_coordination__set__cutoff(self._handle, cutoff)
    
    @property
    def transition_width(self):
        """
        Element transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 290
        
        """
        return quippy._quippy.f90wrap_coordination__get__transition_width(self._handle)
    
    @transition_width.setter
    def transition_width(self, transition_width):
        quippy._quippy.f90wrap_coordination__set__transition_width(self._handle, transition_width)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 291
        
        """
        return quippy._quippy.f90wrap_coordination__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_coordination__set__z(self._handle, z)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 292
        
        """
        return quippy._quippy.f90wrap_coordination__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_coordination__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<coordination>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    transition_width : ')
        ret.append(repr(self.transition_width))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.angle_3b")
class angle_3b(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=angle_3b)
    
    
    Defined at descriptors.fpp lines 294-298
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Angle_3B(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1497-1514
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Angle_3B
        
        
        .. rubric:: args_str options
        
        ======================= ===== ===== ===================================================================
        Name                    Type  Value Doc                                                                
        ======================= ===== ===== ===================================================================
        cutoff                  float 0.00  Cutoff for angle_3b-type descriptors                               
        cutoff_transition_width float 0.50  Cutoff transition width for angle_3b-type descriptors              
        Z_center                int   0     Atomic number of central atom                                      
        Z1                      int   0     Atomic number of neighbour #1                                      
        Z2                      int   0     Atomic number of neighbour #2                                      
        ======================= ===== ===== ===================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_angle_3b_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Angle_3B
        
        
        Defined at descriptors.fpp lines 1516-1525
        
        Parameters
        ----------
        this : Angle_3B
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_angle_3b_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 3864-3998
        
        Parameters
        ----------
        this : Angle_3B
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_angle_3b_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        angle_3b_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8897-8905
        
        Parameters
        ----------
        this : Angle_3B
        error : int
        
        Returns
        -------
        angle_3b_cutoff : float
        
        """
        angle_3b_cutoff = quippy._quippy.f90wrap_angle_3b_cutoff(this=self._handle, error=error)
        return angle_3b_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9295-9333
        
        Parameters
        ----------
        this : Angle_3B
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_angle_3b_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 295
        
        """
        return quippy._quippy.f90wrap_angle_3b__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_angle_3b__set__cutoff(self._handle, cutoff)
    
    @property
    def cutoff_transition_width(self):
        """
        Element cutoff_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 296
        
        """
        return quippy._quippy.f90wrap_angle_3b__get__cutoff_transition_width(self._handle)
    
    @cutoff_transition_width.setter
    def cutoff_transition_width(self, cutoff_transition_width):
        quippy._quippy.f90wrap_angle_3b__set__cutoff_transition_width(self._handle, cutoff_transition_width)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 297
        
        """
        return quippy._quippy.f90wrap_angle_3b__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_angle_3b__set__z(self._handle, z)
    
    @property
    def z1(self):
        """
        Element z1 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 297
        
        """
        return quippy._quippy.f90wrap_angle_3b__get__z1(self._handle)
    
    @z1.setter
    def z1(self, z1):
        quippy._quippy.f90wrap_angle_3b__set__z1(self._handle, z1)
    
    @property
    def z2(self):
        """
        Element z2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 297
        
        """
        return quippy._quippy.f90wrap_angle_3b__get__z2(self._handle)
    
    @z2.setter
    def z2(self, z2):
        quippy._quippy.f90wrap_angle_3b__set__z2(self._handle, z2)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 298
        
        """
        return quippy._quippy.f90wrap_angle_3b__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_angle_3b__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<angle_3b>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    cutoff_transition_width : ')
        ret.append(repr(self.cutoff_transition_width))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    z1 : ')
        ret.append(repr(self.z1))
        ret.append(',\n    z2 : ')
        ret.append(repr(self.z2))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.co_angle_3b")
class co_angle_3b(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=co_angle_3b)
    
    
    Defined at descriptors.fpp lines 300-305
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Co_Angle_3B(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1527-1545
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Co_Angle_3B
        
        
        .. rubric:: args_str options
        
        ============================= ===== ===== =============================================================
        Name                          Type  Value Doc                                                          
        ============================= ===== ===== =============================================================
        cutoff                        float 0.00  Cutoff for co_angle_3b-type descriptors                      
        coordination_cutoff           float 0.00  Cutoff for coordination function in co_angle_3b-type         
                                                  descriptors                                                  
        coordination_transition_width float 0.00  Transition width for co_angle_3b-type descriptors            
        Z_center                      int   0     Atomic number of central atom                                
        Z1                            int   0     Atomic number of neighbour #1                                
        Z2                            int   0     Atomic number of neighbour #2                                
        ============================= ===== ===== =============================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_co_angle_3b_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Co_Angle_3B
        
        
        Defined at descriptors.fpp lines 1547-1558
        
        Parameters
        ----------
        this : Co_Angle_3B
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_co_angle_3b_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4000-4163
        
        Parameters
        ----------
        this : Co_Angle_3B
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_co_angle_3b_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        co_angle_3b_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8907-8915
        
        Parameters
        ----------
        this : Co_Angle_3B
        error : int
        
        Returns
        -------
        co_angle_3b_cutoff : float
        
        """
        co_angle_3b_cutoff = quippy._quippy.f90wrap_co_angle_3b_cutoff(this=self._handle, error=error)
        return co_angle_3b_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9335-9374
        
        Parameters
        ----------
        this : Co_Angle_3B
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_co_angle_3b_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 301
        
        """
        return quippy._quippy.f90wrap_co_angle_3b__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_co_angle_3b__set__cutoff(self._handle, cutoff)
    
    @property
    def coordination_transition_width(self):
        """
        Element coordination_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 303
        
        """
        return quippy._quippy.f90wrap_co_angle_3b__get__coordination_transition_width(self._handle)
    
    @coordination_transition_width.setter
    def coordination_transition_width(self, coordination_transition_width):
        quippy._quippy.f90wrap_co_angle_3b__set__coordination_transition_width(self._handle, coordination_transition_width)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 304
        
        """
        return quippy._quippy.f90wrap_co_angle_3b__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_co_angle_3b__set__z(self._handle, z)
    
    @property
    def z1(self):
        """
        Element z1 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 304
        
        """
        return quippy._quippy.f90wrap_co_angle_3b__get__z1(self._handle)
    
    @z1.setter
    def z1(self, z1):
        quippy._quippy.f90wrap_co_angle_3b__set__z1(self._handle, z1)
    
    @property
    def z2(self):
        """
        Element z2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 304
        
        """
        return quippy._quippy.f90wrap_co_angle_3b__get__z2(self._handle)
    
    @z2.setter
    def z2(self, z2):
        quippy._quippy.f90wrap_co_angle_3b__set__z2(self._handle, z2)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 305
        
        """
        return quippy._quippy.f90wrap_co_angle_3b__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_co_angle_3b__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<co_angle_3b>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    coordination_transition_width : ')
        ret.append(repr(self.coordination_transition_width))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    z1 : ')
        ret.append(repr(self.z1))
        ret.append(',\n    z2 : ')
        ret.append(repr(self.z2))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.co_distance_2b")
class co_distance_2b(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=co_distance_2b)
    
    
    Defined at descriptors.fpp lines 307-313
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Co_Distance_2B(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1560-1578
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Co_Distance_2B
        
        
        .. rubric:: args_str options
        
        ============================= ===== ===== =============================================================
        Name                          Type  Value Doc                                                          
        ============================= ===== ===== =============================================================
        cutoff                        float 0.00  Cutoff for co_distance_2b-type descriptors                   
        transition_width              float 0.50  Transition width of cutoff for co_distance_2b-type           
                                                  descriptors                                                  
        coordination_cutoff           float 0.00  Cutoff for coordination function in co_distance_2b-type      
                                                  descriptors                                                  
        coordination_transition_width float 0.00  Transition width for co_distance_2b-type descriptors         
        Z1                            int   0     Atom type #1 in bond                                         
        Z2                            int   0     Atom type #2 in bond                                         
        ============================= ===== ===== =============================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_co_distance_2b_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Co_Distance_2B
        
        
        Defined at descriptors.fpp lines 1580-1590
        
        Parameters
        ----------
        this : Co_Distance_2B
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_co_distance_2b_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4165-4311
        
        Parameters
        ----------
        this : Co_Distance_2B
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_co_distance_2b_calc(this=self._handle, at=at._handle, \
            do_descriptor=do_descriptor, do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        co_distance_2b_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8877-8885
        
        Parameters
        ----------
        this : Co_Distance_2B
        error : int
        
        Returns
        -------
        co_distance_2b_cutoff : float
        
        """
        co_distance_2b_cutoff = quippy._quippy.f90wrap_co_distance_2b_cutoff(this=self._handle, error=error)
        return co_distance_2b_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9376-9409
        
        Parameters
        ----------
        this : Co_Distance_2B
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_co_distance_2b_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 308
        
        """
        return quippy._quippy.f90wrap_co_distance_2b__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_co_distance_2b__set__cutoff(self._handle, cutoff)
    
    @property
    def transition_width(self):
        """
        Element transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 309
        
        """
        return quippy._quippy.f90wrap_co_distance_2b__get__transition_width(self._handle)
    
    @transition_width.setter
    def transition_width(self, transition_width):
        quippy._quippy.f90wrap_co_distance_2b__set__transition_width(self._handle, transition_width)
    
    @property
    def coordination_transition_width(self):
        """
        Element coordination_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 311
        
        """
        return quippy._quippy.f90wrap_co_distance_2b__get__coordination_transition_width(self._handle)
    
    @coordination_transition_width.setter
    def coordination_transition_width(self, coordination_transition_width):
        quippy._quippy.f90wrap_co_distance_2b__set__coordination_transition_width(self._handle, coordination_transition_width)
    
    @property
    def z1(self):
        """
        Element z1 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 312
        
        """
        return quippy._quippy.f90wrap_co_distance_2b__get__z1(self._handle)
    
    @z1.setter
    def z1(self, z1):
        quippy._quippy.f90wrap_co_distance_2b__set__z1(self._handle, z1)
    
    @property
    def z2(self):
        """
        Element z2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 312
        
        """
        return quippy._quippy.f90wrap_co_distance_2b__get__z2(self._handle)
    
    @z2.setter
    def z2(self, z2):
        quippy._quippy.f90wrap_co_distance_2b__set__z2(self._handle, z2)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 313
        
        """
        return quippy._quippy.f90wrap_co_distance_2b__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_co_distance_2b__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<co_distance_2b>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    transition_width : ')
        ret.append(repr(self.transition_width))
        ret.append(',\n    coordination_transition_width : ')
        ret.append(repr(self.coordination_transition_width))
        ret.append(',\n    z1 : ')
        ret.append(repr(self.z1))
        ret.append(',\n    z2 : ')
        ret.append(repr(self.z2))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.cosnx")
class cosnx(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=cosnx)
    
    
    Defined at descriptors.fpp lines 315-321
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Cosnx(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1592-1625
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Cosnx
        
        
        .. rubric:: args_str options
        
        ========== ===== =============== ======================================================================
        Name       Type  Value           Doc                                                                   
        ========== ===== =============== ======================================================================
        cutoff     float 0.00            Cutoff for cosnx-type descriptors                                     
        min_cutoff float 0.00            Cutoff for minimal distances in cosnx-type descriptors                
        l_max      int   4               L_max for cosnx-type descriptors                                      
        n_max      int   4               N_max for cosnx-type descriptors                                      
        Z_center   int   0               Atomic number of central atom                                         
        n_species  int   1               Number of species for the descriptor                                  
        species_Z  None  PARAM_MANDATORY Atomic number of species                                              
        w          None  PARAM_MANDATORY Weight associated to each atomic type                                 
        ========== ===== =============== ======================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_cosnx_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Cosnx
        
        
        Defined at descriptors.fpp lines 1627-1639
        
        Parameters
        ----------
        this : Cosnx
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_cosnx_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4313-4510
        
        Parameters
        ----------
        this : Cosnx
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_cosnx_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        cosnx_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8917-8925
        
        Parameters
        ----------
        this : Cosnx
        error : int
        
        Returns
        -------
        cosnx_cutoff : float
        
        """
        cosnx_cutoff = quippy._quippy.f90wrap_cosnx_cutoff(this=self._handle, error=error)
        return cosnx_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9411-9433
        
        Parameters
        ----------
        this : Cosnx
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_cosnx_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def l_max(self):
        """
        Element l_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 316
        
        """
        return quippy._quippy.f90wrap_cosnx__get__l_max(self._handle)
    
    @l_max.setter
    def l_max(self, l_max):
        quippy._quippy.f90wrap_cosnx__set__l_max(self._handle, l_max)
    
    @property
    def n_max(self):
        """
        Element n_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 316
        
        """
        return quippy._quippy.f90wrap_cosnx__get__n_max(self._handle)
    
    @n_max.setter
    def n_max(self, n_max):
        quippy._quippy.f90wrap_cosnx__set__n_max(self._handle, n_max)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 316
        
        """
        return quippy._quippy.f90wrap_cosnx__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_cosnx__set__z(self._handle, z)
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 317
        
        """
        return quippy._quippy.f90wrap_cosnx__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_cosnx__set__cutoff(self._handle, cutoff)
    
    @property
    def min_cutoff(self):
        """
        Element min_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 317
        
        """
        return quippy._quippy.f90wrap_cosnx__get__min_cutoff(self._handle)
    
    @min_cutoff.setter
    def min_cutoff(self, min_cutoff):
        quippy._quippy.f90wrap_cosnx__set__min_cutoff(self._handle, min_cutoff)
    
    @property
    def radial(self):
        """
        Element radial ftype=type(radialfunction_type) pytype=Radialfunction_Type
        
        
        Defined at descriptors.fpp line 318
        
        """
        radial_handle = quippy._quippy.f90wrap_cosnx__get__radial(self._handle)
        if tuple(radial_handle) in self._objs:
            radial = self._objs[tuple(radial_handle)]
        else:
            radial = RadialFunction_type.from_handle(radial_handle)
            self._objs[tuple(radial_handle)] = radial
        return radial
    
    @radial.setter
    def radial(self, radial):
        radial = radial._handle
        quippy._quippy.f90wrap_cosnx__set__radial(self._handle, radial)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 319
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_cosnx__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_cosnx__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def w(self):
        """
        Element w ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 320
        
        """
        array_ndim, array_type, array_shape, array_handle =     quippy._quippy.f90wrap_cosnx__array__w(self._handle)
        if array_handle in self._arrays:
            w = self._arrays[array_handle]
        else:
            w = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_cosnx__array__w)
            self._arrays[array_handle] = w
        return w
    
    @w.setter
    def w(self, w):
        self.w[...] = w
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 321
        
        """
        return quippy._quippy.f90wrap_cosnx__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_cosnx__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<cosnx>{\n']
        ret.append('    l_max : ')
        ret.append(repr(self.l_max))
        ret.append(',\n    n_max : ')
        ret.append(repr(self.n_max))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    min_cutoff : ')
        ret.append(repr(self.min_cutoff))
        ret.append(',\n    radial : ')
        ret.append(repr(self.radial))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    w : ')
        ret.append(repr(self.w))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.trihis")
class trihis(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=trihis)
    
    
    Defined at descriptors.fpp lines 323-328
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Trihis(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1641-1668
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Trihis
        
        
        .. rubric:: args_str options
        
        =================== ===== =============== =============================================================
        Name                Type  Value           Doc                                                          
        =================== ===== =============== =============================================================
        cutoff              float 0.00            Cutoff for trihis-type descriptors                           
        n_gauss             int   0               Number of Gaussians for trihis-type descriptors              
        trihis_gauss_centre None  PARAM_MANDATORY Number of Gaussians for trihis-type descriptors              
        trihis_gauss_width  None  PARAM_MANDATORY Number of Gaussians for trihis-type descriptors              
        =================== ===== =============== =============================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_trihis_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Trihis
        
        
        Defined at descriptors.fpp lines 1670-1679
        
        Parameters
        ----------
        this : Trihis
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_trihis_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4512-4632
        
        Parameters
        ----------
        this : Trihis
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_trihis_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        trihis_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8927-8935
        
        Parameters
        ----------
        this : Trihis
        error : int
        
        Returns
        -------
        trihis_cutoff : float
        
        """
        trihis_cutoff = quippy._quippy.f90wrap_trihis_cutoff(this=self._handle, error=error)
        return trihis_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9435-9455
        
        Parameters
        ----------
        this : Trihis
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_trihis_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 324
        
        """
        return quippy._quippy.f90wrap_trihis__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_trihis__set__cutoff(self._handle, cutoff)
    
    @property
    def n_gauss(self):
        """
        Element n_gauss ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 325
        
        """
        return quippy._quippy.f90wrap_trihis__get__n_gauss(self._handle)
    
    @n_gauss.setter
    def n_gauss(self, n_gauss):
        quippy._quippy.f90wrap_trihis__set__n_gauss(self._handle, n_gauss)
    
    @property
    def gauss_centre(self):
        """
        Element gauss_centre ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 326
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_trihis__array__gauss_centre(self._handle)
        if array_handle in self._arrays:
            gauss_centre = self._arrays[array_handle]
        else:
            gauss_centre = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_trihis__array__gauss_centre)
            self._arrays[array_handle] = gauss_centre
        return gauss_centre
    
    @gauss_centre.setter
    def gauss_centre(self, gauss_centre):
        self.gauss_centre[...] = gauss_centre
    
    @property
    def gauss_width(self):
        """
        Element gauss_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 327
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_trihis__array__gauss_width(self._handle)
        if array_handle in self._arrays:
            gauss_width = self._arrays[array_handle]
        else:
            gauss_width = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_trihis__array__gauss_width)
            self._arrays[array_handle] = gauss_width
        return gauss_width
    
    @gauss_width.setter
    def gauss_width(self, gauss_width):
        self.gauss_width[...] = gauss_width
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 328
        
        """
        return quippy._quippy.f90wrap_trihis__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_trihis__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<trihis>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    n_gauss : ')
        ret.append(repr(self.n_gauss))
        ret.append(',\n    gauss_centre : ')
        ret.append(repr(self.gauss_centre))
        ret.append(',\n    gauss_width : ')
        ret.append(repr(self.gauss_width))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.water_monomer")
class water_monomer(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=water_monomer)
    
    
    Defined at descriptors.fpp lines 330-332
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Water_Monomer(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1681-1694
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Water_Monomer
        
        
        .. rubric:: args_str options
        
        ====== ===== ===== ====================================================================================
        Name   Type  Value Doc                                                                                 
        ====== ===== ===== ====================================================================================
        cutoff float 0.00  Cutoff for water_monomer-type descriptors                                           
        ====== ===== ===== ====================================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_water_monomer_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Water_Monomer
        
        
        Defined at descriptors.fpp lines 1696-1702
        
        Parameters
        ----------
        this : Water_Monomer
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_water_monomer_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4634-4750
        
        Parameters
        ----------
        this : Water_Monomer
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_water_monomer_calc(this=self._handle, at=at._handle, \
            do_descriptor=do_descriptor, do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        water_monomer_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8937-8945
        
        Parameters
        ----------
        this : Water_Monomer
        error : int
        
        Returns
        -------
        water_monomer_cutoff : float
        
        """
        water_monomer_cutoff = quippy._quippy.f90wrap_water_monomer_cutoff(this=self._handle, error=error)
        return water_monomer_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9457-9480
        
        Parameters
        ----------
        this : Water_Monomer
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_water_monomer_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 331
        
        """
        return quippy._quippy.f90wrap_water_monomer__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_water_monomer__set__cutoff(self._handle, cutoff)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 332
        
        """
        return quippy._quippy.f90wrap_water_monomer__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_water_monomer__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<water_monomer>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.water_dimer")
class water_dimer(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=water_dimer)
    
    
    Defined at descriptors.fpp lines 334-339
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Water_Dimer(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1704-1722
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Water_Dimer
        
        
        .. rubric:: args_str options
        
        ======================= ===== ===== ===================================================================
        Name                    Type  Value Doc                                                                
        ======================= ===== ===== ===================================================================
        cutoff                  float 0.00  Cutoff for water_dimer-type descriptors                            
        cutoff_transition_width float 0.50  Width of smooth cutoff region for water_dimer-type descriptors     
        monomer_cutoff          float 1.50  Monomer cutoff for water_dimer-type descriptors                    
        OHH_ordercheck          bool  T     T: find water molecules. F: use default order OHH                  
        power                   float 1.0   Power of distances to be used in the kernel                        
        dist_shift              float 0.0   Distance shift for inverse distance descriptors.                   
        ======================= ===== ===== ===================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_water_dimer_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Water_Dimer
        
        
        Defined at descriptors.fpp lines 1724-1735
        
        Parameters
        ----------
        this : Water_Dimer
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_water_dimer_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4752-4952
        
        Parameters
        ----------
        this : Water_Dimer
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_water_dimer_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        water_dimer_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8947-8955
        
        Parameters
        ----------
        this : Water_Dimer
        error : int
        
        Returns
        -------
        water_dimer_cutoff : float
        
        """
        water_dimer_cutoff = quippy._quippy.f90wrap_water_dimer_cutoff(this=self._handle, error=error)
        return water_dimer_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9482-9512
        
        Parameters
        ----------
        this : Water_Dimer
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_water_dimer_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 335
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_water_dimer__set__cutoff(self._handle, cutoff)
    
    @property
    def cutoff_transition_width(self):
        """
        Element cutoff_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 335
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__cutoff_transition_width(self._handle)
    
    @cutoff_transition_width.setter
    def cutoff_transition_width(self, cutoff_transition_width):
        quippy._quippy.f90wrap_water_dimer__set__cutoff_transition_width(self._handle, cutoff_transition_width)
    
    @property
    def monomer_cutoff(self):
        """
        Element monomer_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 336
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__monomer_cutoff(self._handle)
    
    @monomer_cutoff.setter
    def monomer_cutoff(self, monomer_cutoff):
        quippy._quippy.f90wrap_water_dimer__set__monomer_cutoff(self._handle, monomer_cutoff)
    
    @property
    def ohh_ordercheck(self):
        """
        Element ohh_ordercheck ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 337
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__ohh_ordercheck(self._handle)
    
    @ohh_ordercheck.setter
    def ohh_ordercheck(self, ohh_ordercheck):
        quippy._quippy.f90wrap_water_dimer__set__ohh_ordercheck(self._handle, ohh_ordercheck)
    
    @property
    def power(self):
        """
        Element power ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 338
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__power(self._handle)
    
    @power.setter
    def power(self, power):
        quippy._quippy.f90wrap_water_dimer__set__power(self._handle, power)
    
    @property
    def dist_shift(self):
        """
        Element dist_shift ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 338
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__dist_shift(self._handle)
    
    @dist_shift.setter
    def dist_shift(self, dist_shift):
        quippy._quippy.f90wrap_water_dimer__set__dist_shift(self._handle, dist_shift)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 339
        
        """
        return quippy._quippy.f90wrap_water_dimer__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_water_dimer__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<water_dimer>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    cutoff_transition_width : ')
        ret.append(repr(self.cutoff_transition_width))
        ret.append(',\n    monomer_cutoff : ')
        ret.append(repr(self.monomer_cutoff))
        ret.append(',\n    ohh_ordercheck : ')
        ret.append(repr(self.ohh_ordercheck))
        ret.append(',\n    power : ')
        ret.append(repr(self.power))
        ret.append(',\n    dist_shift : ')
        ret.append(repr(self.dist_shift))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.A2_dimer")
class A2_dimer(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=a2_dimer)
    
    
    Defined at descriptors.fpp lines 341-345
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = A2_Dimer(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1737-1752
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : A2_Dimer
        
        
        .. rubric:: args_str options
        
        ============== ===== ===== ============================================================================
        Name           Type  Value Doc                                                                         
        ============== ===== ===== ============================================================================
        cutoff         float 0.00  Cutoff for A2_dimer-type descriptors                                        
        monomer_cutoff float 1.50  Monomer cutoff for A2_dimer-type descriptors                                
        atomic_number  int   1     Atomic number in A2_dimer-type descriptors                                  
        ============== ===== ===== ============================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_a2_dimer_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class A2_Dimer
        
        
        Defined at descriptors.fpp lines 1754-1762
        
        Parameters
        ----------
        this : A2_Dimer
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_a2_dimer_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 4954-5063
        
        Parameters
        ----------
        this : A2_Dimer
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_a2_dimer_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        a2_dimer_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8957-8965
        
        Parameters
        ----------
        this : A2_Dimer
        error : int
        
        Returns
        -------
        a2_dimer_cutoff : float
        
        """
        a2_dimer_cutoff = quippy._quippy.f90wrap_a2_dimer_cutoff(this=self._handle, error=error)
        return a2_dimer_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9514-9549
        
        Parameters
        ----------
        this : A2_Dimer
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_a2_dimer_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 342
        
        """
        return quippy._quippy.f90wrap_a2_dimer__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_a2_dimer__set__cutoff(self._handle, cutoff)
    
    @property
    def monomer_cutoff(self):
        """
        Element monomer_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 343
        
        """
        return quippy._quippy.f90wrap_a2_dimer__get__monomer_cutoff(self._handle)
    
    @monomer_cutoff.setter
    def monomer_cutoff(self, monomer_cutoff):
        quippy._quippy.f90wrap_a2_dimer__set__monomer_cutoff(self._handle, monomer_cutoff)
    
    @property
    def atomic_number(self):
        """
        Element atomic_number ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 344
        
        """
        return quippy._quippy.f90wrap_a2_dimer__get__atomic_number(self._handle)
    
    @atomic_number.setter
    def atomic_number(self, atomic_number):
        quippy._quippy.f90wrap_a2_dimer__set__atomic_number(self._handle, atomic_number)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 345
        
        """
        return quippy._quippy.f90wrap_a2_dimer__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_a2_dimer__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<a2_dimer>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    monomer_cutoff : ')
        ret.append(repr(self.monomer_cutoff))
        ret.append(',\n    atomic_number : ')
        ret.append(repr(self.atomic_number))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.AB_dimer")
class AB_dimer(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=ab_dimer)
    
    
    Defined at descriptors.fpp lines 347-351
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Ab_Dimer(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1764-1783
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Ab_Dimer
        
        
        .. rubric:: args_str options
        
        ============== ===== ===== ============================================================================
        Name           Type  Value Doc                                                                         
        ============== ===== ===== ============================================================================
        cutoff         float 0.00  Cutoff for AB_dimer-type descriptors                                        
        monomer_cutoff float 1.50  Monomer cutoff for AB_dimer-type descriptors                                
        atomic_number1 int   1     Atomic number of atom 1 in AB_dimer-type descriptors                        
        atomic_number2 int   9     Atomic number of atom 2 in AB_dimer-type descriptors                        
        ============== ===== ===== ============================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_ab_dimer_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Ab_Dimer
        
        
        Defined at descriptors.fpp lines 1785-1794
        
        Parameters
        ----------
        this : Ab_Dimer
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_ab_dimer_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 5065-5180
        
        Parameters
        ----------
        this : Ab_Dimer
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_ab_dimer_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        ab_dimer_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8967-8975
        
        Parameters
        ----------
        this : Ab_Dimer
        error : int
        
        Returns
        -------
        ab_dimer_cutoff : float
        
        """
        ab_dimer_cutoff = quippy._quippy.f90wrap_ab_dimer_cutoff(this=self._handle, error=error)
        return ab_dimer_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9551-9593
        
        Parameters
        ----------
        this : Ab_Dimer
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_ab_dimer_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 348
        
        """
        return quippy._quippy.f90wrap_ab_dimer__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_ab_dimer__set__cutoff(self._handle, cutoff)
    
    @property
    def monomer_cutoff(self):
        """
        Element monomer_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 349
        
        """
        return quippy._quippy.f90wrap_ab_dimer__get__monomer_cutoff(self._handle)
    
    @monomer_cutoff.setter
    def monomer_cutoff(self, monomer_cutoff):
        quippy._quippy.f90wrap_ab_dimer__set__monomer_cutoff(self._handle, monomer_cutoff)
    
    @property
    def atomic_number1(self):
        """
        Element atomic_number1 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 350
        
        """
        return quippy._quippy.f90wrap_ab_dimer__get__atomic_number1(self._handle)
    
    @atomic_number1.setter
    def atomic_number1(self, atomic_number1):
        quippy._quippy.f90wrap_ab_dimer__set__atomic_number1(self._handle, atomic_number1)
    
    @property
    def atomic_number2(self):
        """
        Element atomic_number2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 350
        
        """
        return quippy._quippy.f90wrap_ab_dimer__get__atomic_number2(self._handle)
    
    @atomic_number2.setter
    def atomic_number2(self, atomic_number2):
        quippy._quippy.f90wrap_ab_dimer__set__atomic_number2(self._handle, atomic_number2)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 351
        
        """
        return quippy._quippy.f90wrap_ab_dimer__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_ab_dimer__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<ab_dimer>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    monomer_cutoff : ')
        ret.append(repr(self.monomer_cutoff))
        ret.append(',\n    atomic_number1 : ')
        ret.append(repr(self.atomic_number1))
        ret.append(',\n    atomic_number2 : ')
        ret.append(repr(self.atomic_number2))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.atom_real_space")
class atom_real_space(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=atom_real_space)
    
    
    Defined at descriptors.fpp lines 353-359
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Atom_Real_Space(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1796-1813
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : float
        
        
        .. rubric:: args_str options
        
        ======================= ===== ===== ===================================================================
        Name                    Type  Value Doc                                                                
        ======================= ===== ===== ===================================================================
        cutoff                  float 0.00  Space cutoff for atom_real_space-type descriptors                  
        cutoff_transition_width float 0.00  Space transition width for atom_real_space-type descriptors        
        l_max                   int   0     Cutoff for spherical harmonics expansion                           
        alpha                   float 1.0   Width of atomic Gaussians                                          
        zeta                    float 1.0   Exponent of covariance function                                    
        ======================= ===== ===== ===================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_atom_real_space_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Atom_Real_Space
        
        
        Defined at descriptors.fpp lines 1815-1825
        
        Parameters
        ----------
        this : float
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_atom_real_space_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 5182-5312
        
        Parameters
        ----------
        this : float
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_atom_real_space_calc(this=self._handle, at=at._handle, \
            do_descriptor=do_descriptor, do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        atom_real_space_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8977-8985
        
        Parameters
        ----------
        this : float
        error : int
        
        Returns
        -------
        atom_real_space_cutoff : float
        
        """
        atom_real_space_cutoff = quippy._quippy.f90wrap_atom_real_space_cutoff(this=self._handle, error=error)
        return atom_real_space_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9595-9615
        
        Parameters
        ----------
        this : float
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_atom_real_space_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 354
        
        """
        return quippy._quippy.f90wrap_atom_real_space__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_atom_real_space__set__cutoff(self._handle, cutoff)
    
    @property
    def cutoff_transition_width(self):
        """
        Element cutoff_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 355
        
        """
        return quippy._quippy.f90wrap_atom_real_space__get__cutoff_transition_width(self._handle)
    
    @cutoff_transition_width.setter
    def cutoff_transition_width(self, cutoff_transition_width):
        quippy._quippy.f90wrap_atom_real_space__set__cutoff_transition_width(self._handle, cutoff_transition_width)
    
    @property
    def l_max(self):
        """
        Element l_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 356
        
        """
        return quippy._quippy.f90wrap_atom_real_space__get__l_max(self._handle)
    
    @l_max.setter
    def l_max(self, l_max):
        quippy._quippy.f90wrap_atom_real_space__set__l_max(self._handle, l_max)
    
    @property
    def alpha(self):
        """
        Element alpha ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 357
        
        """
        return quippy._quippy.f90wrap_atom_real_space__get__alpha(self._handle)
    
    @alpha.setter
    def alpha(self, alpha):
        quippy._quippy.f90wrap_atom_real_space__set__alpha(self._handle, alpha)
    
    @property
    def zeta(self):
        """
        Element zeta ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 358
        
        """
        return quippy._quippy.f90wrap_atom_real_space__get__zeta(self._handle)
    
    @zeta.setter
    def zeta(self, zeta):
        quippy._quippy.f90wrap_atom_real_space__set__zeta(self._handle, zeta)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 359
        
        """
        return quippy._quippy.f90wrap_atom_real_space__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_atom_real_space__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<atom_real_space>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    cutoff_transition_width : ')
        ret.append(repr(self.cutoff_transition_width))
        ret.append(',\n    l_max : ')
        ret.append(repr(self.l_max))
        ret.append(',\n    alpha : ')
        ret.append(repr(self.alpha))
        ret.append(',\n    zeta : ')
        ret.append(repr(self.zeta))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.power_so3")
class power_so3(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=power_so3)
    
    
    Defined at descriptors.fpp lines 361-367
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Power_So3(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1827-1860
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Power_So3
        
        
        .. rubric:: args_str options
        
        ========== ===== =============== ======================================================================
        Name       Type  Value           Doc                                                                   
        ========== ===== =============== ======================================================================
        cutoff     float 0.00            Cutoff for power_so3-type descriptors                                 
        min_cutoff float 0.00            Cutoff for minimal distances in power_so3-type descriptors            
        l_max      int   4               L_max for power_so3-type descriptors                                  
        n_max      int   4               N_max for power_so3-type descriptors                                  
        Z          int   0               Atomic number of central atom                                         
        n_species  int   1               Number of species for the descriptor                                  
        species_Z  None  PARAM_MANDATORY Atomic number of species                                              
        w          None  PARAM_MANDATORY Weight associated to each atomic type                                 
        ========== ===== =============== ======================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_power_so3_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Power_So3
        
        
        Defined at descriptors.fpp lines 1862-1875
        
        Parameters
        ----------
        this : Power_So3
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_power_so3_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 5314-5541
        
        Parameters
        ----------
        this : Power_So3
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_power_so3_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        power_so3_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8987-8995
        
        Parameters
        ----------
        this : Power_So3
        error : int
        
        Returns
        -------
        power_so3_cutoff : float
        
        """
        power_so3_cutoff = quippy._quippy.f90wrap_power_so3_cutoff(this=self._handle, error=error)
        return power_so3_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9617-9639
        
        Parameters
        ----------
        this : Power_So3
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_power_so3_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def l_max(self):
        """
        Element l_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 362
        
        """
        return quippy._quippy.f90wrap_power_so3__get__l_max(self._handle)
    
    @l_max.setter
    def l_max(self, l_max):
        quippy._quippy.f90wrap_power_so3__set__l_max(self._handle, l_max)
    
    @property
    def n_max(self):
        """
        Element n_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 362
        
        """
        return quippy._quippy.f90wrap_power_so3__get__n_max(self._handle)
    
    @n_max.setter
    def n_max(self, n_max):
        quippy._quippy.f90wrap_power_so3__set__n_max(self._handle, n_max)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 362
        
        """
        return quippy._quippy.f90wrap_power_so3__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_power_so3__set__z(self._handle, z)
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 363
        
        """
        return quippy._quippy.f90wrap_power_so3__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_power_so3__set__cutoff(self._handle, cutoff)
    
    @property
    def min_cutoff(self):
        """
        Element min_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 363
        
        """
        return quippy._quippy.f90wrap_power_so3__get__min_cutoff(self._handle)
    
    @min_cutoff.setter
    def min_cutoff(self, min_cutoff):
        quippy._quippy.f90wrap_power_so3__set__min_cutoff(self._handle, min_cutoff)
    
    @property
    def radial(self):
        """
        Element radial ftype=type(radialfunction_type) pytype=Radialfunction_Type
        
        
        Defined at descriptors.fpp line 364
        
        """
        radial_handle = quippy._quippy.f90wrap_power_so3__get__radial(self._handle)
        if tuple(radial_handle) in self._objs:
            radial = self._objs[tuple(radial_handle)]
        else:
            radial = RadialFunction_type.from_handle(radial_handle)
            self._objs[tuple(radial_handle)] = radial
        return radial
    
    @radial.setter
    def radial(self, radial):
        radial = radial._handle
        quippy._quippy.f90wrap_power_so3__set__radial(self._handle, radial)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 365
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_power_so3__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_power_so3__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def w(self):
        """
        Element w ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 366
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_power_so3__array__w(self._handle)
        if array_handle in self._arrays:
            w = self._arrays[array_handle]
        else:
            w = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_power_so3__array__w)
            self._arrays[array_handle] = w
        return w
    
    @w.setter
    def w(self, w):
        self.w[...] = w
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 367
        
        """
        return quippy._quippy.f90wrap_power_so3__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_power_so3__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<power_so3>{\n']
        ret.append('    l_max : ')
        ret.append(repr(self.l_max))
        ret.append(',\n    n_max : ')
        ret.append(repr(self.n_max))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    min_cutoff : ')
        ret.append(repr(self.min_cutoff))
        ret.append(',\n    radial : ')
        ret.append(repr(self.radial))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    w : ')
        ret.append(repr(self.w))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.power_SO4")
class power_SO4(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=power_so4)
    
    
    Defined at descriptors.fpp lines 369-377
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Power_So4(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1877-1892
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Power_So4
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_power_so4_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Power_So4
        
        
        Defined at descriptors.fpp lines 1894-1908
        
        Parameters
        ----------
        this : Power_So4
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_power_so4_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 5543-5691
        
        Parameters
        ----------
        this : Power_So4
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_power_so4_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        power_so4_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8997-9005
        
        Parameters
        ----------
        this : Power_So4
        error : int
        
        Returns
        -------
        power_so4_cutoff : float
        
        """
        power_so4_cutoff = quippy._quippy.f90wrap_power_so4_cutoff(this=self._handle, error=error)
        return power_so4_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9641-9663
        
        Parameters
        ----------
        this : Power_So4
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_power_so4_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 370
        
        """
        return quippy._quippy.f90wrap_power_so4__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_power_so4__set__cutoff(self._handle, cutoff)
    
    @property
    def j_max(self):
        """
        Element j_max ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 371
        
        """
        return quippy._quippy.f90wrap_power_so4__get__j_max(self._handle)
    
    @j_max.setter
    def j_max(self, j_max):
        quippy._quippy.f90wrap_power_so4__set__j_max(self._handle, j_max)
    
    @property
    def z(self):
        """
        Element z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 371
        
        """
        return quippy._quippy.f90wrap_power_so4__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_power_so4__set__z(self._handle, z)
    
    @property
    def z0_ratio(self):
        """
        Element z0_ratio ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 372
        
        """
        return quippy._quippy.f90wrap_power_so4__get__z0_ratio(self._handle)
    
    @z0_ratio.setter
    def z0_ratio(self, z0_ratio):
        quippy._quippy.f90wrap_power_so4__set__z0_ratio(self._handle, z0_ratio)
    
    @property
    def z0(self):
        """
        Element z0 ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 373
        
        """
        return quippy._quippy.f90wrap_power_so4__get__z0(self._handle)
    
    @z0.setter
    def z0(self, z0):
        quippy._quippy.f90wrap_power_so4__set__z0(self._handle, z0)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 374
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_power_so4__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_power_so4__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def w(self):
        """
        Element w ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 375
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_power_so4__array__w(self._handle)
        if array_handle in self._arrays:
            w = self._arrays[array_handle]
        else:
            w = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_power_so4__array__w)
            self._arrays[array_handle] = w
        return w
    
    @w.setter
    def w(self, w):
        self.w[...] = w
    
    @property
    def fourier_so4(self):
        """
        Element fourier_so4 ftype=type(fourier_so4_type) pytype=Fourier_So4_Type
        
        
        Defined at descriptors.fpp line 376
        
        """
        fourier_so4_handle = quippy._quippy.f90wrap_power_so4__get__fourier_so4(self._handle)
        if tuple(fourier_so4_handle) in self._objs:
            fourier_so4 = self._objs[tuple(fourier_so4_handle)]
        else:
            fourier_so4 = fourier_SO4_type.from_handle(fourier_so4_handle)
            self._objs[tuple(fourier_so4_handle)] = fourier_so4
        return fourier_so4
    
    @fourier_so4.setter
    def fourier_so4(self, fourier_so4):
        fourier_so4 = fourier_so4._handle
        quippy._quippy.f90wrap_power_so4__set__fourier_so4(self._handle, fourier_so4)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 377
        
        """
        return quippy._quippy.f90wrap_power_so4__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_power_so4__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<power_so4>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    j_max : ')
        ret.append(repr(self.j_max))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    z0_ratio : ')
        ret.append(repr(self.z0_ratio))
        ret.append(',\n    z0 : ')
        ret.append(repr(self.z0))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    w : ')
        ret.append(repr(self.w))
        ret.append(',\n    fourier_so4 : ')
        ret.append(repr(self.fourier_so4))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.soap")
class soap(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=soap)
    
    
    Defined at descriptors.fpp lines 379-406
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Soap(args_str[, error])
        
        
        Defined at descriptors.fpp lines 1910-2149
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Soap
        
        
        .. rubric:: args_str options
        
        ============================= ===== =============== ===================================================
        Name                          Type  Value           Doc                                                
        ============================= ===== =============== ===================================================
        cutoff                        None  PARAM_MANDATORY Cutoff for soap-type descriptors                   
        cutoff_transition_width       float 0.50            Cutoff transition width for soap-type descriptors  
        cutoff_dexp                   int   0               Cutoff decay exponent                              
        cutoff_scale                  float 1.0             Cutoff decay scale                                 
        cutoff_rate                   float 1.0             Inverse cutoff decay rate                          
        l_max                         None  PARAM_MANDATORY L_max(spherical harmonics basis band limit) for    
                                                            soap-type descriptors                              
        n_max                         None  PARAM_MANDATORY N_max(number of radial basis functions) for        
                                                            soap-type descriptors                              
        atom_gaussian_width           None  PARAM_MANDATORY Width of atomic Gaussians for soap-type            
                                                            descriptors                                        
        central_weight                float 1.0             Weight of central atom in environment              
        central_reference_all_species bool  F               Place a Gaussian reference for all atom species    
                                                            densities.                                         
        average                       bool  F               Whether to calculate averaged SOAP - one           
                                                            descriptor per atoms object. If false(default)     
                                                            atomic SOAP is returned.                           
        diagonal_radial               bool  F               Only return the n1=n2 elements of the power        
                                                            spectrum.                                          
        covariance_sigma0             float 0.0             sigma_0 parameter in polynomial covariance         
                                                            function                                           
        normalise                     bool  T               Normalise descriptor so magnitude is 1. In this    
                                                            case the kernel of two equivalent environments is  
                                                            1.                                                 
        basis_error_exponent          float 10.0            10^(-basis_error_exponent) is the max difference   
                                                            between the target and the expanded function       
        n_Z                           int   1               How many different types of central atoms to       
                                                            consider                                           
        n_species                     int   1               Number of species for the descriptor               
        species_Z                     None                  Atomic number of species                           
        xml_version                   int   1426512068      Version of GAP the XML potential file was created  
        nu_R                          int   2               radially sensitive correlation order               
        nu_S                          int   2               species sensitive correlation order                
        Z_mix                         bool  F               mix Z channels together                            
        R_mix                         bool  F               mix radial channels together                       
        sym_mix                       bool  F               symmetric mixing                                   
        coupling                      bool  T               Full tensor product(=T) or Elementwise product(=F) 
                                                            between density channels                           
        K                             int   0               Number of mixing channels to create                
        mix_shift                     int   0               shift for random number seed used to generate      
                                                            mixing weights                                     
        Z_map                         None                  string defining the Zmap                           
        radial_basis                  None                  Radial basis functions to use. Options are         
                                                            EQUISPACED_GAUSS, POLY and GTO(default for         
                                                            xml_version > 1987654320                           
        Z                             None  //MANDATORY//   Atomic numbers to be considered for central atom,  
                                                            must be a list                                     
        ============================= ===== =============== ===================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_soap_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Soap
        
        
        Defined at descriptors.fpp lines 2151-2188
        
        Parameters
        ----------
        this : Soap
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_soap_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 6038-7285
        
        Parameters
        ----------
        this : Soap
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ========== ========================================================================
        Name           Type Value      Doc                                                                     
        ============== ==== ========== ========================================================================
        atom_mask_name None NONE       Name of a logical property in the atoms object. For atoms where this    
                                       property is                                                             
        xml_version    int  1423143769 Version of GAP the XML potential file was created                       
        ============== ==== ========== ========================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_soap_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        soap_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 9007-9015
        
        Parameters
        ----------
        this : Soap
        error : int
        
        Returns
        -------
        soap_cutoff : float
        
        """
        soap_cutoff = quippy._quippy.f90wrap_soap_cutoff(this=self._handle, error=error)
        return soap_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9665-9698
        
        Parameters
        ----------
        this : Soap
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_soap_sizes(this=self._handle, at=at._handle, mask=mask, n_index=n_index, \
            error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 380
        
        """
        return quippy._quippy.f90wrap_soap__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_soap__set__cutoff(self._handle, cutoff)
    
    @property
    def cutoff_transition_width(self):
        """
        Element cutoff_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 381
        
        """
        return quippy._quippy.f90wrap_soap__get__cutoff_transition_width(self._handle)
    
    @cutoff_transition_width.setter
    def cutoff_transition_width(self, cutoff_transition_width):
        quippy._quippy.f90wrap_soap__set__cutoff_transition_width(self._handle, cutoff_transition_width)
    
    @property
    def alpha(self):
        """
        Element alpha ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 382
        
        """
        return quippy._quippy.f90wrap_soap__get__alpha(self._handle)
    
    @alpha.setter
    def alpha(self, alpha):
        quippy._quippy.f90wrap_soap__set__alpha(self._handle, alpha)
    
    @property
    def atom_sigma(self):
        """
        Element atom_sigma ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 382
        
        """
        return quippy._quippy.f90wrap_soap__get__atom_sigma(self._handle)
    
    @atom_sigma.setter
    def atom_sigma(self, atom_sigma):
        quippy._quippy.f90wrap_soap__set__atom_sigma(self._handle, atom_sigma)
    
    @property
    def covariance_sigma0(self):
        """
        Element covariance_sigma0 ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 382
        
        """
        return quippy._quippy.f90wrap_soap__get__covariance_sigma0(self._handle)
    
    @covariance_sigma0.setter
    def covariance_sigma0(self, covariance_sigma0):
        quippy._quippy.f90wrap_soap__set__covariance_sigma0(self._handle, covariance_sigma0)
    
    @property
    def central_weight(self):
        """
        Element central_weight ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 382
        
        """
        return quippy._quippy.f90wrap_soap__get__central_weight(self._handle)
    
    @central_weight.setter
    def central_weight(self, central_weight):
        quippy._quippy.f90wrap_soap__set__central_weight(self._handle, central_weight)
    
    @property
    def cutoff_dexp(self):
        """
        Element cutoff_dexp ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 383
        
        """
        return quippy._quippy.f90wrap_soap__get__cutoff_dexp(self._handle)
    
    @cutoff_dexp.setter
    def cutoff_dexp(self, cutoff_dexp):
        quippy._quippy.f90wrap_soap__set__cutoff_dexp(self._handle, cutoff_dexp)
    
    @property
    def cutoff_scale(self):
        """
        Element cutoff_scale ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 384
        
        """
        return quippy._quippy.f90wrap_soap__get__cutoff_scale(self._handle)
    
    @cutoff_scale.setter
    def cutoff_scale(self, cutoff_scale):
        quippy._quippy.f90wrap_soap__set__cutoff_scale(self._handle, cutoff_scale)
    
    @property
    def cutoff_rate(self):
        """
        Element cutoff_rate ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 385
        
        """
        return quippy._quippy.f90wrap_soap__get__cutoff_rate(self._handle)
    
    @cutoff_rate.setter
    def cutoff_rate(self, cutoff_rate):
        quippy._quippy.f90wrap_soap__set__cutoff_rate(self._handle, cutoff_rate)
    
    @property
    def l_max(self):
        """
        Element l_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 386
        
        """
        return quippy._quippy.f90wrap_soap__get__l_max(self._handle)
    
    @l_max.setter
    def l_max(self, l_max):
        quippy._quippy.f90wrap_soap__set__l_max(self._handle, l_max)
    
    @property
    def n_max(self):
        """
        Element n_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 386
        
        """
        return quippy._quippy.f90wrap_soap__get__n_max(self._handle)
    
    @n_max.setter
    def n_max(self, n_max):
        quippy._quippy.f90wrap_soap__set__n_max(self._handle, n_max)
    
    @property
    def n_z(self):
        """
        Element n_z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 386
        
        """
        return quippy._quippy.f90wrap_soap__get__n_z(self._handle)
    
    @n_z.setter
    def n_z(self, n_z):
        quippy._quippy.f90wrap_soap__set__n_z(self._handle, n_z)
    
    @property
    def n_species(self):
        """
        Element n_species ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 386
        
        """
        return quippy._quippy.f90wrap_soap__get__n_species(self._handle)
    
    @n_species.setter
    def n_species(self, n_species):
        quippy._quippy.f90wrap_soap__set__n_species(self._handle, n_species)
    
    @property
    def nu_r(self):
        """
        Element nu_r ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 387
        
        """
        return quippy._quippy.f90wrap_soap__get__nu_r(self._handle)
    
    @nu_r.setter
    def nu_r(self, nu_r):
        quippy._quippy.f90wrap_soap__set__nu_r(self._handle, nu_r)
    
    @property
    def nu_s(self):
        """
        Element nu_s ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 387
        
        """
        return quippy._quippy.f90wrap_soap__get__nu_s(self._handle)
    
    @nu_s.setter
    def nu_s(self, nu_s):
        quippy._quippy.f90wrap_soap__set__nu_s(self._handle, nu_s)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 388
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def z(self):
        """
        Element z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 388
        
        """
        array_ndim, array_type, array_shape, array_handle =     quippy._quippy.f90wrap_soap__array__z(self._handle)
        if array_handle in self._arrays:
            z = self._arrays[array_handle]
        else:
            z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__z)
            self._arrays[array_handle] = z
        return z
    
    @z.setter
    def z(self, z):
        self.z[...] = z
    
    @property
    def r_basis(self):
        """
        Element r_basis ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 389
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap__array__r_basis(self._handle)
        if array_handle in self._arrays:
            r_basis = self._arrays[array_handle]
        else:
            r_basis = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__r_basis)
            self._arrays[array_handle] = r_basis
        return r_basis
    
    @r_basis.setter
    def r_basis(self, r_basis):
        self.r_basis[...] = r_basis
    
    @property
    def cholesky_overlap_basis(self):
        """
        Element cholesky_overlap_basis ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 390
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_soap__array__cholesky_overlap_basis(self._handle)
        if array_handle in self._arrays:
            cholesky_overlap_basis = self._arrays[array_handle]
        else:
            cholesky_overlap_basis = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__cholesky_overlap_basis)
            self._arrays[array_handle] = cholesky_overlap_basis
        return cholesky_overlap_basis
    
    @cholesky_overlap_basis.setter
    def cholesky_overlap_basis(self, cholesky_overlap_basis):
        self.cholesky_overlap_basis[...] = cholesky_overlap_basis
    
    @property
    def transform_basis(self):
        """
        Element transform_basis ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 391
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap__array__transform_basis(self._handle)
        if array_handle in self._arrays:
            transform_basis = self._arrays[array_handle]
        else:
            transform_basis = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__transform_basis)
            self._arrays[array_handle] = transform_basis
        return transform_basis
    
    @transform_basis.setter
    def transform_basis(self, transform_basis):
        self.transform_basis[...] = transform_basis
    
    @property
    def global_(self):
        """
        Element global_ ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 392
        
        """
        return quippy._quippy.f90wrap_soap__get__global_(self._handle)
    
    @global_.setter
    def global_(self, global_):
        quippy._quippy.f90wrap_soap__set__global_(self._handle, global_)
    
    @property
    def central_reference_all_species(self):
        """
        Element central_reference_all_species ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 393
        
        """
        return quippy._quippy.f90wrap_soap__get__central_reference_all_species(self._handle)
    
    @central_reference_all_species.setter
    def central_reference_all_species(self, central_reference_all_species):
        quippy._quippy.f90wrap_soap__set__central_reference_all_species(self._handle, central_reference_all_species)
    
    @property
    def diagonal_radial(self):
        """
        Element diagonal_radial ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 394
        
        """
        return quippy._quippy.f90wrap_soap__get__diagonal_radial(self._handle)
    
    @diagonal_radial.setter
    def diagonal_radial(self, diagonal_radial):
        quippy._quippy.f90wrap_soap__set__diagonal_radial(self._handle, diagonal_radial)
    
    @property
    def normalise(self):
        """
        Element normalise ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 395
        
        """
        return quippy._quippy.f90wrap_soap__get__normalise(self._handle)
    
    @normalise.setter
    def normalise(self, normalise):
        quippy._quippy.f90wrap_soap__set__normalise(self._handle, normalise)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 396
        
        """
        return quippy._quippy.f90wrap_soap__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_soap__set__initialised(self._handle, initialised)
    
    @property
    def z_mix(self):
        """
        Element z_mix ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 397
        
        """
        return quippy._quippy.f90wrap_soap__get__z_mix(self._handle)
    
    @z_mix.setter
    def z_mix(self, z_mix):
        quippy._quippy.f90wrap_soap__set__z_mix(self._handle, z_mix)
    
    @property
    def r_mix(self):
        """
        Element r_mix ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 398
        
        """
        return quippy._quippy.f90wrap_soap__get__r_mix(self._handle)
    
    @r_mix.setter
    def r_mix(self, r_mix):
        quippy._quippy.f90wrap_soap__set__r_mix(self._handle, r_mix)
    
    @property
    def sym_mix(self):
        """
        Element sym_mix ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 399
        
        """
        return quippy._quippy.f90wrap_soap__get__sym_mix(self._handle)
    
    @sym_mix.setter
    def sym_mix(self, sym_mix):
        quippy._quippy.f90wrap_soap__set__sym_mix(self._handle, sym_mix)
    
    @property
    def coupling(self):
        """
        Element coupling ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 400
        
        """
        return quippy._quippy.f90wrap_soap__get__coupling(self._handle)
    
    @coupling.setter
    def coupling(self, coupling):
        quippy._quippy.f90wrap_soap__set__coupling(self._handle, coupling)
    
    @property
    def k(self):
        """
        Element k ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 401
        
        """
        return quippy._quippy.f90wrap_soap__get__k(self._handle)
    
    @k.setter
    def k(self, k):
        quippy._quippy.f90wrap_soap__set__k(self._handle, k)
    
    @property
    def mix_shift(self):
        """
        Element mix_shift ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 402
        
        """
        return quippy._quippy.f90wrap_soap__get__mix_shift(self._handle)
    
    @mix_shift.setter
    def mix_shift(self, mix_shift):
        quippy._quippy.f90wrap_soap__set__mix_shift(self._handle, mix_shift)
    
    @property
    def z_map_str(self):
        """
        Element z_map_str ftype=character(len=string_length) pytype=str
        
        
        Defined at descriptors.fpp line 403
        
        """
        return quippy._quippy.f90wrap_soap__get__z_map_str(self._handle)
    
    @z_map_str.setter
    def z_map_str(self, z_map_str):
        quippy._quippy.f90wrap_soap__set__z_map_str(self._handle, z_map_str)
    
    @property
    def radial_basis(self):
        """
        Element radial_basis ftype=character(len=string_length) pytype=str
        
        
        Defined at descriptors.fpp line 404
        
        """
        return quippy._quippy.f90wrap_soap__get__radial_basis(self._handle)
    
    @radial_basis.setter
    def radial_basis(self, radial_basis):
        quippy._quippy.f90wrap_soap__set__radial_basis(self._handle, radial_basis)
    
    @property
    def qr_factor(self):
        """
        Element qr_factor ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 405
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap__array__qr_factor(self._handle)
        if array_handle in self._arrays:
            qr_factor = self._arrays[array_handle]
        else:
            qr_factor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__qr_factor)
            self._arrays[array_handle] = qr_factor
        return qr_factor
    
    @qr_factor.setter
    def qr_factor(self, qr_factor):
        self.qr_factor[...] = qr_factor
    
    @property
    def qr_tau(self):
        """
        Element qr_tau ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 406
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap__array__qr_tau(self._handle)
        if array_handle in self._arrays:
            qr_tau = self._arrays[array_handle]
        else:
            qr_tau = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap__array__qr_tau)
            self._arrays[array_handle] = qr_tau
        return qr_tau
    
    @qr_tau.setter
    def qr_tau(self, qr_tau):
        self.qr_tau[...] = qr_tau
    
    def __str__(self):
        ret = ['<soap>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    cutoff_transition_width : ')
        ret.append(repr(self.cutoff_transition_width))
        ret.append(',\n    alpha : ')
        ret.append(repr(self.alpha))
        ret.append(',\n    atom_sigma : ')
        ret.append(repr(self.atom_sigma))
        ret.append(',\n    covariance_sigma0 : ')
        ret.append(repr(self.covariance_sigma0))
        ret.append(',\n    central_weight : ')
        ret.append(repr(self.central_weight))
        ret.append(',\n    cutoff_dexp : ')
        ret.append(repr(self.cutoff_dexp))
        ret.append(',\n    cutoff_scale : ')
        ret.append(repr(self.cutoff_scale))
        ret.append(',\n    cutoff_rate : ')
        ret.append(repr(self.cutoff_rate))
        ret.append(',\n    l_max : ')
        ret.append(repr(self.l_max))
        ret.append(',\n    n_max : ')
        ret.append(repr(self.n_max))
        ret.append(',\n    n_z : ')
        ret.append(repr(self.n_z))
        ret.append(',\n    n_species : ')
        ret.append(repr(self.n_species))
        ret.append(',\n    nu_r : ')
        ret.append(repr(self.nu_r))
        ret.append(',\n    nu_s : ')
        ret.append(repr(self.nu_s))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    r_basis : ')
        ret.append(repr(self.r_basis))
        ret.append(',\n    cholesky_overlap_basis : ')
        ret.append(repr(self.cholesky_overlap_basis))
        ret.append(',\n    transform_basis : ')
        ret.append(repr(self.transform_basis))
        ret.append(',\n    global_ : ')
        ret.append(repr(self.global_))
        ret.append(',\n    central_reference_all_species : ')
        ret.append(repr(self.central_reference_all_species))
        ret.append(',\n    diagonal_radial : ')
        ret.append(repr(self.diagonal_radial))
        ret.append(',\n    normalise : ')
        ret.append(repr(self.normalise))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append(',\n    z_mix : ')
        ret.append(repr(self.z_mix))
        ret.append(',\n    r_mix : ')
        ret.append(repr(self.r_mix))
        ret.append(',\n    sym_mix : ')
        ret.append(repr(self.sym_mix))
        ret.append(',\n    coupling : ')
        ret.append(repr(self.coupling))
        ret.append(',\n    k : ')
        ret.append(repr(self.k))
        ret.append(',\n    mix_shift : ')
        ret.append(repr(self.mix_shift))
        ret.append(',\n    z_map_str : ')
        ret.append(repr(self.z_map_str))
        ret.append(',\n    radial_basis : ')
        ret.append(repr(self.radial_basis))
        ret.append(',\n    qr_factor : ')
        ret.append(repr(self.qr_factor))
        ret.append(',\n    qr_tau : ')
        ret.append(repr(self.qr_tau))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.rdf")
class rdf(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=rdf)
    
    
    Defined at descriptors.fpp lines 408-413
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Rdf(args_str[, error])
        
        
        Defined at descriptors.fpp lines 2190-2216
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Rdf
        
        
        .. rubric:: args_str options
        
        ================ ===== ===== ==========================================================================
        Name             Type  Value Doc                                                                       
        ================ ===== ===== ==========================================================================
        cutoff           float 0.00  Cutoff for rdf-type descriptors                                           
        transition_width float 0.20  Width of transition region from 1 to 0                                    
        Z                int   0     Atomic number of central atom                                             
        r_min            float 0.0   Atomic number of central atom                                             
        r_max            float 0.0   Atomic number of central atom                                             
        n_gauss          int   10    Atomic number of central atom                                             
        w_gauss          float 0.0   Atomic number of central atom                                             
        ================ ===== ===== ==========================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_rdf_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Rdf
        
        
        Defined at descriptors.fpp lines 2218-2228
        
        Parameters
        ----------
        this : Rdf
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_rdf_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 7287-7404
        
        Parameters
        ----------
        this : Rdf
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_rdf_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        rdf_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 9017-9025
        
        Parameters
        ----------
        this : Rdf
        error : int
        
        Returns
        -------
        rdf_cutoff : float
        
        """
        rdf_cutoff = quippy._quippy.f90wrap_rdf_cutoff(this=self._handle, error=error)
        return rdf_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9700-9722
        
        Parameters
        ----------
        this : Rdf
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_rdf_sizes(this=self._handle, at=at._handle, mask=mask, n_index=n_index, \
            error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 409
        
        """
        return quippy._quippy.f90wrap_rdf__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_rdf__set__cutoff(self._handle, cutoff)
    
    @property
    def transition_width(self):
        """
        Element transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 410
        
        """
        return quippy._quippy.f90wrap_rdf__get__transition_width(self._handle)
    
    @transition_width.setter
    def transition_width(self, transition_width):
        quippy._quippy.f90wrap_rdf__set__transition_width(self._handle, transition_width)
    
    @property
    def w_gauss(self):
        """
        Element w_gauss ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 410
        
        """
        return quippy._quippy.f90wrap_rdf__get__w_gauss(self._handle)
    
    @w_gauss.setter
    def w_gauss(self, w_gauss):
        quippy._quippy.f90wrap_rdf__set__w_gauss(self._handle, w_gauss)
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 411
        
        """
        return quippy._quippy.f90wrap_rdf__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_rdf__set__z(self._handle, z)
    
    @property
    def n_gauss(self):
        """
        Element n_gauss ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 411
        
        """
        return quippy._quippy.f90wrap_rdf__get__n_gauss(self._handle)
    
    @n_gauss.setter
    def n_gauss(self, n_gauss):
        quippy._quippy.f90wrap_rdf__set__n_gauss(self._handle, n_gauss)
    
    @property
    def r_gauss(self):
        """
        Element r_gauss ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 412
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_rdf__array__r_gauss(self._handle)
        if array_handle in self._arrays:
            r_gauss = self._arrays[array_handle]
        else:
            r_gauss = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_rdf__array__r_gauss)
            self._arrays[array_handle] = r_gauss
        return r_gauss
    
    @r_gauss.setter
    def r_gauss(self, r_gauss):
        self.r_gauss[...] = r_gauss
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 413
        
        """
        return quippy._quippy.f90wrap_rdf__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_rdf__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<rdf>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    transition_width : ')
        ret.append(repr(self.transition_width))
        ret.append(',\n    w_gauss : ')
        ret.append(repr(self.w_gauss))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    n_gauss : ')
        ret.append(repr(self.n_gauss))
        ret.append(',\n    r_gauss : ')
        ret.append(repr(self.r_gauss))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.as_distance_2b")
class as_distance_2b(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=as_distance_2b)
    
    
    Defined at descriptors.fpp lines 415-421
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = As_Distance_2B(args_str[, error])
        
        
        Defined at descriptors.fpp lines 2230-2253
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : As_Distance_2B
        
        
        .. rubric:: args_str options
        
        ============================= ===== =============== ===================================================
        Name                          Type  Value           Doc                                                
        ============================= ===== =============== ===================================================
        min_cutoff                    float 0.00            Lower cutoff for as_distance_2b-type descriptors   
        max_cutoff                    None  PARAM_MANDATORY Higher cutoff for as_distance_2b-type descriptors  
        as_cutoff                     None  PARAM_MANDATORY Cutoff of asymmetricity                            
        overlap_alpha                 float 0.50            Cutoff of asymmetricity                            
        min_transition_width          float 0.50            Transition width of lower cutoff for               
                                                            as_distance_2b-type descriptors                    
        max_transition_width          float 0.50            Transition width of higher cutoff for              
                                                            as_distance_2b-type descriptors                    
        as_transition_width           float 0.10            Transition width of asymmetricity cutoff for       
                                                            as_distance_2b-type descriptors                    
        coordination_cutoff           None  PARAM_MANDATORY Cutoff for coordination function in                
                                                            as_distance_2b-type descriptors                    
        coordination_transition_width float 0.50            Transition width for as_distance_2b-type           
                                                            descriptors                                        
        Z1                            int   0               Atom type #1 in bond                               
        Z2                            int   0               Atom type #2 in bond                               
        ============================= ===== =============== ===================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_as_distance_2b_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class As_Distance_2B
        
        
        Defined at descriptors.fpp lines 2255-2271
        
        Parameters
        ----------
        this : As_Distance_2B
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_as_distance_2b_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 7406-7588
        
        Parameters
        ----------
        this : As_Distance_2B
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_as_distance_2b_calc(this=self._handle, at=at._handle, \
            do_descriptor=do_descriptor, do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        as_distance_2b_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 9027-9035
        
        Parameters
        ----------
        this : As_Distance_2B
        error : int
        
        Returns
        -------
        as_distance_2b_cutoff : float
        
        """
        as_distance_2b_cutoff = quippy._quippy.f90wrap_as_distance_2b_cutoff(this=self._handle, error=error)
        return as_distance_2b_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9724-9753
        
        Parameters
        ----------
        this : As_Distance_2B
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_as_distance_2b_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def min_cutoff(self):
        """
        Element min_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 416
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__min_cutoff(self._handle)
    
    @min_cutoff.setter
    def min_cutoff(self, min_cutoff):
        quippy._quippy.f90wrap_as_distance_2b__set__min_cutoff(self._handle, min_cutoff)
    
    @property
    def max_cutoff(self):
        """
        Element max_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 416
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__max_cutoff(self._handle)
    
    @max_cutoff.setter
    def max_cutoff(self, max_cutoff):
        quippy._quippy.f90wrap_as_distance_2b__set__max_cutoff(self._handle, max_cutoff)
    
    @property
    def as_cutoff(self):
        """
        Element as_cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 416
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__as_cutoff(self._handle)
    
    @as_cutoff.setter
    def as_cutoff(self, as_cutoff):
        quippy._quippy.f90wrap_as_distance_2b__set__as_cutoff(self._handle, as_cutoff)
    
    @property
    def overlap_alpha(self):
        """
        Element overlap_alpha ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 416
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__overlap_alpha(self._handle)
    
    @overlap_alpha.setter
    def overlap_alpha(self, overlap_alpha):
        quippy._quippy.f90wrap_as_distance_2b__set__overlap_alpha(self._handle, overlap_alpha)
    
    @property
    def min_transition_width(self):
        """
        Element min_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 417
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__min_transition_width(self._handle)
    
    @min_transition_width.setter
    def min_transition_width(self, min_transition_width):
        quippy._quippy.f90wrap_as_distance_2b__set__min_transition_width(self._handle, min_transition_width)
    
    @property
    def max_transition_width(self):
        """
        Element max_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 417
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__max_transition_width(self._handle)
    
    @max_transition_width.setter
    def max_transition_width(self, max_transition_width):
        quippy._quippy.f90wrap_as_distance_2b__set__max_transition_width(self._handle, max_transition_width)
    
    @property
    def as_transition_width(self):
        """
        Element as_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 417
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__as_transition_width(self._handle)
    
    @as_transition_width.setter
    def as_transition_width(self, as_transition_width):
        quippy._quippy.f90wrap_as_distance_2b__set__as_transition_width(self._handle, as_transition_width)
    
    @property
    def coordination_transition_width(self):
        """
        Element coordination_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 419
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__coordination_transition_width(self._handle)
    
    @coordination_transition_width.setter
    def coordination_transition_width(self, coordination_transition_width):
        quippy._quippy.f90wrap_as_distance_2b__set__coordination_transition_width(self._handle, coordination_transition_width)
    
    @property
    def z1(self):
        """
        Element z1 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 420
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__z1(self._handle)
    
    @z1.setter
    def z1(self, z1):
        quippy._quippy.f90wrap_as_distance_2b__set__z1(self._handle, z1)
    
    @property
    def z2(self):
        """
        Element z2 ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 420
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__z2(self._handle)
    
    @z2.setter
    def z2(self, z2):
        quippy._quippy.f90wrap_as_distance_2b__set__z2(self._handle, z2)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 421
        
        """
        return quippy._quippy.f90wrap_as_distance_2b__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_as_distance_2b__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<as_distance_2b>{\n']
        ret.append('    min_cutoff : ')
        ret.append(repr(self.min_cutoff))
        ret.append(',\n    max_cutoff : ')
        ret.append(repr(self.max_cutoff))
        ret.append(',\n    as_cutoff : ')
        ret.append(repr(self.as_cutoff))
        ret.append(',\n    overlap_alpha : ')
        ret.append(repr(self.overlap_alpha))
        ret.append(',\n    min_transition_width : ')
        ret.append(repr(self.min_transition_width))
        ret.append(',\n    max_transition_width : ')
        ret.append(repr(self.max_transition_width))
        ret.append(',\n    as_transition_width : ')
        ret.append(repr(self.as_transition_width))
        ret.append(',\n    coordination_transition_width : ')
        ret.append(repr(self.coordination_transition_width))
        ret.append(',\n    z1 : ')
        ret.append(repr(self.z1))
        ret.append(',\n    z2 : ')
        ret.append(repr(self.z2))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.alex")
class alex(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=alex)
    
    
    Defined at descriptors.fpp lines 423-428
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Alex(args_str[, error])
        
        
        Defined at descriptors.fpp lines 2273-2301
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Alex
        
        
        .. rubric:: args_str options
        
        ========= ===== =============== =======================================================================
        Name      Type  Value           Doc                                                                    
        ========= ===== =============== =======================================================================
        cutoff    float 0.00            Cutoff for alex-type descriptors                                       
        Z         int   0               Atomic number of central atom                                          
        power_min int   5               Minimum power of radial basis for the descriptor                       
        power_max int   10              Maximum power of the radial basis for the descriptor                   
        n_species int   1               Number of species for the descriptor                                   
        species_Z None  PARAM_MANDATORY Atomic number of species                                               
        ========= ===== =============== =======================================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_alex_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Alex
        
        
        Defined at descriptors.fpp lines 2303-2310
        
        Parameters
        ----------
        this : Alex
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_alex_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 7590-7834
        
        Parameters
        ----------
        this : Alex
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_alex_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        alex_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 9037-9045
        
        Parameters
        ----------
        this : Alex
        error : int
        
        Returns
        -------
        alex_cutoff : float
        
        """
        alex_cutoff = quippy._quippy.f90wrap_alex_cutoff(this=self._handle, error=error)
        return alex_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9755-9777
        
        Parameters
        ----------
        this : Alex
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_alex_sizes(this=self._handle, at=at._handle, mask=mask, n_index=n_index, \
            error=error)
        return n_descriptors, n_cross
    
    @property
    def z(self):
        """
        Element z ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 424
        
        """
        return quippy._quippy.f90wrap_alex__get__z(self._handle)
    
    @z.setter
    def z(self, z):
        quippy._quippy.f90wrap_alex__set__z(self._handle, z)
    
    @property
    def power_min(self):
        """
        Element power_min ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 424
        
        """
        return quippy._quippy.f90wrap_alex__get__power_min(self._handle)
    
    @power_min.setter
    def power_min(self, power_min):
        quippy._quippy.f90wrap_alex__set__power_min(self._handle, power_min)
    
    @property
    def power_max(self):
        """
        Element power_max ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 424
        
        """
        return quippy._quippy.f90wrap_alex__get__power_max(self._handle)
    
    @power_max.setter
    def power_max(self, power_max):
        quippy._quippy.f90wrap_alex__set__power_max(self._handle, power_max)
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 425
        
        """
        return quippy._quippy.f90wrap_alex__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_alex__set__cutoff(self._handle, cutoff)
    
    @property
    def n_species(self):
        """
        Element n_species ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 426
        
        """
        return quippy._quippy.f90wrap_alex__get__n_species(self._handle)
    
    @n_species.setter
    def n_species(self, n_species):
        quippy._quippy.f90wrap_alex__set__n_species(self._handle, n_species)
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 427
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_alex__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_alex__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 428
        
        """
        return quippy._quippy.f90wrap_alex__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_alex__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<alex>{\n']
        ret.append('    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    power_min : ')
        ret.append(repr(self.power_min))
        ret.append(',\n    power_max : ')
        ret.append(repr(self.power_max))
        ret.append(',\n    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    n_species : ')
        ret.append(repr(self.n_species))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.distance_Nb")
class distance_Nb(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=distance_nb)
    
    
    Defined at descriptors.fpp lines 430-439
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Distance_Nb(args_str[, error])
        
        
        Defined at descriptors.fpp lines 2312-2429
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Distance_Nb
        
        
        .. rubric:: args_str options
        
        ======================= ===== =============== =========================================================
        Name                    Type  Value           Doc                                                      
        ======================= ===== =============== =========================================================
        cutoff                  None  PARAM_MANDATORY Cutoff for distance_Nb-type descriptors                  
        cutoff_transition_width float 0.5             Transition width of cutoff for distance_Nb-type          
                                                      descriptors                                              
        order                   None  PARAM_MANDATORY Many-body order, in terms of number of neighbours        
        compact_clusters        bool  T               If true, generate clusters where the atoms have at least 
                                                      one connection to the central atom. If false, only       
                                                      clusters where all atoms are connected are generated.    
        xml_version             int   1596837814      Version of GAP the XML potential file was created        
        Z                       None  trim(default_Z) Atomic type of neighbours                                
        ======================= ===== =============== =========================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_distance_nb_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Distance_Nb
        
        
        Defined at descriptors.fpp lines 2431-2444
        
        Parameters
        ----------
        this : Distance_Nb
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_distance_nb_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 7836-8039
        
        Parameters
        ----------
        this : Distance_Nb
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_distance_nb_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        distance_nb_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 9047-9055
        
        Parameters
        ----------
        this : Distance_Nb
        error : int
        
        Returns
        -------
        distance_nb_cutoff : float
        
        """
        distance_nb_cutoff = quippy._quippy.f90wrap_distance_nb_cutoff(this=self._handle, error=error)
        return distance_nb_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9779-9795
        
        Parameters
        ----------
        this : Distance_Nb
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_distance_nb_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def cutoff(self):
        """
        Element cutoff ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 431
        
        """
        return quippy._quippy.f90wrap_distance_nb__get__cutoff(self._handle)
    
    @cutoff.setter
    def cutoff(self, cutoff):
        quippy._quippy.f90wrap_distance_nb__set__cutoff(self._handle, cutoff)
    
    @property
    def cutoff_transition_width(self):
        """
        Element cutoff_transition_width ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 432
        
        """
        return quippy._quippy.f90wrap_distance_nb__get__cutoff_transition_width(self._handle)
    
    @cutoff_transition_width.setter
    def cutoff_transition_width(self, cutoff_transition_width):
        quippy._quippy.f90wrap_distance_nb__set__cutoff_transition_width(self._handle, cutoff_transition_width)
    
    @property
    def order(self):
        """
        Element order ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 433
        
        """
        return quippy._quippy.f90wrap_distance_nb__get__order(self._handle)
    
    @order.setter
    def order(self, order):
        quippy._quippy.f90wrap_distance_nb__set__order(self._handle, order)
    
    @property
    def z(self):
        """
        Element z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 434
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_distance_nb__array__z(self._handle)
        if array_handle in self._arrays:
            z = self._arrays[array_handle]
        else:
            z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_distance_nb__array__z)
            self._arrays[array_handle] = z
        return z
    
    @z.setter
    def z(self, z):
        self.z[...] = z
    
    @property
    def n_permutations(self):
        """
        Element n_permutations ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 435
        
        """
        return quippy._quippy.f90wrap_distance_nb__get__n_permutations(self._handle)
    
    @n_permutations.setter
    def n_permutations(self, n_permutations):
        quippy._quippy.f90wrap_distance_nb__set__n_permutations(self._handle, n_permutations)
    
    @property
    def permutations(self):
        """
        Element permutations ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 436
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_distance_nb__array__permutations(self._handle)
        if array_handle in self._arrays:
            permutations = self._arrays[array_handle]
        else:
            permutations = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_distance_nb__array__permutations)
            self._arrays[array_handle] = permutations
        return permutations
    
    @permutations.setter
    def permutations(self, permutations):
        self.permutations[...] = permutations
    
    @property
    def monomerconnectivities(self):
        """
        Element monomerconnectivities ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 437
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_distance_nb__array__monomerconnectivities(self._handle)
        if array_handle in self._arrays:
            monomerconnectivities = self._arrays[array_handle]
        else:
            monomerconnectivities = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_distance_nb__array__monomerconnectivities)
            self._arrays[array_handle] = monomerconnectivities
        return monomerconnectivities
    
    @monomerconnectivities.setter
    def monomerconnectivities(self, monomerconnectivities):
        self.monomerconnectivities[...] = monomerconnectivities
    
    @property
    def compact_clusters(self):
        """
        Element compact_clusters ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 438
        
        """
        return quippy._quippy.f90wrap_distance_nb__get__compact_clusters(self._handle)
    
    @compact_clusters.setter
    def compact_clusters(self, compact_clusters):
        quippy._quippy.f90wrap_distance_nb__set__compact_clusters(self._handle, compact_clusters)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 439
        
        """
        return quippy._quippy.f90wrap_distance_nb__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_distance_nb__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<distance_nb>{\n']
        ret.append('    cutoff : ')
        ret.append(repr(self.cutoff))
        ret.append(',\n    cutoff_transition_width : ')
        ret.append(repr(self.cutoff_transition_width))
        ret.append(',\n    order : ')
        ret.append(repr(self.order))
        ret.append(',\n    z : ')
        ret.append(repr(self.z))
        ret.append(',\n    n_permutations : ')
        ret.append(repr(self.n_permutations))
        ret.append(',\n    permutations : ')
        ret.append(repr(self.permutations))
        ret.append(',\n    monomerconnectivities : ')
        ret.append(repr(self.monomerconnectivities))
        ret.append(',\n    compact_clusters : ')
        ret.append(repr(self.compact_clusters))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.soap_turbo")
class soap_turbo(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=soap_turbo)
    
    
    Defined at descriptors.fpp lines 441-449
    
    """
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Soap_Turbo(args_str[, error])
        
        
        Defined at descriptors.fpp lines 2499-2628
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Soap_Turbo
        
        
        .. rubric:: args_str options
        
        ==================== ===== =============== ============================================================
        Name                 Type  Value           Doc                                                         
        ==================== ===== =============== ============================================================
        l_max                None  PARAM_MANDATORY Angular basis resolution                                    
        n_species            int   1               Number of species for the descriptor                        
        rcut_hard            None  PARAM_MANDATORY Hard cutoff                                                 
        rcut_soft            None  PARAM_MANDATORY Soft cutoff                                                 
        nf                   float 4.0             TODO                                                        
        radial_enhancement   int   0               TODO                                                        
        basis                None  poly3           poly3 or poly3gauss                                         
        scaling_mode         None  polynomial      TODO                                                        
        compress_file        None  None            TODO                                                        
        compress_mode        None  None            TODO                                                        
        central_index        int   1               Index of central atom species_Z in the >species< array      
        alpha_max            None  //MANDATORY//   Radial basis resultion for each species                     
        atom_sigma_r         None  //MANDATORY//   Width of atomic Gaussians for soap-type descriptors in the  
                                                   radial direction                                            
        atom_sigma_r_scaling None  //MANDATORY//   Scaling rate of radial sigma: scaled as a function of       
                                                   neighbour distance                                          
        atom_sigma_t         None  //MANDATORY//   Width of atomic Gaussians for soap-type descriptors in the  
                                                   angular direction                                           
        atom_sigma_t_scaling None  //MANDATORY//   Scaling rate of angular sigma: scaled as a function of      
                                                   neighbour distance                                          
        amplitude_scaling    None  //MANDATORY//   Scaling rate of amplitude: scaled as an inverse function of 
                                                   neighbour distance                                          
        central_weight       None  //MANDATORY//   Weight of central atom in environment                       
        species_Z            None  //MANDATORY//   Atomic number of species, including the central atom        
        ==================== ===== =============== ============================================================
        
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_soap_turbo_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Soap_Turbo
        
        
        Defined at descriptors.fpp lines 2630-2650
        
        Parameters
        ----------
        this : Soap_Turbo
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_soap_turbo_finalise(this=self._handle, error=error)
    
    def calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 8041-8236
        
        Parameters
        ----------
        this : Soap_Turbo
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        do_timing      bool F     Do timing or not                                                             
        ============== ==== ===== =============================================================================
        
        
        """
        descriptor_out = quippy._quippy.f90wrap_soap_turbo_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def cutoff(self, error=None):
        """
        soap_turbo_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 9057-9065
        
        Parameters
        ----------
        this : Soap_Turbo
        error : int
        
        Returns
        -------
        soap_turbo_cutoff : float
        
        """
        soap_turbo_cutoff = quippy._quippy.f90wrap_soap_turbo_cutoff(this=self._handle, error=error)
        return soap_turbo_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 2652-2674
        
        Parameters
        ----------
        this : Soap_Turbo
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_soap_turbo_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    @property
    def rcut_hard(self):
        """
        Element rcut_hard ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 443
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__rcut_hard(self._handle)
    
    @rcut_hard.setter
    def rcut_hard(self, rcut_hard):
        quippy._quippy.f90wrap_soap_turbo__set__rcut_hard(self._handle, rcut_hard)
    
    @property
    def rcut_soft(self):
        """
        Element rcut_soft ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 443
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__rcut_soft(self._handle)
    
    @rcut_soft.setter
    def rcut_soft(self, rcut_soft):
        quippy._quippy.f90wrap_soap_turbo__set__rcut_soft(self._handle, rcut_soft)
    
    @property
    def nf(self):
        """
        Element nf ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 443
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__nf(self._handle)
    
    @nf.setter
    def nf(self, nf):
        quippy._quippy.f90wrap_soap_turbo__set__nf(self._handle, nf)
    
    @property
    def n_species(self):
        """
        Element n_species ftype=integer   pytype=int
        
        
        Defined at descriptors.fpp line 444
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__n_species(self._handle)
    
    @n_species.setter
    def n_species(self, n_species):
        quippy._quippy.f90wrap_soap_turbo__set__n_species(self._handle, n_species)
    
    @property
    def radial_enhancement(self):
        """
        Element radial_enhancement ftype=integer   pytype=int
        
        
        Defined at descriptors.fpp line 444
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__radial_enhancement(self._handle)
    
    @radial_enhancement.setter
    def radial_enhancement(self, radial_enhancement):
        quippy._quippy.f90wrap_soap_turbo__set__radial_enhancement(self._handle, radial_enhancement)
    
    @property
    def central_index(self):
        """
        Element central_index ftype=integer   pytype=int
        
        
        Defined at descriptors.fpp line 444
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__central_index(self._handle)
    
    @central_index.setter
    def central_index(self, central_index):
        quippy._quippy.f90wrap_soap_turbo__set__central_index(self._handle, central_index)
    
    @property
    def l_max(self):
        """
        Element l_max ftype=integer   pytype=int
        
        
        Defined at descriptors.fpp line 444
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__l_max(self._handle)
    
    @l_max.setter
    def l_max(self, l_max):
        quippy._quippy.f90wrap_soap_turbo__set__l_max(self._handle, l_max)
    
    @property
    def compress_p_nonzero(self):
        """
        Element compress_p_nonzero ftype=integer   pytype=int
        
        
        Defined at descriptors.fpp line 444
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__compress_p_nonzero(self._handle)
    
    @compress_p_nonzero.setter
    def compress_p_nonzero(self, compress_p_nonzero):
        quippy._quippy.f90wrap_soap_turbo__set__compress_p_nonzero(self._handle, compress_p_nonzero)
    
    @property
    def basis(self):
        """
        Element basis ftype=character(len=string_length) pytype=str
        
        
        Defined at descriptors.fpp line 445
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__basis(self._handle)
    
    @basis.setter
    def basis(self, basis):
        quippy._quippy.f90wrap_soap_turbo__set__basis(self._handle, basis)
    
    @property
    def scaling_mode(self):
        """
        Element scaling_mode ftype=character(len=string_length) pytype=str
        
        
        Defined at descriptors.fpp line 445
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__scaling_mode(self._handle)
    
    @scaling_mode.setter
    def scaling_mode(self, scaling_mode):
        quippy._quippy.f90wrap_soap_turbo__set__scaling_mode(self._handle, scaling_mode)
    
    @property
    def compress_file(self):
        """
        Element compress_file ftype=character(len=string_length) pytype=str
        
        
        Defined at descriptors.fpp line 445
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__compress_file(self._handle)
    
    @compress_file.setter
    def compress_file(self, compress_file):
        quippy._quippy.f90wrap_soap_turbo__set__compress_file(self._handle, compress_file)
    
    @property
    def compress_mode(self):
        """
        Element compress_mode ftype=character(len=string_length) pytype=str
        
        
        Defined at descriptors.fpp line 445
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__compress_mode(self._handle)
    
    @compress_mode.setter
    def compress_mode(self, compress_mode):
        quippy._quippy.f90wrap_soap_turbo__set__compress_mode(self._handle, compress_mode)
    
    @property
    def atom_sigma_r(self):
        """
        Element atom_sigma_r ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_r(self._handle)
        if array_handle in self._arrays:
            atom_sigma_r = self._arrays[array_handle]
        else:
            atom_sigma_r = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_r)
            self._arrays[array_handle] = atom_sigma_r
        return atom_sigma_r
    
    @atom_sigma_r.setter
    def atom_sigma_r(self, atom_sigma_r):
        self.atom_sigma_r[...] = atom_sigma_r
    
    @property
    def atom_sigma_r_scaling(self):
        """
        Element atom_sigma_r_scaling ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_r_scaling(self._handle)
        if array_handle in self._arrays:
            atom_sigma_r_scaling = self._arrays[array_handle]
        else:
            atom_sigma_r_scaling = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_r_scaling)
            self._arrays[array_handle] = atom_sigma_r_scaling
        return atom_sigma_r_scaling
    
    @atom_sigma_r_scaling.setter
    def atom_sigma_r_scaling(self, atom_sigma_r_scaling):
        self.atom_sigma_r_scaling[...] = atom_sigma_r_scaling
    
    @property
    def atom_sigma_t(self):
        """
        Element atom_sigma_t ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_t(self._handle)
        if array_handle in self._arrays:
            atom_sigma_t = self._arrays[array_handle]
        else:
            atom_sigma_t = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_t)
            self._arrays[array_handle] = atom_sigma_t
        return atom_sigma_t
    
    @atom_sigma_t.setter
    def atom_sigma_t(self, atom_sigma_t):
        self.atom_sigma_t[...] = atom_sigma_t
    
    @property
    def atom_sigma_t_scaling(self):
        """
        Element atom_sigma_t_scaling ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_t_scaling(self._handle)
        if array_handle in self._arrays:
            atom_sigma_t_scaling = self._arrays[array_handle]
        else:
            atom_sigma_t_scaling = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__atom_sigma_t_scaling)
            self._arrays[array_handle] = atom_sigma_t_scaling
        return atom_sigma_t_scaling
    
    @atom_sigma_t_scaling.setter
    def atom_sigma_t_scaling(self, atom_sigma_t_scaling):
        self.atom_sigma_t_scaling[...] = atom_sigma_t_scaling
    
    @property
    def amplitude_scaling(self):
        """
        Element amplitude_scaling ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_soap_turbo__array__amplitude_scaling(self._handle)
        if array_handle in self._arrays:
            amplitude_scaling = self._arrays[array_handle]
        else:
            amplitude_scaling = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__amplitude_scaling)
            self._arrays[array_handle] = amplitude_scaling
        return amplitude_scaling
    
    @amplitude_scaling.setter
    def amplitude_scaling(self, amplitude_scaling):
        self.amplitude_scaling[...] = amplitude_scaling
    
    @property
    def central_weight(self):
        """
        Element central_weight ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_soap_turbo__array__central_weight(self._handle)
        if array_handle in self._arrays:
            central_weight = self._arrays[array_handle]
        else:
            central_weight = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__central_weight)
            self._arrays[array_handle] = central_weight
        return central_weight
    
    @central_weight.setter
    def central_weight(self, central_weight):
        self.central_weight[...] = central_weight
    
    @property
    def compress_p_el(self):
        """
        Element compress_p_el ftype=real(dp) pytype=float
        
        
        Defined at descriptors.fpp line 447
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_soap_turbo__array__compress_p_el(self._handle)
        if array_handle in self._arrays:
            compress_p_el = self._arrays[array_handle]
        else:
            compress_p_el = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__compress_p_el)
            self._arrays[array_handle] = compress_p_el
        return compress_p_el
    
    @compress_p_el.setter
    def compress_p_el(self, compress_p_el):
        self.compress_p_el[...] = compress_p_el
    
    @property
    def species_z(self):
        """
        Element species_z ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 448
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap_turbo__array__species_z(self._handle)
        if array_handle in self._arrays:
            species_z = self._arrays[array_handle]
        else:
            species_z = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__species_z)
            self._arrays[array_handle] = species_z
        return species_z
    
    @species_z.setter
    def species_z(self, species_z):
        self.species_z[...] = species_z
    
    @property
    def alpha_max(self):
        """
        Element alpha_max ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 448
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap_turbo__array__alpha_max(self._handle)
        if array_handle in self._arrays:
            alpha_max = self._arrays[array_handle]
        else:
            alpha_max = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__alpha_max)
            self._arrays[array_handle] = alpha_max
        return alpha_max
    
    @alpha_max.setter
    def alpha_max(self, alpha_max):
        self.alpha_max[...] = alpha_max
    
    @property
    def compress_p_i(self):
        """
        Element compress_p_i ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 448
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap_turbo__array__compress_p_i(self._handle)
        if array_handle in self._arrays:
            compress_p_i = self._arrays[array_handle]
        else:
            compress_p_i = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__compress_p_i)
            self._arrays[array_handle] = compress_p_i
        return compress_p_i
    
    @compress_p_i.setter
    def compress_p_i(self, compress_p_i):
        self.compress_p_i[...] = compress_p_i
    
    @property
    def compress_p_j(self):
        """
        Element compress_p_j ftype=integer pytype=int
        
        
        Defined at descriptors.fpp line 448
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_soap_turbo__array__compress_p_j(self._handle)
        if array_handle in self._arrays:
            compress_p_j = self._arrays[array_handle]
        else:
            compress_p_j = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_soap_turbo__array__compress_p_j)
            self._arrays[array_handle] = compress_p_j
        return compress_p_j
    
    @compress_p_j.setter
    def compress_p_j(self, compress_p_j):
        self.compress_p_j[...] = compress_p_j
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 449
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_soap_turbo__set__initialised(self._handle, initialised)
    
    @property
    def compress(self):
        """
        Element compress ftype=logical pytype=bool
        
        
        Defined at descriptors.fpp line 449
        
        """
        return quippy._quippy.f90wrap_soap_turbo__get__compress(self._handle)
    
    @compress.setter
    def compress(self, compress):
        quippy._quippy.f90wrap_soap_turbo__set__compress(self._handle, compress)
    
    def __str__(self):
        ret = ['<soap_turbo>{\n']
        ret.append('    rcut_hard : ')
        ret.append(repr(self.rcut_hard))
        ret.append(',\n    rcut_soft : ')
        ret.append(repr(self.rcut_soft))
        ret.append(',\n    nf : ')
        ret.append(repr(self.nf))
        ret.append(',\n    n_species : ')
        ret.append(repr(self.n_species))
        ret.append(',\n    radial_enhancement : ')
        ret.append(repr(self.radial_enhancement))
        ret.append(',\n    central_index : ')
        ret.append(repr(self.central_index))
        ret.append(',\n    l_max : ')
        ret.append(repr(self.l_max))
        ret.append(',\n    compress_p_nonzero : ')
        ret.append(repr(self.compress_p_nonzero))
        ret.append(',\n    basis : ')
        ret.append(repr(self.basis))
        ret.append(',\n    scaling_mode : ')
        ret.append(repr(self.scaling_mode))
        ret.append(',\n    compress_file : ')
        ret.append(repr(self.compress_file))
        ret.append(',\n    compress_mode : ')
        ret.append(repr(self.compress_mode))
        ret.append(',\n    atom_sigma_r : ')
        ret.append(repr(self.atom_sigma_r))
        ret.append(',\n    atom_sigma_r_scaling : ')
        ret.append(repr(self.atom_sigma_r_scaling))
        ret.append(',\n    atom_sigma_t : ')
        ret.append(repr(self.atom_sigma_t))
        ret.append(',\n    atom_sigma_t_scaling : ')
        ret.append(repr(self.atom_sigma_t_scaling))
        ret.append(',\n    amplitude_scaling : ')
        ret.append(repr(self.amplitude_scaling))
        ret.append(',\n    central_weight : ')
        ret.append(repr(self.central_weight))
        ret.append(',\n    compress_p_el : ')
        ret.append(repr(self.compress_p_el))
        ret.append(',\n    species_z : ')
        ret.append(repr(self.species_z))
        ret.append(',\n    alpha_max : ')
        ret.append(repr(self.alpha_max))
        ret.append(',\n    compress_p_i : ')
        ret.append(repr(self.compress_p_i))
        ret.append(',\n    compress_p_j : ')
        ret.append(repr(self.compress_p_j))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append(',\n    compress : ')
        ret.append(repr(self.compress))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.descriptor")
class descriptor(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=descriptor)
    
    
    Defined at descriptors.fpp lines 464-489
    
    """
    def dimensions(self, error=None):
        """
        descriptor_dimensions = dimensions(self[, error])
        
        
        Defined at descriptors.fpp lines 8455-8510
        
        Parameters
        ----------
        this : Descriptor
        error : int
        
        Returns
        -------
        descriptor_dimensions : int
        
        """
        descriptor_dimensions = quippy._quippy.f90wrap_descriptor_dimensions(this=self._handle, error=error)
        return descriptor_dimensions
    
    def n_permutations(self, error=None):
        """
        descriptor_n_permutations = n_permutations(self[, error])
        
        
        Defined at descriptors.fpp lines 9813-9835
        
        Parameters
        ----------
        this : Descriptor
        error : int
        
        Returns
        -------
        descriptor_n_permutations : int
        
        """
        descriptor_n_permutations = quippy._quippy.f90wrap_descriptor_n_permutations(this=self._handle, error=error)
        return descriptor_n_permutations
    
    def permutations(self, permutations, error=None):
        """
        permutations(self, permutations[, error])
        
        
        Defined at descriptors.fpp lines 9837-9880
        
        Parameters
        ----------
        this : Descriptor
        permutations : int array
        error : int
        
        """
        quippy._quippy.f90wrap_descriptor_permutations(this=self._handle, permutations=permutations, error=error)
    
    def __init__(self, args_str, error=None, handle=None):
        """
        self = Descriptor(args_str[, error])
        
        
        Defined at descriptors.fpp lines 674-729
        
        Parameters
        ----------
        args_str : str
        error : int
        
        Returns
        -------
        this : Descriptor
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_descriptor_initialise(args_str=args_str, error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self, error=None):
        """
        Destructor for class Descriptor
        
        
        Defined at descriptors.fpp lines 731-782
        
        Parameters
        ----------
        this : Descriptor
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_descriptor_finalise(this=self._handle, error=error)
    
    def cutoff(self, error=None):
        """
        descriptor_cutoff = cutoff(self[, error])
        
        
        Defined at descriptors.fpp lines 8782-8835
        
        Parameters
        ----------
        this : Descriptor
        error : int
        
        Returns
        -------
        descriptor_cutoff : float
        
        """
        descriptor_cutoff = quippy._quippy.f90wrap_descriptor_cutoff(this=self._handle, error=error)
        return descriptor_cutoff
    
    def sizes(self, at, mask=None, n_index=None, error=None):
        """
        n_descriptors, n_cross = sizes(self, at[, mask, n_index, error])
        
        
        Defined at descriptors.fpp lines 9067-9148
        
        Parameters
        ----------
        this : Descriptor
        at : Atoms
        mask : bool array
        n_index : int
        error : int
        
        Returns
        -------
        n_descriptors : int
        n_cross : int
        
        """
        n_descriptors, n_cross = quippy._quippy.f90wrap_descriptor_sizes(this=self._handle, at=at._handle, mask=mask, \
            n_index=n_index, error=error)
        return n_descriptors, n_cross
    
    def _calc(self, at, do_descriptor=None, do_grad_descriptor=None, args_str=None, error=None):
        """
        descriptor_out = _calc(self, at[, do_descriptor, do_grad_descriptor, args_str, error])
        
        
        Defined at descriptors.fpp lines 2789-2851
        
        Parameters
        ----------
        this : Descriptor
        at : Atoms
        do_descriptor : bool
        do_grad_descriptor : bool
        args_str : str
        error : int
        
        Returns
        -------
        descriptor_out : Descriptor_Data
        
        """
        descriptor_out = quippy._quippy.f90wrap_descriptor_calc(this=self._handle, at=at._handle, do_descriptor=do_descriptor, \
            do_grad_descriptor=do_grad_descriptor, args_str=args_str, error=error)
        descriptor_out = f90wrap.runtime.lookup_class("quippy.descriptor_data").from_handle(descriptor_out, alloc=True)
        return descriptor_out
    
    def _calc_array(self, at, descriptor_out=None, covariance_cutoff=None, descriptor_index=None, grad_descriptor_out=None, \
        grad_descriptor_index=None, grad_descriptor_pos=None, grad_covariance_cutoff=None, args_str=None, error=None):
        """
        _calc_array(self, at[, descriptor_out, covariance_cutoff, descriptor_index, grad_descriptor_out, grad_descriptor_index, \
            grad_descriptor_pos, grad_covariance_cutoff, args_str, error])
        
        
        Defined at descriptors.fpp lines 2853-2932
        
        Parameters
        ----------
        this : Descriptor
        at : Atoms
        descriptor_out : float array
        covariance_cutoff : float array
        descriptor_index : int array
        grad_descriptor_out : float array
        grad_descriptor_index : int array
        grad_descriptor_pos : float array
        grad_covariance_cutoff : float array
        args_str : str
        error : int
        
        
        .. rubric:: args_str options
        
        ============== ==== ===== =============================================================================
        Name           Type Value Doc                                                                          
        ============== ==== ===== =============================================================================
        atom_mask_name None NONE  Name of a logical property in the atoms object. For atoms where this         
                                  property is true descriptors are                                             
        ============== ==== ===== =============================================================================
        
        
        """
        quippy._quippy.f90wrap_descriptor_calc_array(this=self._handle, at=at._handle, descriptor_out=descriptor_out, \
            covariance_cutoff=covariance_cutoff, descriptor_index=descriptor_index, grad_descriptor_out=grad_descriptor_out, \
            grad_descriptor_index=grad_descriptor_index, grad_descriptor_pos=grad_descriptor_pos, \
            grad_covariance_cutoff=grad_covariance_cutoff, args_str=args_str, error=error)
    
    def calc(*args, **kwargs):
        """
        calc(*args, **kwargs)
        
        
        Defined at descriptors.fpp lines 531-535
        
        Overloaded interface containing the following procedures:
          _calc
          _calc_array
        
        """
        for proc in [descriptor._calc, descriptor._calc_array]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    @property
    def descriptor_type(self):
        """
        Element descriptor_type ftype=integer  pytype=int
        
        
        Defined at descriptors.fpp line 465
        
        """
        return quippy._quippy.f90wrap_descriptor__get__descriptor_type(self._handle)
    
    @descriptor_type.setter
    def descriptor_type(self, descriptor_type):
        quippy._quippy.f90wrap_descriptor__set__descriptor_type(self._handle, descriptor_type)
    
    @property
    def descriptor_bispectrum_so4(self):
        """
        Element descriptor_bispectrum_so4 ftype=type(bispectrum_so4) pytype=Bispectrum_So4
        
        
        Defined at descriptors.fpp line 466
        
        """
        descriptor_bispectrum_so4_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_bispectrum_so4(self._handle)
        if tuple(descriptor_bispectrum_so4_handle) in self._objs:
            descriptor_bispectrum_so4 = self._objs[tuple(descriptor_bispectrum_so4_handle)]
        else:
            descriptor_bispectrum_so4 = bispectrum_SO4.from_handle(descriptor_bispectrum_so4_handle)
            self._objs[tuple(descriptor_bispectrum_so4_handle)] = descriptor_bispectrum_so4
        return descriptor_bispectrum_so4
    
    @descriptor_bispectrum_so4.setter
    def descriptor_bispectrum_so4(self, descriptor_bispectrum_so4):
        descriptor_bispectrum_so4 = descriptor_bispectrum_so4._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_bispectrum_so4(self._handle, descriptor_bispectrum_so4)
    
    @property
    def descriptor_bispectrum_so3(self):
        """
        Element descriptor_bispectrum_so3 ftype=type(bispectrum_so3) pytype=Bispectrum_So3
        
        
        Defined at descriptors.fpp line 467
        
        """
        descriptor_bispectrum_so3_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_bispectrum_so3(self._handle)
        if tuple(descriptor_bispectrum_so3_handle) in self._objs:
            descriptor_bispectrum_so3 = self._objs[tuple(descriptor_bispectrum_so3_handle)]
        else:
            descriptor_bispectrum_so3 = bispectrum_SO3.from_handle(descriptor_bispectrum_so3_handle)
            self._objs[tuple(descriptor_bispectrum_so3_handle)] = descriptor_bispectrum_so3
        return descriptor_bispectrum_so3
    
    @descriptor_bispectrum_so3.setter
    def descriptor_bispectrum_so3(self, descriptor_bispectrum_so3):
        descriptor_bispectrum_so3 = descriptor_bispectrum_so3._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_bispectrum_so3(self._handle, descriptor_bispectrum_so3)
    
    @property
    def descriptor_behler(self):
        """
        Element descriptor_behler ftype=type(behler) pytype=Behler
        
        
        Defined at descriptors.fpp line 468
        
        """
        descriptor_behler_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_behler(self._handle)
        if tuple(descriptor_behler_handle) in self._objs:
            descriptor_behler = self._objs[tuple(descriptor_behler_handle)]
        else:
            descriptor_behler = behler.from_handle(descriptor_behler_handle)
            self._objs[tuple(descriptor_behler_handle)] = descriptor_behler
        return descriptor_behler
    
    @descriptor_behler.setter
    def descriptor_behler(self, descriptor_behler):
        descriptor_behler = descriptor_behler._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_behler(self._handle, descriptor_behler)
    
    @property
    def descriptor_distance_2b(self):
        """
        Element descriptor_distance_2b ftype=type(distance_2b) pytype=Distance_2B
        
        
        Defined at descriptors.fpp line 469
        
        """
        descriptor_distance_2b_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_distance_2b(self._handle)
        if tuple(descriptor_distance_2b_handle) in self._objs:
            descriptor_distance_2b = self._objs[tuple(descriptor_distance_2b_handle)]
        else:
            descriptor_distance_2b = distance_2b.from_handle(descriptor_distance_2b_handle)
            self._objs[tuple(descriptor_distance_2b_handle)] = descriptor_distance_2b
        return descriptor_distance_2b
    
    @descriptor_distance_2b.setter
    def descriptor_distance_2b(self, descriptor_distance_2b):
        descriptor_distance_2b = descriptor_distance_2b._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_distance_2b(self._handle, descriptor_distance_2b)
    
    @property
    def descriptor_coordination(self):
        """
        Element descriptor_coordination ftype=type(coordination) pytype=Coordination
        
        
        Defined at descriptors.fpp line 470
        
        """
        descriptor_coordination_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_coordination(self._handle)
        if tuple(descriptor_coordination_handle) in self._objs:
            descriptor_coordination = self._objs[tuple(descriptor_coordination_handle)]
        else:
            descriptor_coordination = coordination.from_handle(descriptor_coordination_handle)
            self._objs[tuple(descriptor_coordination_handle)] = descriptor_coordination
        return descriptor_coordination
    
    @descriptor_coordination.setter
    def descriptor_coordination(self, descriptor_coordination):
        descriptor_coordination = descriptor_coordination._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_coordination(self._handle, descriptor_coordination)
    
    @property
    def descriptor_angle_3b(self):
        """
        Element descriptor_angle_3b ftype=type(angle_3b) pytype=Angle_3B
        
        
        Defined at descriptors.fpp line 471
        
        """
        descriptor_angle_3b_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_angle_3b(self._handle)
        if tuple(descriptor_angle_3b_handle) in self._objs:
            descriptor_angle_3b = self._objs[tuple(descriptor_angle_3b_handle)]
        else:
            descriptor_angle_3b = angle_3b.from_handle(descriptor_angle_3b_handle)
            self._objs[tuple(descriptor_angle_3b_handle)] = descriptor_angle_3b
        return descriptor_angle_3b
    
    @descriptor_angle_3b.setter
    def descriptor_angle_3b(self, descriptor_angle_3b):
        descriptor_angle_3b = descriptor_angle_3b._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_angle_3b(self._handle, descriptor_angle_3b)
    
    @property
    def descriptor_co_angle_3b(self):
        """
        Element descriptor_co_angle_3b ftype=type(co_angle_3b) pytype=Co_Angle_3B
        
        
        Defined at descriptors.fpp line 472
        
        """
        descriptor_co_angle_3b_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_co_angle_3b(self._handle)
        if tuple(descriptor_co_angle_3b_handle) in self._objs:
            descriptor_co_angle_3b = self._objs[tuple(descriptor_co_angle_3b_handle)]
        else:
            descriptor_co_angle_3b = co_angle_3b.from_handle(descriptor_co_angle_3b_handle)
            self._objs[tuple(descriptor_co_angle_3b_handle)] = descriptor_co_angle_3b
        return descriptor_co_angle_3b
    
    @descriptor_co_angle_3b.setter
    def descriptor_co_angle_3b(self, descriptor_co_angle_3b):
        descriptor_co_angle_3b = descriptor_co_angle_3b._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_co_angle_3b(self._handle, descriptor_co_angle_3b)
    
    @property
    def descriptor_co_distance_2b(self):
        """
        Element descriptor_co_distance_2b ftype=type(co_distance_2b) pytype=Co_Distance_2B
        
        
        Defined at descriptors.fpp line 473
        
        """
        descriptor_co_distance_2b_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_co_distance_2b(self._handle)
        if tuple(descriptor_co_distance_2b_handle) in self._objs:
            descriptor_co_distance_2b = self._objs[tuple(descriptor_co_distance_2b_handle)]
        else:
            descriptor_co_distance_2b = co_distance_2b.from_handle(descriptor_co_distance_2b_handle)
            self._objs[tuple(descriptor_co_distance_2b_handle)] = descriptor_co_distance_2b
        return descriptor_co_distance_2b
    
    @descriptor_co_distance_2b.setter
    def descriptor_co_distance_2b(self, descriptor_co_distance_2b):
        descriptor_co_distance_2b = descriptor_co_distance_2b._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_co_distance_2b(self._handle, descriptor_co_distance_2b)
    
    @property
    def descriptor_cosnx(self):
        """
        Element descriptor_cosnx ftype=type(cosnx) pytype=Cosnx
        
        
        Defined at descriptors.fpp line 474
        
        """
        descriptor_cosnx_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_cosnx(self._handle)
        if tuple(descriptor_cosnx_handle) in self._objs:
            descriptor_cosnx = self._objs[tuple(descriptor_cosnx_handle)]
        else:
            descriptor_cosnx = cosnx.from_handle(descriptor_cosnx_handle)
            self._objs[tuple(descriptor_cosnx_handle)] = descriptor_cosnx
        return descriptor_cosnx
    
    @descriptor_cosnx.setter
    def descriptor_cosnx(self, descriptor_cosnx):
        descriptor_cosnx = descriptor_cosnx._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_cosnx(self._handle, descriptor_cosnx)
    
    @property
    def descriptor_trihis(self):
        """
        Element descriptor_trihis ftype=type(trihis) pytype=Trihis
        
        
        Defined at descriptors.fpp line 475
        
        """
        descriptor_trihis_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_trihis(self._handle)
        if tuple(descriptor_trihis_handle) in self._objs:
            descriptor_trihis = self._objs[tuple(descriptor_trihis_handle)]
        else:
            descriptor_trihis = trihis.from_handle(descriptor_trihis_handle)
            self._objs[tuple(descriptor_trihis_handle)] = descriptor_trihis
        return descriptor_trihis
    
    @descriptor_trihis.setter
    def descriptor_trihis(self, descriptor_trihis):
        descriptor_trihis = descriptor_trihis._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_trihis(self._handle, descriptor_trihis)
    
    @property
    def descriptor_water_monomer(self):
        """
        Element descriptor_water_monomer ftype=type(water_monomer) pytype=Water_Monomer
        
        
        Defined at descriptors.fpp line 476
        
        """
        descriptor_water_monomer_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_water_monomer(self._handle)
        if tuple(descriptor_water_monomer_handle) in self._objs:
            descriptor_water_monomer = self._objs[tuple(descriptor_water_monomer_handle)]
        else:
            descriptor_water_monomer = water_monomer.from_handle(descriptor_water_monomer_handle)
            self._objs[tuple(descriptor_water_monomer_handle)] = descriptor_water_monomer
        return descriptor_water_monomer
    
    @descriptor_water_monomer.setter
    def descriptor_water_monomer(self, descriptor_water_monomer):
        descriptor_water_monomer = descriptor_water_monomer._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_water_monomer(self._handle, descriptor_water_monomer)
    
    @property
    def descriptor_water_dimer(self):
        """
        Element descriptor_water_dimer ftype=type(water_dimer) pytype=Water_Dimer
        
        
        Defined at descriptors.fpp line 477
        
        """
        descriptor_water_dimer_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_water_dimer(self._handle)
        if tuple(descriptor_water_dimer_handle) in self._objs:
            descriptor_water_dimer = self._objs[tuple(descriptor_water_dimer_handle)]
        else:
            descriptor_water_dimer = water_dimer.from_handle(descriptor_water_dimer_handle)
            self._objs[tuple(descriptor_water_dimer_handle)] = descriptor_water_dimer
        return descriptor_water_dimer
    
    @descriptor_water_dimer.setter
    def descriptor_water_dimer(self, descriptor_water_dimer):
        descriptor_water_dimer = descriptor_water_dimer._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_water_dimer(self._handle, descriptor_water_dimer)
    
    @property
    def descriptor_a2_dimer(self):
        """
        Element descriptor_a2_dimer ftype=type(a2_dimer) pytype=A2_Dimer
        
        
        Defined at descriptors.fpp line 478
        
        """
        descriptor_a2_dimer_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_a2_dimer(self._handle)
        if tuple(descriptor_a2_dimer_handle) in self._objs:
            descriptor_a2_dimer = self._objs[tuple(descriptor_a2_dimer_handle)]
        else:
            descriptor_a2_dimer = A2_dimer.from_handle(descriptor_a2_dimer_handle)
            self._objs[tuple(descriptor_a2_dimer_handle)] = descriptor_a2_dimer
        return descriptor_a2_dimer
    
    @descriptor_a2_dimer.setter
    def descriptor_a2_dimer(self, descriptor_a2_dimer):
        descriptor_a2_dimer = descriptor_a2_dimer._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_a2_dimer(self._handle, descriptor_a2_dimer)
    
    @property
    def descriptor_ab_dimer(self):
        """
        Element descriptor_ab_dimer ftype=type(ab_dimer) pytype=Ab_Dimer
        
        
        Defined at descriptors.fpp line 479
        
        """
        descriptor_ab_dimer_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_ab_dimer(self._handle)
        if tuple(descriptor_ab_dimer_handle) in self._objs:
            descriptor_ab_dimer = self._objs[tuple(descriptor_ab_dimer_handle)]
        else:
            descriptor_ab_dimer = AB_dimer.from_handle(descriptor_ab_dimer_handle)
            self._objs[tuple(descriptor_ab_dimer_handle)] = descriptor_ab_dimer
        return descriptor_ab_dimer
    
    @descriptor_ab_dimer.setter
    def descriptor_ab_dimer(self, descriptor_ab_dimer):
        descriptor_ab_dimer = descriptor_ab_dimer._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_ab_dimer(self._handle, descriptor_ab_dimer)
    
    @property
    def descriptor_atom_real_space(self):
        """
        Element descriptor_atom_real_space ftype=type(atom_real_space) pytype=float
        
        
        Defined at descriptors.fpp line 480
        
        """
        descriptor_atom_real_space_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_atom_real_space(self._handle)
        if tuple(descriptor_atom_real_space_handle) in self._objs:
            descriptor_atom_real_space = self._objs[tuple(descriptor_atom_real_space_handle)]
        else:
            descriptor_atom_real_space = atom_real_space.from_handle(descriptor_atom_real_space_handle)
            self._objs[tuple(descriptor_atom_real_space_handle)] = descriptor_atom_real_space
        return descriptor_atom_real_space
    
    @descriptor_atom_real_space.setter
    def descriptor_atom_real_space(self, descriptor_atom_real_space):
        descriptor_atom_real_space = descriptor_atom_real_space._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_atom_real_space(self._handle, descriptor_atom_real_space)
    
    @property
    def descriptor_power_so3(self):
        """
        Element descriptor_power_so3 ftype=type(power_so3) pytype=Power_So3
        
        
        Defined at descriptors.fpp line 481
        
        """
        descriptor_power_so3_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_power_so3(self._handle)
        if tuple(descriptor_power_so3_handle) in self._objs:
            descriptor_power_so3 = self._objs[tuple(descriptor_power_so3_handle)]
        else:
            descriptor_power_so3 = power_so3.from_handle(descriptor_power_so3_handle)
            self._objs[tuple(descriptor_power_so3_handle)] = descriptor_power_so3
        return descriptor_power_so3
    
    @descriptor_power_so3.setter
    def descriptor_power_so3(self, descriptor_power_so3):
        descriptor_power_so3 = descriptor_power_so3._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_power_so3(self._handle, descriptor_power_so3)
    
    @property
    def descriptor_power_so4(self):
        """
        Element descriptor_power_so4 ftype=type(power_so4) pytype=Power_So4
        
        
        Defined at descriptors.fpp line 482
        
        """
        descriptor_power_so4_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_power_so4(self._handle)
        if tuple(descriptor_power_so4_handle) in self._objs:
            descriptor_power_so4 = self._objs[tuple(descriptor_power_so4_handle)]
        else:
            descriptor_power_so4 = power_SO4.from_handle(descriptor_power_so4_handle)
            self._objs[tuple(descriptor_power_so4_handle)] = descriptor_power_so4
        return descriptor_power_so4
    
    @descriptor_power_so4.setter
    def descriptor_power_so4(self, descriptor_power_so4):
        descriptor_power_so4 = descriptor_power_so4._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_power_so4(self._handle, descriptor_power_so4)
    
    @property
    def descriptor_soap(self):
        """
        Element descriptor_soap ftype=type(soap) pytype=Soap
        
        
        Defined at descriptors.fpp line 483
        
        """
        descriptor_soap_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_soap(self._handle)
        if tuple(descriptor_soap_handle) in self._objs:
            descriptor_soap = self._objs[tuple(descriptor_soap_handle)]
        else:
            descriptor_soap = soap.from_handle(descriptor_soap_handle)
            self._objs[tuple(descriptor_soap_handle)] = descriptor_soap
        return descriptor_soap
    
    @descriptor_soap.setter
    def descriptor_soap(self, descriptor_soap):
        descriptor_soap = descriptor_soap._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_soap(self._handle, descriptor_soap)
    
    @property
    def descriptor_rdf(self):
        """
        Element descriptor_rdf ftype=type(rdf) pytype=Rdf
        
        
        Defined at descriptors.fpp line 484
        
        """
        descriptor_rdf_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_rdf(self._handle)
        if tuple(descriptor_rdf_handle) in self._objs:
            descriptor_rdf = self._objs[tuple(descriptor_rdf_handle)]
        else:
            descriptor_rdf = rdf.from_handle(descriptor_rdf_handle)
            self._objs[tuple(descriptor_rdf_handle)] = descriptor_rdf
        return descriptor_rdf
    
    @descriptor_rdf.setter
    def descriptor_rdf(self, descriptor_rdf):
        descriptor_rdf = descriptor_rdf._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_rdf(self._handle, descriptor_rdf)
    
    @property
    def descriptor_as_distance_2b(self):
        """
        Element descriptor_as_distance_2b ftype=type(as_distance_2b) pytype=As_Distance_2B
        
        
        Defined at descriptors.fpp line 485
        
        """
        descriptor_as_distance_2b_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_as_distance_2b(self._handle)
        if tuple(descriptor_as_distance_2b_handle) in self._objs:
            descriptor_as_distance_2b = self._objs[tuple(descriptor_as_distance_2b_handle)]
        else:
            descriptor_as_distance_2b = as_distance_2b.from_handle(descriptor_as_distance_2b_handle)
            self._objs[tuple(descriptor_as_distance_2b_handle)] = descriptor_as_distance_2b
        return descriptor_as_distance_2b
    
    @descriptor_as_distance_2b.setter
    def descriptor_as_distance_2b(self, descriptor_as_distance_2b):
        descriptor_as_distance_2b = descriptor_as_distance_2b._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_as_distance_2b(self._handle, descriptor_as_distance_2b)
    
    @property
    def descriptor_alex(self):
        """
        Element descriptor_alex ftype=type(alex) pytype=Alex
        
        
        Defined at descriptors.fpp line 486
        
        """
        descriptor_alex_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_alex(self._handle)
        if tuple(descriptor_alex_handle) in self._objs:
            descriptor_alex = self._objs[tuple(descriptor_alex_handle)]
        else:
            descriptor_alex = alex.from_handle(descriptor_alex_handle)
            self._objs[tuple(descriptor_alex_handle)] = descriptor_alex
        return descriptor_alex
    
    @descriptor_alex.setter
    def descriptor_alex(self, descriptor_alex):
        descriptor_alex = descriptor_alex._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_alex(self._handle, descriptor_alex)
    
    @property
    def descriptor_distance_nb(self):
        """
        Element descriptor_distance_nb ftype=type(distance_nb) pytype=Distance_Nb
        
        
        Defined at descriptors.fpp line 487
        
        """
        descriptor_distance_nb_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_distance_nb(self._handle)
        if tuple(descriptor_distance_nb_handle) in self._objs:
            descriptor_distance_nb = self._objs[tuple(descriptor_distance_nb_handle)]
        else:
            descriptor_distance_nb = distance_Nb.from_handle(descriptor_distance_nb_handle)
            self._objs[tuple(descriptor_distance_nb_handle)] = descriptor_distance_nb
        return descriptor_distance_nb
    
    @descriptor_distance_nb.setter
    def descriptor_distance_nb(self, descriptor_distance_nb):
        descriptor_distance_nb = descriptor_distance_nb._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_distance_nb(self._handle, descriptor_distance_nb)
    
    @property
    def descriptor_soap_turbo(self):
        """
        Element descriptor_soap_turbo ftype=type(soap_turbo) pytype=Soap_Turbo
        
        
        Defined at descriptors.fpp line 488
        
        """
        descriptor_soap_turbo_handle = quippy._quippy.f90wrap_descriptor__get__descriptor_soap_turbo(self._handle)
        if tuple(descriptor_soap_turbo_handle) in self._objs:
            descriptor_soap_turbo = self._objs[tuple(descriptor_soap_turbo_handle)]
        else:
            descriptor_soap_turbo = soap_turbo.from_handle(descriptor_soap_turbo_handle)
            self._objs[tuple(descriptor_soap_turbo_handle)] = descriptor_soap_turbo
        return descriptor_soap_turbo
    
    @descriptor_soap_turbo.setter
    def descriptor_soap_turbo(self, descriptor_soap_turbo):
        descriptor_soap_turbo = descriptor_soap_turbo._handle
        quippy._quippy.f90wrap_descriptor__set__descriptor_soap_turbo(self._handle, descriptor_soap_turbo)
    
    def __str__(self):
        ret = ['<descriptor>{\n']
        ret.append('    descriptor_type : ')
        ret.append(repr(self.descriptor_type))
        ret.append(',\n    descriptor_bispectrum_so4 : ')
        ret.append(repr(self.descriptor_bispectrum_so4))
        ret.append(',\n    descriptor_bispectrum_so3 : ')
        ret.append(repr(self.descriptor_bispectrum_so3))
        ret.append(',\n    descriptor_behler : ')
        ret.append(repr(self.descriptor_behler))
        ret.append(',\n    descriptor_distance_2b : ')
        ret.append(repr(self.descriptor_distance_2b))
        ret.append(',\n    descriptor_coordination : ')
        ret.append(repr(self.descriptor_coordination))
        ret.append(',\n    descriptor_angle_3b : ')
        ret.append(repr(self.descriptor_angle_3b))
        ret.append(',\n    descriptor_co_angle_3b : ')
        ret.append(repr(self.descriptor_co_angle_3b))
        ret.append(',\n    descriptor_co_distance_2b : ')
        ret.append(repr(self.descriptor_co_distance_2b))
        ret.append(',\n    descriptor_cosnx : ')
        ret.append(repr(self.descriptor_cosnx))
        ret.append(',\n    descriptor_trihis : ')
        ret.append(repr(self.descriptor_trihis))
        ret.append(',\n    descriptor_water_monomer : ')
        ret.append(repr(self.descriptor_water_monomer))
        ret.append(',\n    descriptor_water_dimer : ')
        ret.append(repr(self.descriptor_water_dimer))
        ret.append(',\n    descriptor_a2_dimer : ')
        ret.append(repr(self.descriptor_a2_dimer))
        ret.append(',\n    descriptor_ab_dimer : ')
        ret.append(repr(self.descriptor_ab_dimer))
        ret.append(',\n    descriptor_atom_real_space : ')
        ret.append(repr(self.descriptor_atom_real_space))
        ret.append(',\n    descriptor_power_so3 : ')
        ret.append(repr(self.descriptor_power_so3))
        ret.append(',\n    descriptor_power_so4 : ')
        ret.append(repr(self.descriptor_power_so4))
        ret.append(',\n    descriptor_soap : ')
        ret.append(repr(self.descriptor_soap))
        ret.append(',\n    descriptor_rdf : ')
        ret.append(repr(self.descriptor_rdf))
        ret.append(',\n    descriptor_as_distance_2b : ')
        ret.append(repr(self.descriptor_as_distance_2b))
        ret.append(',\n    descriptor_alex : ')
        ret.append(repr(self.descriptor_alex))
        ret.append(',\n    descriptor_distance_nb : ')
        ret.append(repr(self.descriptor_distance_nb))
        ret.append(',\n    descriptor_soap_turbo : ')
        ret.append(repr(self.descriptor_soap_turbo))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.descriptor_data")
class descriptor_data(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=descriptor_data)
    
    
    Defined at descriptors.fpp lines 491-492
    
    """
    def __del__(self, error=None):
        """
        Destructor for class Descriptor_Data
        
        
        Defined at descriptors.fpp lines 871-887
        
        Parameters
        ----------
        this : Descriptor_Data
        error : int
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_descriptor_data_finalise(this=self._handle, error=error)
    
    def __init__(self, handle=None):
        """
        self = Descriptor_Data()
        
        
        Defined at descriptors.fpp lines 491-492
        
        
        Returns
        -------
        this : Descriptor_Data
        	Object to be constructed
        
        
        Automatically generated constructor for descriptor_data
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_descriptor_data_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def init_array_x(self):
        self.x = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        quippy._quippy.f90wrap_descriptor_data__array_getitem__x,
                                        quippy._quippy.f90wrap_descriptor_data__array_setitem__x,
                                        quippy._quippy.f90wrap_descriptor_data__array_len__x,
                                        """
        Element x ftype=type(descriptor_data_mono) pytype=Descriptor_Data_Mono
        
        
        Defined at descriptors.fpp line 492
        
        """, descriptor_data_mono)
        return self.x
    
    _dt_array_initialisers = [init_array_x]
    

@f90wrap.runtime.register_class("quippy.cplx_1d")
class cplx_1d(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=cplx_1d)
    
    
    Defined at descriptors.fpp lines 494-495
    
    """
    def __init__(self, handle=None):
        """
        self = Cplx_1D()
        
        
        Defined at descriptors.fpp lines 494-495
        
        
        Returns
        -------
        this : Cplx_1D
        	Object to be constructed
        
        
        Automatically generated constructor for cplx_1d
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_cplx_1d_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Cplx_1D
        
        
        Defined at descriptors.fpp lines 494-495
        
        Parameters
        ----------
        this : Cplx_1D
        	Object to be destructed
        
        
        Automatically generated destructor for cplx_1d
        """
        if self._alloc:
            quippy._quippy.f90wrap_cplx_1d_finalise(this=self._handle)
    
    @property
    def m(self):
        """
        Element m ftype=complex(dp) pytype=complex
        
        
        Defined at descriptors.fpp line 495
        
        """
        array_ndim, array_type, array_shape, array_handle =     quippy._quippy.f90wrap_cplx_1d__array__m(self._handle)
        if array_handle in self._arrays:
            m = self._arrays[array_handle]
        else:
            m = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_cplx_1d__array__m)
            self._arrays[array_handle] = m
        return m
    
    @m.setter
    def m(self, m):
        self.m[...] = m
    
    def __str__(self):
        ret = ['<cplx_1d>{\n']
        ret.append('    m : ')
        ret.append(repr(self.m))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.neighbour_type")
class neighbour_type(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=neighbour_type)
    
    
    Defined at descriptors.fpp lines 506-507
    
    """
    def __init__(self, handle=None):
        """
        self = Neighbour_Type()
        
        
        Defined at descriptors.fpp lines 506-507
        
        
        Returns
        -------
        this : Neighbour_Type
        	Object to be constructed
        
        
        Automatically generated constructor for neighbour_type
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_neighbour_type_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Neighbour_Type
        
        
        Defined at descriptors.fpp lines 506-507
        
        Parameters
        ----------
        this : Neighbour_Type
        	Object to be destructed
        
        
        Automatically generated destructor for neighbour_type
        """
        if self._alloc:
            quippy._quippy.f90wrap_neighbour_type_finalise(this=self._handle)
    
    _dt_array_initialisers = []
    

def real_space_covariance(self, at2, i1, i2, alpha, l_max, f1=None, f2=None):
    """
    real_space_covariance_in = real_space_covariance(self, at2, i1, i2, alpha, l_max[, f1, f2])
    
    
    Defined at descriptors.fpp lines 10055-10108
    
    Parameters
    ----------
    at1 : Atoms
    at2 : Atoms
    i1 : int
    i2 : int
    alpha : float
    l_max : int
    f1 : float array
    f2 : float array
    
    Returns
    -------
    real_space_covariance_in : complex
    
    """
    real_space_covariance_in = quippy._quippy.f90wrap_real_space_covariance(at1=self._handle, at2=at2._handle, i1=i1, i2=i2, \
        alpha=alpha, l_max=l_max, f1=f1, f2=f2)
    return real_space_covariance_in

def get_dt_none():
    """
    Element dt_none ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 155
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_none()

DT_NONE = get_dt_none()

def get_dt_bispectrum_so4():
    """
    Element dt_bispectrum_so4 ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 156
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_bispectrum_so4()

DT_BISPECTRUM_SO4 = get_dt_bispectrum_so4()

def get_dt_bispectrum_so3():
    """
    Element dt_bispectrum_so3 ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 157
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_bispectrum_so3()

DT_BISPECTRUM_SO3 = get_dt_bispectrum_so3()

def get_dt_behler():
    """
    Element dt_behler ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 158
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_behler()

DT_BEHLER = get_dt_behler()

def get_dt_distance_2b():
    """
    Element dt_distance_2b ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 159
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_distance_2b()

DT_DISTANCE_2B = get_dt_distance_2b()

def get_dt_coordination():
    """
    Element dt_coordination ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 160
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_coordination()

DT_COORDINATION = get_dt_coordination()

def get_dt_angle_3b():
    """
    Element dt_angle_3b ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 161
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_angle_3b()

DT_ANGLE_3B = get_dt_angle_3b()

def get_dt_co_angle_3b():
    """
    Element dt_co_angle_3b ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 162
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_co_angle_3b()

DT_CO_ANGLE_3B = get_dt_co_angle_3b()

def get_dt_co_distance_2b():
    """
    Element dt_co_distance_2b ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 163
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_co_distance_2b()

DT_CO_DISTANCE_2B = get_dt_co_distance_2b()

def get_dt_cosnx():
    """
    Element dt_cosnx ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 164
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_cosnx()

DT_COSNX = get_dt_cosnx()

def get_dt_trihis():
    """
    Element dt_trihis ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 165
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_trihis()

DT_TRIHIS = get_dt_trihis()

def get_dt_water_monomer():
    """
    Element dt_water_monomer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 166
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_water_monomer()

DT_WATER_MONOMER = get_dt_water_monomer()

def get_dt_water_dimer():
    """
    Element dt_water_dimer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 167
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_water_dimer()

DT_WATER_DIMER = get_dt_water_dimer()

def get_dt_a2_dimer():
    """
    Element dt_a2_dimer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 168
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_a2_dimer()

DT_A2_DIMER = get_dt_a2_dimer()

def get_dt_ab_dimer():
    """
    Element dt_ab_dimer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 169
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_ab_dimer()

DT_AB_DIMER = get_dt_ab_dimer()

def get_dt_bond_real_space():
    """
    Element dt_bond_real_space ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 170
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_bond_real_space()

DT_BOND_REAL_SPACE = get_dt_bond_real_space()

def get_dt_atom_real_space():
    """
    Element dt_atom_real_space ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 171
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_atom_real_space()

DT_ATOM_REAL_SPACE = get_dt_atom_real_space()

def get_dt_power_so3():
    """
    Element dt_power_so3 ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 172
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_power_so3()

DT_POWER_SO3 = get_dt_power_so3()

def get_dt_power_so4():
    """
    Element dt_power_so4 ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 173
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_power_so4()

DT_POWER_SO4 = get_dt_power_so4()

def get_dt_soap():
    """
    Element dt_soap ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 174
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_soap()

DT_SOAP = get_dt_soap()

def get_dt_an_monomer():
    """
    Element dt_an_monomer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 175
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_an_monomer()

DT_AN_MONOMER = get_dt_an_monomer()

def get_dt_general_monomer():
    """
    Element dt_general_monomer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 176
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_general_monomer()

DT_GENERAL_MONOMER = get_dt_general_monomer()

def get_dt_general_dimer():
    """
    Element dt_general_dimer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 177
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_general_dimer()

DT_GENERAL_DIMER = get_dt_general_dimer()

def get_dt_general_trimer():
    """
    Element dt_general_trimer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 178
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_general_trimer()

DT_GENERAL_TRIMER = get_dt_general_trimer()

def get_dt_rdf():
    """
    Element dt_rdf ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 179
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_rdf()

DT_RDF = get_dt_rdf()

def get_dt_as_distance_2b():
    """
    Element dt_as_distance_2b ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 180
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_as_distance_2b()

DT_AS_DISTANCE_2B = get_dt_as_distance_2b()

def get_dt_molecule_lo_d():
    """
    Element dt_molecule_lo_d ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 181
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_molecule_lo_d()

DT_MOLECULE_LO_D = get_dt_molecule_lo_d()

def get_dt_alex():
    """
    Element dt_alex ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 182
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_alex()

DT_alex = get_dt_alex()

def get_dt_com_dimer():
    """
    Element dt_com_dimer ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 183
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_com_dimer()

DT_COM_DIMER = get_dt_com_dimer()

def get_dt_distance_nb():
    """
    Element dt_distance_nb ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 184
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_distance_nb()

DT_DISTANCE_NB = get_dt_distance_nb()

def get_dt_soap_express():
    """
    Element dt_soap_express ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 185
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_soap_express()

DT_SOAP_EXPRESS = get_dt_soap_express()

def get_dt_soap_turbo():
    """
    Element dt_soap_turbo ftype=integer pytype=int
    
    
    Defined at descriptors.fpp line 186
    
    """
    return quippy._quippy.f90wrap_descriptors_module__get__dt_soap_turbo()

DT_SOAP_TURBO = get_dt_soap_turbo()


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "descriptors_module".')

for func in _dt_array_initialisers:
    func()
