from ase.lattice.cubic import FaceCenteredCubic, BodyCenteredCubic
from . import quat_utils
import numpy as np
import itertools

# DELAYED IMPORTS (may not always be available):
#
# scipy.spatial
# matplotlib
# mpl_toolkits



def random_rotations(ngrains):
    """Return random grain rotations for all grains.

    Parameters:
    grains:  The number of grains.

    Returns:
    A list of 3*3 rotation matrices taken from a uniform distribution of
    rotations.
    """
    return [quat_utils.random_rotation_matrix() for i in range(ngrains)]


def bcc_grains(gridsize, perturbation=0.0):
    """Creates a grain layout based on a perturbed BCC lattice.

    Creates a set of grain centers in scaled space (i.e. with coordinates
    between 0.0 and 1.0), based on a regular BCC lattice, possibly with a
    random perturbation added.

    Parameters:
    gridsize: Size of the BCC lattice in lattice units.  Either an integer,
    or a tuple of three integers.

    perturbation: If non-zero, all grain centers are perturbed by a random
    amount drawn from a normal distribution with this spread.

    Returns:
    A N*3 numpy array of grain centers.
    """
    graincenters = BodyCenteredCubic(symbol='H', latticeconstant=1.0, size=grainsize)
    graincenters = graincenters.get_positions() + 0.25
    graincenters /= grainsize
    pert = np.random.standard_normal(graincenters.shape) * perturbation
    graincenters += pert
    return graincenters

###
### OPTIMIZING VORONOI TESSELATIONS.
###

def lloyd_step(centers, box, resolution=20, alpha=1.0, verbose=True):
    """A single step of Lloyd's algorithm towards a centroid Voronoi tesselation.

    See https://en.wikipedia.org/wiki/Lloyds_algorithm
    
    Parameters:
    centers: List of Voronoi centers (generators).  N*3 numpy array.
    
    box: Three numbers, giving the size of the computational box (PBC!)
    
    resolution: Use 2**resolution points in the Monte Carlo
        evaluation of the centroids.
        
    alpha: Acceleration factor in Lloyd's algorithm.  Values slightly below 2
        are supposedly good.  The default (1.0) gives slow convergence.
    
    Returns:
    Updated Voronoi centers (same shape as centers parameter).
    """
    npoints = len(centers)
    assert centers.shape == (npoints, 3)
    box = np.array(box)
    assert box.shape == (3,)
    
    # Generate the periodic images
    generators = periodic_images(centers, box)
    assert generators.shape == (27*npoints, 3)
    
    # Generate random point distribution
    randsize = (1 << resolution)
    if verbose:
        print(f"Size of random pool: {randsize}  ({randsize:.1e})")
    rpoints = np.transpose([np.random.uniform(-box[i], 2*box[i], randsize) for i in range(3)])
    assert rpoints.shape == (randsize, 3), rpoints.shape
    #print(rpoints)
    
    if verbose:
        print("Assigning to Voronoi cells.")
    belongs_to = [np.argmin( ((p - generators)**2).sum(axis=1)) for p in rpoints]
    belongs_to = np.array(belongs_to)
    
    # Calculate the new centroids (only for the original Voronoi centers)
    if verbose:
        print("Calculating centroids.")
    centroids = np.zeros((npoints, 3))
    for i in range(npoints):
        mypoints = (belongs_to == i)
        centroids[i] = rpoints[mypoints].sum(axis=0) / mypoints.sum()

    # Acceleration of convergence
    centroids = alpha * centroids - (alpha-1) * centers

    # Wrap by PBC - not attempting to do it elegantly
    for i in range(len(centroids)):
        for j in range(3):
            if centroids[i,j] < 0.0:
                centroids[i,j] += box[j]
            if centroids[i,j] >= box[j]:
                centroids[i,j] -= box[j]

    return centroids

###
### EVALUATING AND PLOTTING VORONOI TESSELATIONS
###

def evaluate_voronoi_cells(centers, box):
    """Calculate four parameters evaluating a Voronoi tesselation.

    These four quantities are calculated:
    
    The cell surface area is a measure of some kind of quality/regularity
    of the tesselation, and should decrease is Lloyd's algorithm is applied.

    The total cell volume should be the volume of the box, and is only
    included as a sanity check.

    The largest lateral scaled distance from a cell center to an edge
    measures how close the most critial Voronoi cell is from touching
    itself through the periodic boundary conditions.  The value is 0.5
    if a cell touches itself, values below shows how far it is from doing
    so.

    The number of Voronoi cells touching themselves through the periodic
    boundary conditions.

    
    Parameters:
    centers: A N*3 numpy array of the grain centers (in real space).

    box: The size of the computational box (a 3-tuple).  It is assumed that
        the centers are inside the box, or at most slightly outside.

    Returns:
    A 4-tuple: (total interfacial area; total cell volume; max lateral
    scaled distance to cell boundary; number of self-touching cells)
    """
    import scipy.spatial
    
    npoints = len(centers)
    generators = periodic_images(centers, box)
    voronoi = scipy.spatial.Voronoi(generators)
    regions = [voronoi.regions[voronoi.point_region[i]] for i in range(npoints)]
    for r in regions:
        assert -1 not in r
    # Calculate surface volume and area
    volume = area = 0.0
    for reg in regions:
        cell_vertices = np.array([voronoi.vertices[v] for v in reg])
        hull = scipy.spatial.ConvexHull(cell_vertices)
        volume += hull.volume
        area += hull.area
    # Check if any cell sees itself by calculating the
    # max distance to the vertices in the L1 norm
    maxdist = 0.0
    biggrains = 0
    for i in range(npoints):
        reg = regions[i]
        ctr = centers[i]
        cell_vertices = np.array([voronoi.vertices[v] for v in reg])
        maxdistgrain = 0
        for vert in cell_vertices:
            d = np.abs((vert - ctr)/box).max()
            if d > maxdistgrain:
                maxdistgrain = d
        if maxdistgrain > maxdist:
            maxdist = maxdistgrain
        if maxdistgrain > 0.4999:
            biggrains += 1
    return area, volume, maxdist, biggrains

def plot_voronoi_cells(centers, box, show=True, cellperplot=5):
    """Plot Voronoi tesselations.

    Plots a Voronoi tesselation (nanocrystalline grain structure)
    using matplotlib.

    Parameters:
    centers: A N*3 numpy array of the grain centers (in real space).

    box: The size of the computational box (a 3-tuple).  It is assumed that
        the centers are inside the box, or at most slightly outside.

    show=True: Set to False to skip the call to matplotlib.pyplot.show().
    
    Returns:
    A list-of-figures and a list-of-axes.  They are lists of matplotlib
    figure and Axes3D objects, respectively.
    """
    
    import scipy.spatial
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    import matplotlib.pyplot as plt
    from matplotlib.colors import colorConverter

    npoints = len(centers)
    generators = periodic_images(centers, box)
    voronoi = scipy.spatial.Voronoi(generators)
    regions = [voronoi.regions[voronoi.point_region[i]] for i in range(len(centers))]
    for r in regions:
        assert -1 not in r
    colors = 'rbgyc'
    axlist = []
    figlist = []
    for i, reg in enumerate(regions[:npoints]):
        if i % cellperplot == 0:
            fig = plt.figure()
            ax = Axes3D(fig)
            figlist.append(fig)
            axlist.append(ax)
        cell_vertices = np.array([voronoi.vertices[v] for v in reg])
        hull = scipy.spatial.ConvexHull(cell_vertices)
        verts = [hull.points[simplex] for simplex in hull.simplices]
        poly = Poly3DCollection(verts, facecolors = colorConverter.to_rgba(
            colors[i % cellperplot], alpha=0.6))
        ax.add_collection3d(poly)
        ax.set_xlim3d(0,100.)
        ax.set_ylim3d(0,100.)
        ax.set_zlim3d(0,100.)
    plt.show()
    return figlist, axlist




###
###  Helper tools
###

def periodic_images(points, box):
    points = np.array(points)
    box = np.array(box)
    result = [points]
    for delta in itertools.product((-1,0,1), repeat=3):
        if delta == (0, 0, 0):
            continue # Do not repeat original points.
        newpoints = points + (delta * box)
        result.append(newpoints)
    return np.concatenate(result)
