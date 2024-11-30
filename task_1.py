import numpy as np 
def average(array):
    ar = 0
    for i in range(0, len(array)):
        ar += array[i]
        ar = ar / len(array)
        return ar

array = np.array([])
while 1:
    a = input()
    if a == '':
        break 
    a = int(a)
    array = np.append(array, [a])
    print(average(array))
    print(np.mean(array))
