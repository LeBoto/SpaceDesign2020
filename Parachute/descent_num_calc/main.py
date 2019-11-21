from mission_chutes import drogue_chutes, main_chutes, payload_chutes
from tools import toslugs, tofeet
from set_mission import Mission
import numpy as np

drg = drogue_chutes['24']
main = main_chutes['certXXL']
pay = payload_chutes['main']
fall = payload_chutes['freefall']

# mission contraints
max_ke = 75.0  # ft lbs
max_time = 90.0  # sec

# Rocket mission
initial_state = np.array([4000.0, 0.0])
phases = 2

# phase 1
m_1 = toslugs(30.5)
chute1 = drg
dt1 = 0.01
bc1 = 500.0

# phase 2
m_2 = toslugs(32.5)
chute2 = main
dt2 = 0.01
bc2 = 0.0

# set up mission parameters
dt = [dt1, dt2]
mass = [m_1, m_2]
bc = [bc1, bc2]
chutes = [chute1, chute2]

rocket = Mission(phases, initial_state, dt, bc, mass, chutes, max_time, max_ke)
pos, time = rocket.run_mission()
rocket.results()