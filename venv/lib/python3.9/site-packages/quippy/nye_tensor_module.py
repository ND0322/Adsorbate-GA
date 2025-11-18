"""
Module nye_tensor_module


Defined at nye_tensor.fpp lines 35-269

"""
from __future__ import print_function, absolute_import, division
import quippy._quippy
import f90wrap.runtime
import logging
import numpy

_arrays = {}
_objs = {}

def calc_nye_tensor(self, ref_lat, alpha, g=None):
    """
    calc_nye_tensor(self, ref_lat, alpha[, g])
    
    
    Defined at nye_tensor.fpp lines 44-135
    
    Parameters
    ----------
    at : Atoms
    ref_lat : Atoms
    alpha : float array
    g : float array
    
    """
    quippy._quippy.f90wrap_calc_nye_tensor(at=self._handle, ref_lat=ref_lat._handle, alpha=alpha, g=g)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "nye_tensor_module".')

for func in _dt_array_initialisers:
    func()
