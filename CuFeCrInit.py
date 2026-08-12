from pathlib import Path
from ase.cluster import Icosahedron
from acat.build.ordering import RandomOrderingGenerator as ROG
from ase.io import read,write
from random import uniform
from acat.build.adlayer import min_dist_coverage_pattern
from acat.adsorption_sites import ClusterAdsorptionSites
from ase.ga.data import DataConnection, PrepareDB


BASE_DIR = Path(__file__).resolve().parent

#make it kill db if it already exists

path = BASE_DIR/"clusters.db"

if(path.is_file()):
    path.unlink()

pop_size = 48

particle = Icosahedron("Cu", noshells=4)

particle.center(vacuum=5.)

rog = ROG(particle, elements = ["Cu", "Fe", "Cr"],
            composition={'Cu': 0.435, 'Fe': 0.551, 'Cr': 0.014},
            trajectory='starting_generation.traj'
)

rog.run(num_gen=pop_size)


species = ['H2', 'CO2', "H"]

images = read("starting_generation.traj", index = ":")
patterns = []

for atoms in images:
    dmin = uniform(3.5, 8.5)
    pattern = min_dist_coverage_pattern(atoms, adsorbate_species=species, min_adsorbate_distance=dmin)
    patterns.append(pattern)


# Get the adsorption sites. Composition does not affect GA operations
sas = ClusterAdsorptionSites(particle, composition_effect=False)

# Instantiate the db

db_name = BASE_DIR/"clusters.db"

db = PrepareDB(db_name, cell=particle.cell, population_size=pop_size)

for atoms in patterns:
    if 'data' not in atoms.info:
        atoms.info['data'] = {'tag': None}

    db.add_unrelaxed_candidate(atoms, data=atoms.info['data'])




