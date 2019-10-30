def drift(v, v_wind, c_d, diam, rho):
    area = np.pi * diam**2.0 / 4.0
    return 0.5*rho*(v_wind - v)**2*area + c_d*0.5*rho*(v_wind - v)**2*area
