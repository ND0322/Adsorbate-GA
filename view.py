from ase.io import read
from ase.visualize import view

atoms = read("atoms.traj")   # defaults to last frame
view(atoms)
print(atoms)
