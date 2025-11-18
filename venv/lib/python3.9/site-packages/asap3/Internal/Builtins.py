"""Asap builtin objects.

This module loads the modules from the compiled parts of Asap.  It
chooses between the parallel and serial version based on whether MPI
is active at runtime.
"""

__docformat__ = "restructuredtext en"

import sys

# Now import the relevant C module
import _asap
        
parallelpossible = hasattr(_asap, "Communicator")
AsapError = _asap.AsapError
get_version = _asap.get_version
get_short_version = _asap.get_short_version
timing_results = _asap.timing_results

def set_verbose(v):
    """Set the verbosity level of asap."""
    _asap.verbose = v
    
