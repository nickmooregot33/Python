import numpy as np
import matplotlib.pyplot as plt

seis=np.loadtxt('quakedata.txt')

assert seis.shape == (2,350)
from numpy import isclose
assert isclose(seis[0,1],1.0)
assert isclose(seis[1,-1],0.61910493526870258)


def rolling_mean(data, n):
    n_mean = np.zeros_like(data)
    n_mean[0,:] = data[0,:]
    tmp = data[1].size
    for i in range(0,tmp):
        if i < n:
            n_mean[1,i] = np.nan
        else:
            n_mean[1,i] = np.mean(data[1,i-n+1:i+1])

    return n_mean


def test_rolling_mean(array):
    from numpy import isclose
    rm = rolling_mean(array,2)
    assert isclose( rm[1,2],0.5*(array[1,1]+array[1,2]))
    assert isclose(rm[1,-1],0.5*(array[1,-2]+array[1,-1]))




def rolling_std(data, n):
    n_std = np.zeros_like(data)
    n_std[0,:] = data[0,:]
    tmp = data[1].size
    for i in range(0,tmp):
        if i < n:
            n_std[1,i] = np.nan
        else:
            n_std[1,i] = np.std(data[1,i-n+1:i+1])

    return n_std
    


def test_rolling_std(array):
    from numpy import isclose, std
    rs = rolling_std(array,2)
    assert isclose( rs[1, 2], std( (array[1, 1], array[1, 2])) )
    assert isclose( rs[1,-1], std( (array[1,-2], array[1,-1])) )



def quake(spans, stds):
    pass


def test_quake():
    pass

