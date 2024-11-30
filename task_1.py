import random


array1 = []
array2 = []
array3 = []
for i in range(10):
    array1.append(random.randint(0, 100))
    array2.append(random.randint(0, 100))
    array3.append(random.randint(0, 100))


max_element = max(array1 + array2 + array3)
total_sum = sum(array1) + sum(array2) + sum(array3)

print("massiv1:", array1)
print("massiv 2:", array2)
print("massiv 3:", array3)
print("Наибольший элемент:", max_element)
print("Сумма всех элементов:", total_sum)

