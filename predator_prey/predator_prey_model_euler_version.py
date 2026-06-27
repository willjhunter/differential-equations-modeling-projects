'''
Model rabbits and foxes using the Lotka-Volterra equations where x is prey and y is predator. 
'''
import numpy as np 
import matplotlib.pyplot as plt 

plt.close('all')

alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4
x0 = 10
y0 = 15
t0 = 0
h = 0.01
t_end = 100
num_steps = round((t_end - t0) / h)

x_approx = [x0]
y_approx = [y0]
t_approx = [t0]


for j in range(num_steps):
    # Lotka-Volterra equations 
    dx = (alpha * x0) - (beta * x0 * y0)
    dy = (delta * x0 * y0) - (gamma * y0)
    
    # Euler's method 
    x = x0 + h * dx
    y = y0 + h * dy
    t = t0 + h
    
    # Update loop variables
    x0 = x
    y0 = y
    t0 = t
    
    # Append the updated variables to our arrays
    x_approx.append(x0)
    y_approx.append(y0)
    t_approx.append(t0)
    
    
plt.plot(t_approx, x_approx, label='Prey x(t)')
plt.plot(t_approx, y_approx, label='Predator y(t)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Predator-Prey Model')
plt.legend()
plt.show()

plt.plot(x_approx, y_approx, label='y(x)')
plt.xlabel('Prey population x')
plt.ylabel('Predator population y')
plt.title('Predator-Prey Phase Plot')
plt.legend()
plt.show()