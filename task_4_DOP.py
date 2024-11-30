import random
flowers = ["Роза", "Тюльпан", "Лилия", "Гвоздика", "Сирень"]
colors = ["Красный", "Желтый", "Синий", "Белый", "Розовый"]
random.shuffle(colors)
flower_color_dict = dict(zip(flowers, colors))
print(flower_color_dict)
