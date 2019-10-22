import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from velocity import velocity


def area(d):
    return np.pi*(d/2.0)**2


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

r_x, r_y, v_x, v_y = sy.symbols("r_x, r_y, v_x, v_y")
v_wind = 22.0
g = 32.17405  # ft/s^2
m = 0.0874152 + 1.61621  # slugs
rho = 0.0023769  # slug/ft^3
diameter = 10.0  # ft
A_top = area(diameter)  # ft^2
c_D = 2.59
c_d = 0.45

d_r_x = v_x
d_r_y = v_y
d_v_x = (1 + c_d)*0.5 * rho * (A_top/2.0) * (v_wind - v_x) ** 2
d_v_y = 0.5 * rho * A_top * c_D * v_y ** 2 - m * g

var = [r_x, r_y, v_x, v_y]
equs = sy.Matrix([d_r_x, d_r_y, d_v_x, d_v_y])


l_equ = sy.lambdify([var], equs)

dt = 0.01
t_f = 90.0
y = np.array([0., 700.0, 0., -92.0])
results = []
for i in range(int(t_f/dt)):
    y = rk4(y, l_equ, dt)
    results.append(y)

results = np.asarray(results)

plt.figure(1)
plt.plot(results[:, 0], results[:, 1])
plt.figure(2)
plt.plot(np.arange(int(t_f/dt))*dt, results[:, 2])
plt.figure(3)
plt.plot(np.arange(int(t_f/dt))*dt, results[:, 3])
vel = velocity(diameter, c_D, rho, m, g)
print("Test velocity: {} ft/s\nAnalytical Velocity: {} ft/s".format(results[-1, 3], -vel))
