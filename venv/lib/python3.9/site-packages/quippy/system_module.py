"""
Module system_module


Defined at System.fpp lines 137-2973

The system module contains low-level routines for I/O, timing, random
number generation etc. The Inoutput type is used to abstract both
formatted and unformatted(i.e. binary) I/O.
"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("quippy.Stack")
class Stack(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=stack)
    
    
    Defined at System.fpp lines 154-156
    
    """
    def __init__(self, value=None, handle=None):
        """
        self = Stack([value])
        
        
        Defined at System.fpp lines 2301-2311
        
        Parameters
        ----------
        value : int
        
        Returns
        -------
        this : Stack
        
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_stack_initialise(value=value)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Stack
        
        
        Defined at System.fpp lines 2313-2315
        
        Parameters
        ----------
        this : Stack
        
        """
        if self._alloc:
            quippy._quippy.f90wrap_stack_finalise(this=self._handle)
    
    def print(self, verbosity=None, out=None):
        """
        print(self[, verbosity, out])
        
        
        Defined at System.fpp lines 2352-2360
        
        Parameters
        ----------
        this : Stack
        verbosity : int
        out : Inoutput
        
        Overloaded interface for printing. With the
        'this' parameter omitted output goes to the default mainlog('stdout'). The
        'verbosity' parameter controls whether the object is actually printed;
        if the verbosity is greater than that currently at the top of the
        verbosity stack then output is suppressed. Possible verbosity levels
        range from 'ERROR' through 'NORMAL', 'VERBOSE', 'NERD' and 'ANALYSIS'.
        Other user-defined types define the Print interface in the same way.
        """
        quippy._quippy.f90wrap_stack_print(this=self._handle, verbosity=verbosity, out=None if out is None else out._handle)
    
    def push(self, val):
        """
        push(self, val)
        
        
        Defined at System.fpp lines 2317-2333
        
        Parameters
        ----------
        this : Stack
        val : int
        
        """
        quippy._quippy.f90wrap_stack_push(this=self._handle, val=val)
    
    def pop(self):
        """
        pop(self)
        
        
        Defined at System.fpp lines 2335-2341
        
        Parameters
        ----------
        this : Stack
        
        """
        quippy._quippy.f90wrap_stack_pop(this=self._handle)
    
    def value(self):
        """
        stack_value = value(self)
        
        
        Defined at System.fpp lines 2343-2350
        
        Parameters
        ----------
        this : Stack
        
        Returns
        -------
        stack_value : int
        
        """
        stack_value = quippy._quippy.f90wrap_stack_value(this=self._handle)
        return stack_value
    
    @property
    def pos(self):
        """
        Element pos ftype=integer pytype=int
        
        
        Defined at System.fpp line 155
        
        """
        return quippy._quippy.f90wrap_stack__get__pos(self._handle)
    
    @pos.setter
    def pos(self, pos):
        quippy._quippy.f90wrap_stack__set__pos(self._handle, pos)
    
    @property
    def val(self):
        """
        Element val ftype=integer pytype=int
        
        
        Defined at System.fpp line 156
        
        """
        array_ndim, array_type, array_shape, array_handle =     quippy._quippy.f90wrap_stack__array__val(self._handle)
        if array_handle in self._arrays:
            val = self._arrays[array_handle]
        else:
            val = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_stack__array__val)
            self._arrays[array_handle] = val
        return val
    
    @val.setter
    def val(self, val):
        self.val[...] = val
    
    def __str__(self):
        ret = ['<stack>{\n']
        ret.append('    pos : ')
        ret.append(repr(self.pos))
        ret.append(',\n    val : ')
        ret.append(repr(self.val))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.InOutput")
class InOutput(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=inoutput)
    
    
    Defined at System.fpp lines 158-170
    
    """
    def rewind(self):
        """
        rewind(self)
        
        
        Defined at System.fpp lines 1636-1638
        
        Parameters
        ----------
        this : Inoutput
        
        Rewind to the start of this file. Works for both formatted and unformatted files.
        """
        quippy._quippy.f90wrap_rewind(this=self._handle)
    
    def __init__(self, filename=None, action=None, isformatted=None, append=None, verbosity=None, verbosity_cascade=None, \
        master_only=None, unit=None, error=None, handle=None):
        """
        self = Inoutput([filename, action, isformatted, append, verbosity, verbosity_cascade, master_only, unit, error])
        
        
        Defined at System.fpp lines 449-558
        
        Parameters
        ----------
        filename : str
        action : int
        isformatted : bool
        append : bool
        verbosity : int
        verbosity_cascade : int
        master_only : bool
        unit : int
        error : int
        
        Returns
        -------
        this : Inoutput
        
        Open a file for reading or writing. The action optional parameter can
        be one of 'INPUT' (default), 'OUTPUT' or 'INOUT'.
        For unformatted output, the
        'isformatted' optional parameter must
        be set to false.
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_inoutput_initialise(filename=filename, action=action, isformatted=isformatted, \
            append=append, verbosity=verbosity, verbosity_cascade=verbosity_cascade, master_only=master_only, unit=unit, \
            error=error)
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Inoutput
        
        
        Defined at System.fpp lines 587-593
        
        Parameters
        ----------
        this : Inoutput
        
        Cleans everything and set members to default
        """
        if self._alloc:
            quippy._quippy.f90wrap_inoutput_finalise(this=self._handle)
    
    def activate(self):
        """
        activate(self)
        
        
        Defined at System.fpp lines 582-584
        
        Parameters
        ----------
        this : Inoutput
        
        Activate an Inoutput object temporarily.
        """
        quippy._quippy.f90wrap_inoutput_activate(this=self._handle)
    
    def deactivate(self):
        """
        deactivate(self)
        
        
        Defined at System.fpp lines 577-579
        
        Parameters
        ----------
        this : Inoutput
        
        Deactivate an Inoutput object temporarily.
        """
        quippy._quippy.f90wrap_inoutput_deactivate(this=self._handle)
    
    def mpi_all_inoutput(self, value=None):
        """
        mpi_all_inoutput(self[, value])
        
        
        Defined at System.fpp lines 601-608
        
        Parameters
        ----------
        this : Inoutput
        value : bool
        
        """
        quippy._quippy.f90wrap_inoutput_mpi_all_inoutput(this=self._handle, value=value)
    
    def print_mpi_id(self, value=None):
        """
        print_mpi_id(self[, value])
        
        
        Defined at System.fpp lines 610-617
        
        Parameters
        ----------
        this : Inoutput
        value : bool
        
        """
        quippy._quippy.f90wrap_inoutput_print_mpi_id(this=self._handle, value=value)
    
    def print_inoutput(self):
        """
        print_inoutput(self)
        
        
        Defined at System.fpp lines 736-755
        
        Parameters
        ----------
        this : Inoutput
        
        Overloaded interface for printing. With the
        'this' parameter omitted output goes to the default mainlog('stdout'). The
        'verbosity' parameter controls whether the object is actually printed;
        if the verbosity is greater than that currently at the top of the
        verbosity stack then output is suppressed. Possible verbosity levels
        range from 'ERROR' through 'NORMAL', 'VERBOSE', 'NERD' and 'ANALYSIS'.
        Other user-defined types define the Print interface in the same way.
        """
        quippy._quippy.f90wrap_print_inoutput(this=self._handle)
    
    def read_line(self, status=None):
        """
        inoutput_read_line = read_line(self[, status])
        
        
        Defined at System.fpp lines 801-813
        
        Parameters
        ----------
        this : Inoutput
        status : int
        
        Returns
        -------
        inoutput_read_line : str
        
        Read a line of text from a file(up to a line break, or 1024 characters).
        This can then be parsed by the calling routine(using 'parse_line' for example)
        
        Optionally, a status is returned which is:
        
        \begin{itemize}
        \item $<0$ if the end of the file is reached
        \item $=0$ if no problems were encountered
        \item $>0$ if there was a read error
        \end{itemize}
        
        The actual number returned is implementation specific
        """
        inoutput_read_line = quippy._quippy.f90wrap_inoutput_read_line(this=self._handle, status=status)
        return inoutput_read_line
    
    def parse_line(self, delimiters, fields, status=None):
        """
        num_fields = parse_line(self, delimiters, fields[, status])
        
        
        Defined at System.fpp lines 878-888
        
        Parameters
        ----------
        this : Inoutput
        delimiters : str
        fields : str array
        status : int
        
        Returns
        -------
        num_fields : int
        
        Call parse_string on the next line from a file
        """
        num_fields = quippy._quippy.f90wrap_inoutput_parse_line(this=self._handle, delimiters=delimiters, fields=fields, \
            status=status)
        return num_fields
    
    def _reada_real_dim1(self, da, status=None):
        """
        _reada_real_dim1(self, da[, status])
        
        
        Defined at System.fpp lines 1607-1619
        
        Parameters
        ----------
        this : Inoutput
        da : float array
        status : int
        
        Read scalar and array data from ascii files. These
        interfaces are not yet heavily overloaded to cater for all intrinsic and most
        derived types.
        """
        quippy._quippy.f90wrap_reada_real_dim1(this=self._handle, da=da, status=status)
    
    def _reada_int_dim1(self, ia, status=None):
        """
        _reada_int_dim1(self, ia[, status])
        
        
        Defined at System.fpp lines 1621-1633
        
        Parameters
        ----------
        this : Inoutput
        ia : int array
        status : int
        
        """
        quippy._quippy.f90wrap_reada_int_dim1(this=self._handle, ia=ia, status=status)
    
    def read_ascii(*args, **kwargs):
        """
        read_ascii(*args, **kwargs)
        
        
        Defined at System.fpp lines 260-261
        
        Overloaded interface containing the following procedures:
          _reada_real_dim1
          _reada_int_dim1
        
        """
        for proc in [InOutput._reada_real_dim1, InOutput._reada_int_dim1]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    @property
    def unit(self):
        """
        Element unit ftype=integer pytype=int
        
        
        Defined at System.fpp line 159
        
        """
        return quippy._quippy.f90wrap_inoutput__get__unit(self._handle)
    
    @unit.setter
    def unit(self, unit):
        quippy._quippy.f90wrap_inoutput__set__unit(self._handle, unit)
    
    @property
    def filename(self):
        """
        Element filename ftype=character(256) pytype=str
        
        
        Defined at System.fpp line 160
        
        """
        return quippy._quippy.f90wrap_inoutput__get__filename(self._handle)
    
    @filename.setter
    def filename(self, filename):
        quippy._quippy.f90wrap_inoutput__set__filename(self._handle, filename)
    
    @property
    def prefix(self):
        """
        Element prefix ftype=character(256) pytype=str
        
        
        Defined at System.fpp line 161
        
        """
        return quippy._quippy.f90wrap_inoutput__get__prefix(self._handle)
    
    @prefix.setter
    def prefix(self, prefix):
        quippy._quippy.f90wrap_inoutput__set__prefix(self._handle, prefix)
    
    @property
    def postfix(self):
        """
        Element postfix ftype=character(256) pytype=str
        
        
        Defined at System.fpp line 161
        
        """
        return quippy._quippy.f90wrap_inoutput__get__postfix(self._handle)
    
    @postfix.setter
    def postfix(self, postfix):
        quippy._quippy.f90wrap_inoutput__set__postfix(self._handle, postfix)
    
    @property
    def default_real_precision(self):
        """
        Element default_real_precision ftype=integer pytype=int
        
        
        Defined at System.fpp line 162
        
        """
        return quippy._quippy.f90wrap_inoutput__get__default_real_precision(self._handle)
    
    @default_real_precision.setter
    def default_real_precision(self, default_real_precision):
        quippy._quippy.f90wrap_inoutput__set__default_real_precision(self._handle, default_real_precision)
    
    @property
    def formatted(self):
        """
        Element formatted ftype=logical pytype=bool
        
        
        Defined at System.fpp line 163
        
        """
        return quippy._quippy.f90wrap_inoutput__get__formatted(self._handle)
    
    @formatted.setter
    def formatted(self, formatted):
        quippy._quippy.f90wrap_inoutput__set__formatted(self._handle, formatted)
    
    @property
    def append(self):
        """
        Element append ftype=logical pytype=bool
        
        
        Defined at System.fpp line 164
        
        """
        return quippy._quippy.f90wrap_inoutput__get__append(self._handle)
    
    @append.setter
    def append(self, append):
        quippy._quippy.f90wrap_inoutput__set__append(self._handle, append)
    
    @property
    def active(self):
        """
        Element active ftype=logical pytype=bool
        
        
        Defined at System.fpp line 165
        
        Does it print?
        """
        return quippy._quippy.f90wrap_inoutput__get__active(self._handle)
    
    @active.setter
    def active(self, active):
        quippy._quippy.f90wrap_inoutput__set__active(self._handle, active)
    
    @property
    def action(self):
        """
        Element action ftype=integer pytype=int
        
        
        Defined at System.fpp line 166
        
        """
        return quippy._quippy.f90wrap_inoutput__get__action(self._handle)
    
    @action.setter
    def action(self, action):
        quippy._quippy.f90wrap_inoutput__set__action(self._handle, action)
    
    @property
    def mpi_all_inoutput_flag(self):
        """
        Element mpi_all_inoutput_flag ftype=logical pytype=bool
        
        
        Defined at System.fpp line 167
        
        """
        return quippy._quippy.f90wrap_inoutput__get__mpi_all_inoutput_flag(self._handle)
    
    @mpi_all_inoutput_flag.setter
    def mpi_all_inoutput_flag(self, mpi_all_inoutput_flag):
        quippy._quippy.f90wrap_inoutput__set__mpi_all_inoutput_flag(self._handle, mpi_all_inoutput_flag)
    
    @property
    def mpi_print_id(self):
        """
        Element mpi_print_id ftype=logical pytype=bool
        
        
        Defined at System.fpp line 168
        
        """
        return quippy._quippy.f90wrap_inoutput__get__mpi_print_id(self._handle)
    
    @mpi_print_id.setter
    def mpi_print_id(self, mpi_print_id):
        quippy._quippy.f90wrap_inoutput__set__mpi_print_id(self._handle, mpi_print_id)
    
    @property
    def verbosity_stack(self):
        """
        Element verbosity_stack ftype=type(stack) pytype=Stack
        
        
        Defined at System.fpp line 169
        
        """
        verbosity_stack_handle = quippy._quippy.f90wrap_inoutput__get__verbosity_stack(self._handle)
        if tuple(verbosity_stack_handle) in self._objs:
            verbosity_stack = self._objs[tuple(verbosity_stack_handle)]
        else:
            verbosity_stack = Stack.from_handle(verbosity_stack_handle)
            self._objs[tuple(verbosity_stack_handle)] = verbosity_stack
        return verbosity_stack
    
    @verbosity_stack.setter
    def verbosity_stack(self, verbosity_stack):
        verbosity_stack = verbosity_stack._handle
        quippy._quippy.f90wrap_inoutput__set__verbosity_stack(self._handle, verbosity_stack)
    
    @property
    def verbosity_cascade_stack(self):
        """
        Element verbosity_cascade_stack ftype=type(stack) pytype=Stack
        
        
        Defined at System.fpp line 169
        
        """
        verbosity_cascade_stack_handle = quippy._quippy.f90wrap_inoutput__get__verbosity_cascade_stack(self._handle)
        if tuple(verbosity_cascade_stack_handle) in self._objs:
            verbosity_cascade_stack = self._objs[tuple(verbosity_cascade_stack_handle)]
        else:
            verbosity_cascade_stack = Stack.from_handle(verbosity_cascade_stack_handle)
            self._objs[tuple(verbosity_cascade_stack_handle)] = verbosity_cascade_stack
        return verbosity_cascade_stack
    
    @verbosity_cascade_stack.setter
    def verbosity_cascade_stack(self, verbosity_cascade_stack):
        verbosity_cascade_stack = verbosity_cascade_stack._handle
        quippy._quippy.f90wrap_inoutput__set__verbosity_cascade_stack(self._handle, verbosity_cascade_stack)
    
    @property
    def initialised(self):
        """
        Element initialised ftype=logical pytype=bool
        
        
        Defined at System.fpp line 170
        
        """
        return quippy._quippy.f90wrap_inoutput__get__initialised(self._handle)
    
    @initialised.setter
    def initialised(self, initialised):
        quippy._quippy.f90wrap_inoutput__set__initialised(self._handle, initialised)
    
    def __str__(self):
        ret = ['<inoutput>{\n']
        ret.append('    unit : ')
        ret.append(repr(self.unit))
        ret.append(',\n    filename : ')
        ret.append(repr(self.filename))
        ret.append(',\n    prefix : ')
        ret.append(repr(self.prefix))
        ret.append(',\n    postfix : ')
        ret.append(repr(self.postfix))
        ret.append(',\n    default_real_precision : ')
        ret.append(repr(self.default_real_precision))
        ret.append(',\n    formatted : ')
        ret.append(repr(self.formatted))
        ret.append(',\n    append : ')
        ret.append(repr(self.append))
        ret.append(',\n    active : ')
        ret.append(repr(self.active))
        ret.append(',\n    action : ')
        ret.append(repr(self.action))
        ret.append(',\n    mpi_all_inoutput_flag : ')
        ret.append(repr(self.mpi_all_inoutput_flag))
        ret.append(',\n    mpi_print_id : ')
        ret.append(repr(self.mpi_print_id))
        ret.append(',\n    verbosity_stack : ')
        ret.append(repr(self.verbosity_stack))
        ret.append(',\n    verbosity_cascade_stack : ')
        ret.append(repr(self.verbosity_cascade_stack))
        ret.append(',\n    initialised : ')
        ret.append(repr(self.initialised))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.allocatable_array_pointers")
class allocatable_array_pointers(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=allocatable_array_pointers)
    
    
    Defined at System.fpp lines 172-176
    
    """
    def __init__(self, handle=None):
        """
        self = Allocatable_Array_Pointers()
        
        
        Defined at System.fpp lines 172-176
        
        
        Returns
        -------
        this : Allocatable_Array_Pointers
        	Object to be constructed
        
        
        Automatically generated constructor for allocatable_array_pointers
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_allocatable_array_pointers_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Allocatable_Array_Pointers
        
        
        Defined at System.fpp lines 172-176
        
        Parameters
        ----------
        this : Allocatable_Array_Pointers
        	Object to be destructed
        
        
        Automatically generated destructor for allocatable_array_pointers
        """
        if self._alloc:
            quippy._quippy.f90wrap_allocatable_array_pointers_finalise(this=self._handle)
    
    @property
    def i_a(self):
        """
        Element i_a ftype=integer pytype=int
        
        
        Defined at System.fpp line 173
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_allocatable_array_pointers__array__i_a(self._handle)
        if array_handle in self._arrays:
            i_a = self._arrays[array_handle]
        else:
            i_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_allocatable_array_pointers__array__i_a)
            self._arrays[array_handle] = i_a
        return i_a
    
    @i_a.setter
    def i_a(self, i_a):
        self.i_a[...] = i_a
    
    @property
    def r_a(self):
        """
        Element r_a ftype=real(dp) pytype=float
        
        
        Defined at System.fpp line 174
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_allocatable_array_pointers__array__r_a(self._handle)
        if array_handle in self._arrays:
            r_a = self._arrays[array_handle]
        else:
            r_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_allocatable_array_pointers__array__r_a)
            self._arrays[array_handle] = r_a
        return r_a
    
    @r_a.setter
    def r_a(self, r_a):
        self.r_a[...] = r_a
    
    @property
    def c_a(self):
        """
        Element c_a ftype=complex(dp) pytype=complex
        
        
        Defined at System.fpp line 175
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_allocatable_array_pointers__array__c_a(self._handle)
        if array_handle in self._arrays:
            c_a = self._arrays[array_handle]
        else:
            c_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_allocatable_array_pointers__array__c_a)
            self._arrays[array_handle] = c_a
        return c_a
    
    @c_a.setter
    def c_a(self, c_a):
        self.c_a[...] = c_a
    
    @property
    def l_a(self):
        """
        Element l_a ftype=logical pytype=bool
        
        
        Defined at System.fpp line 176
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            quippy._quippy.f90wrap_allocatable_array_pointers__array__l_a(self._handle)
        if array_handle in self._arrays:
            l_a = self._arrays[array_handle]
        else:
            l_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_allocatable_array_pointers__array__l_a)
            self._arrays[array_handle] = l_a
        return l_a
    
    @l_a.setter
    def l_a(self, l_a):
        self.l_a[...] = l_a
    
    def __str__(self):
        ret = ['<allocatable_array_pointers>{\n']
        ret.append('    i_a : ')
        ret.append(repr(self.i_a))
        ret.append(',\n    r_a : ')
        ret.append(repr(self.r_a))
        ret.append(',\n    c_a : ')
        ret.append(repr(self.c_a))
        ret.append(',\n    l_a : ')
        ret.append(repr(self.l_a))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

def is_open(unit):
    """
    is_open = is_open(unit)
    
    
    Defined at System.fpp lines 561-564
    
    Parameters
    ----------
    unit : int
    
    Returns
    -------
    is_open : bool
    
    OMIT
    """
    is_open = quippy._quippy.f90wrap_is_open(unit=unit)
    return is_open

def print_title(title, verbosity=None):
    """
    print_title(title[, verbosity])
    
    
    Defined at System.fpp lines 767-782
    
    Parameters
    ----------
    title : str
    verbosity : int
    
    Print a centred title, like this:
    
    '==================================== Title ====================================='
    """
    quippy._quippy.f90wrap_print_title(title=title, verbosity=verbosity)

def split_string_simple(str, fields, separators, error=None):
    """
    n_fields = split_string_simple(str, fields, separators[, error])
    
    
    Defined at System.fpp lines 892-922
    
    Parameters
    ----------
    str : str
    	string to be split
    
    fields : str array
    	on return, array of fields
    
    separators : str
    	string of possible separators
    
    error : int
    
    Returns
    -------
    n_fields : int
    	on return, number of fields
    
    
    split a string into fields separated by possible separators
    no quoting, matching separators, just a simple split
    """
    n_fields = quippy._quippy.f90wrap_split_string_simple(str=str, fields=fields, separators=separators, error=error)
    return n_fields

def num_fields_in_string_simple(this, separators):
    """
    num_fields_in_string_simple = num_fields_in_string_simple(this, separators)
    
    
    Defined at System.fpp lines 924-933
    
    Parameters
    ----------
    this : str
    separators : str
    
    Returns
    -------
    num_fields_in_string_simple : int
    
    """
    num_fields_in_string_simple = quippy._quippy.f90wrap_num_fields_in_string_simple(this=this, separators=separators)
    return num_fields_in_string_simple

def split_string(this, separators, quotes, fields, matching=None):
    """
    num_fields = split_string(this, separators, quotes, fields[, matching])
    
    
    Defined at System.fpp lines 939-1071
    
    Parameters
    ----------
    this : str
    separators : str
    quotes : str
    fields : str array
    matching : bool
    
    Returns
    -------
    num_fields : int
    
    split a string at separators, making sure not to break up bits that
    are in quotes(possibly matching opening and closing quotes), and
    also strip one level of quotes off, sort of like a shell would when
    tokenizing
    """
    num_fields = quippy._quippy.f90wrap_split_string(this=this, separators=separators, quotes=quotes, fields=fields, \
        matching=matching)
    return num_fields

def parse_string(this, delimiters, fields, matching=None, error=None):
    """
    num_fields = parse_string(this, delimiters, fields[, matching, error])
    
    
    Defined at System.fpp lines 1097-1188
    
    Parameters
    ----------
    this : str
    delimiters : str
    fields : str array
    matching : bool
    error : int
    
    Returns
    -------
    num_fields : int
    
    outdated - please use split_string
    Parse a string into fields delimited by certain characters. On exit
    the 'fields' array will contain one field per entry and 'num_fields'
    gives the total number of fields. 'status' will be given the error status
    (if present) and so can be used to tell if an end-of-file occurred.
    """
    num_fields = quippy._quippy.f90wrap_parse_string(this=this, delimiters=delimiters, fields=fields, matching=matching, \
        error=error)
    return num_fields

def string_to_int(string_bn, error=None):
    """
    string_to_int = string_to_int(string_bn[, error])
    
    
    Defined at System.fpp lines 1281-1291
    
    Parameters
    ----------
    string_bn : str
    error : int
    
    Returns
    -------
    string_to_int : int
    
    Convert an input string into an integer.
    """
    string_to_int = quippy._quippy.f90wrap_string_to_int(string_bn=string_bn, error=error)
    return string_to_int

def string_to_logical(string_bn, error=None):
    """
    string_to_logical = string_to_logical(string_bn[, error])
    
    
    Defined at System.fpp lines 1294-1306
    
    Parameters
    ----------
    string_bn : str
    error : int
    
    Returns
    -------
    string_to_logical : bool
    
    Convert an input string into a logical.
    """
    string_to_logical = quippy._quippy.f90wrap_string_to_logical(string_bn=string_bn, error=error)
    return string_to_logical

def string_to_real(string_bn, error=None):
    """
    string_to_real = string_to_real(string_bn[, error])
    
    
    Defined at System.fpp lines 1309-1319
    
    Parameters
    ----------
    string_bn : str
    error : int
    
    Returns
    -------
    string_to_real : float
    
    Convert an input string into a real.
    """
    string_to_real = quippy._quippy.f90wrap_string_to_real(string_bn=string_bn, error=error)
    return string_to_real

def round(r, digits):
    """
    round = round(r, digits)
    
    
    Defined at System.fpp lines 1663-1675
    
    Parameters
    ----------
    r : float
    digits : int
    
    Returns
    -------
    round : str
    
    Concatenation functions.
    Overloadings for the // operator to make strings from various other types.
    In each case, we need to work out the exact length of the resultant string
    in order to avoid printing excess spaces.
    Return a string which is the real number 'r' rounded to 'digits' decimal digits
    """
    round = quippy._quippy.f90wrap_round(r=r, digits=digits)
    return round

def get_mpi_size_rank(comm):
    """
    nproc, rank_bn = get_mpi_size_rank(comm)
    
    
    Defined at System.fpp lines 1894-1900
    
    Parameters
    ----------
    comm : int
    	MPI communicator
    
    
    Returns
    -------
    nproc : int
    	Total number of processes
    
    rank_bn : int
    	Rank of this process
    
    
    Return the mpi size and rank for the communicator 'comm'.
    this routine aborts of _MPI is not defined
    """
    nproc, rank_bn = quippy._quippy.f90wrap_get_mpi_size_rank(comm=comm)
    return nproc, rank_bn

def system_initialise(verbosity=None, seed=None, mpi_all_inoutput=None, common_seed=None, enable_timing=None, \
    quippy_running=None, mainlog_file=None, mainlog_unit=None):
    """
    system_initialise([verbosity, seed, mpi_all_inoutput, common_seed, enable_timing, quippy_running, mainlog_file, \
        mainlog_unit])
    
    
    Defined at System.fpp lines 1910-1967
    
    Parameters
    ----------
    verbosity : int
    	mainlog output verbosity
    
    seed : int
    	Seed for the random number generator.
    
    mpi_all_inoutput : bool
    	Print on all MPI nodes(false by default)
    
    common_seed : bool
    enable_timing : bool
    	Enable system_timer() calls
    
    quippy_running : bool
    	.true. if running under quippy(Python interface)
    
    mainlog_file : str
    mainlog_unit : int
    	If 'common_seed' is true(default), random seed will be the same for each
    	MPI process.
    
    
    Must be called at the start of all programs. Initialises MPI if present,
    set the random number seed sets up the default Inoutput objects
    logger and errorlog to point to stdout and stderr respectively. Calls
    Hello_World to do some of the work and print a friendly welcome. If we're
    using MPI, by default we set the same random seed for each process.
    This also attempts to read the executable name, the number of command
    arguments, and the arguments themselves.
    """
    quippy._quippy.f90wrap_system_initialise(verbosity=verbosity, seed=seed, mpi_all_inoutput=mpi_all_inoutput, \
        common_seed=common_seed, enable_timing=enable_timing, quippy_running=quippy_running, mainlog_file=mainlog_file, \
        mainlog_unit=mainlog_unit)

def cmd_arg_count():
    """
    cmd_arg_count = cmd_arg_count()
    
    
    Defined at System.fpp lines 1980-1982
    
    
    Returns
    -------
    cmd_arg_count : int
    
    """
    cmd_arg_count = quippy._quippy.f90wrap_cmd_arg_count()
    return cmd_arg_count

def get_cmd_arg(i, status=None):
    """
    arg = get_cmd_arg(i[, status])
    
    
    Defined at System.fpp lines 1984-1988
    
    Parameters
    ----------
    i : int
    status : int
    
    Returns
    -------
    arg : str
    
    """
    arg = quippy._quippy.f90wrap_get_cmd_arg(i=i, status=status)
    return arg

def get_env_var(name, status=None):
    """
    arg = get_env_var(name[, status])
    
    
    Defined at System.fpp lines 1990-1995
    
    Parameters
    ----------
    name : str
    status : int
    
    Returns
    -------
    arg : str
    
    """
    arg = quippy._quippy.f90wrap_get_env_var(name=name, status=status)
    return arg

def system_finalise():
    """
    system_finalise()
    
    
    Defined at System.fpp lines 1998-2013
    
    
    Shut down gracefully, finalising system objects.
    """
    quippy._quippy.f90wrap_system_finalise()

def print_warning(message):
    """
    print_warning(message)
    
    
    Defined at System.fpp lines 2016-2019
    
    Parameters
    ----------
    message : str
    
    Backward compatible(replaced with print_message) routine to print a warning message to log
    """
    quippy._quippy.f90wrap_print_warning(message=message)

def print_message(message_type, message, verbosity=None):
    """
    print_message(message_type, message[, verbosity])
    
    
    Defined at System.fpp lines 2022-2027
    
    Parameters
    ----------
    message_type : str
    message : str
    verbosity : int
    
    Print a message to log
    """
    quippy._quippy.f90wrap_print_message(message_type=message_type, message=message, verbosity=verbosity)

def system_set_random_seeds(seed):
    """
    system_set_random_seeds(seed)
    
    
    Defined at System.fpp lines 2043-2062
    
    Parameters
    ----------
    seed : int
    
    """
    quippy._quippy.f90wrap_system_set_random_seeds(seed=seed)

def system_resync_rng():
    """
    system_resync_rng()
    
    
    Defined at System.fpp lines 2119-2120
    
    
    """
    quippy._quippy.f90wrap_system_resync_rng()

def th(n):
    """
    th = th(n)
    
    
    Defined at System.fpp lines 2125-2144
    
    Parameters
    ----------
    n : int
    
    Returns
    -------
    th : str
    
    Return the correct ordinal ending(st,nd,rd,th) for the given integer
    """
    th = quippy._quippy.f90wrap_th(n=n)
    return th

def system_reseed_rng(new_seed):
    """
    system_reseed_rng(new_seed)
    
    
    Defined at System.fpp lines 2147-2150
    
    Parameters
    ----------
    new_seed : int
    
    Reseed the random number generator. Useful when restarting from check files.
    """
    quippy._quippy.f90wrap_system_reseed_rng(new_seed=new_seed)

def system_get_random_seed():
    """
    system_get_random_seed = system_get_random_seed()
    
    
    Defined at System.fpp lines 2153-2155
    
    
    Returns
    -------
    system_get_random_seed : int
    
    Return the current random number seed.
    """
    system_get_random_seed = quippy._quippy.f90wrap_system_get_random_seed()
    return system_get_random_seed

def ran():
    """
    dran = ran()
    
    
    Defined at System.fpp lines 2158-2172
    
    
    Returns
    -------
    dran : float
    
    Return a random integer
    """
    dran = quippy._quippy.f90wrap_ran()
    return dran

def ran_uniform():
    """
    ran_uniform = ran_uniform()
    
    
    Defined at System.fpp lines 2175-2184
    
    
    Returns
    -------
    ran_uniform : float
    
    Return a random real number uniformly distributed in the range [0,1]
    """
    ran_uniform = quippy._quippy.f90wrap_ran_uniform()
    return ran_uniform

def ran_normal():
    """
    ran_normal = ran_normal()
    
    
    Defined at System.fpp lines 2187-2195
    
    
    Returns
    -------
    ran_normal : float
    
    Return random real from Normal distribution with mean zero and standard deviation one.
    """
    ran_normal = quippy._quippy.f90wrap_ran_normal()
    return ran_normal

def current_times(cpu_t=None, wall_t=None, mpi_t=None):
    """
    current_times([cpu_t, wall_t, mpi_t])
    
    
    Defined at System.fpp lines 2219-2227
    
    Parameters
    ----------
    cpu_t : float
    wall_t : float
    mpi_t : float
    
    """
    quippy._quippy.f90wrap_current_times(cpu_t=cpu_t, wall_t=wall_t, mpi_t=mpi_t)

def system_timer(name, do_always=None, time_elapsed=None, do_print=None):
    """
    system_timer(name[, do_always, time_elapsed, do_print])
    
    
    Defined at System.fpp lines 2241-2284
    
    Parameters
    ----------
    name : str
    	Unique identifier for this timer
    
    do_always : bool
    time_elapsed : float
    do_print : bool
    
    Measure elapsed CPU and wall clock time between pairs of calls with
    matching 'name' parameter. Calls to 'system_timer' must be properly
    nested(i.e. start and stop from different pairs can't overlap), and
    maximum depth of calls is set by the 'TIMER_STACK' parameter.
    
    >   call system_timer(name)  start the clock
    >   ...                      do something
    >   call system_timer(name)  stop clock and print elapsed time
    >
    > If optional do_always argument is true, routine will do its thing even
    > if system_do_timing is false.
    """
    quippy._quippy.f90wrap_system_timer(name=name, do_always=do_always, time_elapsed=time_elapsed, do_print=do_print)

def is_file_readable(filename):
    """
    is_file_readable = is_file_readable(filename)
    
    
    Defined at System.fpp lines 2287-2299
    
    Parameters
    ----------
    filename : str
    
    Returns
    -------
    is_file_readable : bool
    
    Test if the file 'filename' can be accessed.
    """
    is_file_readable = quippy._quippy.f90wrap_is_file_readable(filename=filename)
    return is_file_readable

def verbosity_to_str(val):
    """
    str = verbosity_to_str(val)
    
    
    Defined at System.fpp lines 2363-2379
    
    Parameters
    ----------
    val : int
    
    Returns
    -------
    str : str
    
    Map from verbsoity codes to descriptive strings
    """
    str = quippy._quippy.f90wrap_verbosity_to_str(val=val)
    return str

def verbosity_of_str(str):
    """
    val = verbosity_of_str(str)
    
    
    Defined at System.fpp lines 2382-2399
    
    Parameters
    ----------
    str : str
    
    Returns
    -------
    val : int
    
    Map from descriptive verbosity names('NORMAL', 'VERBOSE' etc.) to numbers
    """
    val = quippy._quippy.f90wrap_verbosity_of_str(str=str)
    return val

def verbosity_push(val):
    """
    verbosity_push(val)
    
    
    Defined at System.fpp lines 2404-2412
    
    Parameters
    ----------
    val : int
    
    Push a value onto the verbosity stack
    Don't ever lower the verbosity if verbosity minimum is set,
    but always push _something_
    """
    quippy._quippy.f90wrap_verbosity_push(val=val)

def verbosity_pop():
    """
    verbosity_pop()
    
    
    Defined at System.fpp lines 2415-2417
    
    
    pop the current verbosity value off the stack
    """
    quippy._quippy.f90wrap_verbosity_pop()

def current_verbosity():
    """
    current_verbosity = current_verbosity()
    
    
    Defined at System.fpp lines 2420-2422
    
    
    Returns
    -------
    current_verbosity : int
    
    return the current value of verbosity
    """
    current_verbosity = quippy._quippy.f90wrap_current_verbosity()
    return current_verbosity

def verbosity_push_increment(n=None):
    """
    verbosity_push_increment([n])
    
    
    Defined at System.fpp lines 2425-2430
    
    Parameters
    ----------
    n : int
    
    push the current value + n onto the stack
    """
    quippy._quippy.f90wrap_verbosity_push_increment(n=n)

def verbosity_push_decrement(n=None):
    """
    verbosity_push_decrement([n])
    
    
    Defined at System.fpp lines 2433-2438
    
    Parameters
    ----------
    n : int
    
    push the current value - n onto the stack
    """
    quippy._quippy.f90wrap_verbosity_push_decrement(n=n)

def verbosity_set_minimum(verbosity):
    """
    verbosity_set_minimum(verbosity)
    
    
    Defined at System.fpp lines 2442-2445
    
    Parameters
    ----------
    verbosity : int
    
    set the minimum verbosity value, by pushing value onto
    stack and pushing 1 on to verbosity_cascade_stack
    """
    quippy._quippy.f90wrap_verbosity_set_minimum(verbosity=verbosity)

def verbosity_unset_minimum():
    """
    verbosity_unset_minimum()
    
    
    Defined at System.fpp lines 2449-2451
    
    
    unset the minimum verbosity value, by popping value from
    stack and popping from verbosity_cascade_stack
    """
    quippy._quippy.f90wrap_verbosity_unset_minimum()

def enable_timing():
    """
    enable_timing()
    
    
    Defined at System.fpp lines 2533-2534
    
    
    """
    quippy._quippy.f90wrap_enable_timing()

def get_quippy_running():
    """
    get_quippy_running = get_quippy_running()
    
    
    Defined at System.fpp lines 2547-2549
    
    
    Returns
    -------
    get_quippy_running : bool
    
    """
    get_quippy_running = quippy._quippy.f90wrap_get_quippy_running()
    return get_quippy_running

def increase_stack(stack_size):
    """
    increase_stack = increase_stack(stack_size)
    
    
    Defined at System.fpp lines 2551-2555
    
    Parameters
    ----------
    stack_size : int
    
    Returns
    -------
    increase_stack : int
    
    """
    increase_stack = quippy._quippy.f90wrap_increase_stack(stack_size=stack_size)
    return increase_stack

def abort_on_mpi_error(error_code, routine_name):
    """
    abort_on_mpi_error(error_code, routine_name)
    
    
    Defined at System.fpp lines 2558-2563
    
    Parameters
    ----------
    error_code : int
    routine_name : str
    
    Abort with a useful message if an MPI routine returned an error status
    """
    quippy._quippy.f90wrap_abort_on_mpi_error(error_code=error_code, routine_name=routine_name)

def parallel_print(lines, comm, verbosity=None, file=None):
    """
    parallel_print(lines, comm[, verbosity, file])
    
    
    Defined at System.fpp lines 2565-2575
    
    Parameters
    ----------
    lines : str array
    comm : int
    verbosity : int
    file : Inoutput
    
    """
    quippy._quippy.f90wrap_parallel_print(lines=lines, comm=comm, verbosity=verbosity, file=None if file is None else \
        file._handle)

def alloc_trace(str, amt):
    """
    alloc_trace(str, amt)
    
    
    Defined at System.fpp lines 2577-2583
    
    Parameters
    ----------
    str : str
    amt : int
    
    """
    quippy._quippy.f90wrap_alloc_trace(str=str, amt=amt)

def dealloc_trace(str, amt):
    """
    dealloc_trace(str, amt)
    
    
    Defined at System.fpp lines 2585-2591
    
    Parameters
    ----------
    str : str
    amt : int
    
    """
    quippy._quippy.f90wrap_dealloc_trace(str=str, amt=amt)

def mpi_id():
    """
    id = mpi_id()
    
    
    Defined at System.fpp lines 2613-2615
    
    
    Returns
    -------
    id : int
    
    Return this processes' MPI ID
    """
    id = quippy._quippy.f90wrap_mpi_id()
    return id

def mpi_n_procs():
    """
    n = mpi_n_procs()
    
    
    Defined at System.fpp lines 2618-2620
    
    
    Returns
    -------
    n : int
    
    Return the total number of MPI processes.
    """
    n = quippy._quippy.f90wrap_mpi_n_procs()
    return n

def reference_true():
    """
    reference_true = reference_true()
    
    
    Defined at System.fpp lines 2622-2624
    
    
    Returns
    -------
    reference_true : bool
    
    """
    reference_true = quippy._quippy.f90wrap_reference_true()
    return reference_true

def reference_false():
    """
    reference_false = reference_false()
    
    
    Defined at System.fpp lines 2626-2628
    
    
    Returns
    -------
    reference_false : bool
    
    """
    reference_false = quippy._quippy.f90wrap_reference_false()
    return reference_false

def s2a(s):
    """
    a = s2a(s)
    
    
    Defined at System.fpp lines 2631-2637
    
    Parameters
    ----------
    s : str
    
    Returns
    -------
    a : str array
    
    String to character array
    """
    a = quippy._quippy.f90wrap_s2a(s=s)
    return a

def a2s(a):
    """
    s = a2s(a)
    
    
    Defined at System.fpp lines 2640-2646
    
    Parameters
    ----------
    a : str array
    
    Returns
    -------
    s : str
    
    Character array to string
    """
    s = quippy._quippy.f90wrap_a2s(a=a)
    return s

def pad(s, l):
    """
    a = pad(s, l)
    
    
    Defined at System.fpp lines 2649-2657
    
    Parameters
    ----------
    s : str
    l : int
    
    Returns
    -------
    a : str array
    
    String to padded character array of length l
    """
    a = quippy._quippy.f90wrap_pad(s=s, l=l)
    return a

def make_run_directory(basename=None, force_run_dir_i=None, run_dir_i=None, error=None):
    """
    dir = make_run_directory([basename, force_run_dir_i, run_dir_i, error])
    
    
    Defined at System.fpp lines 2659-2694
    
    Parameters
    ----------
    basename : str
    force_run_dir_i : int
    run_dir_i : int
    error : int
    
    Returns
    -------
    dir : str
    
    """
    dir = quippy._quippy.f90wrap_make_run_directory(basename=basename, force_run_dir_i=force_run_dir_i, run_dir_i=run_dir_i, \
        error=error)
    return dir

def link_run_directory(sourcename, basename=None, run_dir_i=None, error=None):
    """
    dir = link_run_directory(sourcename[, basename, run_dir_i, error])
    
    
    Defined at System.fpp lines 2696-2720
    
    Parameters
    ----------
    sourcename : str
    basename : str
    run_dir_i : int
    error : int
    
    Returns
    -------
    dir : str
    
    """
    dir = quippy._quippy.f90wrap_link_run_directory(sourcename=sourcename, basename=basename, run_dir_i=run_dir_i, \
        error=error)
    return dir

def linebreak_string(str, line_len):
    """
    lb_str = linebreak_string(str, line_len)
    
    
    Defined at System.fpp lines 2732-2770
    
    Parameters
    ----------
    str : str
    line_len : int
    
    Returns
    -------
    lb_str : str
    
    """
    lb_str = quippy._quippy.f90wrap_linebreak_string(str=str, line_len=line_len)
    return lb_str

def wait_for_file_to_exist(filename, max_wait_time, cycle_time=None, error=None):
    """
    wait_for_file_to_exist(filename, max_wait_time[, cycle_time, error])
    
    
    Defined at System.fpp lines 2790-2810
    
    Parameters
    ----------
    filename : str
    max_wait_time : float
    cycle_time : float
    error : int
    
    """
    quippy._quippy.f90wrap_wait_for_file_to_exist(filename=filename, max_wait_time=max_wait_time, cycle_time=cycle_time, \
        error=error)

def upper_case(word):
    """
    upper_case = upper_case(word)
    
    
    Defined at System.fpp lines 2813-2825
    
    Parameters
    ----------
    word : str
    
    Returns
    -------
    upper_case : str
    
    Convert a word to upper case
    """
    upper_case = quippy._quippy.f90wrap_upper_case(word=word)
    return upper_case

def lower_case(word):
    """
    lower_case = lower_case(word)
    
    
    Defined at System.fpp lines 2828-2840
    
    Parameters
    ----------
    word : str
    
    Returns
    -------
    lower_case : str
    
    Convert a word to lower case
    """
    lower_case = quippy._quippy.f90wrap_lower_case(word=word)
    return lower_case

def replace(string_bn, search, substitute):
    """
    res = replace(string_bn, search, substitute)
    
    
    Defined at System.fpp lines 2842-2854
    
    Parameters
    ----------
    string_bn : str
    search : str
    substitute : str
    
    Returns
    -------
    res : str
    
    """
    res = quippy._quippy.f90wrap_replace(string_bn=string_bn, search=search, substitute=substitute)
    return res

def progress(total, current, name):
    """
    progress(total, current, name)
    
    
    Defined at System.fpp lines 2857-2873
    
    Parameters
    ----------
    total : int
    current : int
    name : str
    
    Print a progress bar
    """
    quippy._quippy.f90wrap_progress(total=total, current=current, name=name)

def progress_timer(total, current, name, elapsed_seconds):
    """
    progress_timer(total, current, name, elapsed_seconds)
    
    
    Defined at System.fpp lines 2877-2921
    
    Parameters
    ----------
    total : int
    current : int
    name : str
    elapsed_seconds : float
    
    Print a progress bar with an estimate of time to completion
    based on the elapsed time so far
    """
    quippy._quippy.f90wrap_progress_timer(total=total, current=current, name=name, elapsed_seconds=elapsed_seconds)

def increase_to_multiple(a, m):
    """
    res = increase_to_multiple(a, m)
    
    
    Defined at System.fpp lines 2923-2927
    
    Parameters
    ----------
    a : int
    m : int
    
    Returns
    -------
    res : int
    
    """
    res = quippy._quippy.f90wrap_increase_to_multiple(a=a, m=m)
    return res

def _inoutput_print_string(string_bn, verbosity=None, file=None, nocr=None, do_flush=None):
    """
    _inoutput_print_string(string_bn[, verbosity, file, nocr, do_flush])
    
    
    Defined at System.fpp lines 624-671
    
    Parameters
    ----------
    string_bn : str
    verbosity : int
    file : Inoutput
    nocr : bool
    do_flush : bool
    
    """
    quippy._quippy.f90wrap_inoutput_print_string(string_bn=string_bn, verbosity=verbosity, file=None if file is None else \
        file._handle, nocr=nocr, do_flush=do_flush)

def _inoutput_print_integer(int_bn, verbosity=None, file=None):
    """
    _inoutput_print_integer(int_bn[, verbosity, file])
    
    
    Defined at System.fpp lines 700-705
    
    Parameters
    ----------
    int_bn : int
    verbosity : int
    file : Inoutput
    
    """
    quippy._quippy.f90wrap_inoutput_print_integer(int_bn=int_bn, verbosity=verbosity, file=None if file is None else \
        file._handle)

def _inoutput_print_real(real, verbosity=None, file=None, precision=None, format=None, nocr=None):
    """
    _inoutput_print_real(real[, verbosity, file, precision, format, nocr])
    
    
    Defined at System.fpp lines 707-734
    
    Parameters
    ----------
    real : float
    verbosity : int
    file : Inoutput
    precision : int
    format : str
    nocr : bool
    
    """
    quippy._quippy.f90wrap_inoutput_print_real(real=real, verbosity=verbosity, file=None if file is None else file._handle, \
        precision=precision, format=format, nocr=nocr)

def _inoutput_print_logical(log, verbosity=None, file=None):
    """
    _inoutput_print_logical(log[, verbosity, file])
    
    
    Defined at System.fpp lines 693-698
    
    Parameters
    ----------
    log : bool
    verbosity : int
    file : Inoutput
    
    """
    quippy._quippy.f90wrap_inoutput_print_logical(log=log, verbosity=verbosity, file=None if file is None else file._handle)

def _inoutput_print_char_array(char_a, verbosity=None, file=None):
    """
    _inoutput_print_char_array(char_a[, verbosity, file])
    
    
    Defined at System.fpp lines 682-691
    
    Parameters
    ----------
    char_a : str array
    verbosity : int
    file : Inoutput
    
    """
    quippy._quippy.f90wrap_inoutput_print_char_array(char_a=char_a, verbosity=verbosity, file=None if file is None else \
        file._handle)

def print(*args, **kwargs):
    """
    print(*args, **kwargs)
    
    
    Defined at System.fpp lines 252-256
    
    Overloaded interface containing the following procedures:
      _inoutput_print_string
      _inoutput_print_integer
      _inoutput_print_real
      _inoutput_print_logical
      _inoutput_print_char_array
    
    Overloaded interface for printing. With the
    'this' parameter omitted output goes to the default mainlog('stdout'). The
    'verbosity' parameter controls whether the object is actually printed;
    if the verbosity is greater than that currently at the top of the
    verbosity stack then output is suppressed. Possible verbosity levels
    range from 'ERROR' through 'NORMAL', 'VERBOSE', 'NERD' and 'ANALYSIS'.
    Other user-defined types define the Print interface in the same way.
    """
    for proc in [_inoutput_print_string, _inoutput_print_integer, _inoutput_print_real, _inoutput_print_logical, \
        _inoutput_print_char_array]:
        try:
            return proc(*args, **kwargs)
        except TypeError:
            continue
    

def _mem_info_i():
    """
    total_mem_i, free_mem_i = _mem_info_i()
    
    
    Defined at System.fpp lines 2772-2777
    
    
    Returns
    -------
    total_mem_i : int
    free_mem_i : int
    
    """
    total_mem_i, free_mem_i = quippy._quippy.f90wrap_mem_info_i()
    return total_mem_i, free_mem_i

def _mem_info_r():
    """
    total_mem, free_mem = _mem_info_r()
    
    
    Defined at System.fpp lines 2779-2781
    
    
    Returns
    -------
    total_mem : float
    free_mem : float
    
    """
    total_mem, free_mem = quippy._quippy.f90wrap_mem_info_r()
    return total_mem, free_mem

def mem_info(*args, **kwargs):
    """
    mem_info(*args, **kwargs)
    
    
    Defined at System.fpp lines 315-316
    
    Overloaded interface containing the following procedures:
      _mem_info_i
      _mem_info_r
    
    """
    for proc in [_mem_info_i, _mem_info_r]:
        try:
            return proc(*args, **kwargs)
        except TypeError:
            continue
    

def _optional_default_l(def_, opt_val=None):
    """
    optional_default_l = _optional_default_l(def_[, opt_val])
    
    
    Defined at System.fpp lines 2453-2461
    
    Parameters
    ----------
    def_ : bool
    opt_val : bool
    
    Returns
    -------
    optional_default_l : bool
    
    """
    optional_default_l = quippy._quippy.f90wrap_optional_default_l(def_=def_, opt_val=opt_val)
    return optional_default_l

def _optional_default_i(def_, opt_val=None):
    """
    optional_default_i = _optional_default_i(def_[, opt_val])
    
    
    Defined at System.fpp lines 2463-2471
    
    Parameters
    ----------
    def_ : int
    opt_val : int
    
    Returns
    -------
    optional_default_i : int
    
    """
    optional_default_i = quippy._quippy.f90wrap_optional_default_i(def_=def_, opt_val=opt_val)
    return optional_default_i

def _optional_default_r(def_, opt_val=None):
    """
    optional_default_r = _optional_default_r(def_[, opt_val])
    
    
    Defined at System.fpp lines 2483-2491
    
    Parameters
    ----------
    def_ : float
    opt_val : float
    
    Returns
    -------
    optional_default_r : float
    
    """
    optional_default_r = quippy._quippy.f90wrap_optional_default_r(def_=def_, opt_val=opt_val)
    return optional_default_r

def _optional_default_c(def_, opt_val=None):
    """
    optional_default_c = _optional_default_c(def_[, opt_val])
    
    
    Defined at System.fpp lines 2513-2521
    
    Parameters
    ----------
    def_ : str
    opt_val : str
    
    Returns
    -------
    optional_default_c : str
    
    """
    optional_default_c = quippy._quippy.f90wrap_optional_default_c(def_=def_, opt_val=opt_val)
    return optional_default_c

def _optional_default_ca(def_, opt_val=None):
    """
    optional_default_ca = _optional_default_ca(def_[, opt_val])
    
    
    Defined at System.fpp lines 2523-2531
    
    Parameters
    ----------
    def_ : str array
    opt_val : str array
    
    Returns
    -------
    optional_default_ca : str array
    
    """
    optional_default_ca = quippy._quippy.f90wrap_optional_default_ca(def_=def_, opt_val=opt_val)
    return optional_default_ca

def _optional_default_z(def_):
    """
    optional_default_z = _optional_default_z(def_)
    
    
    Defined at System.fpp lines 2503-2511
    
    Parameters
    ----------
    def_ : complex
    
    Returns
    -------
    optional_default_z : complex
    
    """
    optional_default_z = quippy._quippy.f90wrap_optional_default_z(def_=def_)
    return optional_default_z

def _optional_default_ia(def_, opt_val=None):
    """
    optional_default_ia = _optional_default_ia(def_[, opt_val])
    
    
    Defined at System.fpp lines 2473-2481
    
    Parameters
    ----------
    def_ : int array
    opt_val : int array
    
    Returns
    -------
    optional_default_ia : int array
    
    """
    optional_default_ia = quippy._quippy.f90wrap_optional_default_ia(def_=def_, opt_val=opt_val)
    return optional_default_ia

def _optional_default_ra(def_, opt_val=None):
    """
    optional_default_ra = _optional_default_ra(def_[, opt_val])
    
    
    Defined at System.fpp lines 2493-2501
    
    Parameters
    ----------
    def_ : float array
    opt_val : float array
    
    Returns
    -------
    optional_default_ra : float array
    
    """
    optional_default_ra = quippy._quippy.f90wrap_optional_default_ra(def_=def_, opt_val=opt_val)
    return optional_default_ra

def optional_default(*args, **kwargs):
    """
    optional_default(*args, **kwargs)
    
    
    Defined at System.fpp lines 352-355
    
    Overloaded interface containing the following procedures:
      _optional_default_l
      _optional_default_i
      _optional_default_r
      _optional_default_c
      _optional_default_ca
      _optional_default_z
      _optional_default_ia
      _optional_default_ra
    
    takes as arguments a default value and an optional argument, and
    returns the optional argument value if it's present, otherwise
    the default value
    """
    for proc in [_optional_default_l, _optional_default_i, _optional_default_r, _optional_default_c, _optional_default_ca, \
        _optional_default_z, _optional_default_ia, _optional_default_ra]:
        try:
            return proc(*args, **kwargs)
        except TypeError:
            continue
    

def _string_to_real_sub(string_bn, error=None):
    """
    real_number = _string_to_real_sub(string_bn[, error])
    
    
    Defined at System.fpp lines 1321-1331
    
    Parameters
    ----------
    string_bn : str
    error : int
    
    Returns
    -------
    real_number : float
    
    """
    real_number = quippy._quippy.f90wrap_string_to_real_sub(string_bn=string_bn, error=error)
    return real_number

def _string_to_integer_sub(string_bn, error=None):
    """
    integer_number = _string_to_integer_sub(string_bn[, error])
    
    
    Defined at System.fpp lines 1333-1343
    
    Parameters
    ----------
    string_bn : str
    error : int
    
    Returns
    -------
    integer_number : int
    
    """
    integer_number = quippy._quippy.f90wrap_string_to_integer_sub(string_bn=string_bn, error=error)
    return integer_number

def _string_to_logical_sub(string_bn, error=None):
    """
    logical_number = _string_to_logical_sub(string_bn[, error])
    
    
    Defined at System.fpp lines 1345-1355
    
    Parameters
    ----------
    string_bn : str
    error : int
    
    Returns
    -------
    logical_number : bool
    
    """
    logical_number = quippy._quippy.f90wrap_string_to_logical_sub(string_bn=string_bn, error=error)
    return logical_number

def _string_to_real1d(string_bn, real1d, error=None):
    """
    _string_to_real1d(string_bn, real1d[, error])
    
    
    Defined at System.fpp lines 1357-1367
    
    Parameters
    ----------
    string_bn : str
    real1d : float array
    error : int
    
    """
    quippy._quippy.f90wrap_string_to_real1d(string_bn=string_bn, real1d=real1d, error=error)

def _string_to_integer1d(string_bn, integer1d, error=None):
    """
    _string_to_integer1d(string_bn, integer1d[, error])
    
    
    Defined at System.fpp lines 1369-1379
    
    Parameters
    ----------
    string_bn : str
    integer1d : int array
    error : int
    
    """
    quippy._quippy.f90wrap_string_to_integer1d(string_bn=string_bn, integer1d=integer1d, error=error)

def _string_to_logical1d(string_bn, logical1d, error=None):
    """
    _string_to_logical1d(string_bn, logical1d[, error])
    
    
    Defined at System.fpp lines 1381-1391
    
    Parameters
    ----------
    string_bn : str
    logical1d : bool array
    error : int
    
    """
    quippy._quippy.f90wrap_string_to_logical1d(string_bn=string_bn, logical1d=logical1d, error=error)

def string_to_numerical(*args, **kwargs):
    """
    string_to_numerical(*args, **kwargs)
    
    
    Defined at System.fpp lines 360-362
    
    Overloaded interface containing the following procedures:
      _string_to_real_sub
      _string_to_integer_sub
      _string_to_logical_sub
      _string_to_real1d
      _string_to_integer1d
      _string_to_logical1d
    
    """
    for proc in [_string_to_real_sub, _string_to_integer_sub, _string_to_logical_sub, _string_to_real1d, \
        _string_to_integer1d, _string_to_logical1d]:
        try:
            return proc(*args, **kwargs)
        except TypeError:
            continue
    

def _int_format_length_isp(i):
    """
    len_bn = _int_format_length_isp(i)
    
    
    Defined at System.fpp lines 1691-1694
    
    Parameters
    ----------
    i : int
    
    Returns
    -------
    len_bn : int
    
    """
    len_bn = quippy._quippy.f90wrap_int_format_length_isp(i=i)
    return len_bn

def _int_format_length_idp(i):
    """
    len_bn = _int_format_length_idp(i)
    
    
    Defined at System.fpp lines 1696-1699
    
    Parameters
    ----------
    i : int
    
    Returns
    -------
    len_bn : int
    
    """
    len_bn = quippy._quippy.f90wrap_int_format_length_idp(i=i)
    return len_bn

def int_format_length(*args, **kwargs):
    """
    int_format_length(*args, **kwargs)
    
    
    Defined at System.fpp lines 365-366
    
    Overloaded interface containing the following procedures:
      _int_format_length_isp
      _int_format_length_idp
    
    """
    for proc in [_int_format_length_isp, _int_format_length_idp]:
        try:
            return proc(*args, **kwargs)
        except TypeError:
            continue
    

def get_system_always_flush():
    """
    Element system_always_flush ftype=logical pytype=bool
    
    
    Defined at System.fpp line 143
    
    """
    return quippy._quippy.f90wrap_system_module__get__system_always_flush()

def set_system_always_flush(system_always_flush):
    quippy._quippy.f90wrap_system_module__set__system_always_flush(system_always_flush)

def get_system_use_fortran_random():
    """
    Element system_use_fortran_random ftype=logical pytype=bool
    
    
    Defined at System.fpp line 144
    
    """
    return quippy._quippy.f90wrap_system_module__get__system_use_fortran_random()

def set_system_use_fortran_random(system_use_fortran_random):
    quippy._quippy.f90wrap_system_module__set__system_use_fortran_random(system_use_fortran_random)

def get_quip_new_line():
    """
    Element quip_new_line ftype=character pytype=str
    
    
    Defined at System.fpp line 146
    
    """
    return quippy._quippy.f90wrap_system_module__get__quip_new_line()

def set_quip_new_line(quip_new_line):
    quippy._quippy.f90wrap_system_module__set__quip_new_line(quip_new_line)

def get_integer_size():
    """
    Element integer_size ftype=integer pytype=int
    
    
    Defined at System.fpp line 147
    
    """
    return quippy._quippy.f90wrap_system_module__get__integer_size()

INTEGER_SIZE = get_integer_size()

def get_real_size():
    """
    Element real_size ftype=integer pytype=int
    
    
    Defined at System.fpp line 148
    
    """
    return quippy._quippy.f90wrap_system_module__get__real_size()

REAL_SIZE = get_real_size()

def get_complex_size():
    """
    Element complex_size ftype=integer pytype=int
    
    
    Defined at System.fpp line 149
    
    """
    return quippy._quippy.f90wrap_system_module__get__complex_size()

COMPLEX_SIZE = get_complex_size()

def get_trace_memory():
    """
    Element trace_memory ftype=logical pytype=bool
    
    
    Defined at System.fpp line 150
    
    """
    return quippy._quippy.f90wrap_system_module__get__trace_memory()

def set_trace_memory(trace_memory):
    quippy._quippy.f90wrap_system_module__set__trace_memory(trace_memory)

def get_traced_memory():
    """
    Element traced_memory ftype=integer pytype=int
    
    
    Defined at System.fpp line 151
    
    """
    return quippy._quippy.f90wrap_system_module__get__traced_memory()

def set_traced_memory(traced_memory):
    quippy._quippy.f90wrap_system_module__set__traced_memory(traced_memory)

def get_line():
    """
    Element line ftype=character(system_string_length_long) pytype=str
    
    
    Defined at System.fpp line 182
    
    """
    return quippy._quippy.f90wrap_system_module__get__line()

def set_line(line):
    quippy._quippy.f90wrap_system_module__set__line(line)

def get_mainlog():
    """
    Element mainlog ftype=type(inoutput) pytype=Inoutput
    
    
    Defined at System.fpp line 184
    
    main output, connected to 'stdout' by default
    """
    global mainlog
    mainlog_handle = quippy._quippy.f90wrap_system_module__get__mainlog()
    if tuple(mainlog_handle) in _objs:
        mainlog = _objs[tuple(mainlog_handle)]
    else:
        mainlog = InOutput.from_handle(mainlog_handle)
        _objs[tuple(mainlog_handle)] = mainlog
    return mainlog

def set_mainlog(mainlog):
    mainlog = mainlog._handle
    quippy._quippy.f90wrap_system_module__set__mainlog(mainlog)

def get_errorlog():
    """
    Element errorlog ftype=type(inoutput) pytype=Inoutput
    
    
    Defined at System.fpp line 185
    
    error output, connected to 'stderr' by default
    """
    global errorlog
    errorlog_handle = quippy._quippy.f90wrap_system_module__get__errorlog()
    if tuple(errorlog_handle) in _objs:
        errorlog = _objs[tuple(errorlog_handle)]
    else:
        errorlog = InOutput.from_handle(errorlog_handle)
        _objs[tuple(errorlog_handle)] = errorlog
    return errorlog

def set_errorlog(errorlog):
    errorlog = errorlog._handle
    quippy._quippy.f90wrap_system_module__set__errorlog(errorlog)

def get_mpilog():
    """
    Element mpilog ftype=type(inoutput) pytype=Inoutput
    
    
    Defined at System.fpp line 186
    
    MPI output, written to by each mpi process
    """
    global mpilog
    mpilog_handle = quippy._quippy.f90wrap_system_module__get__mpilog()
    if tuple(mpilog_handle) in _objs:
        mpilog = _objs[tuple(mpilog_handle)]
    else:
        mpilog = InOutput.from_handle(mpilog_handle)
        _objs[tuple(mpilog_handle)] = mpilog
    return mpilog

def set_mpilog(mpilog):
    mpilog = mpilog._handle
    quippy._quippy.f90wrap_system_module__set__mpilog(mpilog)

def get_numerical_zero():
    """
    Element numerical_zero ftype=real(dp) pytype=float
    
    
    Defined at System.fpp line 189
    
    """
    return quippy._quippy.f90wrap_system_module__get__numerical_zero()

NUMERICAL_ZERO = get_numerical_zero()

def get_ran_max():
    """
    Element ran_max ftype=integer pytype=int
    
    
    Defined at System.fpp line 191
    
    """
    return quippy._quippy.f90wrap_system_module__get__ran_max()

def set_ran_max(ran_max):
    quippy._quippy.f90wrap_system_module__set__ran_max(ran_max)

def get_print_always():
    """
    Element print_always ftype=integer pytype=int
    
    
    Defined at System.fpp line 193
    
    """
    return quippy._quippy.f90wrap_system_module__get__print_always()

PRINT_ALWAYS = get_print_always()

def get_print_silent():
    """
    Element print_silent ftype=integer pytype=int
    
    
    Defined at System.fpp line 194
    
    """
    return quippy._quippy.f90wrap_system_module__get__print_silent()

PRINT_SILENT = get_print_silent()

def get_print_normal():
    """
    Element print_normal ftype=integer pytype=int
    
    
    Defined at System.fpp line 195
    
    """
    return quippy._quippy.f90wrap_system_module__get__print_normal()

PRINT_NORMAL = get_print_normal()

def get_print_verbose():
    """
    Element print_verbose ftype=integer pytype=int
    
    
    Defined at System.fpp line 196
    
    """
    return quippy._quippy.f90wrap_system_module__get__print_verbose()

PRINT_VERBOSE = get_print_verbose()

def get_print_nerd():
    """
    Element print_nerd ftype=integer pytype=int
    
    
    Defined at System.fpp line 197
    
    """
    return quippy._quippy.f90wrap_system_module__get__print_nerd()

PRINT_NERD = get_print_nerd()

def get_print_analysis():
    """
    Element print_analysis ftype=integer pytype=int
    
    
    Defined at System.fpp line 198
    
    """
    return quippy._quippy.f90wrap_system_module__get__print_analysis()

PRINT_ANALYSIS = get_print_analysis()

def get_input():
    """
    Element input ftype=integer pytype=int
    
    
    Defined at System.fpp line 199
    
    """
    return quippy._quippy.f90wrap_system_module__get__input()

INPUT = get_input()

def get_output():
    """
    Element output ftype=integer pytype=int
    
    
    Defined at System.fpp line 200
    
    """
    return quippy._quippy.f90wrap_system_module__get__output()

OUTPUT = get_output()

def get_inout():
    """
    Element inout ftype=integer pytype=int
    
    
    Defined at System.fpp line 201
    
    """
    return quippy._quippy.f90wrap_system_module__get__inout()

INOUT = get_inout()

def get_ran_a():
    """
    Element ran_a ftype=integer pytype=int
    
    
    Defined at System.fpp line 203
    
    """
    return quippy._quippy.f90wrap_system_module__get__ran_a()

ran_A = get_ran_a()

def get_ran_m():
    """
    Element ran_m ftype=integer pytype=int
    
    
    Defined at System.fpp line 204
    
    """
    return quippy._quippy.f90wrap_system_module__get__ran_m()

ran_M = get_ran_m()

def get_ran_q():
    """
    Element ran_q ftype=integer pytype=int
    
    
    Defined at System.fpp line 205
    
    """
    return quippy._quippy.f90wrap_system_module__get__ran_q()

ran_Q = get_ran_q()

def get_ran_r():
    """
    Element ran_r ftype=integer pytype=int
    
    
    Defined at System.fpp line 206
    
    """
    return quippy._quippy.f90wrap_system_module__get__ran_r()

ran_R = get_ran_r()

def get_timer_stack():
    """
    Element timer_stack ftype=integer pytype=int
    
    
    Defined at System.fpp line 208
    
    """
    return quippy._quippy.f90wrap_system_module__get__timer_stack()

TIMER_STACK = get_timer_stack()

def get_num_command_args():
    """
    Element num_command_args ftype=integer pytype=int
    
    
    Defined at System.fpp line 210
    
    The number of arguments on the command line
    """
    return quippy._quippy.f90wrap_system_module__get__num_command_args()

def set_num_command_args(num_command_args):
    quippy._quippy.f90wrap_system_module__set__num_command_args(num_command_args)

def get_max_readable_args():
    """
    Element max_readable_args ftype=integer pytype=int
    
    
    Defined at System.fpp line 211
    
    The maximum number of arguments that will be read
    """
    return quippy._quippy.f90wrap_system_module__get__max_readable_args()

MAX_READABLE_ARGS = get_max_readable_args()

def get_exec_name():
    """
    Element exec_name ftype=character(255) pytype=str
    
    
    Defined at System.fpp line 212
    
    The name of the executable
    """
    return quippy._quippy.f90wrap_system_module__get__exec_name()

def set_exec_name(exec_name):
    quippy._quippy.f90wrap_system_module__set__exec_name(exec_name)

def get_array_command_arg():
    """
    Element command_arg ftype=character(2550) pytype=str
    
    
    Defined at System.fpp line 213
    
    The first 'MAX_READABLE_ARGS' command arguments
    """
    global command_arg
    array_ndim, array_type, array_shape, array_handle = \
        quippy._quippy.f90wrap_system_module__array__command_arg(f90wrap.runtime.empty_handle)
    if array_handle in _arrays:
        command_arg = _arrays[array_handle]
    else:
        command_arg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                f90wrap.runtime.empty_handle,
                                quippy._quippy.f90wrap_system_module__array__command_arg)
        _arrays[array_handle] = command_arg
    return command_arg

def set_array_command_arg(command_arg):
    globals()['command_arg'][...] = command_arg


_array_initialisers = [get_array_command_arg]
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "system_module".')

for func in _dt_array_initialisers:
    func()
