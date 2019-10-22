import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from velocity import velocity
from sim import sim
from tools import area

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
breakc = lambda state: state[1] > 0

res, time = sim(y, dt, l_equ, breakc)

plt.figure(1)
plt.plot(res[:, 0], res[:, 1])
plt.title("2D Drift")
plt.xlabel("x (ft)")
plt.ylabel("y (ft)")
plt.figure(2)
plt.plot(time, res[:, 2])
plt.title("Drift Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (ft/s")
plt.figure(3)
plt.plot(time, res[:, 3])
plt.title("Descent Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (ft/s")
vel = velocity(diameter, c_D, rho, m, g)
print("Test velocity: {} ft/s\nAnalytical Velocity: {} ft/s".format(res[-1, 3], -vel))
