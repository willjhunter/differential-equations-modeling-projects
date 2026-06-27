import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

plt.close('all')

fig, ax = plt.subplots()

D = 0.1
r = 0.3
L = 1.0
N = 100

x = np.linspace(0, L, N)
dx = x[1] - x[0]

t_span = [0, 5]
t_eval = np.linspace(0, 5, 200)

# Initial conditions
u0 = np.exp(-100 * ((x - 0.5)**2))

u0[0] = 0
u0[-1] = 0

def logisitic_reaction_diffusion_equation(t, state):
    u = state[:N]
    dudt = np.zeros_like(u)
    
    dudt[1:-1] = (
        (u[1:-1]) + 
        ((D * (u[2:] - 2*u[1:-1] + u[:-2]) / dx**2) + 
        (r * u[1:-1] * (1 - u[1:-1])))
    )
    dudt[0] = 0
    dudt[-1] = 0 
    
    
    return dudt

sol = solve_ivp(
    logisitic_reaction_diffusion_equation,
    t_span,
    u0,
    t_eval=t_eval
)

line, = ax.plot(x, sol.y[:N, 0])
ax.set_xlim(0, L)
ax.set_ylim(0, 1.3)
ax.set_xlabel('x')
ax.set_ylabel('u(x,t)')
ax.set_title('Logistic Reaction-Diffusion Equation')

def update(frame):
    u = sol.y[:N, frame]
    line.set_ydata(u)
    ax.set_label(f"t = {sol.t[frame]:.2f}")
    return line,  

ani = FuncAnimation(
    fig, 
    update,
    frames=len(sol.t),
    interval=70,
    blit=False,
    repeat=False
)

ax.legend()
plt.show()