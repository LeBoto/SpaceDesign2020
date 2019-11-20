import numpy as np
from rk4 import rk4


def sim(y_i, dt, func, bc):
    y = y_i
    results = []
    it = 0
    while bc(y):
        it += 1
        y = rk4(y, func, dt)
        results.append(y)
    results = np.asarray(results)
    time = np.arange(it)*dt
    return results, time