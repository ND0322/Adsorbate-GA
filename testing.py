import acat.build.action as action
from ase.build import molecule as ase_molecule


_orig_factory = action.adsorbate_molecule

def _patched_molecule(name, *args, **kwargs):

    if str(name).upper() == "HH2":
        return ase_molecule("H2")

    return _orig_factory(name, *args, **kwargs)
action.adsorbate_molecule = _patched_molecule

import acat.settings as settings
from acat.adsorption_sites import ClusterAdsorptionSites
from acat.adsorbate_coverage import ClusterAdsorbateCoverage
from acat.build.ordering import RandomOrderingGenerator as ROG
from acat.build.adlayer import min_dist_coverage_pattern
from acat.ga.adsorbate_operators import (AddAdsorbate, RemoveAdsorbate,
                                         MoveAdsorbate, ReplaceAdsorbate,
                                         SimpleCutSpliceCrossoverWithAdsorbates)

from acat.ga.particle_mutations import (RandomPermutation, COM2surfPermutation,
                                        Rich2poorPermutation, Poor2richPermutation)
from ase.visualize import view
from ase.ga.particle_comparator import NNMatComparator
from ase.ga.standard_comparators import SequentialComparator, StringComparator
from ase.ga.offspring_creator import OperationSelector
from ase.ga.population import Population, RankFitnessPopulation
from ase.ga.convergence import GenerationRepetitionConvergence
from ase.formula import Formula
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
import acat.build.action as action
from ase import Atoms
from ase.io import Trajectory
import traceback
from copy import deepcopy
import matplotlib.pyplot as plt
import math





class SafeMoveAdsorbate(MoveAdsorbate):
    def __init__(self, adsorbate_species, adsorption_sites, num_muts=1):
        super().__init__(
            adsorbate_species=adsorbate_species,
            adsorption_sites=adsorption_sites,
            num_muts=num_muts
        )
        self._species = adsorbate_species
        self._ads_sites = adsorption_sites

    def get_new_individual(self, parents):
        try:
            return super().get_new_individual(parents)
        except ValueError as e:
            print("[SafeMoveAdsorbate] caught ValueError:", e)
            add_op = AddAdsorbate(self._species,
                                  adsorption_sites=self._ads_sites,
                                  num_muts=1)
            offspring, desc = add_op.get_new_individual(parents)
            return offspring, f"SafeMoveFallback: {desc}"

def get_ads(atoms):
    """Returns a list of adsorbate names and corresponding indices."""
    if 'data' not in atoms.info:
        atoms.info['data'] = {'tag': None}
    if 'adsorbates' in atoms.info['data']:
        adsorbates = atoms.info['data']['adsorbates']
    else:
        cac = ClusterAdsorbateCoverage(atoms)
        adsorbates = cac.get_adsorbates()

    return adsorbates



def vf(atoms):
    """Returns the descriptor that distinguishes candidates in the
    niched population."""

    return len(get_ads(atoms))

def get_emt_calculator():
    """Returns a new instance of EMT calculator that can be pickled."""
    return EMT()

def remove_calculator(atoms):
    """Remove calculator from atoms to make it picklable."""
    atoms.calc = None
    return atoms

# Define the relax function
def relax(atoms, single_point=False):
    atoms.center(vacuum=5.)
    atoms.calc = get_emt_calculator()
    if not single_point:
        opt = BFGS(atoms, logfile=None)
        opt.run(fmax=0.1)

    Epot = atoms.get_potential_energy()
    num_H = len([s for s in atoms.symbols if s == 'H'])
    num_C = len([s for s in atoms.symbols if s == 'C'])
    num_O = len([s for s in atoms.symbols if s == 'O'])
    mutot = num_C * chem_pots['CH4'] + num_O * chem_pots['H2O'] + (
            num_H - 4 * num_C - 2 * num_O) * chem_pots['H2'] / 2
    f = -(Epot - mutot)

    atoms.info['key_value_pairs']['raw_score'] = f
    atoms.info['key_value_pairs']['potential_energy'] = Epot

    # Parallelize nnmat calculations to accelerate NNMatComparator
    atoms.info['data']['nnmat'] = get_nnmat(atoms)

    return remove_calculator(atoms)

#Relax starting generation
def relax_an_unrelaxed_candidate(atoms):
    if 'data' not in atoms.info:
        atoms.info['data'] = {'tag': None}
    nncomp = atoms.get_chemical_formula(mode='hill')
    print('Relaxing ' + nncomp)

    return relax(atoms, single_point=True) # Single point only for testing

def procreation(x):
    # Select an operator and use it
    op = op_selector.get_operator()

    while True:
        # Assign rng with a random seed
        np.random.seed(randint(1, 10000))
        pop.rng = np.random
        # Select parents for a new candidate
        p1, p2 = pop.get_two_candidates()
        parents = [p1, p2]
        # Pure or bare nanoparticles are not considered
        if len(set(p1.numbers)) < 3:
            continue
        op = op_selector.get_operator()

        
        offspring, desc = op.get_new_individual(parents)
       
        # An operator could return None if an offspring cannot be formed
        # by the chosen parents
        if offspring is not None:
            break
    nncomp = offspring.get_chemical_formula(mode='hill')
    print('Relaxing ' + nncomp)
    if 'data' not in offspring.info:
        offspring.info['data'] = {'tag': None}

    return relax(offspring, single_point=True) # Single point only for testing


# Define population
# Recommend to choose a number that is a multiple of the number of cpu
pop_size = 50


particle = Icosahedron('Ni', noshells=4)
particle.center(vacuum=5.)

#Platinium and Nickel 

# Generate random coverage on each nanoparticle
#CO, H, H2, CO2
species = ["H", "H2","CO", "CO2"]




 


# Get the adsorption sites. Composition does not affect GA operations
sas = ClusterAdsorptionSites(particle, composition_effect=False)

# Instantiate the db
db_name = os.path.abspath('ridge_Ni110Pt37_ads.db')

# Connect to the db
db = DataConnection(db_name)

# Define operators

soclist = ([1, 1, 2, 1, 1, 1, 1, 2],
           [Rich2poorPermutation(elements=['Ni', 'Pt'], num_muts=5),
            Poor2richPermutation(elements=['Ni', 'Pt'], num_muts=5),
            RandomPermutation(elements=['Ni', 'Pt'], num_muts=5),
            AddAdsorbate(species, adsorption_sites=sas, num_muts=5),
            RemoveAdsorbate(species, adsorption_sites=sas, num_muts=5),
            SafeMoveAdsorbate(species, adsorption_sites=sas, num_muts=5),
            ReplaceAdsorbate(species, adsorption_sites=sas, num_muts=5),
            SimpleCutSpliceCrossoverWithAdsorbates(species, keep_composition=True,
                                                   adsorption_sites=sas),])

op_selector = OperationSelector(*soclist)


# Define comparators
comp = SequentialComparator([StringComparator('potential_energy'),
                             NNMatComparator(0.2, ['Ni', 'Pt'])],
                            [0.5, 0.5])



# Give fittest candidates at different coverages equal fitness.
# Use this to find global minimum at each adsorbate coverage
pop = RankFitnessPopulation(data_connection=db,
                            population_size=pop_size,
                            comparator=comp,
                            variable_function=vf,
                            exp_function=True,
                            logfile='log.txt')

# Normal fitness ranking irrespective of adsorabte coverage
#pop = Population(data_connection=db,
#                 population_size=pop_size,
#                 comparator=comp,
#                 logfile='log.txt')

# Set convergence criteria
cc = GenerationRepetitionConvergence(pop, 5)

# Calculate chemical potentials
chem_pots = {'CH4': -24.039, 'H2O': -14.169, 'H2': -6.989}

traj = Trajectory(os.path.abspath("atoms.traj"), 'w')
if __name__ == '__main__':

    pool = Pool(os.cpu_count())
    # Perform relaxations in parallel. Especially
    # useful when running GA on large nanoparticles
    chig = db.get_all_unrelaxed_candidates()
    relaxed_candidates = pool.map(relax_an_unrelaxed_candidate,
    chig)
    pool.close()
    pool.join()

    f_gen1 = -1e5
    atoms_gen1 = None

    for atoms in relaxed_candidates:
        if atoms is None:
            continue
        f = atoms.info['key_value_pairs']['raw_score']
        if f > f_gen1:
            f_gen1 = f
            atoms_gen1 = atoms
    f_gm = [f_gen1]
    atoms_gm = [atoms_gen1]

   

    with open( os.path.abspath("fitness.txt", "w"))as file:
        file.write(str(f_gen1) + "\n")

    traj.write(atoms_gen1)
    #write("atoms.xyz", atoms_gen1, append=True)


    db.add_more_relaxed_candidates(relaxed_candidates)
    pop.update()

    # Number of generations
    num_gens = 1000

    # Below is the iterative part of the algorithm
    gen_num = db.get_generation_number()
    for i in range(num_gens):
        # Check if converged
        if cc.converged():
            print('Converged')
            break
        print('Creating and evaluating generation {0}'.format(gen_num + i))
        
        pool = Pool(os.cpu_count())
        relaxed_candidates = pool.map(procreation, range(pop_size))
        pool.close()
        pool.join()

        f_gen = -1e5
        atoms_gen = None

        for atoms in relaxed_candidates:
            if atoms is None:
                continue
            f = atoms.info['key_value_pairs']['raw_score']
            if f > f_gen:
                f_gen = f
                atoms_gen = atoms
        f_gm.append(f_gen)
        atoms_gm.append(atoms_gen)

        with open( os.path.abspath("fitness.txt", "a")) as file:
            file.write(str(f_gen) + "\n")

        traj.write(atoms_gen)
        #write("atoms.xyz", atoms_gen, append=True)


        #x = list(range(gen_num + i + 2 - len(f_gm), gen_num + i + 2))
        #y = -np.array(f_gm)
        #plt.xticks(range(min(x), math.ceil(max(x)) + 1))
        #plt.xlabel('Generation')
        #plt.ylabel(r'Stability ($-f$)')
        #plt.plot(x, y, marker='.', markersize=10)
        #plt.show()
        db.add_more_relaxed_candidates(relaxed_candidates)

        pop.update()


        """
         # Create a multiprocessing Pool
        pool = Pool(os.cpu_count())
        # Perform procreations in parallel. Especially useful when
        # using adsorbate operators which requires site identification
        relaxed_candidates = pool.map(procreation, range(pop_size))
        pool.close()
        pool.join()
        db.add_more_relaxed_candidates(relaxed_candidates)

        # Update the population to allow new candidates to enter
        pop.update()
        """


        
"""
Final geometry
Energy System total 
Graph energy over generations 
CO2, H2
CuFeCr
On surface of periodic system or particles 

ase gui ridge_Ni110Pt37_ads.db
czMHrca-UELC
nohup conda run -n venv python3 ~/Adsorbate-GA/testing.py & 
"""

