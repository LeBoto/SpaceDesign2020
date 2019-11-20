import numpy as np


def rk4(yn, f, h):
    shp = yn.shape
    yn = yn.flatten()
    k1 = (f(yn) * h).flatten()
    y = yn + 0.5 * k1
    k2 = (f(y) * h).flatten()
    y = yn + 0.5 * k2
    k3 = (f(y) * h).flatten()
    y = yn + k3
    k4 = (f(y) * h).flatten()
    return (yn + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0).reshape(shp)