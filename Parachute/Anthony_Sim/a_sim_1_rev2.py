# Anthony Lehmenkuler
# M08480678
# Rocket Simulations
# October 21, 2019
import numpy as np

## Flight Profile
g = 9.8 # gravity m/s^2
c_d = input('Input coefficient of drag for rocket:  ') # coefficient of drag, typically .75 need to check
rho = 1.22 # air density kg/m^3
m_r = input('Input the mass of the rocket in kg:  ') # mass of rocket in kg
m_e = input('Input the mass of the loaded motor in kg:  ') # mass of loaded motor in kg
m_p = input('Input the mass of the propellant in kg:  ') # mass of propellant in kg
i_m = input('Input motor impulse in Newton Seconds:  ') # motor impulse in N*s
thrust = input('Input motor thrust in Newtons:  ') # motor thrust in N
d_in = 7.67 # cross sectional diameter in inches
r = (d_in * .0254)/2 # cross sectional radius in m
c_area = pi * r^2 # cross sectional area in m^2
m_b = m_r + m_e - (m_p/2) # boost mass in kg
m_c = m_r + m_e - m_p # coast mass in kg
k = .5 * rho * c_d * c_area # calc simplifier
q = np.sqrt((thrust - (m_b * g)) / k) # calc simplifier
x = (2 * k * q) / m_b # calc simplifier
b_time = i_m / thrust # burn time in sec
v_burn = q * ((1 - np.exp(-x * b_time)) / (1 + np.exp(-x * b_time))) # burn out velocity in m/s
y_b = (-m_b / (2 * k)) * np.log((thrust - m_b * g - k * v_burn^2) / (thrust - (m_b * g))) # altitude at burn out in m
y_c = (m_c / (2 * k)) * np.log((m_c * g + k * v_burn^2) / (m_c * g)) # cost distance in m
q_a = np.sqrt((m_c * g) / k) # calc simplifier
q_b = np.sqrt((g * k) / m_c) # calc simplifier
c_time = np.arctan(v_burn / q_a) / q_b # coasting time in sec
y_max = y_b + y_c # max altitude in meters
y_max_ft = y_max * 3.28084 # max altitude in feet
print('Max Altitude: #8.3f ft \n',y_max_ft)

## Thrust Curve
b_time_v = 0.1:0.01:b_time # burn time vector in sec
thrust_v = i_m ./ b_time_v # thrust vector in N
figure(1)
plot(b_time_v , thrust_v) 
xlabel('Burn Time in Seconds')
ylabel('Thrust in Newtons')
title('Thrust Curve Plot')

## Kinetic Energy at Landing
c_d_p_lv = input('Input drag coefficient for launch vehicle parachute:  ') # drag coefficient for parachute launch vehicle
p_d_lv = input('Input diameter of launch vehicle parachute in meters:  ') # diameter of parachute in m launch vehicle
c_d_p_pay = input('Input drag coefficient for payload parachute:  ') # drag coefficient for parachute payload
p_d_pay = input('Input diameter of payload parachute in meters:  ') # diameter of parachute in m payload
m_pay = 7 * 0.453592 # mass of payload section in kg 
p_r_lv = (p_d_lv / 2) # radius of parachute in m launch vehicle
p_r_p = (p_d_lv / 2) # radius of parachute in m payload
v_d_lv = np.sqrt((2 * (m_c - m_pay) * g) / (pi * rho * c_d_p_lv * p_r_lv^2)) # descent velocity in m/s launch vehicle
k_e_lv = .5 * (m_c - m_pay) * v_d_lv^2 # kinetic energy of rocket at landing in J launch vehicle
v_d_p = np.sqrt((2 * (m_pay) * g) / (pi * rho * c_d_p_pay * p_r_p^2)) # descent velocity in m/s payload
k_e_p = .5 * (m_pay) * v_d_p^2 # kinetic energy of rocket at landing in J payload
print('Kinetic Energy of Launch Vehicle at landing: #8.3f J \n',k_e_lv)
print('Kinetic Energy of Payload at landing: #8.3f J \n',k_e_p)

## Descent Time
deploy_a = input('Input altitude for main chute deployment in feet:  ') # user input deployment altitude in ft
d_a = deploy_a * 0.3048 # altitude for main chute deploy in m
a_d = pi * .5^2 # area of drog in m
c_d_drogue = .75 # coefficient of drag for drogue
v_d_drogue = np.sqrt((2 * (m_c - m_pay) * g) / (a_d * rho * c_d_drogue)) # descent velocity in m/s
d_drogue = .75 * .5 * rho * a_d * v_d_drogue^2 # drag force of drogue
a_drogue = d_drogue / (m_c - m_pay) # drag acceleration in m/s
t_drogue = np.sqrt((2*(y_max - d_a)) / g) # time for rocket to fall before main chute deply in s
d_f = c_d_p_lv * rho * v_d_lv^2 * pi * p_r_lv^2 / 2 # drag force in N
w = (m_c - m_pay) * g # weight of rocket in N
t_vel = v_d_lv / g  # time to reach terminal velocity with parachute in sec
d_t_vel = .5 * g * t_vel^2 # distance travel during acceleration to terminal in m
d_final = d_a - d_t_vel # final distance to descend at terminal velocity in m
t_main = d_final / v_d_lv # time for final descent stage in sec
t_total = t_drogue + t_main # total time for launch vehicle to descend in s
print('Total Time for Launch Vehicle to descend: #8.3f sec \n',t_total)

## Drift Distance
w0 = 0 * 1.46667 # wind speed in ft/s
w5 = 5 * 1.46667 # wind speed in ft/s
w10 = 10 * 1.46667 # wind speed in ft/s
w15 = 15 * 1.46667 # wind speed in ft/s
w20 = 20 * 1.46667 # wind speed in ft/s
d0 = t_total * w0 # drift in ft
d5 = t_total * w5 # drift in ft
d10 = t_total * w10 # drift in ft
d15 = t_total * w15 # drift in ft
d20 = t_total * w20 # drift in ft
print('np.expected Drift if Wind Speed is 0 mph:  #8.3f ft \n',d0)
print('np.expected Drift if Wind Speed is 5 mph:  #8.3f ft \n',d5)
print('np.expected Drift if Wind Speed is 10 mph:  #8.3f ft \n',d10)
print('np.expected Drift if Wind Speed is 15 mph:  #8.3f ft \n',d15)
print('np.expected Drift if Wind Speed is 20 mph:  #8.3f ft \n',d20)