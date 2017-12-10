import numpy as np

# Create array of time indices.
t_start = 0.0                           # initial time, s
t_end = 1.001                           # final time, s
dt = 1e-3                               # time step size, s
times = np.arange(t_start, t_end, dt)   # array of time steps
nt = len(times)                         # number of time steps

# Create solar sail body.
sail = {'m': 44.8,                  # kg
        'x': np.zeros( (nt, 2) )}   # position history, m
sail['x'][0] = np.array( (0, 0) )   # initial position, m
sail['x'][1] = np.array( (0, 0) )   # initial position, m

# Integrate equations of motion forward.
for i,t in enumerate(times):
    if i == 0:
        continue    # if first time step, we already have initial condition
    if i+1 == nt:
        continue    # the last time step is calculated in the loop prior
    
    # Calculate force on body.
    force = np.array( ( 5.0 , 0.0 ) )   # force along x-axis, N
    
    # Update position.
    xnew = 2*sail['x'][i] - sail['x'][i-1] + force/sail['m']*dt**2
    
    sail['x'][i+1] = xnew
    
    # Output the results.
    print 'Time %f:  sail at (%f, %f).'%(t,sail['x'][i,0],sail['x'][i,1])

print 'The final position of the solar sail is (%f, %f).'%(sail['x'][-1,0],sail['x'][-1,1])
