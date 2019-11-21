from mission_chutes import drogue_chutes, main_chutes, payload_chutes
from tools import toslugs, tofeet
from set_mission import Mission
import numpy as np

drogue = drogue_chutes['24']
main = main_chutes['certXXL']
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
pos, time = rocket.run_mission()
rocket.results()