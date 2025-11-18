import numpy as np


def plane_equation(centre, h, cell):

    vertices = [cell[e] for e in h]
    p = vertices[0]

    n = np.cross(vertices[1] - p, vertices[2] - p)
    n /= np.linalg.norm(n)

    side = np.dot(n, centre - p)
    if side < 0:
        n = -n
        side = np.dot(n, centre - p)
        if side < 0:
            raise Exception("n is not a normal vector")
    return (p, n)

def lies_in_cell(bounding_planes, point):

    for (p, n) in bounding_planes:
        side = np.dot(n, point - p)
        if side < 0:
            return False
    return True

