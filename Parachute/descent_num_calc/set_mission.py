import sympy as sy
import numpy as np


class mission(object):
    def __init__(self, n_phases, initial_state, time_step, break_alt, masses, chutes, max_time, max_ke, alt_state=0):
        assert n_phases == len(break_alt) == len(masses)
        self.n = n_phases
        self.dt = time_step
        self.time_lim = max_time
        self.ke_lim = max_ke
        self.phase = break_alt
        self.equ = []
        self.state = initial_state
        self.__breaks = []
        for i in range(n_phases):
            self.equ.append(self.make_equ(masses[i], chutes[i].S, chutes[i].cd))
            self.__breaks.append(lambda state: state[alt_state] > self.phase[i])

    def make_equ(self, mass, area, c_d):
        r_y, v_y = sy.symbols("r_y, v_y")
        g = 32.17405  # ft/s^2
        rho = 0.0023769  # slug/ft^3
        d_r_y = v_y

        d_v_drag = (c_d * 0.5 * rho * area * v_y ** 2) / mass
        d_v_y = d_v_drag - g

        var = [r_y, v_y]
        equs = sy.Matrix([d_r_y, d_v_y])
        l_equ = sy.lambdify([var], equs)
        return l_equ

    def run_mission(self):
        bc = self.__breaks
        y = self.state
        time = np.array([0])
        state = y
        state = state.reshape((1, len(y)))
        for i in range(self.n):
            y, t = self.sim(y, self.dt[i], self.equ[i], bc[i])
            time = np.append(time, t + time[-1])
            state = np.append(state, y, axis=0)
            y = y[-1, :]
        return state, time

    def sim(self, y_i, dt, func, bc):
        y = y_i
        results = []
        it = 0
        while bc(y):
            it += 1
            y = self.rk4(y, func, dt)
            results.append(y)
        results = np.asarray(results)
        time = np.arange(it) * dt
        return results, time

    @staticmethod
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