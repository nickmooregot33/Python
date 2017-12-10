import numpy as np

def dist(a):
    return np.sqrt(np.sum(a**2))

def f_g(m1, x1, m2, x2):
    d  = dist(x2 - x1)
    G  = 1.0
    return -G * m1 * m2 / d**3 * (x2-x1)

# Create array of time indices.
t_start = 0.0                           # initial time
t_end = 750                            # final time
dt = 1e-3                               # time step size
times = np.arange(t_start, t_end, dt)   # array of time steps
nt = len(times)                         # number of time steps

# Create bodies for earth and moon.
earth = {'m': 1000,                  # mass
         'x': np.zeros( (nt, 2) )}  # position history
earth['x'][0] = np.array( (0, 0) )  # initial position
earth['x'][1] = np.array( (0, 0) )  # initial position

moon  = {'m': 0.01,                    # mass
         'x': np.zeros( (nt, 2) )}  # position history
moon_vel = 1.0                      # initial velocity of moon
moon['x'][0] = np.array( ( moon_vel*dt/2, 100) ) # initial pos + vel
moon['x'][1] = np.array( (-moon_vel*dt/2, 100) ) # initial pos + vel

# Integrate equations of motion forward.
for i,t in enumerate(times):
    if i == 0 or i+1 == nt:
        continue    # if first time step, we already have initial condition
                    # and the last time step is calculated in the loop prior
    
    # Calculate forces on earth and moon
    force = f_g(moon['m'], moon['x'][i], earth['m'], earth['x'][i])
    
    # Update position of moon (earth is stationary)
    moon['x'][i+1]  = 2*moon['x'][i]  - moon['x'][i-1]  - force/moon['m'] *dt**2
    
import matplotlib.pyplot as plt
plt.plot(moon['x'][:,0],  moon['x'][:,1],  'b-',
         earth['x'][:,0], earth['x'][:,1], 'ro')
plt.show()
