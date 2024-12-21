import matplotlib.pyplot as plt
import numpy as np
def hyperbola_plot( x_min, x_max, N):
    x = np.linspace(x_min, x_max, N)
    x != 0
    y = 1/x
    plt.plot(x,y)
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.title('hyperbola')
    plt.axis('equal')
    plt.show()


x_min = -10
x_max = 10
N = 100
hyperbola_plot(  x_min, x_max, N)
plt.savefig('fig_81.png')