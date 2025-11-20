from acat.settings import adsorbate_elements
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
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from collections import defaultdict
from ase.visualize import view
from random import uniform, randint
from multiprocessing import Pool
import numpy as np
import time
from ase import Atoms
import os

# Define population
# Recommend to choose a number that is a multiple of the number of cpu
pop_size = 50

# Generate 50 icosahedral Ni110Pt37 nanoparticles with random orderings
particle = Icosahedron('Ni', noshells=4)
particle.center(vacuum=5.)
rog = ROG(particle, elements=['Ni', 'Pt'],
          composition={'Ni': 0.75, 'Pt': 0.25},
          trajectory='starting_generation.traj')
rog.run(num_gen=pop_size)

# Generate random coverage on each nanoparticle

#species = ['H', 'H2', 'CO', 'CO2']
species = ['H', 'C', 'O', 'OH', 'CO', 'CH', 'CH2', 'CH3']



images = read('starting_generation.traj', index=':')
patterns = []
for atoms in images:
    dmin = uniform(3.5, 8.5)
    pattern = min_dist_coverage_pattern(atoms, adsorbate_species=species,
                                        min_adsorbate_distance=dmin)
    patterns.append(pattern)

# Get the adsorption sites. Composition does not affect GA operations
sas = ClusterAdsorptionSites(particle, composition_effect=False)

# Instantiate the db
db_name = 'ridge_Ni110Pt37_ads.db'

db = PrepareDB(db_name, cell=particle.cell, population_size=pop_size)

for atoms in patterns:
    if 'data' not in atoms.info:
        atoms.info['data'] = {'tag': None}
    #view(atoms)
    db.add_unrelaxed_candidate(atoms, data=atoms.info['data'])

