import random
import numpy as np
import math


def quaternion_to_rotation_matrix(q):
    [a, b, c, d] = q.tolist()

    return np.array([[a*a + b*b - c*c - d*d, 2*b*c - 2*a*d, 2*b*d + 2*a*c],\
            [2*b*c + 2*a*d, a*a - b*b + c*c - d*d, 2*c*d - 2*a*b],\
            [2*b*d - 2*a*c, 2*c*d + 2*a*b, a*a - b*b - c*c + d*d]])

def random_quaternion():

    x0 = random.uniform(0.0, 1.0)
    x1 = random.uniform(0.0, 2.0 * math.pi)
    x2 = random.uniform(0.0, 2.0 * math.pi)

    r1 = math.sqrt(1.0 - x0)
    r2 = math.sqrt(x0)

    s1 = math.sin(x1)
    c1 = math.cos(x1)
    s2 = math.sin(x2)
    c2 = math.cos(x2)
    return np.array([s1*r1, c1*r1, s2*r2, c2*r2])

def random_rotation_matrix():
    """Returns a random rotation matrix."""
    return quaternion_to_rotation_matrix(random_quaternion())

def rotation_matrix_to_quaternion(u):

    r11 = u[0][0]
    r12 = u[0][1]
    r13 = u[0][2]
    r21 = u[1][0]
    r22 = u[1][1]
    r23 = u[1][2]
    r31 = u[2][0]
    r32 = u[2][1]
    r33 = u[2][2]

    q = np.array([    1.0 + r11 + r22 + r33,
            1.0 + r11 - r22 - r33,
            1.0 - r11 + r22 - r33,
            1.0 - r11 - r22 + r33    ]).astype(np.double) / 4.0

    q = np.sqrt(np.maximum(0, q))
    i = np.argmax(q)

    if i == 0:
        q[1] *= np.sign(r32 - r23)
        q[2] *= np.sign(r13 - r31)
        q[3] *= np.sign(r21 - r12)

    elif i == 1:
        q[0] *= np.sign(r32 - r23)
        q[2] *= np.sign(r21 + r12)
        q[3] *= np.sign(r13 + r31)

    elif i == 2:
        q[0] *= np.sign(r13 - r31)
        q[1] *= np.sign(r21 + r12)
        q[3] *= np.sign(r32 + r23)

    elif i == 3:
        q[0] *= np.sign(r21 - r12)
        q[1] *= np.sign(r31 + r13)
        q[2] *= np.sign(r32 + r23)

    return q / np.linalg.norm(q)

HALF_SQRT_2 = 0.7071067811865474617150084668537601828575
generator_cubic = [    [1,    0,    0,    0    ],
            [0,    1,    0,    0    ],
            [0,    0,    1,    0    ],
            [0,    0,    0,    1    ],
            [0.5,    0.5,    0.5,    0.5    ],
            [0.5,    0.5,    -0.5,    0.5    ],
            [0.5,    -0.5,    0.5,    0.5    ],
            [0.5,    -0.5,    -0.5,    0.5    ],
            [-0.5,    0.5,    0.5,    0.5    ],
            [-0.5,    0.5,    -0.5,    0.5    ],
            [-0.5,    -0.5,    0.5,    0.5    ],
            [-0.5,    -0.5,    -0.5,    0.5    ],
            [HALF_SQRT_2,    HALF_SQRT_2,    0,    0    ],
            [HALF_SQRT_2,    0,    HALF_SQRT_2,    0    ],
            [HALF_SQRT_2,    0,    0,    HALF_SQRT_2    ],
            [-HALF_SQRT_2,    HALF_SQRT_2,    0,    0    ],
            [-HALF_SQRT_2,    0,    HALF_SQRT_2,    0    ],
            [-HALF_SQRT_2,    0,    0,    HALF_SQRT_2    ],
            [0,    HALF_SQRT_2,    HALF_SQRT_2,    0    ],
            [0,    HALF_SQRT_2,    0,    HALF_SQRT_2    ],
            [0,    0,    HALF_SQRT_2,    HALF_SQRT_2    ],
            [0,    -HALF_SQRT_2,    HALF_SQRT_2,    0    ],
            [0,    -HALF_SQRT_2,    0,    HALF_SQRT_2    ],
            [0,    0,    -HALF_SQRT_2,    HALF_SQRT_2    ]]

def quat_rot(r, a):
    b0 = r[0] * a[0] - r[1] * a[1] - r[2] * a[2] - r[3] * a[3]
    b1 = r[0] * a[1] + r[1] * a[0] + r[2] * a[3] - r[3] * a[2]
    b2 = r[0] * a[2] - r[1] * a[3] + r[2] * a[0] + r[3] * a[1]
    b3 = r[0] * a[3] + r[1] * a[2] - r[2] * a[1] + r[3] * a[0]
    return np.array([b0, b1, b2, b3]).astype(np.double)

def quat_map_cubic(r, i):
    return quat_rot(r, generator_cubic[i])

def rotate_quaternion_into_cubic_fundamental_zone(q):
    q = max([quat_map_cubic(q, i) for i in range(24)], key= lambda e: abs(e[0]))
    if q[0] < 0:
        q = -q
    return q

def quat_to_rodrigues(q):
    return np.array([q[1] / q[0], q[2] / q[0], q[3] / q[0]]).astype(np.double)

def rod_to_rgb(r):

    minh = math.radians(-62.8)
    maxh = math.radians(62.8)

    size = np.linalg.norm(r)
    r /= size
    theta = 2 * math.atan(size)
    return (r * theta - minh) / (maxh - minh)

def quat_to_rgb(q):

    rod = quat_to_rodrigues(q)
    return rod_to_rgb(rod)

def quat_inverse(q):
    return np.array([-q[0], q[1], q[2], q[3]])

def quat_quick_misorientation(q1, q2):

    t = np.dot(q1, q2)
    t = min(1, max(-1, t))
    return 2 * t * t - 1

def quat_misorientation(q1, q2):
    return math.acos(quat_quick_misorientation(q1, q2))

