import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

	
def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y


fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r', label='Ball')

ball_line, = plt.plot([], [], '-', color='r', label='Ball') 

frames = 360

coords = np.zeros((frames, 4))

def animate(i):
    coords[i] = circle_move(R=2, angle_vel=1, time=i)
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return ball, ball_line

edge = 13
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani = FuncAnimation(fig, animate, frames=frames, interval=20)

ani.save('animation_2.gif', writer="pillow") 