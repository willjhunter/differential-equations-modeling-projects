'''
Simulating the temperature of an object in a room using Newton's law of Cooling. 
'''



import numpy as np 
import matplotlib.pyplot as plt 
from euler_method.euler import euler


k = 0.8
h = 0.1
y_room = 22

def function(t,y):
    return -k * (y - y_room)

x_approx, y_approx = euler(function, 0, 90, h, 100)
y_exact = y_room + (90 - y_room) * np.exp(-k * x_approx)
error = y_exact - y_approx

plt.plot(x_approx, y_approx, label=f"Euler approximation with k = {k}, h={h}")
plt.plot(x_approx, y_exact, label=f"Exact solution with k={k}, h={h}")
plt.title(f"Modeling Newton's Law of Cooling")
plt.xlabel(f"Time")
plt.ylabel(f"Temperature")
plt.legend()
plt.show()

plt.plot(error, label='Error')
plt.show()


# Code below here shows how we can see what value of x outputs a certain y value. 
target_temp = 40

index = np.argmin(np.abs(y_approx - target_temp))

time_value = x_approx[index]
temperature_value = y_approx[index]

print(f"Temperature is closest to {target_temp} at t = {time_value}")
print(f"Actual approximate temperature there is {temperature_value}")
