"""Python module for running PTM on an Asap list of atoms.

This module runs Polyhedral Template Matching on an Atoms object from ASE/Asap.
It requires that both ASE and Asap are installed.

This module can also be used as inspiration for how to use Polyhedral Template
Matching in other codes.

"""

import asap3
from asap3.Internal.Subject import Subject
import numpy as np
import sys

def PTM(atoms, cutoff=10.0, rmsd_max=None, **kwargs):
    """Run Complex Hull Analysis on an Atoms object.

    Parameters:
    atoms: The atoms object

    cutoff: A cutoff used for the neighborlist.  Must be large enough that all
        nearest neighbors are returned (second-nearest for BCC).  Using a too
        large value may impact performance, but not results.
        
    rmsd_max=None: If set, matches with a RMSD above this threshold are 
        reclassified as unknown structure (type 0).
        
        This is done as post-processing, and is completely equivalent to
            data['structure'][data['rmsd'] > rmsd_max] = 0

    target_structures=None: A tuple of structures to be investigated.
        It defaults to ('sc', 'fcc', 'hcp', 'ico', 'bcc').
        It MUST be a tuple, not a list or other sequence (bug?).
    
    calculate_strains=False: Set to True to calculate strains.

    quick=False: Set to True to skip topological ordering of neighbors.
        It gives a factor of two in speed, but more misclassified atoms at
        high temperatures.

    return_nblist=False:
        Return the NeighborList object used internally. This may be used for
        preprocessing. Do not enable unless you need it, as this object can
        use a lot of memory.

    return_mappings=None:
        Return the mapping of neighbors to the template used internally.
        Set to True to get mappings for all structures, or a tuple of
        structures to get for some (see target_structures).
         
    Returns:
    A dictionary with NumPy arrays as values.
    Each of these are a NumPy array of the same length as the number of atoms.
    
    Key names and descriptions of returned data.  In the description, i is the
    first index of the array and identifies the atom.
    
    'structure': The local crystal structure around atom i, if any.
        0 = none; 1 = SC; 2 = FCC; 3 = HCP; 4 = Icosahedral; 5 = BCC.

    'alloytype': The alloy structure identified.
        0 = unidentified; 1 = pure element; 2 = L1_0;
        3 = L1_2 majority atom; 4 = L1_2 minority atom.
        (0 is returned if structure != 2 or if no known alloy structure
        is recognized)

    'rmsd': The RMSD error in the fitting to the template, or INF if
        no structure was identified.

    'scale': The average distance to the nearest neighbors for
        structures 1-4; or the average distance to nearest and
        next-nearest neighbors for structure 5 (BCC); or INF if no
        structure was identified.

    'orientation': The orientation of the crystal lattice, expressed as a
        unit quaternion.  If no structure was found, the illegal
        value (0, 0, 0, 0) is returned.

    'strain' (only present if calculate_strains=True).  The strain
        tensor as a symmetric 3x3 matrix.  The trace of the matrix is
        1.0, since a hydrostatic component of the strain cannot be
        determined without a-priori knowledge of the reference
        lattice parameter.  If such knowledge is available, the
        hydrostatic component of the strain can be calculated from
        scales[i].
         
    'info': A tuple of two integers, the number of atoms analyzed by PTM
        and the number of atoms skipped due to insufficient neighbors.

    'nblist': (only if return_nblist is True) A neighbor list object.

    """
    for argument in ('target_structures', 'return_mappings'):
        if argument in kwargs:
            # The C++ code only accepts tuples of bytes (str in Python 2),
            # we need more flexibility.
            structs = kwargs[argument]
            if structs is None:
                continue
            if isinstance(structs, tuple):
                structs = list(structs)  # Make mutable
            for i, s in enumerate(structs):
                if isinstance(s, str):
                    structs[i] = s.encode()  # Convert to bytes
            kwargs[argument] = tuple(structs)
    data = asap3._asap.PTM_allatoms(atoms, cutoff, **kwargs)
    if rmsd_max:
        data['structure'][data['rmsd'] > rmsd_max] = 0
    return data

class PTMobserver(Subject):
    """Polyhedral Template Matching observer object.

    Per default, sets the tags of the atoms according to their local crystal
    structure.  0 = none; 1 = FCC; 2 = HCP; 3 = BCC; 4 = Icosahedral; 5 = SC.
        
    An optional argument `quantity` can be set to 'alloytype' or None, then
    the tags are set to the alloytype calculated by the PTM function (see 
    that function's documentation); or not set if None is given.
    
    This class is intended to use as an observer, so its analyze()
    function is called automatically by e.g. the dynamics.  It can
    itself act as a subject, so a Plotter or a Trajectory can be
    called just after the calculations.
    
    It has a method get_data which returns the full dictionary of PTM
    data from the last calculation.

    Parameters:
    atoms: The atoms object

    cutoff: A cutoff used for the neighborlist.  Must be large enough that all
        nearest neighbors are returned (second-nearest for BCC).  Using a too
        large value may impact performance, but not results.
        
    rmsd_max=None: If set, matches with a RMSD above this threshold are 
        reclassified as unknown structure (type 0).
        
        This is done as post-processing, and is completely equivalent to
            data['structure'][data['rmsd'] > rmsd_max] = 0

    target_structures=None: A tuple of structures to be investigated.
        It defaults to ('sc', 'fcc', 'hcp', 'ico', 'bcc').
        It MUST be a tuple, not a list or other sequence (bug?).
    
    calculate_strains=False: Set to True to calculate strains.

    quick=False: Set to True to skip topological ordering of neighbors.
        It gives a factor of two in speed, but more misclassified atoms at
        high temperatures.

    quantity='structure': The quantity used to set the tags.
    
    analyze_first=True: Should an analysis be made as soon as
        this object is created?  Leave as true if you plan to attach a
        Trajectory as an observer to this object, and if the
        Trajectory will save the initial state.
    """
    def __init__(self, atoms, cutoff=10.0, rmsd_max=None, target_structures=None, 
                 calculate_strains=False, quick=False, quantity='structure',
                 analyze_first=True):
        Subject.__init__(self)
        self.atoms = atoms
        self.cutoff = cutoff
        self.rmsd_max = rmsd_max
        self.target_structures = target_structures
        self.strains = calculate_strains
        self.quick = quick
        self.quantity = quantity
        if analyze_first:
            self.analyze()  # There will not be any observers yet.
        
    def analyze(self):
        "Runs the PTM analysis."
        self.data = PTM(self.atoms, cutoff=self.cutoff, rmsd_max=self.rmsd_max, 
                        target_structures=self.target_structures,
                        calculate_strains=self.strains,
                        quick=self.quick)
        if self.quantity:
            self.atoms.set_tags(self.data[self.quantity])
        self.call_observers()
        
    update = analyze
    
    def get_data(self):
        return self.data
    
    
class PTMdislocations(PTMobserver):
    """Polyhedral Template Matching observer object.

    Sets the tags of the atoms according to their local crystal
    structure, after postprocessing of the HCP atoms for
    dislocation detection.  The dislocation detection assumes
    that the majority of the system is in the FCC structure.

    Tags are set to 0 = none; 1 = FCC; 2 = HCP; 3 = BCC;
    4 = Icosahedral; 5 = SC; 6 = Twin boundary;
    7 = Stacking fault; 8 = Partial dislocation line.
   
    Otherwise, this object is like the PTMobserver, refer
    to it for further documentation and parameters (with the
    exception that the ``structure`` parameter is ignored).
    """
    # For HCP atoms, which neighbors are in the same basal plane, and
    # which are in the planes above and below?  The neighbors are located
    # like this.
    #
    #  (x) Basal plane atom         [y] Atom in plane above
    #
    #                      (7)
    #
    #
    #           (11)  [5]             (8)
    #
    #
    #                      (@)   [3]
    #
    #
    #           (12)  [1]             (9)
    #
    #
    #                      (10)
    #
    #   6 below 5; 4 below 3; 2 below 1.
    #   In this numbering, the central atom(@) is number 0, but that is not returned
    #   by the PTM code, so all indices must be one less than the number above.
    hcp_inplane = np.array((7, 8, 9, 10, 12, 11)) - 1
    hcp_above = np.array((5, 3, 1)) - 1
    hcp_below = np.array((6, 4, 2)) - 1
    def analyze(self):
        "Runs the PTM analysis."
        self.data = PTM(self.atoms, cutoff=self.cutoff, rmsd_max=self.rmsd_max, 
                        target_structures=self.target_structures,
                        calculate_strains=self.strains,
                        quick=self.quick, return_mappings=('hcp',))
        new_s = self.data['structure']
        s = np.array(new_s)  # A copy so we can change the original.
        mappings = self.data['mappings']
        hcpatoms = (s == 2).nonzero()[0]
        if getattr(self.atoms, "parallel", False):
            # Parallel simulation - we need to communicate the structures
            nghosts = len(self.atoms.ghosts['positions'])
            label = '_ptm_disloc_analysis_internal'
            self.atoms.arrays[label] = s
            self.atoms.ghosts[label] = np.zeros(nghosts, dtype=s.dtype)
            del s # Suppress a warning from asap - no extra references are allowed
            self.atoms.calc.update_ghost_data(self.atoms)
            s = self.atoms.arrays[label]  # Restore s - same as before.
            ghost_structs = self.atoms.ghosts[label]
            del self.atoms.ghosts[label]
            del self.atoms.arrays[label]
            s = np.concatenate((s, ghost_structs))
        for i in hcpatoms:
            mapping = mappings[i]
            nhcp = 0
            nfcc = 0
            nbsum = np.zeros(3)
            # Atom types of the neighbors
            inplane = s[mapping[self.hcp_inplane]] == 2
            inplanesum = inplane.sum()
            above = s[mapping[self.hcp_above]] == 2
            abovesum = above.sum()
            below = s[mapping[self.hcp_below]] == 2
            belowsum = below.sum()
            fccsum = (s[mapping] == 1).sum()
            # Heuristic for finding typical structures of HCP atoms
            if inplanesum == 6 and abovesum == 0 and belowsum == 0:
                # A single basal plane of HCP atoms: Twin boundary
                new_s[i] = 6
            elif inplanesum == 6 and ((abovesum == 3 and belowsum == 0) or
                                      (abovesum == 0 and belowsum == 3)):
                # Looks like two parallel planes of HCP atoms: Stacking fault.
                new_s[i] = 7
            elif (3 <= inplanesum <= 5
                  and inplanesum + abovesum + belowsum + fccsum >= 11
                  and (bool(abovesum) ^ bool(belowsum))):
                # A partial basal plane, with a possibly partial plane either
                # above or below, but not both. At most one non-HCP/FCC atom.
                #
                # This could be the edge of a SF ribbon (i.e. a partial dislocation
                # core) if the atoms in the plane are on the same side.  Check that
                # there are only two boundaries between HCP and non-HCP atoms
                rolled = np.roll(inplane, 1)
                if np.logical_xor(inplane, rolled).sum() == 2:
                    new_s[i] = 8
        # Kill the mappings dictionary to save memory
        del mappings, self.data['mappings']
        self.atoms.set_tags(new_s)
        self.atoms.set_array("rmsd", self.data['rmsd'])
        self.call_observers()
        
    update = analyze
