from asap3 import FullNeighborList
import numpy as np
import collections

def findclusters(atoms, tag, cutoff, arrayname='cluster', tags=None,
                 returnclusters=False):
    """Find clusters of atoms with a given tag.

    Find connected clusters of atoms with a given tag.  Each cluster
    is assigned a cluster number starting with 0, the cluster numbers
    are assigned to an array named 'cluster' on the atoms.  The name
    of the array can be changed.

    In addition to setting the 'cluster' array on the atoms, the
    function returns a list of cluster sizes.

    If the returnclusters parameter is set to True, the function
    returns two objects: a list of cluster sizes, and a map mapping
    cluster sizes to lists of clusters; each such cluster is itself
    a list of atom indices.
    
    Parameters:

    atoms: The atoms to be analyzed.

    tag: The tag identifying interesting atoms.  atoms.get_tags() is
        used to read the tags from the atoms, and only atoms matching
        'tag' are considered in the clustering.  Set tag=None to
        consider all atoms (for a dense sample this gives a single
        cluster spanning the entire system).

    cutoff: The cutoff distance used to identify if two atoms are
        neighbors.

    arrayname='cluster': The name of the array on the atoms where the
        cluster ID is stored.  Changed to 'dislocation' by the
        dislocation module.

    tags=None: An array to be used as tags instead of atoms.get_tags().
        Ignored if tag=None.

    returnclusters=False: If True, the function also returns a dictionary
        mapping cluster sizes to lists of clusters.
    """
    if tag is None:
        # All atoms match
        tag = 1
        tags = np.ones(len(atoms), np.int8)
    if tags is None:
        tags = atoms.get_tags()
    # Find the interesting atoms
    interesting = np.nonzero(tags == tag)[0]
    # Assign all interesting atoms to cluster -1 (unassigned), and all
    # other atoms to cluster -2 (not considered)
    cluster = -2 * np.ones(len(atoms))
    cluster[interesting] = -1
    print(len(atoms))
    print(interesting.shape)
    print(cluster.shape)
    if returnclusters:
        clustermap = collections.defaultdict(list)
        
    # Loop over interesting atoms not assigned so far.  Use flood fill
    # to find their cluster
    neighborlist = FullNeighborList(cutoff, atoms, driftfactor=0.0)
    print("Neighbor list ready.")
    next_cluster = 0
    cluster_sizes = []
    # Loop over the indices of the interesting atoms
    for i in interesting:
        if cluster[i] == -1:
            # Not yet identified
            in_cluster = flood_fill(neighborlist, i, next_cluster, cluster)
            n = len(in_cluster)
            cluster_sizes.append(n)
            if returnclusters:
                clustermap[n].append(in_cluster)
            next_cluster += 1
            if (next_cluster % 10000 == 0):
                print("  cluster {}:  size = {},  longest = {},  remaining = {}".format(
                    next_cluster, n, max(cluster_sizes), (cluster == -1).sum()))
    if returnclusters:
        return cluster_sizes, clustermap
    else:
        return cluster_sizes

def flood_fill(nblist, idx, cluster_id, cluster_array):
    """Flood fill algorithm used to identify atoms in this cluster.

    Parameters:

    nblist: An up-to-date neighborlist.

    idx: The index of the starting atom in the cluster.

    cluster_id: The ID being assigned to atoms in this cluster.

    cluster_array: The IDs of all atoms.  Unassigned atoms have ID -1.
        This array is modified by the algorithm.

    Returns:

    A list of the atoms in the cluster.  In addition, cluster_array is
    modified.
    """
    assert(cluster_array[idx] == -1)
    cluster_array[idx] = cluster_id
    queue = collections.deque()
    queue.append(idx)
    n = 1   # We already have the first atom
    result = [idx]
    while queue:
        i = queue.popleft()
        for nb in nblist[i]:
            if cluster_array[nb] == -1:
                n += 1
                cluster_array[nb] = cluster_id
                result.append(nb)
                queue.append(nb)
    return result

    
if __name__ == '__main__':
    import sys
    import ase.io
    import matplotlib.pyplot as plt
    
    filename = sys.argv[1]
    if len(sys.argv) >= 3:
        frame = int(sys.argv[2])
    else:
        frame = -1
    print(f"Reading frame {frame} of {filename}")
    atoms = ase.io.read(filename, frame)
    cutoff = 3.615 * (1/np.sqrt(2) + 1) / 2
    print(f"Cutoff is {cutoff} A")
    data = findclusters(atoms, 8, cutoff)
    w_histo = np.bincount(data)
    w_histo *= np.arange(len(w_histo))
    w_histo = w_histo[:25]
    plt.bar(np.arange(len(w_histo)), w_histo)
    #plt.axis([0, 800, 0, 5000])
    plt.show()

    
