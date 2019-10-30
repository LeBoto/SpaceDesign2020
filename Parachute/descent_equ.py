import sympy as sy


def descent_equ(mass, area, c_d_fall, v_w):
    r_x, r_y, v_x, v_y = sy.symbols("r_x, r_y, v_x, v_y")
    v_wind = v_w
    # wind frame
    v_w = sy.sqrt((v_x - v_wind)**2 + v_y**2)
    tht_w = sy.atan2(v_y, (v_x - v_wind))

    g = 32.17405  # ft/s^2
    m = mass  # slugs
    rho = 0.0023769  # slug/ft^3
    A_top = area  # ft^2
    c_d = c_d_fall

    d_r_x = v_w*sy.sin(tht_w)
    d_r_y = v_w*sy.cos(tht_w)

    d_v_drag = (c_d * 0.5 * rho * (A_top / 2.0) * v_w**2)/mass
    d_v_x = d_v_drag*sy.sin(tht_w)
    d_v_y = d_v_drag*sy.cos(tht_w) - m * g

    var = [r_x, r_y, v_x, v_y]
    equs = sy.Matrix([d_r_x, d_r_y, d_v_x, d_v_y])
    l_equ = sy.lambdify([var], equs)
    return l_equ
