import matplotlib.pyplot as plt
import numpy as np

def plot_ellipse(a, b, N):
   
    ygol= np.linspace(0, 2 * np.pi, N)
    x = a * np.cos(ygol)
    y = b * np.sin(ygol)
    plt.plot(x, y)
    plt.title("эллипс")
    plt.axis('equal')
    plt.show()


a = 5
b = 3
N= 100
plot_ellipse(a, b, N)
plt.savefig('fig_82.png')
