import numpy as np
from lb2slug import lb2slug
from velocity import velocity
from kinetic_energy import kinetic_energy
from descent_time import descent_time

################################### Vehicle Data ###################################
# C_D
c_d_drogue = .75  # coefficient of drag for drogue
c_d_main = np.array([1.89, 1.26, 2.59, 2.92])  # drag coefficient for main chute
c_d_pay = 1.75  # drag coefficient for parachute payload

# Masses
m_rocket = lb2slug(30.5)  # mass of rocket body (slug)
m_can = lb2slug(8.7)  # mass of payload section (slug)
m_nose = lb2slug(2)  # mass of nose cone (slug)
m_drone = lb2slug(2.7)  # mass of drone (slug)
m_pay = m_can + m_nose - m_drone

# Dimensions
diam_drogue = 3.0  # diameter of drogue chute (ft)
diam_pay = np.array([36.0, 42.0, 50.0, 58.0])/12.0  # diameter of parachute payload (ft)

area_drogue = np.pi * (diam_drogue / 2.0) ** 2  # area of drogue in ft
area_main = np.array([39.3, 57.0, 89.0, 129.0])  # Main chute area (ft**2)
area_pay = np.pi*(diam_pay/2.0)**2  # area of the payload chute (ft**2)
# ---------------------------------- Environmental Constants ----------------------------------
# Local constants
g = 32.17405  # gravity ft/s**2
rho = 0.0023769  # air density slug/ft**3
# Wind
v_wind = np.arange(0.0, 20.0) * 1.46667  # wind speed in ft/s
# ---------------------------------- Launch Phase Parameters ----------------------------------
y_max = 4000.0  # Beginning of descent ft
deploy_main = 700.0  # user input deployment altitude in ft
deploy_payload = 600.0  # user input deployment altitude in ft
# ---------------------------------- Kinetic Energy ----------------------------------
v_drogue = velocity(area_drogue, c_d_drogue, rho, m_rocket, g)
v_main = velocity(area_main, c_d_main, rho, m_rocket, g)
v_pay = velocity(area_pay, c_d_pay, rho, m_pay, g)

ke_drogue = kinetic_energy(v_drogue, m_rocket)
ke_main = kinetic_energy(v_main, m_rocket)
ke_pay = kinetic_energy(v_pay, m_pay)