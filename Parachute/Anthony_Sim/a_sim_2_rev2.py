# Anthony Lehmenkuler
# M08480678
# Parachute Simulations
# October 29, 2019
import numpy as np

# TODO: change to calculations into imperial
################################### Vehicle Data ###################################
# C_D
c_d = .75  # coefficient of drag during launch
c_d_p_lv = 1.75  # drag coefficient for parachute launch vehicle
c_d_p_pay = 1.75  # drag coefficient for parachute payload
c_d_drogue = .75  # coefficient of drag for drogue

# Masses
m_apogee = 41.203 # Mass at apogee (lbs)
m_r = 30.5  # mass of rocket body in lb
m_e = 4.53592  # mass of loaded motor in kg
m_p = 2.394  # mass of propellant in kg
m_pay = 9.2 * 0.453592  # mass of payload section in kg
m_b = m_r + m_e - (m_p / 2)  # boost mass in kg
m_c = m_r + m_e - m_p  # coast mass in kg
# m_r = 14.9685 # mass of rocket in kg
# m_e = 4.53592 # mass of loaded motor in kg
# m_p = 2.394 # mass of propellant in kg
# m_pay = 9.2 * 0.453592 # mass of payload section in kg
# m_b = m_r + m_e - (m_p/2) # boost mass in kg
# m_c = m_r + m_e - m_p # coast mass in kg

# Dimensions
d_in = 7.67  # cross sectional diameter in inches
r = (d_in * .0254) / 2  # cross sectional radius in m
c_area = np.pi * r ** 2  # cross sectional area in m**2

d_drogue = 3.0 # diameter of drogue chute (ft)
a_d = np.pi * (d_drogue/2.0) ** 2  # area of drogue in ft

p_d_lv = np.arange(.5, 5, .5)  # diameter of parachute in m launch vehicle
p_r_lv = (p_d_lv / 2.0)  # radius of parachute in m launch vehicle

p_d_pay = np.arange(.5, 5, .5)  # diameter of parachute in m payload
p_r_p = (p_d_pay * 2)  # radius of parachute in m payload

# Forces
i_m = 5015  # motor impulse in N*s
thrust = 1119  # motor thrust in N
################################### Environmental Constants ###################################
# Local constants
g = 9.8  # gravity m/s**2
g = 32.17405  # gravity ft/s**2
rho = 1.22  # air density kg/m**3
rho = 0.0765  # air density lb/ft**3
# Wind
w0 = 0.0 * 1.46667  # wind speed in ft/s
w5 = 5.0 * 1.46667  # wind speed in ft/s
w10 = 10.0 * 1.46667  # wind speed in ft/s
w15 = 15.0 * 1.46667  # wind speed in ft/s
w20 = 20.0 * 1.46667  # wind speed in ft/s
################################### Launch Phase Parameters ###################################
y_max = 4000.0  # Beginning of descent ft

deploy_a = 700.0  # user input deployment altitude in ft
d_a = deploy_a * 0.3048  # altitude for main chute deploy in m

deploy_a_p = 600.0  # user input deployment altitude in ft
d_a_p = deploy_a_p * 0.3048  # pay altitude for main chute deploy in m
################################### Launch Simulation ###################################
## Not gonna use this for now since we have rocksim
# k = .5 * rho * c_d * c_area # calc simplifier
# q = np.sqrt((thrust - (m_b * g)) / k) # calc simplifier
# x = (2 * k * q) / m_b # calc simplifier
# b_time = i_m / thrust # burn time in sec
# v_burn = q * ((1 - np.exp(-x * b_time)) / (1 + np.exp(-x * b_time))) # burn out velocity in m/s
# y_b = (-m_b / (2 * k)) * np.log((thrust - m_b * g - k * v_burn**2) / (thrust - (m_b * g))) # altitude at burn out in m
# y_c = (m_c / (2 * k)) * np.log((m_c * g + k * v_burn**2) / (m_c * g)) # cost distance in m
# q_a = np.sqrt((m_c * g) / k) # calc simplifier
# q_b = np.sqrt((g * k) / m_c) # calc simplifier
# c_time = np.arctan(v_burn / q_a) / q_b # coasting time in sec
# y_max = y_b + y_c # max altitude in meters
# y_max_ft = y_max * 3.28084 # max altitude in feet
################################### Drogue Descent Calculations ###################################
v_d_drogue = np.sqrt((2 * m_apogee * g) / (a_d * rho * c_d_drogue))  # descent velocity in (ft/s)
drag_drogue = c_d_drogue * .5 * rho * a_d * v_d_drogue ** 2  # drag force of drogue (lbs)
a_drogue = drag_drogue / m_apogee  # drag acceleration in m/s
t_drogue = np.sqrt((2 * (y_max - deploy_a)) / g)  # time for rocket to fall before main chute deploy in s
###################################
v_d_lv = np.sqrt((2 * (m_c - m_pay) * g) * (np.pi * rho * c_d_p_lv * p_r_lv ** 2))  # descent velocity in m/s launch vehicle
k_e_lv = .5 * (m_c - m_pay) * v_d_lv ** 2  # kinetic energy of rocket at landing in J launch vehicle
d_f = c_d_p_lv * rho * v_d_lv ** 2 * np.pi * p_r_lv ** 2 * 2  # drag force in N
w = (m_c - m_pay) * g  # weight of rocket in N
t_vel_lv = v_d_lv * g  # time to reach terminal velocity with parachute in sec
d_t_vel_lv = .5 * g * t_vel_lv ** 2  # distance travel during acceleration to terminal in m
d_final_lv = deploy_a - d_t_vel_lv  # final distance to descend at terminal velocity in m
t_main_lv = d_final_lv * v_d_lv  # time for final descent stage in sec
t_total_lv = t_drogue + t_main_lv  # total time for launch vehicle to descend in s

v_d_p = np.sqrt((2 * (m_pay) * g) * (np.pi * rho * c_d_p_pay * p_r_p ** 2))  # descent velocity in m/s payload
k_e_p = .5 * (m_pay) * v_d_p ** 2  # kinetic energy of rocket at landing in J payload

a_d_p = np.pi * .05 ** 2  # pay area of drogue in m
c_d_drogue_p = .75  # pay coefficient of drag for drogue
v_d_drogue_p = np.sqrt((2.0 * (m_pay) * g) / (a_d_p * rho * c_d_drogue_p))  # pay descent velocity in m/s
d_drogue_p = .75 * .5 * rho * a_d_p * v_d_drogue_p ** 2  # pay drag force of drogue
a_drogue_p = d_drogue_p / (m_c - m_pay)  # pay drag acceleration in m/s
t_drogue_p = np.sqrt((2 * (y_max - d_a_p)) / g)  # pay time for rocket to fall before main chute deploy in s
t_vel_p = v_d_p * g  # time to reach terminal velocity with parachute payload in sec
d_t_vel_p = .5 * g * t_vel_p ** 2  # distance travel during acceleration to terminal payload in m
d_free_p = .5 * g * 2 ** 2  # distance in free fall before chute opens
d_final_p = d_a_p - d_t_vel_p - d_free_p  # final distance to descend at terminal velocity payload in m
t_main_p = d_final_p * v_d_p  # time for final descent stage in payload sec
t_total_p = t_main_p + t_drogue_p  # total time for payload to descend in s

################################### Drift Distance ###################################
d0_lv = t_total_lv * w0  # drift in ft
d5_lv = t_total_lv * w5  # drift in ft
d10_lv = t_total_lv * w10  # drift in ft
d15_lv = t_total_lv * w15  # drift in ft
d20_lv = t_total_lv * w20  # drift in ft
d0_p = t_total_p * w0  # drift in ft
d5_p = t_total_p * w5  # drift in ft
d10_p = t_total_p * w10  # drift in ft
d15_p = t_total_p * w15  # drift in ft
d20_p = t_total_p * w20  # drift in ft
