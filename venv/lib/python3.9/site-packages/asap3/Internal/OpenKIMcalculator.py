"""A calculator based on the OpenKIM project.

This module defines three object.

OpenKIMcalculator is a calculator class that interfaces to any OpenKIM V2 model.

OpenKIMparameters is a dictionary-like object that gives access to any
mutable parameters of the OpenKIM model, the object is created by
calling OpenKIMcalculator.get_parameters().

OpenKIMavailable is a function returning a list of available OpenKIM models.
"""

from ase.calculators.calculator import Calculator
from asap3 import _asap, AsapError
from asap3.Internal.ListOfElements import ListOfElements
from asap3.Internal.BuiltinPotentials import get_cell_heights, smallest_pbc_direction, AsapPotential
from ase.data import atomic_numbers, chemical_symbols
from ase.utils import basestring
import numpy as np
from copy import copy
import subprocess
import shutil
import os
from collections.abc import MutableMapping
import numbers

class OpenKIMcalculator(_asap.OpenKIMcalculator, AsapPotential):
    """A calculator interfacing to the OpenKIM models.
    
    Parameters:
    
    name: The long name of the KIM Model.
    
    Optional parameters:
    
    atoms:  If set, set_atoms is called immediately.  Default: no atoms set.
                           
    stress:  Set to False to refrain from calculate the global virial, even if the model
             supports it.  Default:  True (calculate global virial / stress).
             
    stresses: As above, but for atomic virials / stresses.
    
    verbose:  Set to True to print additional info during neigborlist matching.
    """
    def __init__(self, name, atoms=None,
                 stress=True, stresses=True, verbose=False):
        _asap.OpenKIMcalculator.__init__(self, name, verbose)
        self.kimname = name
        self.atoms = None
        self.support_stress = stress
        self.support_stresses = stresses
        self.verbose = verbose
        if atoms is not None:
            self.set_atoms(atoms)
            
    def set_atoms(self, atoms, *args):
        """Set the atoms belonging to this calculator.
        
        The function set_atoms(atoms) is defined in C++, and just calls this
        Python function.  This ensures that this Python function is called
        regardless of whether set_atoms() is called from C++ or Python.
        """
        # Inform the calculator about the translation from atomic numbers to particle types.
        self.z_to_typecode = {}
        elements = ListOfElements(atoms)
        for e in elements:
            symbol = chemical_symbols[e]
            try:
                code = self.get_type_code(chemical_symbols[e])
            except AsapError:
                raise RuntimeError("The OpenKIM model '%s' does not support element Z=%i (%s)."
                                   % (self.kimname, e, chemical_symbols[e]))
            self.z_to_typecode[e] = code
            if self.verbose:
                print("Translation: Z = %i -> id = %i" % (e, code))
        self.set_translation(self.z_to_typecode)

        # Check the compute arguments required by the Model.
        computearguments = self._get_compute_arguments()
        requiredargs = ['numberOfParticles', 'particleSpeciesCodes', 'particleContributing',
                        'coordinates', 'partialEnergy', 'partialForces', 'GetNeighborList']
        for a in requiredargs:
            if computearguments[a] == 'notSupported':
                raise AsapError(f"The OpenKIM model '{self.kimname}' does not support '{a}'")
            del computearguments[a]  # Processed
        self.supported_calculations = {}
        for k in ('partialEnergy', 'partialForces'):
            self.supported_calculations[k] = True
        
        # partialParticleEnergy is optional, but we will calculate it if possible
        arg = 'partialParticleEnergy'
        self.supported_calculations[arg] = computearguments[arg] != 'notSupported'
        del computearguments[arg]
        # partialVirial and partialParticleVirial are allocated if they are required by the model, or if
        # they are optional and stress is requested.
        arg = 'partialVirial'
        self.supported_calculations[arg] = (
            computearguments[arg] == 'required' or
            (self.support_stress and computearguments[arg] == 'optional'))
        del computearguments[arg]
        arg = 'partialParticleVirial'
        self.supported_calculations[arg] = (
            computearguments[arg] == 'required' or
            (self.support_stress and computearguments[arg] == 'optional'))
        del computearguments[arg]
        # Make sure that the model does not require something extra.
        for a, s in computearguments.items():
            if s == 'required' or s == 'requiredByAPI':
                raise RuntimeError("OpenKIM model '{}' requires parameter '{}' (status: '{}')".format(
                    self.name, a, s))
        
        # Inform the calculator about which quantities should be allocated and calculated.
        for k,v in self.supported_calculations.items():
            self.please_support(k, v)

        # Find out which neighborlist type we got.  Check sanity and if ImageAtoms should be used.
        pbc = atoms.get_pbc()
        if self.verbose:
            print(f"Activating Image atoms (pbc = {str(pbc)})")
        self._use_imageatoms()
        _asap.OpenKIMcalculator.set_atoms(self, atoms, *args)

    def get_supported_elements(self, user=True):
        """Get a list of supported elements (as chemical symbols).

        If the optional argument user=True (the default) then elements with
        names 'user01' to 'user20' may also be returned as supported.
        """
        supported = []
        candidates = chemical_symbols[1:]  # chemical_symbols[0] is 'X' and should be skipped.
        if user:
            candidates += [f'user{x:02d}' for x in range(1,21)]
        for element in candidates:
            try:
                self.get_type_code(element)
            except AsapError:
                pass
            else:
                supported.append(element)
        return supported
    
    def get_parameters(self, kind='free', integers=[]):
        """Get the parameters of the model as a dictionary.
        
        The optional parameter 'kind' specifies which kind of parameters you get.
        It can take three values:
        'free' (the default).  You only get the "free" parameters, i.e. those that
            can be changed.
        'fixed': You only get the fixed parameters.
        'all': You get both free and fixed parameters.

        The optional argument 'integers' is a list of parameter names that are
        defined as integers in the parameter file.  This should be detected
        automatically once the KIM API specification is updated.
        
        WARNING: Currently using any other value than 'free' is dangerous, as the
        fixed parameter may be of unexpected types.  Once type-checking of parameters
        appear in the KIM API, accessing the fixed parameters will become safe, and 
        the default will change to 'all'.
        
        NOTE: The prefix PARAM_FREE_ or PARAM_FIXED_ is removed from the parameter 
        names.  If kind=='all', free parameters may shadow fixed parameters of the 
        same name.
        """
        if kind not in ['free', 'fixed', 'all']:
            raise ValueError("get_parameters: kind must be 'free', 'fixed' or 'all'.")
        result = {}
        if kind == 'fixed' or kind == 'all':
            prf = 'PARAM_FIXED_'
            for name in self.get_fixed_parameter_names():
                assert name.startswith(prf)
                shortname = name[len(prf):]
                if shortname in integers or name in integers:
                    value = self._get_parameter(name, is_integer=True)
                else:
                    value = self._get_parameter(name)
                result[shortname] = value
        if kind == 'free' or kind == 'all':
            prf = 'PARAM_FREE_'
            for name in self.get_free_parameter_names():
                assert name.startswith(prf)
                shortname = name[len(prf):]
                if shortname in integers or name in integers:
                    value = self._get_parameter(name, is_integer=True)
                else:
                    value = self._get_parameter(name)
                result[shortname] = value
        return result
    
    def set_parameters(self, **kwargs):
        """Set the free parameters of an OpenKIM model.
        
        Examples (these three are equivalent):
        
        model.set_parameters(cutoff = 3.7)
        
        model.set_parameters(PARAM_FREE_cutoff = 3.7)
        
        pars = {'cutoff': 3.7}
        model.set_parameters(**pars)
        
        Note that prefixing the parameter name with PARAM_FREE_ is optional.
        
        If a bad parameter specification is given, and this function fails,
        the model will be left in an undefined state.  That can be fixed by
        calling this function again, possibly without parameters.
        """
        prefix = 'PARAM_FREE_'
        allowed = self.get_free_parameter_names()
        for key, value in kwargs.items():
            if key.startswith(prefix):
                realkey = key
            else:
                realkey = prefix+key
            if realkey not in allowed:
                raise TypeError(f"Got an unexpected parameter name '{key}'")
            if isinstance(value, float):
                self._set_parameter_scalar(realkey, value)
            elif isinstance(value, np.ndarray):
                self._set_parameter_array(realkey, value)
            else:
                raise TypeError("Unsupported value type - must be float or numpy array.")
        self._reinit()

    def get_name(self):
        return "asap3.OpenKIMcalculator(" + self.kimname + ")"

    def _get_parameters(self):
        return OpenKIMparameters(self)
    
    name = property(get_name, doc="Name of the potential")

    parameters = property(_get_parameters, doc="Published parameters of the OpenKIM model")

class OpenKIMparameters(MutableMapping):
    def __init__(self, model):
        self.model = model
        self.parameters = {}
        self.descriptions = {}
        for i, (name, typecode, size, description) in enumerate(model._get_parameter_names_types()):
            self.parameters[name] = (i, typecode, size)
            self.descriptions[name] = description

    def __len__(self):
        return len(self.parameters)

    def __getitem__(self, key):
        return self.model._get_parameter(*self.parameters[key])

    def __setitem__(self, key, value):
        index = self.parameters[key][0]
        if isinstance(value, numbers.Number):
            # A scalar
            self.model._set_parameter(index, value)
        else:
            # An array - flatten it.
            self.model._set_parameter(index, np.ravel(value)) 

    def __delitem__(self, key):
        raise RuntimeError("Cannot delete a parameter from an OpenKIM model.")
    
    def __iter__(self):
        yield from self.parameters
        
    def get_parameter(self, key, shape=None):
        p = self[key]
        if shape is None:
            return p
        elif isinstance(shape, tuple):
            return p.reshape(shape)
        shape = shape.lower()
        if shape == "square":
            size = int(np.round(np.sqrt(len(p))))
            if size*size == len(p):
                return p.reshape((size,size))
            else:
                raise ValueError(f"Cannot return parameter as a square matrix, its length is {len(p)}")
        if shape == "upper triangular":
            shape = "ut"
        elif shape == "lower triangular":
            shape = "lt"
        if shape == "ut" or shape == "lt":
            size =  int(np.floor(np.sqrt(2*len(p))))
            if size * (size + 1) // 2 == len(p):
                result = np.zeros((size, size), dtype=p.dtype)
                if shape == "ut":
                    idx = np.triu_indices(size)
                else:
                    idx = np.tril_indices(size)
                result[idx] = p
                return result
            else:
                raise ValueError(f"Cannot return parameter as a triangular matrix ({shape}), its length is {len(p)}")
        else:
            raise ValueError("Unknown shape "+shape)
        
    def set_parameter(self, key, value, shape=None):
        if shape is None:
            self[key] = value
            return
        if len(value.shape) != 2 or value.shape[0] != value.shape[1]:
            raise ValueError("All supported shapes assume a square matrix")
        shape = shape.lower()
        if shape == "square":
            self[key] = value  # Flattened in __setitem__
        elif shape == "ut" or shape == "upper triangular":
            idx = np.triu_indices(len(value))
            self[key] = value[idx]
        elif shape == "lt" or shape == "lower triangular":
            idx = np.tril_indices(len(value))
            self[key] = value[idx]


def _get_openkim_model_string(verbose):
    exename = "kim-api-collections-info"
    args = ' portable_models'
    sistername = 'kim-api-collections-management'

    # First try if the program is on the path.
    try:
        modelstring = subprocess.check_output(exename+args, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        return modelstring
    except subprocess.CalledProcessError:
        pass

    # Then look for it using pkg-config
    exepath = None
    try:
        prefix = subprocess.check_output("pkg-config libkim-api --variable=libexecdir", shell=True).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        pass
    else:
        exepath = os.path.join(prefix, 'kim-api', exename)
        if verbose:
            print("Found using pkg-config:", exepath)

    # Finally, try to look for where kim-api-collections-management and then check ../libexec
    if not exepath and hasattr(shutil, 'which'):
        management = shutil.which(sistername)
        if management:
            prefix = os.path.dirname(os.path.dirname(management))
            exepath = os.path.join(prefix, 'libexec', 'kim-api', exename)
            if verbose:
                print("Found relative to", sistername, ":", exepath)
    if not exepath:
        raise RuntimeError("Cannot locate "+exename+" to generate list of KIM models.")

    if not os.access(exepath, os.R_OK):
        raise RuntimeError("Executable should be at "+exepath+" but is absent or not usable.")

    try:
        modelstring = subprocess.check_output(exepath+args, shell=True).decode('utf-8')
        return modelstring
    except subprocess.CalledProcessError:
        raise RuntimeError("Running "+exepath+" failed.")


def OpenKIMavailable(verbose=0):
    """Get the list of installed OpenKIM models.

    The list is obtained by locating and running the command line tool
    kim-api-collections-info
    """
    modelstring = _get_openkim_model_string(verbose)
    models = []
    for line in modelstring.split('\n'):
        if line:
            models.append(line.split()[1])
    return models


if __name__ == '__main__':
    from ase.lattice.cubic import FaceCenteredCubic
    atoms = FaceCenteredCubic(size=(10,10,10), symbol='Cu')
    print("Creating calculator")
    pot = OpenKIMcalculator('EMT_Asap_Standard_AlAgAuCuNiPdPt__MO_118428466217_000')
    print("Setting atoms")
    atoms.set_calculator(pot)
    print("Calculating energy")
    print(atoms.get_potential_energy())
    print(atoms.get_forces()[10:])
    print(atoms.get_stress())

