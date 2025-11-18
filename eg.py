import acat.settings as settings
from acat.adsorption_sites import ClusterAdsorptionSites
from acat.adsorbate_coverage import ClusterAdsorbateCoverage
from acat.build.ordering import RandomOrderingGenerator as ROG
from acat.build.adlayer import min_dist_coverage_pattern
from acat.ga.adsorbate_operators import (AddAdsorbate, RemoveAdsorbate,
                                         MoveAdsorbate, ReplaceAdsorbate,
                                         SimpleCutSpliceCrossoverWithAdsorbates)
# Import particle_mutations from acat instead of ase to get the indexing-preserved version
from acat.ga.particle_mutations import (RandomPermutation, COM2surfPermutation,
                                        Rich2poorPermutation, Poor2richPermutation)
from ase.ga.particle_comparator import NNMatComparator
from ase.ga.standard_comparators import SequentialComparator, StringComparator
from ase.ga.offspring_creator import OperationSelector
from ase.ga.population import Population, RankFitnessPopulation
from ase.ga.convergence import GenerationRepetitionConvergence
from ase.ga.utilities import closest_distances_generator, get_nnmat
from ase.ga.data import DataConnection, PrepareDB
from ase.io import read, write
from ase.cluster import Icosahedron
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from collections import defaultdict
from random import uniform, randint
from multiprocessing import Pool
import numpy as np
import time
import os
from ase import Atoms

settings._original_adsorbate_molecule = settings.adsorbate_molecule

def patched_adsorbate_molecule(adsorbate):
    if adsorbate == 'HH2':
        ads = molecule("H2")
        ads.rotate(90, 'x')
        return ads
    else:
        return settings._original_adsorbate_molecule(adsorbate)


settings.adsorbate_molecule = patched_adsorbate_molecule

