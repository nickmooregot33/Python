def P_ig(V, T):
    R = 8.314 # ideal gas constant, joules / kelvin
    return (R*T) / V

def P_vdw(V, T, T_c, P_c):
    R = 8.314 # ideal gas constant, joules / kelvin
    a = (27./64) * (R*T_c)**2 / P_c
    b = R * T_c / (8. * P_c)
    return ((R * T)/(V - b) - (a)/(V**2))

def P_rk(V, T, T_c, P_c):
    R = 8.314 # ideal gas constant, joules / kelvin
    a = 0.42748 * R**2 * T_c**2.5 / P_c
    b = 0.08662 * R * T_c / P_c
    return ((R * T)/(V - b)) - (a/((T**.5) *( V * (V + b))))

def getData():
    return {'H2':(33.19,1313000),
            'O2':(154.6,5043000),
            'N2':(126.2,3400000),
            'CO2':(304.2,7383000),
            'Ar':(150.9,4894000),
            'air':(132.2,3745000),
            'H20':(647.1,22055000),
            'butane':(408.1, 3648000)}

#print "Ideal gas law:%f" %(P_ig(0.01,100))
#print "Ideal gas law:%f"%(P_ig(.01,200))
#print "Vanderwahlz:%f"%(P_vdw(0.056634, 273.15, 190.6, 4599000))
#print "Vanderwahlz:%f"%(P_vdw(0.056634, 323.15, 190.6, 4599000)) #P_vdw(V, T, T_c, P_c)
#P_rk(V, T, T_c, P_c)
#print "Redlich-Kwong:%f"%(P_rk(0.056634, 273.15, 190.6, 4599000))
#print "Redlich-Kwong:%f"%(P_rk(0.056634, 323.15, 190.6, 4599000))
#print P_rk(0.01,373.15, gasdata['H2'][0],gasdata['H2'][1])

import numpy as np
gasdata = getData()
temps = np.array((273.15,298.15,323.15,348.15,373.15,398.15))
volume = 0.044 # m**3
Pcyl_rk = P_rk(volume, temps, gasdata['O2'][0],gasdata['O2'][1])
print Pcyl_rk
Pcyl_vdw = P_vdw(volume, temps, gasdata['O2'][0],gasdata['O2'][1])
print Pcyl_vdw
Pcyl_ig = P_ig(volume,temps)
print Pcyl_ig

import matplotlib.pyplot as plt

plt.plot(temps,Pcyl_rk,'r-',label="P_rk")
plt.plot(temps,Pcyl_vdw,'go',label="P_vdw")
plt.plot(temps,Pcyl_ig,'b.',label="P_ig")
plt.title("Pressure vs. Temperature")
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.legend(loc=4)
plt.savefig("figure_5.png")
plt.show()
#print temps[5]
six = abs((Pcyl_rk[5] - Pcyl_ig[5])/Pcyl_rk[5]) * 100
print six
volume = 0.0044 # m**3
Pcyl_rk = P_rk(volume, temps, gasdata['O2'][0],gasdata['O2'][1])
Pcyl_vdw = P_vdw(volume, temps, gasdata['O2'][0],gasdata['O2'][1])
Pcyl_ig = P_ig(volume,temps)
seven  = abs((Pcyl_rk[5] - Pcyl_ig[5])/Pcyl_rk[5]) * 100
#print "seven = %f" % seven
volume = 0.044 #m**3
Pcyl_ig = P_ig(volume, temps)
Pcyl_rk = P_rk(volume, temps, gasdata['Ar'][0], gasdata['Ar'][1])
plt.plot(temps, Pcyl_ig, 'g-',label="P_ig")
plt.plot(temps, Pcyl_rk, 'r-',label="P_rk")
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.title("Temperature vs Pressure for Argon")
plt.legend(loc=4)
plt.savefig("figure_8.png")
plt.show()
nine = abs((Pcyl_rk[5] - Pcyl_ig[5])/Pcyl_rk[5]) * 100
print "nine = %f" % nine
volume = 0.044 #m**3
Pcyl_ig = P_ig(volume,temps)
Pcyl_rk = P_rk(volume, temps, gasdata['butane'][0], gasdata['butane'][1])

plt.plot(temps, Pcyl_ig, 'g-',label="P_ig")
plt.plot(temps, Pcyl_rk, 'r-',label="P_rk")
plt.title("Temperature vs Pressure for Butane")
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.legend(loc=4)
plt.savefig("figure_10.png")
plt.show()
ten = abs((Pcyl_rk[5] - Pcyl_ig[5])/Pcyl_rk[5]) * 100
print "ten = %f"%ten
#P_ig(V, T):
print "12 = %f"%P_ig(0.000667, 248.15)
#P_vdw(V, T, T_c, P_c)
print "13 = %f"%P_vdw(0.000667, 248.15,gasdata['CO2'][0], gasdata['CO2'][1]) 
#P_rk(V, T, T_c, P_c):
print "14 = %f"%P_rk(0.000667, 248.15,gasdata['CO2'][0], gasdata['CO2'][1]) 
temps = np.linspace(100,500,101)
pig = P_ig(0.000667, temps)
prk = P_rk(0.000667, temps,gasdata['CO2'][0], gasdata['CO2'][1])
pvdw = P_vdw(0.000667, temps,gasdata['CO2'][0], gasdata['CO2'][1]) 
plt.plot(temps,pig,'r',label="P_ig")
plt.plot(temps,pvdw,'b',label="P_vdw")
plt.plot(temps,prk,'g',label="P_rk") 
plt.title("Temperature vs Pressure at Small Volume for CO2")
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.legend(loc=4)
plt.savefig("figure_15.png")
plt.show()
volume = .0000667
pig = P_ig(volume, temps)
prk = P_rk(volume, temps,gasdata['CO2'][0], gasdata['CO2'][1])
pvdw = P_vdw(volume, temps,gasdata['CO2'][0], gasdata['CO2'][1]) 
plt.plot(temps,pig,'r',label="P_ig")
plt.plot(temps,pvdw,'b',label="P_vdw")
plt.plot(temps,prk,'g',label="P_rk") 
plt.title("Temperature vs Pressure at Small Volume for CO2")
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.legend(loc=4)
plt.savefig("figure_16.png")
plt.show()
#print temps
seventeen= abs((prk[100] - pig[100])/prk[100]) * 100
print "seventeen = %f"%seventeen
eighteen= abs((prk[100] - pvdw[100])/prk[100]) * 100
print "eighteen= %f"%eighteen
