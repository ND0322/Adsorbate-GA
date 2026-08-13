from ase.cluster import Octahedron
from acat.adsorption_sites import ClusterAdsorptionSites
from acat.adsorbate_coverage import ClusterAdsorbateCoverage
from acat.build import add_adsorbate_to_site

# 1. Build nanoparticle
atoms = Octahedron('Ni', length=5, cutoff=1)
atoms.center(vacuum=5.0)

# 2. Get adsorption sites
cas = ClusterAdsorptionSites(atoms, composition_effect=False)
sites = cas.get_sites()

# 3. Add H2 and atomic H on adjacent sites
add_adsorbate_to_site(atoms, adsorbate='H2', site=sites[0])
add_adsorbate_to_site(atoms, adsorbate='H', site=sites[1])

# 4. Pass adsorption_sites=cas explicitly to avoid the TypeError
cac = ClusterAdsorbateCoverage(atoms, adsorption_sites=cas)
adsorbates = cac.get_adsorbates()

print("Detected adsorbates:")
print(adsorbates)