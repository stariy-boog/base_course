import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


t = np.linspace(0, 4*np.pi, 300)  

x1 = np.cos(t) + 8 * np.cos(1.5*t)

y1 = 12 * np.sin(t) - 8 * np.sin(1.5*t)



fig, ax = plt.subplots()

ax.set_xlim(-25, 25)

ax.set_ylim(-25, 25)



line, = ax.plot([], [], lw=2)

def animate(frame):
    fi = 0.01 * frame

    x = x1 * np.cos(fi) - y1* np.sin(fi)

    y = y1 * np.cos(fi) + x1 * np.sin(fi)

    line.set_data(x[:frame], y[:frame])

    return line,



ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=30)
ani.save('animation_8.gif', writer="pillow")
