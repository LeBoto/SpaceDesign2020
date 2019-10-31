import numpy as np


def area(d):
    """Calculate area of a circle"""
    return np.pi*(d/2.0)**2


def lb2slug(mass):
    """Convert lbm to slugs"""
    return mass*0.031081


def area_eff(v, m, c_d, rho, g):
    """Calculate effective area of a parachute"""
    return (m * g) / (0.5 * c_d * rho * v ** 2)