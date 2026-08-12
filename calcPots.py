from mace.calculators import mace_mp
from ase.build import molecule
import json

def getChemPot(formula, calc):
    mol = molecule(formula)
    mol.calc = calc

    mol.center(10.0)

    return mol.get_potential_energy()

calc = mace_mp(model="medium", dispersion=True, default_dtype="float64", device="cuda")

pots = {"H2" : getChemPot("H2", calc), "CO2" : getChemPot("CO2", calc), "H" : getChemPot("H", calc)}
s = json.dumps(pots)

with open("pots.json", "w") as f:
    f.write(s)