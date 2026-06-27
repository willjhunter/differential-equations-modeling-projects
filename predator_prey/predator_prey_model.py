import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

plt.close('all')


alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4


def lotka_volterra(t, z):
    x, y = z
    
    dx = alpha * x - beta * x * y
    dy = delta * x * y - gamma * y
    
    return [dx, dy]

x0 = 10
y0 = 15

t0 = 0
t_end = 100

initial_conditions = [x0, y0]
solution = solve_ivp(
    lotka_volterra, 
    [t0, t_end],
    initial_conditions
)

t_values = solution.t
x_values = solution.y[0]
y_values = solution.y[1]

plt.plot(t_values, x_values, label='Prey x(t)')
plt.plot(t_values, y_values, label='Predator y(t)')
plt.xlabel("Time")
plt.ylabel('Population')
plt.title('Lotka-Volterra Model using solve_ivp')
plt.legend()
plt.show()

plt.plot(x_values, y_values)
plt.xlabel('Prey population x')
plt.ylabel('Predator population y')
plt.title('Predator-Prey Phase Plot')
plt.show()