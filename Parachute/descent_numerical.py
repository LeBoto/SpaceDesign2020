import numpy as np
import matplotlib.pyplot as plt
from velocity import velocity
from sim import sim
from descent_equ import descent_equ
from tools import area
from kinetic_energy import kinetic_energy

# sim setup drogue
mass = 1.61621
diam = 3.0  # ft
cd_para = 0.75
cd_drift = 0.45
v_wind = 15.0  # ft/s
sa = area(diam)
equ_drogue = descent_equ(mass, sa, cd_para, cd_drift, v_wind)

# sim setup Main
mass = 1.61621 - 0.217567
diam = 8.0
cd_para = 2.59
cd_drift = 0.45
v_wind = 10.0  # ft/s
sa = area(diam)
equ_main = descent_equ(mass, sa, cd_para, cd_drift, v_wind)

# sim setup Payload
mass = 0.217567
diam = 3.0
cd_para = 1.00
cd_drift = 0.45
v_wind = 10.0  # ft/s
sa = area(diam)
equ_pay = descent_equ(mass, sa, cd_para, cd_drift, v_wind)

dt = 0.01
t_f = 0.0
y = np.array([0., 4000.0, 0., 0.0])
breakd = lambda state: state[1] > 700
breakm = lambda state: state[1] > 0
res_d, time01 = sim(y, dt, equ_drogue, breakd)
y = res_d[-1, :]
res_m, time12 = sim(y, dt, equ_main, breakm)
res_p, time13 = sim(y, dt, equ_pay, breakm)
time12 += time01[-1]
time13 += time01[-1]
res_full = np.append(res_d, res_m, axis=0)
time_r = np.append(time01, time12, axis=0)
time_p = np.append(time01, time13, axis=0)
plt.figure(1)
plt.plot(res_full[:, 0], res_full[:, 1])
plt.plot(res_p[:, 0], res_p[:, 1])
plt.title("2D Drift")
plt.xlabel("x (ft)")
plt.ylabel("y (ft)")
plt.figure(2)
plt.plot(time_r, res_full[:, 2])
plt.plot(time13, res_p[:, 2])
plt.title("Drift Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (ft/s")
plt.figure(3)
plt.plot(time_r, res_full[:, 3])
plt.plot(time13, res_p[:, 3])
plt.title("Descent Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (ft/s")

g = 32.17405  # ft/s^2
rho = 0.0023769  # slug/ft^3
print("____________________________________")
print("Analytical Terminal Velocity Main: {} ft/s".format(velocity(8.0, 2.59, rho, 1.61621 - 0.217567, g)))
print("AnalyticalTerminal Velocity Payload: {} ft/s".format(velocity(3.0, 1.0, rho, 0.217567, g)))
print("____________________________________")
print("Descent time rocket: {0:.2f} secs".format(time_r[-1]))
print("Descent time payload: {0:.2f} secs".format(time_p[-1]))
print("Terminal velocity drogue: {0:.2f} ft/s".format(res_d[-1, 3]))
print("Terminal velocity main: {0:.2f} ft/s".format(res_m[-1, 3]))
print("Terminal velocity payload: {0:.2f} ft/s".format(res_p[-1, 3]))
print("Kinetic energy: {0:.2f} ft lbf".format(kinetic_energy(mass, np.linalg.norm(res_full[-1, 2:3]))))
print("____________________________________")