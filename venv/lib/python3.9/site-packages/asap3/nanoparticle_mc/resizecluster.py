from asap3 import CoordinationNumbers
import numpy as np
from asap3.MonteCarlo.Moves import SurfaceMove
from ase import Atom
import random as rd
#1.1 Now removes 1 atom at a time.
def mychoice(a, n):
	#Could be obsolete now.
	"Replaces numpy.random.choice(a, n, False) as our numpy is ancient."
	a = list(a)
	while len(a) > n:
		# Remove a random element
		del a[np.random.randint(len(a))]
	return np.array(a)

def resizecluster(atoms, nwanted):
	print("Resizing Cluster 1 atom at a time")
	nactual = len(atoms)
	if nactual == nwanted:
		return
	elif nactual > nwanted:
		removeatoms(atoms, nactual - nwanted)		
	else:
		addatoms(atoms, nwanted - nactual)
		
def removeatoms(atoms, n):
	"Remove n atoms from the cluster."
	for i in range(n):
		# We still have atoms to remove
		# Find the ones with lowest coordination number
		coords = CoordinationNumbers(atoms)
		coordination = coords.min()
		idx = np.arange(len(atoms))
		candidates = idx[np.equal(coords, coordination)]
		# candidates now contains the indices of the atoms with
		# low coordination number
		atom_delete = np.random.randint(len(candidates))
		del atoms[candidates[atom_delete]]

def addatoms(atoms,n):
	element = atoms[0].symbol
	SM = SurfaceMove()
	
	for i in range(n):
		SM.set_atoms(atoms)
		idx = SM.vacant_indexes()
		#Find the n highest coordinated sites(this is in ids of SM)
		coords = SM.vacant_coordinations[idx]
		candidates = idx[np.equal(coords,coords.max())]
		vacPos = SM.vacant_positions
		chosenID = np.random.randint(len(candidates)) #Random ids
		#print "Adding atom at site", id1
		atoms.append(Atom(element, position=vacPos[chosenID]))
		
		
def objarraysize(arr): #Outputs the size of array objects of arrays
	out = 0
	for i in range(0,arr.size):
		out+=arr[i].size
	return out
