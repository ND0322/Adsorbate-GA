"""asap3.analysis.cutcluster - cut out clusters of atoms based on certain conditions."""


from asap3.analysis.findcluster import findclusters
import ase.io
import os
import sys
import numpy as np

def cut_clusters_by_size(atoms, tag, cutoff, size, folder, environment=0,
                         environ_exclude=[1,]):
    """Find clusters of specific size, save to files.

    Find connected clusters (using asap3.analysis.findcluster.findclusters),
    pick the ones with a given size, and save them to a folder as Trajectory
    files.

    Parameters:

    atoms: The atoms to be analyzed.

    tag: The tag identifying interesting atoms.  atoms.get_tags() is
        used to read the tags from the atoms, and only atoms matching
        'tag' are considered in the clustering.  Set tag=None to
        consider all atoms (for a dense sample this gives a single
        cluster spanning the entire system).

    cutoff: The cutoff distance used to identify if two atoms are
        neighbors.

    size: The cluster size(s) picked out.  Either an integer, or a
        sequence of integers

    folder: The folder where the output is saved.

    environment=0.0: If a nonzero number is given, any atom within that
        range will be included in the cluster, unless the tag is in
        environ_exclude.

    environ_exclude=[1,]:  Atoms with these tags are not included in the
        environment.

    """
    _, clustermap = findclusters(atoms, tag, cutoff, returnclusters=True)
    if size not in clustermap:
        raise RuntimeError(f"No clusters of size {size} found.")
    os.mkdir(folder)
    for i, cluster in enumerate(clustermap[size]):
        cl_atoms = atoms[cluster]
        cl_atoms.set_pbc(False)
        cl_atoms.center(vacuum=1.0)
        assert len(cl_atoms) == size
        filename = os.path.join(folder, f"cluster_{size}_{i}.traj")
        ase.io.write(filename, cl_atoms)
        print("Wrote", filename)
        
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage:")
        print(" python -m asap3.analysis.cutcluster infile.bundle outfolder TAG SIZE")
        sys.exit(1)
    infile = sys.argv[1]
    folder = sys.argv[2]
    tag = int(sys.argv[3])
    size = int(sys.argv[4])
    cutoff = 3.615 * (1/np.sqrt(2) + 1) / 2
    atoms = ase.io.read(infile)
    cut_clusters_by_size(atoms, tag, cutoff, size, folder)
    
    
