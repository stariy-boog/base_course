import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


t = np.linspace(0, 4*np.pi, 300)  

x1 = 12*np.cos(t) + 8 * np.cos(1.5*t)

y1 = 12 * np.sin(t) - 8 * np.sin(1.5*t)
def rotate(x,y,fi):
    x = x1 * np.cos(fi) - y1 * np.sin(fi)
    y = y1 * np.cos(fi) + x1* np.sin(fi)
    return x,y


fig, ax = plt.subplots()

ax.set_xlim(-25, 25)

ax.set_ylim(-25, 25)

line, = ax.plot([], [], lw=2)

def animate(frame):
  rotate_fi = frame / 1000 *2 * np.pi
  x,y=rotate(x1,y1,rotate_fi)
  line.set_data(x,y)
  return line,



ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=30)
ani.save('animation_9.gif', writer="pillow")
