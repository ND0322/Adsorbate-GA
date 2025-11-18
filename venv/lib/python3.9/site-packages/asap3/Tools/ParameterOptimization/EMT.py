from math import pi, sqrt

from ase.data import atomic_numbers, reference_states, chemical_symbols

from asap3 import EMT, EMT2013
from asap3.Internal.EMTParameters import _std_emt_params

beta = (16.0 * pi / 3.0)**(1.0 / 3.0) / sqrt(2.0)

def EMTFit(elements, parameters):
    """Create an EMT object from a list (not dict!) of parameters."""
    #print "EMTFit called with:"
    #print "  elements =", elements
    #print "  parameters =", parameters
    parameternames = ['eta2', 'lambda', 'kappa', 'E0', 'V0', 'S0', 'n0']
    param = {}
    for k, v in parameters.items():
        if isinstance(k, tuple):
            k, k2 = k
            assert k == k2
        p = {}
        for name, value in zip(parameternames, v):
            p[name] = value
        # Check for resonable parameters
        #if p['eta2'] * 1.809 - p['kappa'] < 0.01:
        #    return None
        param[k] = p
    #print "  new parameters:", param
    return EMT(param)

def EMT2013Fit(elements, parameters, order='kappa'):
    """Create an EMT2013 object from a list (not dict!) of parameters."""
    #print "EMT2013Fit called with:"
    #print "  elements =", elements
    #print "  parameters =", parameters
    if order == 'kappa':
        parameternames = ['eta2', 'lambda', 'kappa', 'E0', 'V0', 'S0', 'n0']
    elif order == 'delta':
        parameternames = ['eta2', 'lambda', 'delta', 'E0', 'V0', 'S0', 'n0']
    else:
        raise ValueError('"order" must be either "kappa" or "delta"')
    limits = (('eta2', 0.1, 25.0),
              ('lambda', 0.1, 25.0),
              ('kappa', 0.2, 50.0),
              ('E0', -25, 0.0),
              ('V0', 0.0, 12.0),
              ('S0', 0.5, 5.0),
              ('n0', 0.0, 1.0))
    
    param = {'Calculator': "EMT2013_V1"}
    for k, v in parameters.items():
        if isinstance(k, tuple):
            k, k2 = k
            assert k == k2

        # Copy parameters
        p = {}
        if isinstance(v, dict):
            p = v.copy()
        else:
            p = dict(zip(parameternames, v))

        # Convert 'delta' to 'kappa'
        if order == 'delta':
            p['kappa'] = beta * p['eta2'] - p['delta']
            del p['delta']

        # Check for resonable parameters
        if beta * p['eta2'] - p['kappa'] < 0.01:
            raise ValueError(str(k) + ':  beta * eta2 - kappa < 0.01')
        for name, lower, higher in limits:
            if p[name] < lower or p[name] > higher:
                raise ValueError('%s(%s) = %.5f is not in [%.5f, %.5f]' 
                                 % (name, str(k), p[name], lower, higher))
        param[k] = p
    #print "  new parameters:", param
    return EMT2013(param)

EMT2011Fit = EMT2013Fit

def EMTStdParameters(z, order='kappa', guess=False, ecoh={}):
    """Get the standard EMT parameters, to be used as a starting guess for optimization.
    
    Parameters:
    z:  Atomic number or chemical symbol.
    order: Whether kappa or delta is on the list.  Default: kappa.
    guess: If true, values are guesstimated for unknown elements.
    ec: If guessing then E0 anc V0 can be based on cohesive energies from this dict.
        Keys are chemical symbols, values are cohesive energies in eV.
    
    Returns:
    A list of parameters in the order [eta2, lambda, kappa or delta, E0, V0, S0, n0].
    """
    if isinstance(z, str):
        z = atomic_numbers[z]

    parameternames = ['eta2', 'lambda', 'kappa', 'E0', 'V0', 'S0', 'n0']
    if z in _std_emt_params and guess != 'force':
        # Known in std EMT
        parameters = [_std_emt_params[z][x] for x in parameternames]
    elif guess:
        # eta2, lambda and kappa vary little amongst the elements, an not in a systematic way.
        # Use average values
        parameters = [3.07, 3.48, 5.14]
        # E0 and V0 can be estimated from the cohesive energy, if known
        try:
            ec = ecoh[chemical_symbols[z]]
        except KeyError:
            ec = 2.5
        parameters.append(-abs(ec))  # E0
        parameters.append(0.68 * abs(ec))  # V0
        # S0
        refstate = reference_states[z]
        if refstate['symmetry'] == 'fcc':
            a = refstate['a'] 
        elif refstate['symmetry'] == 'hcp':
            a = refstate['a'] * sqrt(2)
        else: 
            # Assume BCC.  If something else the BCC guess is probably better than nothing.
            a = refstate['a'] / (0.5**0.3333)
        parameters.append(a * 0.39)
        # n0  Guesstimate from inverse atomic volume.
        parameters.append(2.97 * a**(-3))
    else:
        raise RuntimeError(f"EMT parameters not known for Z={z} and guessing not allowed.")
    if order == 'delta':
        parameters[2] = beta * parameters[0] - parameters[2]

    return parameters

if __name__ == "__main__":
    # This script is an example of how to fit EMT parameters.
    import sys
    from asap3.Tools.ParameterOptimization import ParameterOptimization
    from asap3.Internal.EMTParameters import _std_emt_params
    from asap3.Tools.OptimizationDatabase import get_data

    initparameters = {('Cu','Cu'): EMTStdParameters('Cu')}

    varparameters = {('Cu','Cu'): [True, True, True, True, True, True, False]}

    # This should be generated semi-automatically
    fitquantities = [('lattice_constant_a', 'fcc', 'Cu', get_data('Cu', 'a'), 0.005),
                     ('cohesive_energy', 'fcc', 'Cu', get_data('Cu', 'Ecoh'), 0.01),
                     ('bulk_modulus', 'fcc', 'Cu', get_data('Cu', 'B'), 0.01),
                     ('elastic_constant_C11', 'fcc', 'Cu', get_data('Cu', 'C11'), 0.01),
                     ('elastic_constant_C12', 'fcc', 'Cu', get_data('Cu', 'C12'), 0.01),
                     ('elastic_constant_C44', 'fcc', 'Cu', get_data('Cu', 'C44'), 0.01),
                     ]

    # Initial guesses?
    latticeconstants = [['fcc', 'Cu', 4.00],  
                        ['bcc', 'Cu', 4.00]]

    opt = ParameterOptimization(['Cu'], EMT2013Fit, initparameters, varparameters,
                                fitquantities, latticeconstants, debug=False)
    (optparam, optvalues) = opt.fit(log=sys.stdout)

    print("Initial parameters:", initparameters)
    print("Optimal parameters:", optparam)
    #print ""
    #print "Fitting values", fitquantities
    #print "Optimal values", optvalues

