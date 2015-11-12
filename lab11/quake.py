import numpy as np
import matplotlib.pyplot as plt

"""
Compose a function rolling_mean which accepts as parameters an array with rows of time values and of measurements (just like seis) data, and a window size n.

Create a new array n_mean = np.zeros_like(data). Assign the first row of data to n_mean (the time values are the same).

Now loop through the length of the array (since you want the index, not the row). For the n values close to the beginning of the array, you will assign np.nan (not a number) to the array entry (since there are not yet n values to calculate a moving-window average with). For values n and greater, use the last n data points to calculate the moving-window average and assign that value to the array entry in the second row. This expression may help:

np.mean(data[i-n+1:i+1,1])  # where i is the loop counter
The function should return the resulting array of time points and calculated rolling-window means.
"""

def rolling_mean(data, n):
    pass


def test_rolling_mean(array):
    pass


"""
Compose a function rolling_std which accepts as parameters an array with rows of time values and of measurements (just like seis) data, and a window size n.

Create a new array n_std = np.zeros_like(data). Assign the first row of data to n_std (the time values are the same).

Now loop through the array. For values closer than n to the lower end of the array, you will assign np.nan (not a number) to the array entry. For values n and greater, use the last n data points to calculate the moving-window standard deviation and assign that value to the array entry in the second row.

The function should return the resulting array of time points and calculated rolling-window means.
"""

def rolling_std(data, n):
    pass


def test_rolling_std(array):
    pass


"""
Compose a function quake which accepts as parameters a list of time lengths spans and a list of corresponding standard deviations stds.

The function should first ensure that the lists are the same length and contain only numbers; if either condition is not true, then the function should halt and return None.

Next, create an array data = np.zeros( (np.sum(spans), 2) ). The function should loop over the time length spans in spans and generate a corresponding number of random data points with the standard deviation in stds. The time should increase uniformly (i.e., starting from 0 each time step is one more than the previous time step—the time value and the index will be the same, although one is float and one is int). One way to do this is to assign np.array(range(np.sum(spans)) to the first row of data.

The random data points will be created using numpy.random.normal. Make sure that your scale value in the function is taken from the current element of stds instead.

The function should return the resulting array of time points and generated measurements.
"""

def quake(spans, stds):
    pass


def test_quake():
    pass

