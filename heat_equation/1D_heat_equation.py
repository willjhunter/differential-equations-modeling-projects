import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation


plt.close('all')

fig, ax = plt.subplots()

D = 0.1
L = 1.0
N = 100

x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Initial conditions
u0 = np.piecewise(x, [(x < 0.4),((x >= 0.4) & (x <= 0.6)),(x > 0.6)], [0, 1, 0])


# Boundary conditions
u0[0] = 0
u0[-1] = 0

def heat_equation(t, state):
    u = state[:N]
    dudt = np.zeros_like(u)
    
    dudt[1:-1]= (D * (u[2:] - 2*u[1:-1] + u[:-2]) / dx**2)
    
    dudt[0] = 0
    dudt[-1] = 0
    
    return dudt

t_span = [0, 5]
t_eval = np.linspace(0, 5, 200)

sol = solve_ivp(
    heat_equation,
    t_span,
    u0,
    t_eval=t_eval
)

line, = ax.plot(x, sol.y[:N, 0])
ax.set_xlim(0, L)
ax.set_ylim(-1.2, 1.2)

def update(frame):
    u = sol.y[:N, frame]
    line.set_ydata(u)
    ax.set_title(f"t = {sol.t[frame]:.2f}")
    return line,  

ani = FuncAnimation(
    fig, 
    update,
    frames=len(sol.t),
    interval=50,
    blit=False,
    repeat=False
)

plt.xlabel('Position x')
plt.ylabel('Temperature u(x,t)')
plt.show()