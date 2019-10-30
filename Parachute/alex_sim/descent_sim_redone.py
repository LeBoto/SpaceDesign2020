import numpy as np
from lb2slug import lb2slug
from velocity import velocity
from kinetic_energy import kinetic_energy
from descent_time import descent_time
from to_terminal import to_terminal
################################### Vehicle Data ###################################
# C_D
c_d_drogue = 0.75  # coefficient of drag for drogue
c_d_pay_free = 0.4  # coefficient of drag for payload pre chute
c_d_main = np.array([1.89, 1.26, 2.59, 2.92])  # drag coefficient for main chute
c_d_pay = 1.75  # drag coefficient for parachute payload

# Masses
m_rocket = lb2slug(30.5)  # mass of rocket body (slug)
m_drone = lb2slug(1.57)
m_nose = lb2slug(1.875)  # mass of nose cone (slug)
m_can = lb2slug(7.67 - m_nose)  # mass of payload section (slug)
m_pay = m_can + m_nose

# Dimensions
diam_drogue = 24.0/12.0  # diameter of drogue chute (ft)
diam_pay = np.array([36.0, 42.0, 50.0, 58.0])/12.0  # diameter of parachute payload (ft)
diam_can = 7.5/12.0  # diameter of canister (ft)

area_drogue = np.pi * (diam_drogue / 2.0) ** 2  # area of drogue in ft
area_can = np.pi * (diam_can / 2.0) ** 2   # area of drogue in ft
area_main = np.array([39.3, 57.0, 89.0, 129.0])  # Main chute area (ft**2)
area_pay = np.pi*(diam_pay/2.0)**2  # area of the payload chute (ft**2)
# ---------------------------------- Environmental Constants ----------------------------------
# Local constants
g = 32.17405  # gravity ft/s**2
rho = 0.0023769  # air density slug/ft**3
# Wind
v_wind = np.arange(5.0, 25.0, 5.0) * 1.46667  # wind speed in ft/s
# ---------------------------------- Launch Phase Parameters ----------------------------------
h_apo = 4000.0  # Beginning of descent (ft)
h_main = 500.0  # main chute deployment altitude (ft)
h_payload = 600.0  # payload deployment altitude (ft)
h_drone = 400.0  # altitude of drone deployment (ft)
# ---------------------------------- Kinetic Energy ----------------------------------
v_drogue = velocity(c_d_drogue, m_rocket, area_drogue, rho, g)
v_pay_free = velocity(c_d_pay_free, m_pay + m_drone, area_can, rho, g)
v_main = velocity(c_d_main, m_rocket, area_main, rho, g)
v_pay_w_drone = velocity(c_d_pay, m_pay + m_drone, area_pay, rho, g)
v_pay = velocity(c_d_pay, m_pay, area_pay, rho, g)

ke_drogue = kinetic_energy(v_drogue, m_rocket)
ke_main = kinetic_energy(v_main, m_rocket)
ke_nose = kinetic_energy(v_pay, m_nose)
ke_can = kinetic_energy(v_pay, m_can)
ke_nose_el = kinetic_energy(v_pay_w_drone, m_nose)
ke_can_el = kinetic_energy(v_pay_w_drone, m_can)

print("Area drogue chute: {0:.5f} ft^2".format(area_drogue))
print("Area main chute: {} ft^2".format(area_main))
print("Area payload chute: {} ft^2".format(area_pay))
print()
print("Mass of rocket: {0:.5f} slugs".format(m_rocket))
print("Mass of canister: {0:.5f} slugs".format(m_can))
print("Mass of nose cone: {0:.5f} slugs".format(m_nose))
print()
print("Velocity drogue chute: {0:.5f} ft/s".format(v_drogue))
print("Velocity main chute: {} ft/s".format(v_main))
print("Velocity payload chute: {} ft/s".format(v_pay))
print()
print("KE rocket: {} ft lbs".format(ke_main))
print("KE canister: {} ft lbs".format(ke_can))
print("KE nose cone: {} ft lbs".format(ke_nose))
print()
# ---------------------------------- Descent Time ----------------------------------
# Phase 1
t_pay_free = descent_time(h_apo - h_payload, v_pay_free)
t_drogue = descent_time(h_apo - h_main, v_drogue)
# Phase 2 rocket
t_main = descent_time(h_main, v_main)
# Phase 2 payload
t_pay_w_drone = descent_time(h_payload - h_drone, v_pay_w_drone)
t_pay = descent_time(h_drone, v_pay)
t_emergency = descent_time(h_payload, v_pay_w_drone)
# rocket descent time
t_rocket = t_drogue + t_main
# Payload descent time
t_payload = t_pay_free + t_pay_w_drone + t_pay
t_payload_el = t_pay_free + t_emergency
print("Drogue descent time: {0:.5f} s".format(t_drogue))
print("Total rocket descent time: {} s".format(t_rocket))
print("Total payload descent time: {} s".format(t_payload))
print("Total payload emergency descent time: {} s".format(t_payload_el))
print()
# ---------------------------------- Drift ----------------------------------
max_drift_rocket = np.asarray(np.asmatrix(v_wind).T*np.asmatrix(t_rocket))
max_drift_payload = np.asarray(np.asmatrix(v_wind).T*np.asmatrix(t_payload))