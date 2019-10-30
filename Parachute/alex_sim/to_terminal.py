import numpy as np
from rk4 import rk4
import sympy as sy


def to_terminal(v, v_term, c_d, m, area, rho, g, dt=0.005):
    vel = sy.Symbol('v')
    pos = sy.Symbol('x')
    f_d = (c_d * 0.5 * rho * (area / 2.0) * vel ** 2)
    f_g = g * m
    d_v = (f_d - f_g)/m
    d_x = vel
    equ = sy.lambdify([sy.Matrix([pos, vel])], sy.Matrix([d_x, d_v]))
    t = 0.0
    x = 0.0
    v = -abs(v)
    state = np.array([x, v])
    while (abs(v) + abs(v_term))**2 > 0.1:
        print("error: {}".format((abs(v) + abs(v_term))**2))
        t += dt
        state = rk4(state, equ, dt)
        x = state[0]
        v = state[1]
    return t, abs(x), abs(v)
