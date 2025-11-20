from ase.io import read

atoms = read("atoms.traj")   # defaults to last frame
print(atoms)
