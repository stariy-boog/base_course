import numpy as np
def func(x):
    y = x**2
    return y

print('Значение параметров:')
a = int(input('Значение a:'))
b = int(input('Значение b:'))
N = int(input('Значение N:'))
array = np.linspace(a, b, N+2)
array = np.delete(array, [0, -1])
print(func(array))