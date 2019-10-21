import numpy as np


def f_drift(v, v_wind, diam, rho):
    area = np.pi * diam**2.0 / 4.0
    return 0.5*rho*(v_wind - v)**2*area
