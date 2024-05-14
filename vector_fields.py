import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom
import random

plt.arrow(0, 0, 4, 4, width=0.02)
plt.savefig('vector.png')
plt.close()

x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
u = 1
v = -1
plt.title(f'Векторное поле скоростей, v = {v}, u = {u}')
plt.xlabel('Координата X, м')
plt.ylabel('Координата Y, м')
plt.quiver(x, y, u, v, width=0.001)
plt.savefig('vector_field_1.png')
plt.close()



u = x / np.sqrt(x**2 + y**2)
v = y / np.sqrt(x**2, y**2)
plt.title(f'Векторное поле скоростей')
plt.xlabel('Координата X, м')
plt.ylabel('Координата Y, м')
plt.quiver(x, y, u, v)
plt.savefig('vector_field_2.png')
plt.close()



u =-y / np.sqrt(x**2 + y**2)
v = x / np.sqrt(x**2 + y**2)
plt.title(f'Векторное поле скоростей')
plt.xlabel('Координата X, м')
plt.ylabel('Координата Y, м')
plt.quiver(x, y, u, v)
plt.savefig('vector_field_3.png')
plt.close()



u =-y / np.sqrt(x**2 + y**2) + y
v = x / np.sqrt(x**2 + y**2)
plt.title(f'Векторное поле скоростей')
plt.xlabel('Координата X, м')
plt.ylabel('Координата Y, м')
plt.quiver(x, y, u, v)
plt.savefig('vector_field_4.png')
plt.close()