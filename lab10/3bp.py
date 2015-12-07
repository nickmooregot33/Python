import numpy as np

def dist(a):
    return np.sqrt(np.sum(a**2))

def f_g(m1, x1, m2, x2):
    d  = dist(x2 - x1)
    G  = 1.0
    return -G * m1 * m2 / d**3 * (x2-x1)

# Create array of time indices.
t_start = 0.0                           # initial time
t_end = 50                             # final time
dt = 1e-3                               # time step size
times = np.arange(t_start, t_end, dt)   # array of time steps
nt = len(times)                         # number of time steps

# Create three orbiting bodies.
bodies = []

earth = {'m': 1000,                 # mass
         'x': np.zeros( (nt, 2) )}  # position history
earth['x'][0] = np.array( (0, 0) )  # initial position
earth['x'][1] = np.array( (0, 0) )  # initial position
bodies.append(earth)

moon = {'m': 0.01,                  # mass
        'x': np.zeros( (nt, 2) )}   # position history
moon_vel = 1.0                      # initial velocity of moon
moon['x'][0] = np.array( (-moon_vel*dt/2, 100) ) # initial position
moon['x'][1] = np.array( ( moon_vel*dt/2, 100) ) # initial velocity
bodies.append(moon)

caps = {'m': 0.001,                 # mass
       'x': np.zeros( (nt, 2) )}    # position history
caps_vel = 1.0                      # initial velocity of capsule
caps['x'][0] = np.array( (-caps_vel*dt/2, 20) ) # initial pos + vel
caps['x'][1] = np.array( ( caps_vel*dt/2, 20) ) # initial pos + vel
bodies.append(caps)


# Integrate equations of motion forward.  (This will be your `loop` function.)
for i,t in enumerate(times):
    if i == 0 or i+1 == nt:
        continue    # if first time step, we already have initial condition
                    # and the last time step is calculated in the loop prior
    
    # Calculate forces on bodies.
    forces = np.zeros( (len(bodies), 2) )
    for body_j in range(len(bodies)):
        for body_k in range(body_j+1, len(bodies)):
            this_force = f_g(bodies[body_j]['m'], bodies[body_j]['x'][i], bodies[body_k]['m'], bodies[body_k]['x'][i])
            forces[body_j] += this_force
            forces[body_k] -= this_force
            
    # Update position of moon (earth is stationary)
    for body_j in range(len(bodies)):
        bodies[body_j]['x'][i+1] = 2*bodies[body_j]['x'][i] - bodies[body_j]['x'][i-1] - forces[body_j]/bodies[body_j]['m'] *dt**2
    
    print i

import matplotlib.pyplot as plt
plt.plot(moon['x'][:,0],  moon['x'][:,1],  'b-',
         earth['x'][:,0], earth['x'][:,1], 'ro',
         caps['x'][:,0],  caps['x'][:,1],  'c-')
plt.show()
