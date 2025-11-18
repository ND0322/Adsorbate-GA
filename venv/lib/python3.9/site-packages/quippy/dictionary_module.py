"""
Module dictionary_module


Defined at Dictionary.fpp lines 127-2662

A Dictionary object contains a list of keys(strings) and corresponding entries.
Entries are a variable type, containing one of:
'integer', 'real(dp)', 'complex(dp)', 'logical', extendable_str
or a 1-D array of any of those. 2-D arrays of integers and reals are also supported.
"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("quippy.DictData")
class DictData(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=dictdata)
    
    
    Defined at Dictionary.fpp lines 152-153
    
    """
    def __init__(self, handle=None):
        """
        self = Dictdata()
        
        
        Defined at Dictionary.fpp lines 152-153
        
        
        Returns
        -------
        this : Dictdata
        	Object to be constructed
        
        
        Automatically generated constructor for dictdata
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_dictdata_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Dictdata
        
        
        Defined at Dictionary.fpp lines 152-153
        
        Parameters
        ----------
        this : Dictdata
        	Object to be destructed
        
        
        Automatically generated destructor for dictdata
        """
        if self._alloc:
            quippy._quippy.f90wrap_dictdata_finalise(this=self._handle)
    
    @property
    def d(self):
        """
        Element d ftype=integer pytype=int
        
        
        Defined at Dictionary.fpp line 153
        
        """
        array_ndim, array_type, array_shape, array_handle =     quippy._quippy.f90wrap_dictdata__array__d(self._handle)
        if array_handle in self._arrays:
            d = self._arrays[array_handle]
        else:
            d = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictdata__array__d)
            self._arrays[array_handle] = d
        return d
    
    @d.setter
    def d(self, d):
        self.d[...] = d
    
    def __str__(self):
        ret = ['<dictdata>{\n']
        ret.append('    d : ')
        ret.append(repr(self.d))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.DictEntry")
class DictEntry(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=dictentry)
    
    
    Defined at Dictionary.fpp lines 156-174
    
    OMIT
    """
    def __del__(self):
        """
        Destructor for class Dictentry
        
        
        Defined at Dictionary.fpp lines 458-476
        
        Parameters
        ----------
        this : Dictentry
        
        Finalise dictionary
        """
        if self._alloc:
            quippy._quippy.f90wrap_dictentry_finalise(this=self._handle)
    
    def print(self, key, verbosity=None, file=None):
        """
        print(self, key[, verbosity, file])
        
        
        Defined at Dictionary.fpp lines 335-393
        
        Parameters
        ----------
        this : Dictentry
        key : str
        verbosity : int
        file : Inoutput
        
        Print a DictEntry or a Dictionary
        """
        quippy._quippy.f90wrap_dictentry_print(this=self._handle, key=key, verbosity=verbosity, file=None if file is None else \
            file._handle)
    
    def __init__(self, handle=None):
        """
        self = Dictentry()
        
        
        Defined at Dictionary.fpp lines 156-174
        
        
        Returns
        -------
        this : Dictentry
        	Object to be constructed
        
        
        Automatically generated constructor for dictentry
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_dictentry_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    @property
    def type_bn(self):
        """
        Element type_bn ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 158
        
        """
        return quippy._quippy.f90wrap_dictentry__get__type_bn(self._handle)
    
    @type_bn.setter
    def type_bn(self, type_bn):
        quippy._quippy.f90wrap_dictentry__set__type_bn(self._handle, type_bn)
    
    @property
    def len_bn(self):
        """
        Element len_bn ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 159
        
        """
        return quippy._quippy.f90wrap_dictentry__get__len_bn(self._handle)
    
    @len_bn.setter
    def len_bn(self, len_bn):
        quippy._quippy.f90wrap_dictentry__set__len_bn(self._handle, len_bn)
    
    @property
    def len2(self):
        """
        Element len2 ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 160
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__len2(self._handle)
        if array_handle in self._arrays:
            len2 = self._arrays[array_handle]
        else:
            len2 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__len2)
            self._arrays[array_handle] = len2
        return len2
    
    @len2.setter
    def len2(self, len2):
        self.len2[...] = len2
    
    @property
    def own_data(self):
        """
        Element own_data ftype=logical pytype=bool
        
        
        Defined at Dictionary.fpp line 161
        
        True if we own the data and should free it in finalise()
        """
        return quippy._quippy.f90wrap_dictentry__get__own_data(self._handle)
    
    @own_data.setter
    def own_data(self, own_data):
        quippy._quippy.f90wrap_dictentry__set__own_data(self._handle, own_data)
    
    @property
    def i(self):
        """
        Element i ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 162
        
        """
        return quippy._quippy.f90wrap_dictentry__get__i(self._handle)
    
    @i.setter
    def i(self, i):
        quippy._quippy.f90wrap_dictentry__set__i(self._handle, i)
    
    @property
    def r(self):
        """
        Element r ftype=real(dp) pytype=float
        
        
        Defined at Dictionary.fpp line 163
        
        """
        return quippy._quippy.f90wrap_dictentry__get__r(self._handle)
    
    @r.setter
    def r(self, r):
        quippy._quippy.f90wrap_dictentry__set__r(self._handle, r)
    
    @property
    def c(self):
        """
        Element c ftype=complex(dp) pytype=complex
        
        
        Defined at Dictionary.fpp line 164
        
        """
        return quippy._quippy.f90wrap_dictentry__get__c(self._handle)
    
    @c.setter
    def c(self, c):
        quippy._quippy.f90wrap_dictentry__set__c(self._handle, c)
    
    @property
    def l(self):
        """
        Element l ftype=logical pytype=bool
        
        
        Defined at Dictionary.fpp line 165
        
        """
        return quippy._quippy.f90wrap_dictentry__get__l(self._handle)
    
    @l.setter
    def l(self, l):
        quippy._quippy.f90wrap_dictentry__set__l(self._handle, l)
    
    @property
    def i_a(self):
        """
        Element i_a ftype=integer pytype=int
        
        
        Defined at Dictionary.fpp line 167
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__i_a(self._handle)
        if array_handle in self._arrays:
            i_a = self._arrays[array_handle]
        else:
            i_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__i_a)
            self._arrays[array_handle] = i_a
        return i_a
    
    @i_a.setter
    def i_a(self, i_a):
        self.i_a[...] = i_a
    
    @property
    def r_a(self):
        """
        Element r_a ftype=real(dp) pytype=float
        
        
        Defined at Dictionary.fpp line 168
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__r_a(self._handle)
        if array_handle in self._arrays:
            r_a = self._arrays[array_handle]
        else:
            r_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__r_a)
            self._arrays[array_handle] = r_a
        return r_a
    
    @r_a.setter
    def r_a(self, r_a):
        self.r_a[...] = r_a
    
    @property
    def c_a(self):
        """
        Element c_a ftype=complex(dp) pytype=complex
        
        
        Defined at Dictionary.fpp line 169
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__c_a(self._handle)
        if array_handle in self._arrays:
            c_a = self._arrays[array_handle]
        else:
            c_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__c_a)
            self._arrays[array_handle] = c_a
        return c_a
    
    @c_a.setter
    def c_a(self, c_a):
        self.c_a[...] = c_a
    
    @property
    def l_a(self):
        """
        Element l_a ftype=logical pytype=bool
        
        
        Defined at Dictionary.fpp line 170
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__l_a(self._handle)
        if array_handle in self._arrays:
            l_a = self._arrays[array_handle]
        else:
            l_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__l_a)
            self._arrays[array_handle] = l_a
        return l_a
    
    @l_a.setter
    def l_a(self, l_a):
        self.l_a[...] = l_a
    
    @property
    def s_a(self):
        """
        Element s_a ftype=character(len=1) pytype=str
        
        
        Defined at Dictionary.fpp line 171
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__s_a(self._handle)
        if array_handle in self._arrays:
            s_a = self._arrays[array_handle]
        else:
            s_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__s_a)
            self._arrays[array_handle] = s_a
        return s_a
    
    @s_a.setter
    def s_a(self, s_a):
        self.s_a[...] = s_a
    
    @property
    def i_a2(self):
        """
        Element i_a2 ftype=integer pytype=int
        
        
        Defined at Dictionary.fpp line 172
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__i_a2(self._handle)
        if array_handle in self._arrays:
            i_a2 = self._arrays[array_handle]
        else:
            i_a2 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__i_a2)
            self._arrays[array_handle] = i_a2
        return i_a2
    
    @i_a2.setter
    def i_a2(self, i_a2):
        self.i_a2[...] = i_a2
    
    @property
    def r_a2(self):
        """
        Element r_a2 ftype=real(dp) pytype=float
        
        
        Defined at Dictionary.fpp line 173
        
        """
        array_ndim, array_type, array_shape, array_handle = quippy._quippy.f90wrap_dictentry__array__r_a2(self._handle)
        if array_handle in self._arrays:
            r_a2 = self._arrays[array_handle]
        else:
            r_a2 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    quippy._quippy.f90wrap_dictentry__array__r_a2)
            self._arrays[array_handle] = r_a2
        return r_a2
    
    @r_a2.setter
    def r_a2(self, r_a2):
        self.r_a2[...] = r_a2
    
    @property
    def d(self):
        """
        Element d ftype=type(dictdata) pytype=Dictdata
        
        
        Defined at Dictionary.fpp line 174
        
        """
        d_handle = quippy._quippy.f90wrap_dictentry__get__d(self._handle)
        if tuple(d_handle) in self._objs:
            d = self._objs[tuple(d_handle)]
        else:
            d = DictData.from_handle(d_handle)
            self._objs[tuple(d_handle)] = d
        return d
    
    @d.setter
    def d(self, d):
        d = d._handle
        quippy._quippy.f90wrap_dictentry__set__d(self._handle, d)
    
    def __str__(self):
        ret = ['<dictentry>{\n']
        ret.append('    type_bn : ')
        ret.append(repr(self.type_bn))
        ret.append(',\n    len_bn : ')
        ret.append(repr(self.len_bn))
        ret.append(',\n    len2 : ')
        ret.append(repr(self.len2))
        ret.append(',\n    own_data : ')
        ret.append(repr(self.own_data))
        ret.append(',\n    i : ')
        ret.append(repr(self.i))
        ret.append(',\n    r : ')
        ret.append(repr(self.r))
        ret.append(',\n    c : ')
        ret.append(repr(self.c))
        ret.append(',\n    l : ')
        ret.append(repr(self.l))
        ret.append(',\n    i_a : ')
        ret.append(repr(self.i_a))
        ret.append(',\n    r_a : ')
        ret.append(repr(self.r_a))
        ret.append(',\n    c_a : ')
        ret.append(repr(self.c_a))
        ret.append(',\n    l_a : ')
        ret.append(repr(self.l_a))
        ret.append(',\n    s_a : ')
        ret.append(repr(self.s_a))
        ret.append(',\n    i_a2 : ')
        ret.append(repr(self.i_a2))
        ret.append(',\n    r_a2 : ')
        ret.append(repr(self.r_a2))
        ret.append(',\n    d : ')
        ret.append(repr(self.d))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("quippy.Dictionary")
class Dictionary(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=dictionary)
    
    
    Defined at Dictionary.fpp lines 178-197
    
    Fortran implementation of a dictionary to store key/value pairs of the following types:
    
    - Integer
    - Real
    - String
    - Complex
    - Logical
    - 1D integer array
    - 1D real array
    - 1D complex array
    - 1D logical array
    - 2D integer array
    - 2D real array
    - Arbitrary data, via Fortran ``transform()`` intrinsic
    """
    def get_key(self, i, error=None):
        """
        key = get_key(self, i[, error])
        
        
        Defined at Dictionary.fpp lines 478-487
        
        Parameters
        ----------
        this : Dictionary
        i : int
        error : int
        
        Returns
        -------
        key : str
        
        """
        key = quippy._quippy.f90wrap_dictionary_get_key(this=self._handle, i=i, error=error)
        return key
    
    def get_type_and_size(self, key, thesize2, error=None):
        """
        type_bn, thesize = get_type_and_size(self, key, thesize2[, error])
        
        
        Defined at Dictionary.fpp lines 489-502
        
        Parameters
        ----------
        this : Dictionary
        key : str
        thesize2 : int array
        error : int
        
        Returns
        -------
        type_bn : int
        thesize : int
        
        """
        type_bn, thesize = quippy._quippy.f90wrap_dictionary_get_type_and_size(this=self._handle, key=key, thesize2=thesize2, \
            error=error)
        return type_bn, thesize
    
    def lookup_entry_i(self, key, case_sensitive=None):
        """
        lookup_entry_i = lookup_entry_i(self, key[, case_sensitive])
        
        
        Defined at Dictionary.fpp lines 2218-2239
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        
        Returns
        -------
        lookup_entry_i : int
        
        OMIT
        """
        lookup_entry_i = quippy._quippy.f90wrap_lookup_entry_i(this=self._handle, key=key, case_sensitive=case_sensitive)
        return lookup_entry_i
    
    def _array__(self, key):
        """
        nd, dtype, dshape, dloc = _array__(self, key)
        
        
        Defined at Dictionary.fpp lines 2607-2661
        
        Parameters
        ----------
        this : Dictionary
        key : str
        
        Returns
        -------
        nd : int
        dtype : int
        dshape : int array
        dloc : int
        
        """
        nd, dtype, dshape, dloc = quippy._quippy.f90wrap_dictionary__array__(this=self._handle, key=key)
        return nd, dtype, dshape, dloc
    
    def __init__(self, handle=None):
        """
        self = Dictionary()
        
        
        Defined at Dictionary.fpp lines 427-432
        
        
        Returns
        -------
        this : Dictionary
        
        Initialise a new empty dictionary
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_dictionary_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Dictionary
        
        
        Defined at Dictionary.fpp lines 434-456
        
        Parameters
        ----------
        this : Dictionary
        
        Finalise dictionary
        """
        if self._alloc:
            quippy._quippy.f90wrap_dictionary_finalise(this=self._handle)
    
    def print(self, verbosity=None, file=None):
        """
        print(self[, verbosity, file])
        
        
        Defined at Dictionary.fpp lines 412-420
        
        Parameters
        ----------
        this : Dictionary
        verbosity : int
        file : Inoutput
        
        Print a DictEntry or a Dictionary
        """
        quippy._quippy.f90wrap_dictionary_print(this=self._handle, verbosity=verbosity, file=None if file is None else \
            file._handle)
    
    def print_keys(self, verbosity=None, file=None):
        """
        print_keys(self[, verbosity, file])
        
        
        Defined at Dictionary.fpp lines 395-410
        
        Parameters
        ----------
        this : Dictionary
        verbosity : int
        file : Inoutput
        
        """
        quippy._quippy.f90wrap_dictionary_print_keys(this=self._handle, verbosity=verbosity, file=None if file is None else \
            file._handle)
    
    def remove_value(self, key):
        """
        remove_value(self, key)
        
        
        Defined at Dictionary.fpp lines 1802-1811
        
        Parameters
        ----------
        this : Dictionary
        key : str
        
        Remove an entry from a Dictionary
        """
        quippy._quippy.f90wrap_dictionary_remove_value(this=self._handle, key=key)
    
    def write_string(self, real_format=None, entry_sep=None, char_a_sep=None, quote_char=None, error=None):
        """
        dictionary_write_string = write_string(self[, real_format, entry_sep, char_a_sep, quote_char, error])
        
        
        Defined at Dictionary.fpp lines 2043-2121
        
        Parameters
        ----------
        this : Dictionary
        real_format : str
        	Output format for reals, default is 'f9.3'
        
        entry_sep : str
        	Entry seperator, default is single space
        
        char_a_sep : str
        	Output separator for character arrays, default is ','
        
        quote_char : str
        	Character to use to quote output fields containing whitespace, default is '"'
        
        error : int
        
        Returns
        -------
        dictionary_write_string : str
        
        Write a string representation of this dictionary
        """
        dictionary_write_string = quippy._quippy.f90wrap_dictionary_write_string(this=self._handle, real_format=real_format, \
            entry_sep=entry_sep, char_a_sep=char_a_sep, quote_char=quote_char, error=error)
        return dictionary_write_string
    
    def read_string(self, str, append=None, error=None):
        """
        read_string(self, str[, append, error])
        
        
        Defined at Dictionary.fpp lines 1813-1848
        
        Parameters
        ----------
        this : Dictionary
        str : str
        append : bool
        	If true, append to dictionary(default false)
        
        error : int
        
        Read into this dictionary from a string
        """
        quippy._quippy.f90wrap_dictionary_read_string(this=self._handle, str=str, append=append, error=error)
    
    def subset(self, keys, out, case_sensitive=None, out_no_initialise=None, error=None):
        """
        subset(self, keys, out[, case_sensitive, out_no_initialise, error])
        
        
        Defined at Dictionary.fpp lines 2249-2268
        
        Parameters
        ----------
        this : Dictionary
        keys : str array
        out : Dictionary
        case_sensitive : bool
        out_no_initialise : bool
        error : int
        
        """
        quippy._quippy.f90wrap_dictionary_subset(this=self._handle, keys=keys, out=out._handle, case_sensitive=case_sensitive, \
            out_no_initialise=out_no_initialise, error=error)
    
    def swap(self, key1, key2, case_sensitive=None, error=None):
        """
        swap(self, key1, key2[, case_sensitive, error])
        
        
        Defined at Dictionary.fpp lines 2371-2398
        
        Parameters
        ----------
        this : Dictionary
        key1 : str
        key2 : str
        case_sensitive : bool
        error : int
        
        Swap the positions of two entries in the dictionary. Arrays are not moved in memory.
        """
        quippy._quippy.f90wrap_dictionary_swap(this=self._handle, key1=key1, key2=key2, case_sensitive=case_sensitive, \
            error=error)
    
    def has_key(self, key, case_sensitive=None):
        """
        dictionary_has_key = has_key(self, key[, case_sensitive])
        
        
        Defined at Dictionary.fpp lines 2242-2247
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        
        Returns
        -------
        dictionary_has_key : bool
        
        Return true if 'key' is in Dictionary or false if not
        """
        dictionary_has_key = quippy._quippy.f90wrap_dictionary_has_key(this=self._handle, key=key, \
            case_sensitive=case_sensitive)
        return dictionary_has_key
    
    def deepcopy(self, from_, error=None):
        """
        deepcopy(self, from_[, error])
        
        
        Defined at Dictionary.fpp lines 2593-2599
        
        Parameters
        ----------
        this : Dictionary
        from_ : Dictionary
        error : int
        
        Make a deep copy of 'from' in 'this', allocating new memory for array components
        """
        quippy._quippy.f90wrap_dictionary_deepcopy(this=self._handle, from_=from_._handle, error=error)
    
    def _set_value_none(self, key):
        """
        _set_value_none(self, key)
        
        
        Defined at Dictionary.fpp lines 509-518
        
        Parameters
        ----------
        this : Dictionary
        key : str
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_none(this=self._handle, key=key)
    
    def _set_value_i(self, key, value):
        """
        _set_value_i(self, key, value)
        
        
        Defined at Dictionary.fpp lines 520-531
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_i(this=self._handle, key=key, value=value)
    
    def _set_value_r(self, key, value):
        """
        _set_value_r(self, key, value)
        
        
        Defined at Dictionary.fpp lines 533-544
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_r(this=self._handle, key=key, value=value)
    
    def _set_value_c(self, key, value):
        """
        _set_value_c(self, key, value)
        
        
        Defined at Dictionary.fpp lines 546-557
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : complex
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_c(this=self._handle, key=key, value=value)
    
    def _set_value_l(self, key, value):
        """
        _set_value_l(self, key, value)
        
        
        Defined at Dictionary.fpp lines 559-570
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : bool
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_l(this=self._handle, key=key, value=value)
    
    def _set_value_i_a(self, key, value):
        """
        _set_value_i_a(self, key, value)
        
        
        Defined at Dictionary.fpp lines 599-616
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_i_a(this=self._handle, key=key, value=value)
    
    def _set_value_r_a(self, key, value):
        """
        _set_value_r_a(self, key, value)
        
        
        Defined at Dictionary.fpp lines 618-635
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_r_a(this=self._handle, key=key, value=value)
    
    def _set_value_c_a(self, key, value):
        """
        _set_value_c_a(self, key, value)
        
        
        Defined at Dictionary.fpp lines 677-694
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : complex array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_c_a(this=self._handle, key=key, value=value)
    
    def _set_value_l_a(self, key, value):
        """
        _set_value_l_a(self, key, value)
        
        
        Defined at Dictionary.fpp lines 696-713
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : bool array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_l_a(this=self._handle, key=key, value=value)
    
    def _set_value_s(self, key, value):
        """
        _set_value_s(self, key, value)
        
        
        Defined at Dictionary.fpp lines 572-584
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : str
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_s(this=self._handle, key=key, value=value)
    
    def _set_value_s_a2(self, key, value):
        """
        _set_value_s_a2(self, key, value)
        
        
        Defined at Dictionary.fpp lines 739-757
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : str array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_s_a2(this=self._handle, key=key, value=value)
    
    def _set_value_s_a(self, key, value):
        """
        _set_value_s_a(self, key, value)
        
        
        Defined at Dictionary.fpp lines 715-737
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : str array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_s_a(this=self._handle, key=key, value=value)
    
    def _set_value_d(self, key, value):
        """
        _set_value_d(self, key, value)
        
        
        Defined at Dictionary.fpp lines 759-771
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : Dictdata
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_d(this=self._handle, key=key, value=value._handle)
    
    def _set_value_i_a2(self, key, value):
        """
        _set_value_i_a2(self, key, value)
        
        
        Defined at Dictionary.fpp lines 637-655
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_i_a2(this=self._handle, key=key, value=value)
    
    def _set_value_r_a2(self, key, value):
        """
        _set_value_r_a2(self, key, value)
        
        
        Defined at Dictionary.fpp lines 657-675
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_r_a2(this=self._handle, key=key, value=value)
    
    def _set_value_dict(self, key, value):
        """
        _set_value_dict(self, key, value)
        
        
        Defined at Dictionary.fpp lines 773-786
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : Dictionary
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_dict(this=self._handle, key=key, value=value._handle)
    
    def set_value(*args, **kwargs):
        """
        set_value(*args, **kwargs)
        
        
        Defined at Dictionary.fpp lines 224-233
        
        Overloaded interface containing the following procedures:
          _set_value_none
          _set_value_i
          _set_value_r
          _set_value_c
          _set_value_l
          _set_value_i_a
          _set_value_r_a
          _set_value_c_a
          _set_value_l_a
          _set_value_s
          _set_value_s_a2
          _set_value_s_a
          _set_value_d
          _set_value_i_a2
          _set_value_r_a2
          _set_value_dict
        
        Set a value in a Dictionary
        """
        for proc in [Dictionary._set_value_none, Dictionary._set_value_i, Dictionary._set_value_r, Dictionary._set_value_c, \
            Dictionary._set_value_l, Dictionary._set_value_i_a, Dictionary._set_value_r_a, Dictionary._set_value_c_a, \
            Dictionary._set_value_l_a, Dictionary._set_value_s, Dictionary._set_value_s_a2, Dictionary._set_value_s_a, \
            Dictionary._set_value_d, Dictionary._set_value_i_a2, Dictionary._set_value_r_a2, Dictionary._set_value_dict]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    def _set_value_pointer_i(self, key, ptr):
        """
        _set_value_pointer_i(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1335-1349
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : int array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_i(this=self._handle, key=key, ptr=ptr)
    
    def _set_value_pointer_r(self, key, ptr):
        """
        _set_value_pointer_r(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1351-1365
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : float array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_r(this=self._handle, key=key, ptr=ptr)
    
    def _set_value_pointer_c(self, key, ptr):
        """
        _set_value_pointer_c(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1367-1381
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : complex array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_c(this=self._handle, key=key, ptr=ptr)
    
    def _set_value_pointer_l(self, key, ptr):
        """
        _set_value_pointer_l(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1383-1397
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : bool array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_l(this=self._handle, key=key, ptr=ptr)
    
    def _set_value_pointer_s(self, key, ptr):
        """
        _set_value_pointer_s(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1399-1414
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : str array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_s(this=self._handle, key=key, ptr=ptr)
    
    def _set_value_pointer_i2(self, key, ptr):
        """
        _set_value_pointer_i2(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1416-1431
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : int array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_i2(this=self._handle, key=key, ptr=ptr)
    
    def _set_value_pointer_r2(self, key, ptr):
        """
        _set_value_pointer_r2(self, key, ptr)
        
        
        Defined at Dictionary.fpp lines 1433-1448
        
        Parameters
        ----------
        this : Dictionary
        key : str
        ptr : float array
        
        """
        quippy._quippy.f90wrap_dictionary_set_value_pointer_r2(this=self._handle, key=key, ptr=ptr)
    
    def set_value_pointer(*args, **kwargs):
        """
        set_value_pointer(*args, **kwargs)
        
        
        Defined at Dictionary.fpp lines 236-243
        
        Overloaded interface containing the following procedures:
          _set_value_pointer_i
          _set_value_pointer_r
          _set_value_pointer_c
          _set_value_pointer_l
          _set_value_pointer_s
          _set_value_pointer_i2
          _set_value_pointer_r2
        
        """
        for proc in [Dictionary._set_value_pointer_i, Dictionary._set_value_pointer_r, Dictionary._set_value_pointer_c, \
            Dictionary._set_value_pointer_l, Dictionary._set_value_pointer_s, Dictionary._set_value_pointer_i2, \
            Dictionary._set_value_pointer_r2]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    def _get_value_i(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_i, v = _get_value_i(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 793-812
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_i : bool
        v : int
        
        """
        dictionary_get_value_i, v = quippy._quippy.f90wrap_dictionary_get_value_i(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_i, v
    
    def _get_value_r(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_r, v = _get_value_r(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 814-833
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_r : bool
        v : float
        
        """
        dictionary_get_value_r, v = quippy._quippy.f90wrap_dictionary_get_value_r(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_r, v
    
    def _get_value_c(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_c, v = _get_value_c(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 835-854
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_c : bool
        v : complex
        
        """
        dictionary_get_value_c, v = quippy._quippy.f90wrap_dictionary_get_value_c(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_c, v
    
    def _get_value_l(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_l, v = _get_value_l(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 856-875
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_l : bool
        v : bool
        
        """
        dictionary_get_value_l, v = quippy._quippy.f90wrap_dictionary_get_value_l(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_l, v
    
    def _get_value_i_a(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_i_a = _get_value_i_a(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 920-943
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : int array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_i_a : bool
        
        """
        dictionary_get_value_i_a = quippy._quippy.f90wrap_dictionary_get_value_i_a(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_i_a
    
    def _get_value_r_a(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_r_a = _get_value_r_a(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 945-968
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : float array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_r_a : bool
        
        """
        dictionary_get_value_r_a = quippy._quippy.f90wrap_dictionary_get_value_r_a(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_r_a
    
    def _get_value_c_a(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_c_a = _get_value_c_a(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 1022-1045
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : complex array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_c_a : bool
        
        """
        dictionary_get_value_c_a = quippy._quippy.f90wrap_dictionary_get_value_c_a(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_c_a
    
    def _get_value_l_a(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_l_a = _get_value_l_a(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 1047-1070
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : bool array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_l_a : bool
        
        """
        dictionary_get_value_l_a = quippy._quippy.f90wrap_dictionary_get_value_l_a(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_l_a
    
    def _get_value_s(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_s, v = _get_value_s(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 877-897
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_s : bool
        v : str
        
        """
        dictionary_get_value_s, v = quippy._quippy.f90wrap_dictionary_get_value_s(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_s, v
    
    def _get_value_s_a(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_s_a = _get_value_s_a(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 1072-1099
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : str array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_s_a : bool
        
        """
        dictionary_get_value_s_a = quippy._quippy.f90wrap_dictionary_get_value_s_a(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_s_a
    
    def _get_value_s_a2(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_s_a2 = _get_value_s_a2(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 1101-1124
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : str array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_s_a2 : bool
        
        """
        dictionary_get_value_s_a2 = quippy._quippy.f90wrap_dictionary_get_value_s_a2(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_s_a2
    
    def _get_value_d(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_d, v = _get_value_d(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 1126-1145
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_d : bool
        v : Dictdata
        
        """
        dictionary_get_value_d, v = quippy._quippy.f90wrap_dictionary_get_value_d(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        v = f90wrap.runtime.lookup_class("quippy.DictData").from_handle(v, alloc=True)
        return dictionary_get_value_d, v
    
    def _get_value_i_a2(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_i_a2 = _get_value_i_a2(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 970-994
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : int array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_i_a2 : bool
        
        """
        dictionary_get_value_i_a2 = quippy._quippy.f90wrap_dictionary_get_value_i_a2(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_i_a2
    
    def _get_value_r_a2(self, key, v, case_sensitive=None, i=None):
        """
        dictionary_get_value_r_a2 = _get_value_r_a2(self, key, v[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 996-1020
        
        Parameters
        ----------
        this : Dictionary
        key : str
        v : float array
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_r_a2 : bool
        
        """
        dictionary_get_value_r_a2 = quippy._quippy.f90wrap_dictionary_get_value_r_a2(this=self._handle, key=key, v=v, \
            case_sensitive=case_sensitive, i=i)
        return dictionary_get_value_r_a2
    
    def _get_value_dict(self, key, case_sensitive=None, i=None):
        """
        dictionary_get_value_dict, v = _get_value_dict(self, key[, case_sensitive, i])
        
        
        Defined at Dictionary.fpp lines 1147-1171
        
        Parameters
        ----------
        this : Dictionary
        key : str
        case_sensitive : bool
        i : int
        
        Returns
        -------
        dictionary_get_value_dict : bool
        v : Dictionary
        
        """
        dictionary_get_value_dict, v = quippy._quippy.f90wrap_dictionary_get_value_dict(this=self._handle, key=key, \
            case_sensitive=case_sensitive, i=i)
        v = f90wrap.runtime.lookup_class("quippy.Dictionary").from_handle(v, alloc=True)
        return dictionary_get_value_dict, v
    
    def get_value(*args, **kwargs):
        """
        get_value(*args, **kwargs)
        
        
        Defined at Dictionary.fpp lines 247-254
        
        Overloaded interface containing the following procedures:
          _get_value_i
          _get_value_r
          _get_value_c
          _get_value_l
          _get_value_i_a
          _get_value_r_a
          _get_value_c_a
          _get_value_l_a
          _get_value_s
          _get_value_s_a
          _get_value_s_a2
          _get_value_d
          _get_value_i_a2
          _get_value_r_a2
          _get_value_dict
        
        Get a value from a Dictionary
        """
        for proc in [Dictionary._get_value_i, Dictionary._get_value_r, Dictionary._get_value_c, Dictionary._get_value_l, \
            Dictionary._get_value_i_a, Dictionary._get_value_r_a, Dictionary._get_value_c_a, Dictionary._get_value_l_a, \
            Dictionary._get_value_s, Dictionary._get_value_s_a, Dictionary._get_value_s_a2, Dictionary._get_value_d, \
            Dictionary._get_value_i_a2, Dictionary._get_value_r_a2, Dictionary._get_value_dict]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    def _add_array_i(self, key, value, len_bn, overwrite=None):
        """
        _add_array_i(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1455-1477
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_i(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_r(self, key, value, len_bn, overwrite=None):
        """
        _add_array_r(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1479-1501
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_r(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_c(self, key, value, len_bn, overwrite=None):
        """
        _add_array_c(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1503-1525
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : complex
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_c(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_l(self, key, value, len_bn, overwrite=None):
        """
        _add_array_l(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1527-1549
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : bool
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_l(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_s(self, key, value, len2, overwrite=None):
        """
        _add_array_s(self, key, value, len2[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1551-1574
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : str
        len2 : int array
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_s(this=self._handle, key=key, value=value, len2=len2, overwrite=overwrite)
    
    def _add_array_i2(self, key, value, len2, overwrite=None):
        """
        _add_array_i2(self, key, value, len2[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1576-1599
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int
        len2 : int array
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_i2(this=self._handle, key=key, value=value, len2=len2, overwrite=overwrite)
    
    def _add_array_r2(self, key, value, len2, overwrite=None):
        """
        _add_array_r2(self, key, value, len2[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1601-1624
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float
        len2 : int array
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_r2(this=self._handle, key=key, value=value, len2=len2, overwrite=overwrite)
    
    def _add_array_i_a(self, key, value, len_bn, overwrite=None):
        """
        _add_array_i_a(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1626-1648
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int array
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_i_a(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_r_a(self, key, value, len_bn, overwrite=None):
        """
        _add_array_r_a(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1650-1672
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float array
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_r_a(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_c_a(self, key, value, len_bn, overwrite=None):
        """
        _add_array_c_a(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1674-1696
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : complex array
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_c_a(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_l_a(self, key, value, len_bn, overwrite=None):
        """
        _add_array_l_a(self, key, value, len_bn[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1698-1720
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : bool array
        len_bn : int
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_l_a(this=self._handle, key=key, value=value, len_bn=len_bn, \
            overwrite=overwrite)
    
    def _add_array_s_a(self, key, value, len2, overwrite=None):
        """
        _add_array_s_a(self, key, value, len2[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1722-1745
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : str array
        len2 : int array
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_s_a(this=self._handle, key=key, value=value, len2=len2, overwrite=overwrite)
    
    def _add_array_i2_a(self, key, value, len2, overwrite=None):
        """
        _add_array_i2_a(self, key, value, len2[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1747-1770
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : int array
        len2 : int array
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_i2_a(this=self._handle, key=key, value=value, len2=len2, \
            overwrite=overwrite)
    
    def _add_array_r2_a(self, key, value, len2, overwrite=None):
        """
        _add_array_r2_a(self, key, value, len2[, overwrite])
        
        
        Defined at Dictionary.fpp lines 1772-1795
        
        Parameters
        ----------
        this : Dictionary
        key : str
        value : float array
        len2 : int array
        overwrite : bool
        
        """
        quippy._quippy.f90wrap_dictionary_add_array_r2_a(this=self._handle, key=key, value=value, len2=len2, \
            overwrite=overwrite)
    
    def add_array(*args, **kwargs):
        """
        add_array(*args, **kwargs)
        
        
        Defined at Dictionary.fpp lines 268-282
        
        Overloaded interface containing the following procedures:
          _add_array_i
          _add_array_r
          _add_array_c
          _add_array_l
          _add_array_s
          _add_array_i2
          _add_array_r2
          _add_array_i_a
          _add_array_r_a
          _add_array_c_a
          _add_array_l_a
          _add_array_s_a
          _add_array_i2_a
          _add_array_r2_a
        
        """
        for proc in [Dictionary._add_array_i, Dictionary._add_array_r, Dictionary._add_array_c, Dictionary._add_array_l, \
            Dictionary._add_array_s, Dictionary._add_array_i2, Dictionary._add_array_r2, Dictionary._add_array_i_a, \
            Dictionary._add_array_r_a, Dictionary._add_array_c_a, Dictionary._add_array_l_a, Dictionary._add_array_s_a, \
            Dictionary._add_array_i2_a, Dictionary._add_array_r2_a]:
            try:
                return proc(*args, **kwargs)
            except TypeError:
                continue
        
    
    @property
    def n(self):
        """
        Element n ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 193
        
        number of entries in use
        """
        return quippy._quippy.f90wrap_dictionary__get__n(self._handle)
    
    @n.setter
    def n(self, n):
        quippy._quippy.f90wrap_dictionary__set__n(self._handle, n)
    
    def init_array_entries(self):
        self.entries = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        quippy._quippy.f90wrap_dictionary__array_getitem__entries,
                                        quippy._quippy.f90wrap_dictionary__array_setitem__entries,
                                        quippy._quippy.f90wrap_dictionary__array_len__entries,
                                        """
        Element entries ftype=type(dictentry) pytype=Dictentry
        
        
        Defined at Dictionary.fpp line 195
        
        array of entries
        """, DictEntry)
        return self.entries
    
    @property
    def cache_invalid(self):
        """
        Element cache_invalid ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 196
        
        non-zero on exit from set_value(), set_value_pointer(), add_array(), remove_entry() if any array memory locations \
            changed
        """
        return quippy._quippy.f90wrap_dictionary__get__cache_invalid(self._handle)
    
    @cache_invalid.setter
    def cache_invalid(self, cache_invalid):
        quippy._quippy.f90wrap_dictionary__set__cache_invalid(self._handle, cache_invalid)
    
    @property
    def key_cache_invalid(self):
        """
        Element key_cache_invalid ftype=integer  pytype=int
        
        
        Defined at Dictionary.fpp line 197
        
        non-zero on exit from set_value(), set_value_pointer(), add_array(), remove_entry() if any keys changed
        """
        return quippy._quippy.f90wrap_dictionary__get__key_cache_invalid(self._handle)
    
    @key_cache_invalid.setter
    def key_cache_invalid(self, key_cache_invalid):
        quippy._quippy.f90wrap_dictionary__set__key_cache_invalid(self._handle, key_cache_invalid)
    
    def __str__(self):
        ret = ['<dictionary>{\n']
        ret.append('    n : ')
        ret.append(repr(self.n))
        ret.append(',\n    cache_invalid : ')
        ret.append(repr(self.cache_invalid))
        ret.append(',\n    key_cache_invalid : ')
        ret.append(repr(self.key_cache_invalid))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = [init_array_entries]
    

@f90wrap.runtime.register_class("quippy.c_dictionary_ptr_type")
class c_dictionary_ptr_type(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=c_dictionary_ptr_type)
    
    
    Defined at Dictionary.fpp lines 200-201
    
    """
    def __init__(self, handle=None):
        """
        self = C_Dictionary_Ptr_Type()
        
        
        Defined at Dictionary.fpp lines 200-201
        
        
        Returns
        -------
        this : C_Dictionary_Ptr_Type
        	Object to be constructed
        
        
        Automatically generated constructor for c_dictionary_ptr_type
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = quippy._quippy.f90wrap_c_dictionary_ptr_type_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class C_Dictionary_Ptr_Type
        
        
        Defined at Dictionary.fpp lines 200-201
        
        Parameters
        ----------
        this : C_Dictionary_Ptr_Type
        	Object to be destructed
        
        
        Automatically generated destructor for c_dictionary_ptr_type
        """
        if self._alloc:
            quippy._quippy.f90wrap_c_dictionary_ptr_type_finalise(this=self._handle)
    
    @property
    def p(self):
        """
        Element p ftype=type(dictionary) pytype=Dictionary
        
        
        Defined at Dictionary.fpp line 201
        
        """
        p_handle = quippy._quippy.f90wrap_c_dictionary_ptr_type__get__p(self._handle)
        if tuple(p_handle) in self._objs:
            p = self._objs[tuple(p_handle)]
        else:
            p = Dictionary.from_handle(p_handle)
            self._objs[tuple(p_handle)] = p
        return p
    
    @p.setter
    def p(self, p):
        p = p._handle
        quippy._quippy.f90wrap_c_dictionary_ptr_type__set__p(self._handle, p)
    
    def __str__(self):
        ret = ['<c_dictionary_ptr_type>{\n']
        ret.append('    p : ')
        ret.append(repr(self.p))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

def get_t_none():
    """
    Element t_none ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_none()

T_NONE = get_t_none()

def get_t_integer():
    """
    Element t_integer ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_integer()

T_INTEGER = get_t_integer()

def get_t_real():
    """
    Element t_real ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_real()

T_REAL = get_t_real()

def get_t_complex():
    """
    Element t_complex ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_complex()

T_COMPLEX = get_t_complex()

def get_t_logical():
    """
    Element t_logical ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_logical()

T_LOGICAL = get_t_logical()

def get_t_integer_a():
    """
    Element t_integer_a ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_integer_a()

T_INTEGER_A = get_t_integer_a()

def get_t_real_a():
    """
    Element t_real_a ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_real_a()

T_REAL_A = get_t_real_a()

def get_t_complex_a():
    """
    Element t_complex_a ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_complex_a()

T_COMPLEX_A = get_t_complex_a()

def get_t_logical_a():
    """
    Element t_logical_a ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_logical_a()

T_LOGICAL_A = get_t_logical_a()

def get_t_char():
    """
    Element t_char ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_char()

T_CHAR = get_t_char()

def get_t_char_a():
    """
    Element t_char_a ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_char_a()

T_CHAR_A = get_t_char_a()

def get_t_data():
    """
    Element t_data ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_data()

T_DATA = get_t_data()

def get_t_integer_a2():
    """
    Element t_integer_a2 ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_integer_a2()

T_INTEGER_A2 = get_t_integer_a2()

def get_t_real_a2():
    """
    Element t_real_a2 ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_real_a2()

T_REAL_A2 = get_t_real_a2()

def get_t_dict():
    """
    Element t_dict ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 142
    
    OMIT
    """
    return quippy._quippy.f90wrap_dictionary_module__get__t_dict()

T_DICT = get_t_dict()

def get_property_int():
    """
    Element property_int ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 146
    
    """
    return quippy._quippy.f90wrap_dictionary_module__get__property_int()

PROPERTY_INT = get_property_int()

def get_property_real():
    """
    Element property_real ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 146
    
    """
    return quippy._quippy.f90wrap_dictionary_module__get__property_real()

PROPERTY_REAL = get_property_real()

def get_property_str():
    """
    Element property_str ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 146
    
    """
    return quippy._quippy.f90wrap_dictionary_module__get__property_str()

PROPERTY_STR = get_property_str()

def get_property_logical():
    """
    Element property_logical ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 146
    
    """
    return quippy._quippy.f90wrap_dictionary_module__get__property_logical()

PROPERTY_LOGICAL = get_property_logical()

def get_c_key_len():
    """
    Element c_key_len ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 148
    
    """
    return quippy._quippy.f90wrap_dictionary_module__get__c_key_len()

C_KEY_LEN = get_c_key_len()

def get_string_length():
    """
    Element string_length ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 149
    
    Maximum string length
    """
    return quippy._quippy.f90wrap_dictionary_module__get__string_length()

STRING_LENGTH = get_string_length()

def get_dict_n_fields():
    """
    Element dict_n_fields ftype=integer pytype=int
    
    
    Defined at Dictionary.fpp line 150
    
    Maximum number of fields during parsing
    """
    return quippy._quippy.f90wrap_dictionary_module__get__dict_n_fields()

DICT_N_FIELDS = get_dict_n_fields()


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "dictionary_module".')

for func in _dt_array_initialisers:
    func()
