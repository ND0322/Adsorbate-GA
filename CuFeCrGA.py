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
from ase.optimize import LBFGS
from random import randint
from multiprocessing import Pool, set_start_method
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
import contextlib
import json

_orig_factory = action.adsorbate_molecule

def _patched_molecule(name, *args, **kwargs):

    if str(name).upper() == "HH2":
        return ase_molecule("H2")

    return _orig_factory(name, *args, **kwargs)
action.adsorbate_molecule = _patched_molecule

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
            return None

BASE_DIR = str(Path(__file__).resolve().parent)
MACE = None
with open(BASE_DIR + "/pots.json", "r") as f:
    chem_pots = json.load(f)

def getChemPot(formula, calc):
    mol = molecule(formula)
    mol.calc = calc

    mol.center(10.0)

    return mol.get_potential_energy()

def get_silent_mace():
    with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
        calc = mace_mp(model="medium", dispersion=True, default_dtype="float64", device="cuda")
        
    return calc


def init_worker(cp):
    warnings.filterwarnings("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore"
    logging.getLogger("mace").setLevel(logging.ERROR)
    logging.getLogger("e3nn").setLevel(logging.ERROR)

    global MACE, chem_pots
    chem_pots = cp
    if MACE is None:
        MACE = get_silent_mace()
            


# Define the relax function
def relax(atoms, single_point=False):
    atoms.center(vacuum=5.)
    atoms.calc = MACE
    if not single_point:
        opt = LBFGS(atoms, logfile=None)
        opt.run(fmax=0.05, steps = 200)

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
    print('Relaxing ' + nncomp, flush = True)

    return relax(atoms, single_point=False) # Single point only for testing



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

species = ["H2", "CO2", "H"]

sas = ClusterAdsorptionSites(particle, composition_effect=False)

db_name = BASE_DIR+"/clusters.db"


db = DataConnection(db_name)


soclist = ([1, 1, 2, 1, 1, 1, 1, 2],
           [Rich2poorPermutation(elements=['Cu', 'Fe', 'Cr'], num_muts=5),
            Poor2richPermutation(elements=['Cu', 'Fe', 'Cr'], num_muts=5),
            RandomPermutation(elements=['Cu', 'Fe', 'Cr'], num_muts=5),
            AddAdsorbate(species, adsorption_sites=sas, num_muts=5),
            RemoveAdsorbate(species, adsorption_sites=sas, num_muts=5),
            SafeMoveAdsorbate(species, adsorption_sites=sas, num_muts=5),
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
    print("Starting worker pool...", flush=True)

    set_start_method("spawn")

    
    pool = Pool(4, initializer=init_worker, initargs=(chem_pots,))

    cands = db.get_all_unrelaxed_candidates()

    if len(cands) > 0:
        relaxed_candidates = pool.map(relax_an_unrelaxed_candidate, cands)
        db.add_more_relaxed_candidates(relaxed_candidates)
        pop.update()

    pool.close()
    pool.join()

    num_gens = 1000

    gen_num = db.get_generation_number()

    for i in range(gen_num, num_gens):
        if cc.converged():
            print("Converged")
            break

        print("Creating and evaluating generation {0}".format(i))

        unrelaxed_candidates = []

        for _ in range(pop_size):
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
                    nncomp = offspring.get_chemical_formula(mode="hill")
                    print("Generating " + nncomp, flush=True)
                    unrelaxed_candidates.append(offspring)
                    break

        for cand in unrelaxed_candidates:
            if "data" not in cand.info:
                cand.info["data"] = {"tag": None}

        pool = Pool(4, initializer=init_worker, initargs=(chem_pots,))
        relaxed_candidates = pool.map(relax, unrelaxed_candidates)
        pool.close()
        pool.join()

        print("Done relaxing", flush=True)

        db.add_more_relaxed_candidates(relaxed_candidates)
        pop.update()

    



