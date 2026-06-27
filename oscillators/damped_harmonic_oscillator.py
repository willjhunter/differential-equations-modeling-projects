'''
Modeling a damped harmonic oscillator using Euler's method to approximate the solution the system of differential equations. 
'''


import numpy as np 
import matplotlib.pyplot as plt 

plt.close('all')

m = 1
b = 2.4
k = 4
x0 = 1
v0 = 0
t0 = 0
t_end = 10
h = 0.1
num_steps = round((t_end - t0) / h)
energy_initial = (1/2 * m * v0**2) + (1/2 * k * x0**2)

x_approx = [x0]
v_approx = [v0]
t_approx = [t0]
energy = [energy_initial]


for j in range(num_steps):
    dx = v0
    dv = (-(b/m) * v0) - ((k/m) * x0)
    
    # Storing the current position using the velocity and the current velocity using the acceleration
    x1 = x0 + h * dx
    v1 = v0 + h * dv
    t1 = t0 + h
    
    # Update the variables in the loop 
    v0 = v1
    x0 = x1
    t0 = t1
    
    # Compute energy after the update
    energy_current = (1/2 * m * v0**2) + (1/2 * k * x0**2)
    
    #Add the updated variables to array 
    x_approx.append(x0)
    v_approx.append(v0)
    t_approx.append(t0)
    energy.append(energy_current)


discriminant = b**2 - (4*m*k)



if discriminant < 0:
    damping_type = "underdamped"
elif discriminant > 0:
    damping_type = "overdamped"
else:
    damping_type = "critically damped"

plt.plot(t_approx, x_approx, label="x(t)")
plt.plot(t_approx, v_approx, label="v(t)")
plt.title(f"Modeling a Damped Harmonic Oscillator({damping_type})")
plt.legend()
plt.show()

plt.plot(t_approx, energy)
plt.title("Energy")
plt.show()