import numpy as np


def velocity(weight, diam, c_d, rho, m, g):
    v = sqrt((8*m*g) / (np.pi*rho*c_d*diam**2))
    return v