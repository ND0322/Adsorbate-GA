#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Comparator objects based on graph theory."""
from ..adsorbate_coverage import ClusterAdsorbateCoverage
from ..adsorbate_coverage import SlabAdsorbateCoverage
from ..utilities import neighbor_shell_list, get_adj_matrix
from ase.atoms import Atoms
from copy import deepcopy
import networkx as nx
import numpy as np


class AdsorptionGraphComparator(object):
    """Compares the graph of adsorbate overlayer + surface atoms and 
    returns True if they are automorphic with node matches. Before checking 
    graph automorphism by color refinement, a cheap label match is used to 
    reject graphs that are impossible to be automorphic.

    Parameters
    ----------
    adsorption_sites : acat.adsorption_sites.ClusterAdsorptionSites object or acat.adsorption_sites.SlabAdsorptionSites object or the corresponding pickle file path
        Provide the acat built-in adsorption sites class to accelerate the 
        pattern generation. Make sure all the structures have the same 
        atom indexing. 

    composition_effect : bool, default True
        Whether to consider sites with different elemental compositions as 
        different sites. It is recommended to set composition_effet=False 
        for monometallics.

    subtract_heights : bool, default None
        A dictionary that contains the height to be subtracted from the
        bond length when allocating a type of site to an adsorbate.
        Default is to allocate the site that is closest to the adsorbate's
        binding atom without subtracting height. Useful for ensuring the
        allocated site for each adsorbate is consistent with the site to
        which the adsorbate was added.

    hmax : int, default 2
        Maximum number of iterations for color refinement.

    dmax : float, default 2.5
        The maximum bond length (in Angstrom) between an atom and its
        nearest site to be considered as the atom being bound to the site.

    dx : float, default 0.5
        Buffer to calculate nearest neighbor pairs.

    """

    def __init__(self, adsorption_sites,  
                 composition_effect=True,
                 subtract_heights=None,
                 hmax=2, dmax=2.5, dx=.5, **kwargs):
        
        self.adsorption_sites = adsorption_sites
        self.composition_effect = composition_effect
        self.subtract_heights = subtract_heights
        self.hmax = hmax
        self.dmax = dmax
        self.dx = dx
        self.kwargs = kwargs
        self.kwargs['return_adj_matrix'] = False
        self.comp = WLGraphComparator(hmax=self.hmax, dx=self.dx)

    def looks_like(self, a1, a2):
        sas = deepcopy(self.adsorption_sites)        
 
        if hasattr(sas, 'surface'):
            sas.update(a1, full_update=self.composition_effect)
            sac1 = SlabAdsorbateCoverage(a1, sas, subtract_heights=
                                         self.subtract_heights, 
                                         label_occupied_sites=True, 
                                         dmax=self.dmax)
            sas.update(a2, full_update=self.composition_effect)
            sac2 = SlabAdsorbateCoverage(a2, sas, subtract_heights=
                                         self.subtract_heights, 
                                         label_occupied_sites=True, 
                                         dmax=self.dmax)
        else:
            sas.update(a1, full_update=self.composition_effect)
            sac1 = ClusterAdsorbateCoverage(a1, sas, subtract_heights=
                                            self.subtract_heights, 
                                            label_occupied_sites=True,
                                            dmax=self.dmax)
            sas.update(a2, full_update=self.composition_effect)
            sac2 = ClusterAdsorbateCoverage(a2, sas, subtract_heights=
                                            self.subtract_heights, 
                                            label_occupied_sites=True,
                                            dmax=self.dmax)
        labs1 = sac1.get_occupied_labels(fragmentation=self.kwargs.get(
                                         'fragmentation', True))
        labs2 = sac2.get_occupied_labels(fragmentation=self.kwargs.get(
                                         'fragmentation', True))       
 
        if labs1 == labs2:
            G1 = sac1.get_graph(**self.kwargs)
            G2 = sac2.get_graph(**self.kwargs)
            if self.comp.looks_like(G1, G2):
                return True

        return False


class WLGraphComparator(object):
    """Compares two structures (or graphs) based on the Weisfeiler-Lehman 
    subtree kernel (color refinement), as described in N. Shervashidze et 
    al., Journal of Machine Learning Research 2011, 12, 2539–2561. This 
    serves as a scalable solver for checking graph automorphism of two 
    structures. 

    The graphs (nx.Graph objects) can be quite costly to obtain every time 
    a graph is required (and disk intensive if saved), thus it makes sense 
    to get the adjacency matrix along with e.g. the potential energy and 
    save it in atoms.info['data']['adj_matrix'].

    Parameters
    ----------
    hmax : int, default 2
        Maximum number of iterations for color refinement.

    dx : float, default 0.5
        Buffer to calculate nearest neighbor pairs.

    tol : float, default 1e-5
        Tolerance of the discrepancy between K12 and sqrt(K11*K22)

    """

    def __init__(self, hmax=2, dx=.5, tol=1e-5):
        self.hmax = hmax
        self.dx = dx
        self.tol = tol

    def looks_like(self, a1, a2):
        """a1, a2 can be eithr 2 ase.Atoms objects or 2 networkx graphs."""

        if isinstance(a1, Atoms) and isinstance(a2, Atoms):
            if ('data' in a1.info and 'adj_matrix' in a1.info['data']) and (
            'data' in a2.info and 'adj_matrix' in a2.info['data']):
                A1 = a1.info['data']['adj_matrix']
                G1 = nx.Graph(A1)
                A2 = a2.info['data']['adj_matrix']
                G2 = nx.Graph(A2)
            else:
                nblist1 = neighbor_shell_list(a1, dx=self.dx, neighbor_number=1,
                                              mic=(True in a1.pbc))
                A1 = get_adj_matrix(nblist1)
                G1 = nx.Graph(A1)
                nblist2 = neighbor_shell_list(a2, dx=self.dx, neighbor_number=1,
                                              mic=(True in a2.pbc))
                A2 = get_adj_matrix(nblist2)
                G2 = nx.Graph(A2)
            s1 = a1.symbols
            s2 = a2.symbols
        else:
            G1, G2 = a1, a2
            s1 = np.asarray([G1.nodes[n]['symbol'] for n in G1.nodes()], dtype=object)
            s2 = np.asarray([G2.nodes[n]['symbol'] for n in G2.nodes()], dtype=object)

        d1 = WLGraphComparator.get_label_dict(G1, s1, self.hmax, self.dx)
        d2 = WLGraphComparator.get_label_dict(G2, s2, self.hmax, self.dx)
        d12 = {k: [d[k] if k in d else 0 for d in (d1, d2)] 
               for k in set(d1.keys()) | set(d2.keys())}
        X12 = np.asarray(list(d12.values()))

        # Compute the inner products
        k11 = sum(v**2 for v in d1.values())
        k22 = sum(v**2 for v in d2.values())
        k12 = X12[:,0] @ X12[:,1].T

        return abs(k12 - (k11 * k22)**0.5) <= self.tol 

    @classmethod
    def get_label_dict(cls, G, symbols, hmax, dx):                                                        
        d = {}
        N = G.number_of_nodes()
        nnlabs, neighbors = {}, {}
        isolates = []
        for i in range(N):
            lab0 = str(symbols[i])
            if lab0 in d:
                d[lab0] += 1.
            else:
                d[lab0] = 1.
            if hmax > 0:
                nnd = nx.single_source_shortest_path_length(G, i, cutoff=1)
                nns = [j for j, v in nnd.items() if v == 1]
                neighbors[i] = nns
                if len(nns) == 0:
                    isolates.append(i)
                    continue
                sorted_symbols = sorted(symbols[nns])
                lab1 = lab0 + ':' + ','.join(sorted_symbols)
                nnlabs[i] = lab1
                if lab1 in d:
                    d[lab1] += 1 
                else:
                    d[lab1] = 1
        if hmax > 1: 
            for k in range(1, hmax):
                nnnlabs = {}
                for i in range(N):
                    if i in isolates:
                        continue
                    nnlab = nnlabs[i]
                    nnnlab = ','.join(sorted(nnlabs[nn] for nn in neighbors[i]))
                    lab = nnlab + ':' * (k + 1) + nnnlab
                    nnnlabs[i] = lab
                    if lab in d:
                        d[lab] += 1
                    else:
                        d[lab] = 1
                nnlabs = nnnlabs 

        return d
