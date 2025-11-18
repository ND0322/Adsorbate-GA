import resource
from asap3.mpi import world
import sys

if sys.platform == 'darwin':
    _memory_unit = 1   # Bytes
else:
    _memory_unit = 1024  # kB

_megabytes = 1024.0**2 / _memory_unit

def get_max_memory():
    """Return the max resident memory used by the process.

    It tries to return the value in MB, but this may fail on
    some platforms.
    """
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if world.size > 1:
        mem = world.sum(mem)
    return mem / _megabytes

