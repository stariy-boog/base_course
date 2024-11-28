import numpy as np
def area(figur):

    if figur == '1':
        r = int(input('Radius -'))
        area = np.pi*(r**2)


    if figur == '2':
        a = int(input('Dlina - '))
        b = int(input('Shirina - '))
        area = a*b

    if figur == '3':
        k = int(input('Osnovanie - '))
        h = int(input('Visota - '))
        area = (k*h)/2
    return area
print(area(input('Figuru выбирай - ')))\

# 1 - круг    2- прямокугольник  3 - треугольник