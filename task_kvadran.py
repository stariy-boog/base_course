import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a = 5; n = 100; s = 0.05
x = np.array([-a/2, a/2, a/2, -a/2, -a/2])
y = np.array([-a/2, -a/2, a/2, a/2, -a/2])

fig, ax = plt.subplots()
ax.set_xlim(-a*1.5, a*1.5)
ax.set_ylim(-a*1.5, a*1.5)
ax.set_aspect('equal')
line, = ax.plot([], [], lw=2)

