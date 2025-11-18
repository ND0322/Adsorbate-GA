#!/usr/bin/env python3
"""
Smoke‐test for SafeMoveAdsorbate:
 - patches HH2→H2 factory
 - defines a SafeMoveAdsorbate that never passes `height`/`pattern` into MoveAdsorbate.__init__
 - adds H2, then safely “moves” it without crashing
"""

# 1) Global patch — must come BEFORE any acat.ga.adsorbate_operators import
import acat.build.action as action
from ase.build import molecule as ase_molecule

_orig = action.adsorbate_molecule
def _patched(name, *args, **kwargs):
    if str(name).upper() == "HH2":
        return ase_molecule("H2")
    return _orig(name, *args, **kwargs)
action.adsorbate_molecule = _patched

# 2) Imports + SafeMoveAdsorbate
from acat.adsorption_sites               import ClusterAdsorptionSites
from acat.ga.adsorbate_operators         import AddAdsorbate, MoveAdsorbate
from ase.cluster                         import Icosahedron

class SafeMoveAdsorbate(MoveAdsorbate):
    def __init__(self, adsorbate_species, adsorption_sites, num_muts=1):
        # Only pass exactly what MoveAdsorbate expects
        super().__init__(
            adsorbate_species=adsorbate_species,
            adsorption_sites=adsorption_sites,
            num_muts=num_muts
        )
        # stash for fallback
        self._species = adsorbate_species
        self._ads_sites = adsorption_sites

    def get_new_individual(self, parents):
        try:
            return super().get_new_individual(parents)
        except ValueError as e:
            print("[SafeMoveAdsorbate] caught ValueError:", e)
            # fallback to a plain add
            add_op = AddAdsorbate(self._species,
                                  adsorption_sites=self._ads_sites,
                                  num_muts=1)
            offspring, desc = add_op.get_new_individual(parents)
            return offspring, f"SafeMoveFallback: {desc}"

# 3) Build a tiny test case
particle = Icosahedron('Ni', noshells=2)
particle.center(vacuum=5.0)
sas = ClusterAdsorptionSites(particle, composition_effect=False)

# ACAT needs info['data'] to exist
parents = [particle.copy(), particle.copy()]
for i, p in enumerate(parents):
    p.info.setdefault('data', {})
    p.info['confid'] = i

# 4) Add H2
add_op = AddAdsorbate(["H2"], adsorption_sites=sas, num_muts=1)
parent, desc1 = add_op.get_new_individual(parents)
print("After AddAdsorbate:   ", parent.get_chemical_formula(), "|", desc1)

# ensure the new parent also has data dict
parent.info.setdefault('data', {})
parent.info.setdefault('confid', 0)

# 5) Safe‐move H2
move_op = SafeMoveAdsorbate(["H2"], adsorption_sites=sas, num_muts=1)
offspring, desc2 = move_op.get_new_individual([parent, parent])
print("After SafeMoveAdsorbate:", offspring.get_chemical_formula(), "|", desc2)
