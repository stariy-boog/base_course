import matplotlib.pyplot as plt
import numpy as np
def hyperbola_plot(x_min, x_max, N)
x = np.linspace(x_min, x_max, N)
y = 1/x
plt.xlabel('Coord: x') 
plt.ylabel('Coord: y') 
plt.title('Hyperbola')