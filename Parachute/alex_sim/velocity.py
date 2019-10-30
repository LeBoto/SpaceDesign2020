import numpy as np


def velocity(c_d, m, area, rho, g):
    v = np.sqrt((2*m*g) / (rho*c_d*area))
    return v
