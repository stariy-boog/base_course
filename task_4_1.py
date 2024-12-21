import numpy as np
import matplotlib.pyplot as plt
b = 0.2
f = np.linspace(0,8 *np.pi, 1000)
r = np.exp(b*f)
x = r * np.cos(f)
y = r * np.sin(f)
plt.plot(x,y)
plt.show()
plt.axis('equal')
plt.savefig('fig_7.png')
