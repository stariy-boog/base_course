import numpy as np
from scipy.constants import g
x0 = 0
y0 = 0
v0 = 0
alpha = np.radians(45)
v0x = v0 * np.cos(alpha)
v0y = v0 * np.sin(alpha)
results = []
for t in range(6):
    x = x0 + v0x * t
    y = y0 + v0y * t - 0.5 * g * t ** 2
    results.append((t, x, y))
for row in results:
    print(f"t: {row[0]}, x: {row[1]:.2f}, y: {row[2]:.2f}")