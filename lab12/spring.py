"""
Compose a function `fit_spring_data` which accepts as a parameter a filename `datafile`.  This function should return the spring constant obtained from fitting the data in that file to a line.
"""

def fit_spring_data(datafile):
    import numpy as np
    import numpy.polynomial.polynomial as pf
    data = np.loadtxt(datafile)
    x = data[0]
    y = data[1]
    fit = pf.polyfit(x,y,1)
    return abs(fit[1])

