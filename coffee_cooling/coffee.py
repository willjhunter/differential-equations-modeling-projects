'''
Make sure to use run and debug when running this so it actually works 
'''



import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from euler_method.euler import euler

plt.close('all')

# 1. Load the CSV file into a DataFrame
df = pd.read_csv('/Users/willhunterjr/diffeq-projects/coffee_cooling/synthetic_ceramic_mug_coffee_temperature_2hr.csv')

# 2. Select columns to plot (Replace 'X_Column' and 'Y_Column' with your actual CSV headers)
plt.plot(df['minute'], df['temperature_c'], label="Data")

k = 0.025
h = 1.0
y_room = 22
t0 = 0
y0 = 88.0
t_end = 120
num_steps = round((t_end - t0) / h)

def function(t,y):
    return -k * (y - y_room)


for k in [0.01, 0.015, 0.02, 0.025 ]:
    x_approx, y_approx = euler(function, t0, y0, h, num_steps)
    plt.plot(x_approx, y_approx, label=f"Model with k = {k}")
    residual = df['temperature_c'] - y_approx
    plt.plot(residual, label=f"Residual with k = {k}")
    plt.xlabel('Time')
    plt.ylabel('Temperature in C')

plt.legend()
plt.show()
