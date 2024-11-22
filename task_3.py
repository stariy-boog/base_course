import numpy as np
from task_1 import g 
v0x = int(input("Значение:"))
x0 = int(input("Значение:"))
y0 = int(input("Значение:"))
massiv = [['t', 'x', 'y']]
for t in range(0, 6):
    x = x0 + v0x * t 
    y = y0 + v0x * t - g * t**2 / 2  
    massiv.append([t, x , y])
massiv = np.array(massiv)
print(massiv)
