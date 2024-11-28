import numpy as np 

N = 10  
array1 = np.random.randint(0, 101, size=N)
array2 = np.random.randint(0, 101, size=N)
array3 = np.random.randint(0, 101, size=N)


max_element = max(np.max(array1), np.max(array2), np.max(array3))

total_sum = np.sum(array1) + np.sum(array2) + np.sum(array3)

print("Наибольший элемент:", max_element)

print("Сумма всех элементов:", total_sum)
