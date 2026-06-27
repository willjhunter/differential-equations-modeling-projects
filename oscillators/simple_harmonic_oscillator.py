'''
Models a mass on a spring of a simple harmonic oscillator by using Euler's method. 
'''
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

m = 1
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
    dv = -(k/m) * x0
    
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



plt.plot(t_approx, x_approx, label="x(t)")
plt.plot(t_approx, v_approx, label="v(t)")
plt.title("Modeling a Simple Harmonic Oscillator")
plt.legend()
plt.show()

plt.plot(t_approx, energy, label='Energy')
plt.legend()
plt.show()

'''
Question: Does Euler's method conserve energy?
'''
