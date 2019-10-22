import numpy as np
import matplotlib.pyplot as plt
from velocity import velocity
from sim import sim
from descent_equ import descent_equ

# sim setup drogue
mass = 1.61621
diam = 2.0  # ft
cd_para = 1.5
cd_drift = 0.4
v_wind = 15.0  # ft/s
equ_drogue = descent_equ(mass, diam, cd_para, cd_drift, v_wind)

# sim setup Main
mass = 1.61621
diam = 10.0
cd_para = 2.59
cd_drift = 0.45
v_wind = 10.0  # ft/s
equ_main = descent_equ(mass, diam, cd_para, cd_drift, v_wind)

dt = 0.01
t_f = 0.0
y = np.array([0., 4000.0, 0., 0.0])
breakd = lambda state: state[1] > 700
breakm = lambda state: state[1] > 0
res_d, time01 = sim(y, dt, equ_drogue, breakd)
y = res_d[-1, :]
res_m, time12 = sim(y, dt, equ_main, breakm)
time12 += time01[-1]
res_full = np.append(res_d, res_m, axis=0)
time = np.append(time01, time12, axis=0)
plt.figure(1)
plt.plot(res_full[:, 0], res_full[:, 1])
plt.title("2D Drift")
plt.xlabel("x (ft)")
plt.ylabel("y (ft)")
plt.figure(2)
plt.plot(time, res_full[:, 2])
plt.title("Drift Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (ft/s")
plt.figure(3)
plt.plot(time, res_full[:, 3])
plt.title("Descent Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (ft/s")

# g = 32.17405  # ft/s^2
# rho = 0.0023769  # slug/ft^3
# vel = velocity(diam, cd_para, rho, mass, g)
print("____________________________________")
print("Descent time: {0:.2f} secs".format(time[-1]))
print("Stable velocity drogue: {0:.2f} ft/s".format(res_d[-1, 3]))
print("Stable velocity main: {0:.2f} ft/s".format(res_m[-1, 3]))
print("____________________________________")