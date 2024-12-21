import numpy as np
import matplotlib.pyplot as plt
k = 1
f = np.linspace(0.01, 9 * np.pi, 1000)
r = k / np.sqrt(f)
x = r * np.cos(f)
y = r * np.sin(f)
plt.figure()
plt.plot(x,y)
plt.show()
plt.savefig('fig_9.png')