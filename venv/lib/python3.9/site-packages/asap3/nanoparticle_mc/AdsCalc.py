import numpy as np
from asap3 import CoordinationNumbers
from ase import units
from .langmuirExpression import getCoverages,getEnergies


class adscalc:
	
	
	def __init__(self,calc,pressure=1E2,temperature=300,species = "AuCO", relax_calc=None):
		self.calc = calc
		self.relax_calc = relax_calc
		self.species = species
		self.pressure = float(pressure)
		self.temperature = float(temperature)
		
		self.covbyc = np.array(getCoverages(T=temperature,P=pressure,species = self.species)) #Once and for all since it is not system specific.
		
		self.ebyc=np.array(getEnergies(self.species))
		
		
		self.active = True
		
	def set_atoms(self,atoms):
		self.calc.set_atoms(atoms)
		
	
	
	def get_potential_energy(self,atoms):
		e = self.calc.get_potential_energy(atoms)
		if self.active:
			acoord = CoordinationNumbers(atoms) #Contains coordination indexed by atoms index.
			
			eret = self.ebyc[acoord]*self.covbyc[acoord]
			
			#Debug:
			#print "Coordinations:"+str(acoord)
			#print "return array:"+str(eret)
			e+= eret.sum()
		return e
		
	def use_adsorbates(self, active):
		self.active = active
		
	#Overrides needed to write to pickle trajectory!
	def get_forces(self,atmref):
		return self.calc.get_forces(atmref)
		
	def get_stress(self,atmref):
		return self.calc.get_stress(atmref)
		
	def get_neighborlist(self):
		return self.calc.get_neighborlist()

	def calculation_required(self, *args, **kwargs):
		return self.calc.calculation_required(*args, **kwargs)
