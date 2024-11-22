import numpy as np
N = int(input('Значение:'))
M = int(input('Значение:'))
trigonometry_array = np.zeros((N, M))
for i in range(0,N):
    for j in range(0, M):
        trigonometry_array[i,j] = np.sin(N * i + M * j + 1)
    if trigonometry_array[i,j] < 0:    
        trigonometry_array[i,j] = 0

n = int(input('Выберете первый столбец:'))
m = int(input('Выберете второй столбец:'))
for i in range(0,N):
    trigonometry_array[i, n- 1], trigonometry_array[i, m - 1] = trigonometry_array[i, m - 1], trigonometry_array[i, n - 1]
    print(trigonometry_array)