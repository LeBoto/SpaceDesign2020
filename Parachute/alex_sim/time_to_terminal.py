import numpy as np


def to_terminal(v, c_d, m, area, rho):
    return (c_d * 0.5 * rho * (area / 2.0) * v ** 2) / m
