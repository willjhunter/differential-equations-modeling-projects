'''
Code demonstrates how to animate a point following a sine curve
'''


import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.close('all')

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

point, = ax.plot([], [], "o")

def update(frame):
    x = frame 
    y = np.sin(frame)
    
    point.set_data([x], [y])
    
    return point, 

ani = FuncAnimation(
    fig, 
    update,
    frames=np.linspace(0, 10, 200),
    interval=30,
    blit=True,
    repeat=False
)
plt.show()