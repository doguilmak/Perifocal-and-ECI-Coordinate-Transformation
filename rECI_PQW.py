import numpy as np
import math as m


def r_eci(P, Q, W, i, omega, w):

    PQW = np.array([[P],
                    [Q],
                    [W]])

    R1i = np.array([[1, 0, 0],
                   [0, m.cos(m.radians(-i)), m.sin(m.radians(-i))],
                   [0, -m.sin(m.radians(-i)), m.cos(m.radians(-i))]])

    R3omega = np.array([[m.cos(m.radians(-omega)), -m.sin(m.radians(-omega)), 0],
                   [m.sin(m.radians(-omega)), m.cos(m.radians(-omega)), 0],
                   [0, 0, 1]])

    R3w = np.array([[m.cos(m.radians(-w)), -m.sin(m.radians(-w)), 0],
                   [m.sin(m.radians(-w)), m.cos(m.radians(-w)), 0],
                   [0, 0, 1]])

    R1ixR3w = np.matmul(R1i, R3w)
    R3wR1R3 = np.matmul(R3omega, R1ixR3w)
    ECI = np.matmul(R3wR1R3, PQW)

    print("R1(-i):\n", R1i)
    print("R3(-\u03A9):\n", R3omega)
    print("R3(-w):\n", R3w)
    print("R1(-i)xR3(-w):\n", R1ixR3w)
    print("R3(-\u03A9)xR1(-i)xR3(-w):\n", R3wR1R3)
    print("rECI:\n", ECI)


r_eci(-80.8821594551, 40.1138553510, 0, 58.322222222, 5.45, 268.9310345)
