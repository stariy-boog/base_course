import numpy as np


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])


column_index_1 = 0
column_index_2 = 2


arr[:,[column_index_1, column_index_2]] = arr[:,[column_index_2, column_index_1]]


print(arr)