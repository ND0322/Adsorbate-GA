from acat.adsorption_sites import ClusterAdsorptionSites
from acat.adsorbate_coverage import ClusterAdsorbateCoverage
import acat.build.action as action
from ase.build import molecule as ase_molecule
from acat.ga.particle_mutations import (RandomPermutation, COM2surfPermutation,
                                        Rich2poorPermutation, Poor2richPermutation)
from acat.ga.adsorbate_operators import (AddAdsorbate, RemoveAdsorbate,
                                         MoveAdsorbate, ReplaceAdsorbate,
                                         SimpleCutSpliceCrossoverWithAdsorbates)
from ase.ga.particle_comparator import NNMatComparator
from ase.ga.standard_comparators import SequentialComparator, StringComparator
from ase.ga.offspring_creator import OperationSelector
from ase.ga.population import Population, RankFitnessPopulation
from ase.ga.convergence import GenerationRepetitionConvergence
from ase.ga.utilities import get_nnmat
from ase.ga.data import DataConnection
from ase.ga.convergence import GenerationRepetitionConvergence
from ase.cluster import Icosahedron
from ase.optimize import BFGS
from random import randint
from multiprocessing import Pool
import numpy as np
import os
from pathlib import Path
import acat.build.action as action
from ase.io import Trajectory
from mace.calculators import mace_mp
from ase.build import molecule
import logging
import warnings
import sys





BASE_DIR = str(Path(__file__).resolve().parent)
MACE = None

def init_worker():
    warnings.filterwarnings("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore"
    logging.getLogger("mace").setLevel(logging.ERROR)
    logging.getLogger("e3nn").setLevel(logging.ERROR)

    global MACE
    if MACE is None:
        
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        
        try:
            MACE = mace_mp(model="medium", dispersion=True, default_dtype="float64", device="cpu")
        finally:
            sys.stdout.close()
            sys.stdout = old_stdout
            

def getChemPot(formula):
    mol = molecule(formula)
    mol.calc = MACE

    mol.center(10.0)

    return mol.get_potential_energy()

chem_pots = {"H2" : getChemPot("H2"), "CO2" : getChemPot("CO2")}




# Define the relax function
def relax(atoms, single_point=False):
    atoms.center(vacuum=5.)
    atoms.calc = MACE
    if not single_point:
        opt = BFGS(atoms, logfile=None)
        opt.run(fmax=0.05)

    Epot = atoms.get_potential_energy()
    num_H = len([s for s in atoms.symbols if s == 'H'])
    num_C = len([s for s in atoms.symbols if s == 'C'])
    num_O = len([s for s in atoms.symbols if s == 'O'])
    mutot = (
        num_C * chem_pots['CO2'] 
        + (num_O - 2 * num_C) * (chem_pots['CO2'] / 2.0) 
        + (num_H / 2.0) * chem_pots['H2']
    )

    f = -(Epot - mutot)

    atoms.info['key_value_pairs']['raw_score'] = f
    atoms.info['key_value_pairs']['potential_energy'] = Epot
    atoms.info['data']['nnmat'] = get_nnmat(atoms)

    atoms.calc = None
    return atoms

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


pop_size = 48

particle = Icosahedron("Cu", noshells=4)
particle.center(vacuum=5.)

species = ["H2", "CO2"]

sas = ClusterAdsorptionSites(particle, composition_effect=False)

db_name = BASE_DIR+"/clusters.db"


db = DataConnection(db_name)


soclist = ([1, 1, 2, 1, 1, 1, 1, 2],
           [Rich2poorPermutation(elements=['Cu', 'Fe', 'Cr'], num_muts=5),
            Poor2richPermutation(elements=['Cu', 'Fe', 'Cr'], num_muts=5),
            RandomPermutation(elements=['Cu', 'Fe', 'Cr'], num_muts=5),
            AddAdsorbate(species, adsorption_sites=sas, num_muts=5),
            RemoveAdsorbate(species, adsorption_sites=sas, num_muts=5),
            MoveAdsorbate(species, adsorption_sites=sas, num_muts=5),
            ReplaceAdsorbate(species, adsorption_sites=sas, num_muts=5),
            SimpleCutSpliceCrossoverWithAdsorbates(species, keep_composition=True,
                                                   adsorption_sites=sas),])

op_selector = OperationSelector(*soclist)

comp = SequentialComparator([StringComparator('raw_score'),
                             NNMatComparator(0.2, ['Cu', 'Fe', 'Cr'])],
                            [0.5, 0.5])

pop = RankFitnessPopulation(data_connection=db,
                            population_size=pop_size,
                            comparator=comp,
                            variable_function=vf,
                            exp_function=True,
                            logfile='log.txt')


cc = GenerationRepetitionConvergence(pop, 5)
traj = Trajectory(BASE_DIR + "/atoms.traj", 'w')


if __name__ == "__main__":

    
    pool = Pool(processes = os.cpu_count(), initializer=init_worker())

    cands = db.get_all_unrelaxed_candidates()

    relaxed_candidates = pool.map(relax_an_unrelaxed_candidate, cands)

    pool.close()
    pool.join()
    db.add_more_relaxed_candidates(relaxed_candidates)
    pop.update()

    num_gens = 1000

    gen_num = db.get_generation_number()

    for i in range(num_gens):
        if(cc.converged()):
            print("Converged")
            break

        print('Creating and evaluating generation {0}'.format(gen_num + i))

        pool = Pool(os.cpu_count())
        relaxed_candidates = pool.map(procreation, range(pop_size))
        pool.close()
        pool.join()

        db.add_more_relaxed_candidates(relaxed_candidates)
        pop.update()

    



