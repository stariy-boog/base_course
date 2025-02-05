import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heart_equation(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

t = np.linspace(0, 2*np.pi, 1000)  
x, y = heart_equation(t)

fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

line, = ax.plot([], [], lw=2, color='red') 

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20)
ani.save('animation_5.gif', writer="pillow")

