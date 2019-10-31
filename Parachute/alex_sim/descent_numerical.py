import numpy as np
import matplotlib.pyplot as plt
from sim import sim
from descent_equ import descent_equ
from kinetic_energy import kinetic_energy
from tools import lb2slug, area, area_eff

# Wind
v_wind = np.arange(0.0, 25.0, 5.0) * 1.46667  # wind speed in ft/s
g = 32.17405
rho = 0.0023769

# sim setup drogue
m_rocket = lb2slug(32.5)  # slugs
diam = 24.0/12.0  # ft
cd_dro = 0.75
sa = area(diam)
equ_drogue = descent_equ(m_rocket, sa, cd_dro)

# sim setup Main
# cd_para = .97
# sa = area_eff(17.0, lb2slug(44.0), cd_para, rho, g)
# cd_para = .97
# sa = area_eff(17.0, lb2slug(60), cd_para, rho, g)
# cd_para = 2.59
# sa = area_eff(17.0, lb2slug(32.6), cd_para, rho, g)
cd_para = 2.92
sa = area_eff(17.0, lb2slug(60.0), cd_para, rho, g)
equ_main = descent_equ(m_rocket, sa, cd_para)

# sim setup Payload free fall
m_drone = lb2slug(1.57)
m_nose = lb2slug(1.875)  # mass of nose cone (slug)
m_can = lb2slug(7.67 - m_nose)  # mass of payload section (slug)
m_pay = m_can + m_nose + m_drone
diam = 7.5/12.0
cd_can = 0.47
sa = area(diam)
equ_free = descent_equ(m_pay, sa, cd_can)

diam_pay = 58.0
# sim setup Payload with drone
m_drone = lb2slug(1.57)
m_nose = lb2slug(1.875)  # mass of nose cone (slug)
m_can = lb2slug(7.67 - m_nose)  # mass of payload section (slug)
m_pay = m_can + m_nose + m_drone
diam = diam_pay/12.0
cd_pay = 1.75
sa = area(diam)
equ_pay = descent_equ(m_pay, sa, cd_pay)

# sim setup Payload without drone
m_nose = lb2slug(1.875)  # mass of nose cone (slug)
m_can = lb2slug(7.67 - m_nose)  # mass of payload section (slug)
m_pay = m_can + m_nose
diam = diam_pay/12.0
sa = area(diam)
equ_drone = descent_equ(m_pay, sa, cd_pay)
dt = 0.01
t_f = 0.0

h_apo = 4000.0  # Beginning of descent (ft)
h_main = 500.0  # main chute deployment altitude (ft)
h_payload = 600.0  # payload deployment altitude (ft)
h_drone = 400.0  # altitude of drone deployment (ft)
break_drogue = lambda state: state[0] > h_main
break_gnd = lambda state: state[0] > 0.0
break_payload = lambda state: state[0] > h_payload
break_drone = lambda state: state[0] > h_drone

# ------------------------- simulation of vehicle body -------------------------
y = np.array([h_apo, 0.0])
res_d, time00 = sim(y, dt, equ_drogue, break_drogue)
y = res_d[-1, :]
res_m, time01 = sim(y, dt, equ_main, break_gnd)
rocket_sim = np.append(res_d, res_m, axis=0)
time01 += time00[-1]
rocket_time = np.append(time00, time01, axis=0)

# ------------------------- simulation of payload normal -------------------------
y = np.array([h_apo, 0.0])
res_f, time10 = sim(y, dt, equ_free, break_payload)
y = res_f[-1, :]
res_p, time11 = sim(y, dt, equ_pay, break_drone)
y = res_p[-1, :]
res_dr, time12 = sim(y, dt, equ_drone, break_gnd)
time11 += time10[-1]
time12 += time11[-1]
payload_sim = np.append(res_f, res_p, axis=0)
payload_sim = np.append(payload_sim, res_dr, axis=0)
payload_time = np.append(time10, time11, axis=0)
payload_time = np.append(payload_time, time12, axis=0)

# ------------------------- simulation of payload emergency -------------------------
y = np.array([h_apo, 0.0])
res_f_e, time20 = sim(y, dt, equ_free, break_payload)
y = res_f_e[-1, :]
res_p_e, time21 = sim(y, dt, equ_pay, break_gnd)
time21 += time20[-1]
payload_e_sim = np.append(res_f_e, res_p_e, axis=0)
payload_e_time = np.append(time20, time21, axis=0)

# ------------------------- plot simulation -------------------------
plt.figure(1)
plt.title("Descent Altitude vs Time")
plt.plot(rocket_time, rocket_sim[:, 0], label="Rocket")
plt.plot(payload_time, payload_sim[:, 0], label="Payload config 1")
plt.plot(payload_e_time, payload_e_sim[:, 0], label="Payload config 2")
plt.axvline(x=90.0, label="Descent time requirement")
plt.xlabel("Time (s)")
plt.ylabel("Distance (ft)")
plt.legend()

plt.figure(2)
plt.title("Descent Velocity vs Time")
plt.plot(rocket_time, rocket_sim[:, 1], label="Rocket")
plt.plot(payload_time, payload_sim[:, 1], label="Payload config 1")
plt.plot(payload_e_time, payload_e_sim[:, 1], label="Payload config 2")
plt.axvline(x=90.0, label="Descent time requirement")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (ft/s)")
plt.legend()

print("Kinetic Energy of Vehicle on Touchdown: \t\t\t{0:.2f} ft lbs".format(kinetic_energy(rocket_sim[-1, 1], m_rocket-lb2slug(4.0))))
print("Kinetic Energy of Canister with Drone on Touchdown: {0:.2f} ft lbs".format(kinetic_energy(payload_e_sim[-1, 1], m_can + m_drone)))
print("Kinetic Energy of Canister on Touchdown: \t\t\t{0:.2f} ft lbs".format(kinetic_energy(payload_sim[-1, 1], m_can)))
print("Kinetic Energy of Nosecone on Touchdown: \t\t\t{0:.2f} ft lbs".format(kinetic_energy(payload_sim[-1, 1], m_nose)))
print()
print("Max Velocity of Vehicle under Drogue: \t\t\t{0:.2f} ft/s".format(abs(res_d[-1, 1])))
print("Max Velocity of Vehicle under Main Parachute:  \t{0:.2f} ft/s".format(abs(rocket_sim[-1, 1])))
print("Max Velocity of Payload: \t\t\t\t\t\t{0:.2f} ft/s".format(abs(res_f[-1, 1])))
print("Max Velocity of Payload + Drone under parachute:{0:.2f} ft/s".format(abs(payload_e_sim[-1, 1])))
print("Max Velocity of Payload under parachute: \t\t{0:.2f} ft/s".format(abs(payload_sim[-1, 1])))
print()
print("Descent Time of Vehicle: \t\t{0:.2f} s".format(rocket_time[-1]))
print("Descent Time Under Main: \t\t{0:.2f} s".format(time01[-1] - time00[-1]))
print("Descent Time of Payload: \t\t{0:.2f} s".format(payload_time[-1]))
print("Descent Time of Payload+Drone: {0:.2f} s".format(payload_e_time[-1]))
print()
print("Rocket Drift: {}".format(rocket_time[-1]*v_wind))
print("Payload Drift: {}".format(payload_time[-1]*v_wind))