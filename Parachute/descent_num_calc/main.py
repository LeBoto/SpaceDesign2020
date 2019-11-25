from mission_chutes import drogue_chutes, main_chutes, payload_chutes
from tools import toslugs, tofeet
from set_mission import Mission
import matplotlib.pyplot as plt
import numpy as np

drogue = drogue_chutes['36']
main = main_chutes['certXL']
pay = payload_chutes['main']
fall = payload_chutes['freefall']

# mission contraints
max_ke = 75.0  # ft lbs
max_time = 90.0  # sec

# Rocket mission
initial_state = np.array([4000.0, 0.0])
phases = 2
# set up mission parameters
dt = [0.01, 0.01]  # time step for each phase
mass = [toslugs(31.8), toslugs(31.8 - 4.0)]  # mass for each phase
bc = [500.0, 0.0]  # altitude breaking conditions
chutes = [drogue, main]  # parachute used for each phase

rocket = Mission(phases, initial_state, dt, bc, mass, chutes, max_time, max_ke)
rocket.run_mission()
rocket.results("Rocket", masses=[toslugs(14.2), toslugs(17.6)])

# Rocket mission
initial_state = np.array([4000.0, 0.0])
phases = 3
# set up mission parameters
m_drone = toslugs(1.57)
m_nose = toslugs(1.875)  # mass of nose cone (slug)
m_can = toslugs(7.67 - 1.875)  # mass of payload section (slug)
m_pay = m_can + m_nose + m_drone
m_pay_empty = m_can + m_nose
dt = [0.01, 0.01, 0.01]  # time step for each phase
mass = [m_pay, m_pay, m_pay_empty]  # mass for each phase
bc = [600.0, 400, 0.0]  # altitude breaking conditions
chutes = [fall, pay, pay]  # parachute used for each phase

payload = Mission(phases, initial_state, dt, bc, mass, chutes, max_time, max_ke)
payload.run_mission()
payload.results("Payload", masses=[m_can, m_nose])

plt.figure(1)
rocket.plot_path("Rocket Path")
payload.plot_path("Payload Path")
plt.legend()

plt.figure(2)
rocket.plot_vel("Rocket Velocity")
payload.plot_vel("Payload Velocity")
plt.legend()