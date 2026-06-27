import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

plt.close('all')

fig, ax = plt.subplots()

# Parameters
c = 1.0
L = 1.0
N = 100

x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Initial conditions 
u0 = np.sin(np.pi * x)  # initial string shape 
v0 = np.zeros_like(x)   # initial velocity 

# Enforced fixed endpoints
u0[0] = 0
u0[-1] = 0

# State vector contains both u and v
initial_state = np.concatenate([u0, v0])


def wave_equation(t, state):
    # Take the first N entries 
    u = state[:N]
    # Take everything from index N to the end
    v = state[N:]
    
    dudt = v
    dvdt = np.zeros_like(u)
    
    # Approximate u_xx at interior points
    dvdt[1:-1] = c**2 * (u[2:] - 2*u[1:-1] + u[:-2]) / dx**2
    
    # Boundary conditions: Fixed endpoints
    dudt[0] = 0
    dudt[-1] = 0
    dvdt[0] = 0
    dvdt[-1] = 0
    
    return np.concatenate([dudt, dvdt])

t_span = [0, 5]
t_eval = np.linspace(0, 5, 200)

sol = solve_ivp(
    wave_equation,
    t_span,
    initial_state,
    t_eval=t_eval
)

# Plot the string at a few different times
#for time_index in [0, 40, 80, 120, 160, 199]:
#    # sol.y is a 2D array. Means at this particular time, grab only the u values, not the v values. 
#    u = sol.y[:N, time_index]
#    t = sol.t[time_index]
#    plt.plot(x, u, label=f"t = {t:.2f}")

#plt.xlabel('x')
#plt.ylabel("u(x,t)")
#plt.title("1D Wave Equation: Vibrating String")
#plt.legend()
#plt.grid(True)
#plt.show()

# Initial string shape 
line, = ax.plot(x, sol.y[:N, 0])
ax.set_xlim(0, L)
ax.set_ylim(-1.2, 1.2)

def update(frame):
    u = sol.y[:N, frame]
    line.set_ydata(u)
    ax.set_title(f"t = {sol.t[frame]:.2f}")
    return line 

ani = FuncAnimation(
    fig, 
    update,
    frames=len(sol.t),
    interval=30,
    blit=False
)

plt.show()