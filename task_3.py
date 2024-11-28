import numpy as np
g = 10
def energy(m, h, v):
    E = (m * v ** 2)/2 + m*g*h 
    return E 
print(energy(int(input('Massa:')),  int(input('Высота?')), int(input('Скорость?'))))
