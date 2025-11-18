"""The ASAP version number is specified in this file.

This file sets the __version__ variable to ASAP's version number.
The variable is imported by the main Asap module.  Furthermore, this module
prints the version number when executed, this is used by the makefile.

The __ase_version_required__ variable specified the version of ASE this
version of Asap is designed to work with.  Some functionality may be broken
with earlier versions.  If newer versions break something it is a bug that
should be reported and fixed.
"""

__version__ = '3.13.6'
__ase_version_required__ = '3.23.0'


if __name__ == '__main__':
    print(__version__)
    
