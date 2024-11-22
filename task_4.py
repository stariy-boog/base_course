import numpy as np
N = int(input('Значение:'))
M = int(input('Значение:'))
trigonometry_array = np.zeros((N, M))
for i in range(0,N):
    for j in range(0, M):
        trigonometry_array[i,j] = np.sin(N * i + M * j + 1)
    if trigonometry_array[i,j] < 0:    
        trigonometry_array[i,j] = 0

print(trigonometry_array)
