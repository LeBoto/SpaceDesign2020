import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from velocity import velocity
from sim import sim
from descent_equ import descent_equ

# sim setup

mass = 0.0874152 + 1.61621
diam = 10.0
cd_para = 2.59
cd_drift = 0.45
v_wind = 10.0 # ft/s
l_equ = descent_equ(mass, diam, cd_para, cd_drift, v_wind)

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

g = 32.17405  # ft/s^2
rho = 0.0023769  # slug/ft^3
vel = velocity(diam, cd_para, rho, mass, g)
print("Test velocity: {} ft/s\nAnalytical Velocity: {} ft/s".format(res[-1, 3], -vel))
