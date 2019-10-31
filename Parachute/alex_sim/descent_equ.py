import sympy as sy


def descent_equ(mass, area, c_d_fall):
    r_y, v_y = sy.symbols("r_y, v_y")
    g = 32.17405  # ft/s^2
    m = mass  # slugs
    rho = 0.0023769  # slug/ft^3
    A_top = area  # ft^2
    c_d = c_d_fall

    d_r_y = v_y

    d_v_drag = (c_d * 0.5 * rho * (A_top / 2.0) * v_y**2)/mass
    d_v_y = d_v_drag - m * g

    var = [r_y, v_y]
    equs = sy.Matrix([d_r_y, d_v_y])
    l_equ = sy.lambdify([var], equs)
    return l_equ
