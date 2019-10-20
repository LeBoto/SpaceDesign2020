import numpy as np


def drift(v, area, c_d, rho):
    return 0.5*rho*v**2*area - c_d*0.5*rho*v**2*area
