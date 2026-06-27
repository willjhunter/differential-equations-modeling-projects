'''
A function that uses Euler's method to approximate the solution for exponential growth. 
'''

import numpy as np 
import matplotlib.pyplot as plt 


k = 0.5
h = 0.5


def function(t,y):
    return k * y
# The function should take in five inputs, the function f, initial time t0, initial y0 value, step size h, and the number of steps num_steps.
def euler(f, t0, y0, h, num_steps):
    
    # Stores the x and y values to plot for later. 
    y_approx = [y0]
    t_approx = [t0]
    t0 = t0
    
    # Euler's method implemented as a for loop. 
    for j in range(num_steps):
        slope = f(t0, y0)
        y1 = y0 + h * slope
        t1 = t0 + h
        t0 = t1
        y0 = y1
        
        y_approx.append(y0)
        t_approx.append(t0)
        
    y_approx = np.array(y_approx)
    t_approx = np.array(t_approx)
    
    return t_approx, y_approx

t_approx, y_approx = euler(function,0,2,0.5, 100)


y_exact = 2 * np.exp(k * t_approx)


plt.plot(t_approx, y_approx, label=f'Euler approximation, h={h}, k={k}')
plt.plot(t_approx, y_exact, label=f'Exact solution, k={k}')
plt.title(f"Euler's Method for y' = ky, h={h}, k={k}")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
#plt.show()