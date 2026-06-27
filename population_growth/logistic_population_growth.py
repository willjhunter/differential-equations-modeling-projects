'''
Model population growth with limited resources. 
'''


import numpy as np 
import matplotlib.pyplot as plt 
from euler_method.euler import euler

r = 0.3
K = 1000
t_end = 100
t0 = 0
y0 = 10

# Clears all old figures before making a new one
plt.close('all')

def f(t,y):
    return r * y * (1 - (y/K))


# Used a for loop to plot different graphs with varying step sizes. t_end lets me control how big I want the x axis to be 
for h in [0.5, 0.1, 0.01]:
    num_steps = round((t_end - t0) / h)
    x_approx, y_approx = euler(f, t0, y0, h, num_steps)
    plt.plot(x_approx, y_approx, label=f"h = {h}")

plt.title("Modeling Logistic Population Growth")
plt.legend()
plt.show()