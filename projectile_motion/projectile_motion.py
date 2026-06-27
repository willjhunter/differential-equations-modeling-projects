import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

g = 9.8 
v0_magnitude = 40
t_span = [0, 5]
t_eval = np.linspace(0, 5, 300)
theta = np.deg2rad(45)

def function(t,z):
    x, y, v_x, v_y = z

    dxdt = v_x
    dydt = v_y
    dv_x = -c * v_x
    dv_y = -g - c*v_y
    
    return [dxdt, dydt, dv_x, dv_y]

# An event function that returns the quantity you want to be zero
def hit_ground(t, z):
    x, y, v_x, v_y = z
    return y 

# Stop the solver when this happens
hit_ground.terminal = True 
# Only detect the crossing when y is moving from position to negative. Avoids counting the initial point y = 0 at launch. 
hit_ground.direction = -1

v_x_initial = v0_magnitude * np.cos(theta)
v_y_initial = v0_magnitude * np.sin(theta)
initial_conditions = [0, 1, v_x_initial, v_y_initial]

for c in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
    sol = solve_ivp(
        function,
        t_span,
        initial_conditions,
        t_eval=t_eval,
        events=hit_ground,
        dense_output=True
    )
    plt.plot(sol.y[0], sol.y[1], label=f'{c}')
    
# Point at t = 3
z_at_3 = sol.sol(3)
x_at_3 = z_at_3[0]
y_at_3 = z_at_3[1]

plt.scatter(x_at_3, y_at_3)
plt.text(x_at_3, y_at_3, f"  t = 3\n y = {y_at_3:.2f}")

# Ground hit point
t_hit = sol.t_events[0][0]
z_hit = sol.sol(t_hit)
x_hit = z_hit[0]
y_hit = z_hit[1]

plt.scatter(x_hit, y_hit)
plt.text(x_hit, y_hit, f"  hit ground\n  t = {t_hit:.2f}\n  x = {x_hit:.2f}")

# Max height
max_index = np.argmax(sol.y[1])
x_max = sol.y[0][max_index]
y_max = sol.y[1][max_index]
t_max = sol.t[max_index]

plt.scatter(x_max, y_max)
plt.text(x_max, y_max, f"  max height\n  t = {t_max:.2f}\n  y = {y_max:.2f}")

plt.xlabel('x distance')
plt.ylabel('y distance')
plt.title('Projectile motion with key points')
plt.legend()
plt.grid(True)
plt.show()
