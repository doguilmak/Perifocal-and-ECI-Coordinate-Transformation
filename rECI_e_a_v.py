import numpy as np
import math as m


def r_eci(e, a, v, i, omega, w):

    r_v = a * (1 - e**2) / (1 + e * m.cos(m.radians(v)))

    P = r_v * m.cos(m.radians(v))
    Q = r_v * m.sin(m.radians(v))
    W = 0

    PQW = np.array([[P],
                    [Q],
                    [W]])

    R1i = np.array([[1, 0, 0],
                   [0, m.cos(m.radians(-i)), m.sin(m.radians(-i))],
                   [0, -m.sin(m.radians(-i)), m.cos(m.radians(-i))]])

    R3omega = np.array([[m.cos(m.radians(-omega)), m.sin(m.radians(-omega)), 0],
                   [-m.sin(m.radians(-omega)), m.cos(m.radians(-omega)), 0],
                   [0, 0, 1]])

    R3w = np.array([[m.cos(m.radians(-w)), m.sin(m.radians(-w)), 0],
                   [-m.sin(m.radians(-w)), m.cos(m.radians(-w)), 0],
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


#  r_eci(0.01, 26610212.9739, 12.75108336, 58.85422, 4.332314, 268.7328)
r_eci(7.704, 9.13100835200, 153.6206896552, 58.3222222222, 5.45, 268.9310344828)
