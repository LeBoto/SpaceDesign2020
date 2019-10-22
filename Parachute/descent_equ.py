
import sympy as sy


def descent_equ(mass, area, c_d_fall, c_d_drift, v_w):
    r_x, r_y, v_x, v_y = sy.symbols("r_x, r_y, v_x, v_y")
    v_wind = v_w
    g = 32.17405  # ft/s^2
    m = mass  # slugs
    rho = 0.0023769  # slug/ft^3
    A_top = area  # ft^2
    c_D = c_d_fall
    c_d = c_d_drift

    d_r_x = v_x
    d_r_y = v_y
    d_v_x = c_d*0.5 * rho * (A_top /2.0) * (v_wind - v_x) ** 2
    d_v_y = 0.5 * rho * A_top * c_D * v_y ** 2 - m * g

    var = [r_x, r_y, v_x, v_y]
    equs = sy.Matrix([d_r_x, d_r_y, d_v_x, d_v_y])
    l_equ = sy.lambdify([var], equs)
    return l_equ