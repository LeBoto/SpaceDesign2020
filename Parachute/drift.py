import numpy as np


def drift(v, diam, c_d, rho):
    area = np.pi * diam**2.0 / 4.0
    return 0.5*rho*v**2*area - c_d*0.5*rho*v**2*area
