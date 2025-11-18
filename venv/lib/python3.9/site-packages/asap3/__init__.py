# Copyright (C) 2004-2011 Jakob Schiotz and Center for Individual
# Nanoparticle Functionality, Department of Physics, Technical
# University of Denmark.  Email: schiotz@fysik.dtu.dk
#
# This file is part of Asap version 3.
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 3 as published by the Free Software Foundation.  Permission
# to use other versions of the GNU Lesser General Public License may
# granted by Jakob Schiotz or the head of department of the
# Department of Physics, Technical University of Denmark, as
# described in section 14 of the GNU General Public License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# and the GNU Lesser Public License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.

"""The Asap module.

The following **classes** are defined in this module:

`ListOfAtoms`: A list of atoms object used for the simulations.

`ParallelAtoms`: A parallel version of `ListOfAtoms`.  Only defined if
parallel simulations are possible.  Should not be created directly,
use `MakeParallelAtoms`.

`EMT`: The Effective Medium Theory potential.

`MonteCarloEMT`: EMT potential with optimizations for Monte Carlo simulations.

`MoPotential`: An experimental molybdenum potential.

`LennardJones`: Calculator using Lennard-Jones potential.

`Morse`: Calculator using Morse potential.

`BrennerPotential`: Calculates the Brenner potential.

The following **functions** are defined:

`Verbose`: Changes the verbosity level of the C code.

`CNA`: Runs Common Neighbor Analysis on a (Parallel)ListOfAtoms object.

`CoordinationNumber`: Calculates coordination numbers for the atoms
in a (Parallel)ListOfAtoms object.

`MakeParallelAtoms`: A factory function creating a ParallelAtoms
object safely.  Only defined if parallel simulations are possible.

This module detects if parallel simulations are possible, and then
loads the serial or the parallel version of the C module into memory.
If parallel simulations are possible, a Python exit function is set,
so MPI is shut down if one of the processes exits.

*Note on the automatic documentation*: Most of the classes mentioned
above are not listed below.  This is because the way epydoc_ works
interacts badly with the structure of these modules.  Click on
class/function name above to see the documentation.

.. _epydoc: http://epydoc.sf.net
"""


__docformat__ = "restructuredtext en"

import sys, os
from asap3.version import __version__
from asap3.Internal.Builtins import _asap, parallelpossible, AsapError, set_verbose
from asap3.Internal.UtilityFunctions import print_version, get_version, \
     get_short_version, DebugOutput, memory_usage, print_memory
from asap3.Internal.BuiltinPotentials import EMT, MonteCarloEMT, \
     EMTParameters, EMTDefaultParameters, EMTRasmussenParameters, \
     LennardJones, BrennerPotential, Morse, EMT2013, EMT2011, RGL, Gupta, \
     RahmanStillingerLemberg, MetalOxideInterface, MetalOxideInterface2
from asap3.Internal.EMTParameters import EMTStandardParameters, \
     EMThcpParameters, EMTMetalGlassParameters
from asap3.Internal.Threads import AsapThreads
from asap3.Internal.MonteCarloAtoms import MonteCarloAtoms
from asap3.Internal.checkversion import check_version
from asap3.io.trajectory import Trajectory
from asap3.io.bundletrajectory import BundleTrajectory
from asap3.md.verlet import VelocityVerlet
from asap3.md.langevin import Langevin
from asap3.md import MDLogger
    
if parallelpossible:
    from asap3.Internal.ParallelListOfAtoms import ParallelAtoms, \
        MakeParallelAtoms
    from asap3.Internal.Collector import Collector
    from ase.parallel import paropen

# OpenKIM may or may not be built into Asap
from asap3.Internal.BuiltinPotentials import OpenKIMsupported
if OpenKIMsupported:
    from asap3.Internal.OpenKIMcalculator import OpenKIMcalculator, OpenKIMavailable

import ase
from ase import Atoms
from ase.visualize import view
import ase.units as units
# from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

try:
    from ase.calculators.calculator import PropertyNotImplementedError
except ImportError:
    # ASE version 3.12 or earlier.
    class PropertyNotImplementedError(NotImplementedError):
        pass

NeighborList = _asap.NeighborList
NeighborCellLocator = _asap.NeighborCellLocator
FullNeighborList = _asap.FullNeighborList
heap_mallinfo = _asap.heap_mallinfo

# Check Asap installation for consistency
check_version()

# Check that a modern ASE is used in parallel simulations
#
# Due to a change in ASEs build system, older ASEs will not detect
# that ASAP is running in parallel, and ase.parallel will not work.
if parallelpossible:
    import asap3.mpi
    import ase.parallel
    if asap3.mpi.world.size != ase.parallel.world.size:
        print(asap3.mpi.world.size, ase.parallel.world.size)
        raise ImportError("Asap requires ASE version 3.22.0 or updated developer installation.")
    
