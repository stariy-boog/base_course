import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def butterfly_equation(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
    return x, y


t = np.linspace(0, 12*np.pi, 1000) 

x, y = butterfly_equation(t)
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

line, = ax.plot([], [], lw=2)

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20)
ani.save('animation_4.gif', writer="pillow")