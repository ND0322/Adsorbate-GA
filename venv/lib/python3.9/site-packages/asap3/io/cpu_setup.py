import math
import numpy as np


def multiple_factorization(n, length):
    '''
    finds all unique factorizations of n of a given length
    factors are in sorted order
    '''

    if length == 1:
        return []

    factorizations = []

    ulim0 = int(math.floor(math.sqrt(n + 1)))
    for i in range(1, ulim0 + 1):

        if n % i == 0:
            a = i
            b = n / i

            fa = multiple_factorization(a, length - 1)
            fb = multiple_factorization(b, length - 1)

            if not fa or not fb:
                factorizations += [[a, b]]

            for e in fa:
                factorizations += [[b] + e]
            for e in fb:
                factorizations += [[a] + e]

    return sorted([list(e) for e in {tuple(sorted(e)) for e in factorizations}])

def calculate_optimal_cpu_setup(n, dim):
    '''
    finds optimal cpu setup for n processors with given sample dimensions
    '''

    if type(dim) == np.array:
        dim = dim.tolist()

    if len(dim) != 3:
        raise Exception("dim must be length 3")

    factorizations = multiple_factorization(n, 3)

    (dim, order) = zip(*sorted(zip(dim, range(3))))
    [len0, len1, len2] = [float(e) for e in dim]

    cubes = [(len0 / a, len1 / b, len2 / c) for (a, b, c) in factorizations]
    ratios = [(x*y*z) / (2*x*y + 2*y*z + 2*z*x) for (x, y, z) in cubes]

    best_fac = max([(e, bf) for e, bf in zip(ratios, factorizations)])[1]
    cpus = [e[1] for e in sorted(zip(order, best_fac))]
    return np.array(cpus).astype(int)

