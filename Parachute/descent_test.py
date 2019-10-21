import numpy as np
import matplotlib.pyplot as plt

def area(d):
    return np.pi*(d/2.0)**2


def rk4(yn, f, h):
    shp = yn.shape
    yn = yn.flatten()
    k1 = (f(yn) * h).flatten()
    y = yn + 0.5 * k1
    k2 = (f(y) * h).flatten()
    y = yn + 0.5 * k2
    k3 = (f(y) * h).flatten()
    y = yn + k3
    k4 = (f(y) * h).flatten()
    return (yn + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0).reshape(shp)


## Parachute Properties

c_D_d = 1.5
c_D_s = 0.45
diameter = 1.2  # ft
A_top = area(diameter)  # ft^2
A_side = area(diameter)/2.0  # ft^2
mass = 0.155405  # slug
v_y = 0.0
v_x = 0.

## atmospheric properties

rho = 0.0023769  # slug/ft^3
g = 32.17405  # ft/s^2
v_wind = 60.0  # ft/s

# force balance
f_g = mass*g
f_d_y = 0.5*rho*A_top*c_D_d*v_y**2
f_w = 0.5*rho*A_side*(v_wind - v_x)**2
f_d_x = c_D_s*0.5*rho*A_side*(v_wind - v_x)**2

a_x = (0.5 * rho * A_side * (v_wind - v_x) ** 2 - c_D_s * 0.5 * rho * A_side * (v_wind - v_x) ** 2)/mass
a_y = mass*g - 0.5*rho*A_top*c_D_d*v_y**2

def f(state):
    v_x, v_y, r_x, r_y = state
    r_x = v_x
    r_y = v_y
    v_x = (0.5 * rho * A_side * (v_wind - v_x) ** 2 - c_D_s * 0.5 * rho * A_side * (v_wind - v_x) ** 2) / mass
    v_y = mass * g - 0.5 * rho * A_top * c_D_d * v_y ** 2
    return np.array([v_x, v_y, r_x, r_y])


s = np.array([0, 0, 0, 0])
res = []
for i in range(150):
    res.append(s)
    s = rk4(s, f, 0.1)
res.append(s)
res = np.asarray(res)
plt.figure(1)
plt.plot(res[:, 0], 40 - res[:, 1])
plt.figure(2)
plt.plot(res[:, 2], 40 - res[:, 3])
# plt.xlim(0, 40)