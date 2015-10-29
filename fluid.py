def P_ig(V, T):
    R = 8.314 # ideal gas constant, joules / kelvin
    pass

def P_vdw(V, T, T_c, P_c):
    R = 8.314 # ideal gas constant, joules / kelvin
    a = (27./64) * (R*T_c)**2 / P_c
    b = R * T_c / (8. * P_c)
    pass

def P_rk(V, T, T_c, P_c):
    R = 8.314 # ideal gas constant, joules / kelvin
    a = 0.42748 * R**2 * T_c**2.5 / P_c
    b = 0.08662 * R * T_c / P_c
    pass

def getData():
    return {'H2':(33.19,1313000),
            'O2':(154.6,5043000),
            'N2':(126.2,3400000),
            'CO2':(304.2,7383000),
            'Ar':(150.9,4894000)}

