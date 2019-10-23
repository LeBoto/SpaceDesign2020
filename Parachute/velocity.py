import numpy as np


def velocity(diam, c_d, rho, m, g):
    area = np.pi*(diam/2)**2
    v = np.sqrt((2*m*g) / (rho*c_d*area))
    return v