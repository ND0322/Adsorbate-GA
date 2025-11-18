"""multidislocation - a module for setting up multiple dislocations."""


import itertools
import numpy as np

def fcc_slipsystems(withlines=False):
    """Return the different slip systems in FCC.

    Returns a list with the 12 slip systems.  Each system is
    a slip plane and a double Burgers vector.  The double of
    Burgers vector is used since that consists of integers.

    If the optional argument withlines is True, then each
    combination of a slip system and one of 6 possible
    dislocation line vectors are chosen, giving 72 "extended
    slip systems" instead.
    """
    # Four kinds of {111} planes
    planes111 = [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1)]
    # Find all possible <110> directions
    temp = (set(itertools.permutations((1,1,0)))
            | set(itertools.permutations((1,-1,0)))
            | set(itertools.permutations((-1,-1,0)))
            )
    # But keep only the ones where the first nonzero index is positive
    direct110 = [x for x in temp if x > (0,0,0)]
    direct110.sort()
    direct110_signed = [x for x in temp]
    direct110_signed.sort()
    
    slipsystems = []
    for plane in planes111:
        for direction in direct110:
            if np.dot(plane, direction) == 0:
                if not withlines:
                    # Just use the slip system
                    slipsystems.append((plane, direction))
                else:
                    # Loop over possible dislocation lines as well
                    for dislline in direct110_signed:
                        if np.dot(plane, dislline) == 0:
                            slipsystems.append((plane, direction, dislline))
    if withlines:
        assert len(slipsystems) == 72
    else:
        assert len(slipsystems) == 12
    return slipsystems

def random_in_sphere(radius):
    """Returns a random point inside sphere of a given radius."""
    while True:
        candidate = np.random.uniform(-1,1,3)
        if np.dot(candidate, candidate) < 1.0:
            return radius * candidate

def random_dislocations(radius, density, verbose=True):
    """Create a random collection of dislocations.

    The dislocations all pass through a sphere with a
    given radius (the first parameters, in Angstrom).

    The dislocation density inside the sphere is given
    by the second parameter (in SI units, i.e. m^-2).

    This function returns parameters for creating the dislocations:
    a list of (point on line, Burgers vector, direction).
    """
    # Convert the density to A^-2:
    density /= 1e20
    cross_section = np.pi * radius**2
    avg_num = density * cross_section
    actual_num = np.random.poisson(avg_num)
    if verbose:
        print("Average number of dislocations:", avg_num)
        print("Actual number of dislocations:", actual_num)
    slipsys = fcc_slipsystems(True)
    result = []
    for i in range(actual_num):
        point = random_in_sphere(radius)
        plane, burgers, line = slipsys[np.random.randint(len(slipsys))]
        result.append((point, 0.5*np.array(burgers), line))
    return result


if __name__ == "__main__":
    from ase.lattice.cubic import FaceCenteredCubic
    from asap3.setup.dislocation import Dislocation
    from asap3 import EMT
    from asap3.analysis import CNA
    from ase.io import write
    import ase.data
    
    metal = 29  # Copper
    a0 = ase.data.reference_states[metal]['a']
    system = FaceCenteredCubic(metal, size=(30,30,30), latticeconstant=a0)
    system.set_pbc(False)
    size = system.get_cell()[0,0]
    print(f"System size: {size} A;  Number of atoms: {len(system)}")
    center = 0.5 * size * np.ones(3)
    disloc = random_dislocations(size * np.sqrt(3), 3e16)
    field = None
    for point, burgers, line in disloc:
        print(point, burgers, line)
        new = Dislocation(point+center, line, a0 * burgers)
        if field is None:
            field = new
        else:
            field = field + new
    # Apply the field
    field.apply_to(system)
    write("disl.xyz", system)
    system.set_calculator(EMT())
    t = CNA(system)
    system.set_tags(t)
    write("disl.traj", system)
    sys2 = system[t != 0]
    write("disl2.traj", sys2)
    
    
        
        
