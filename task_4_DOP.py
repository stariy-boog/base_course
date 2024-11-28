import random


flowers = ["Роза", "Тюльпан", "Лилия", "Гвоздика", "Сирень"]


colors = ["Красный", "Желтый", "Синий", "Белый", "Розовый"]


flower_color_dict = {flower: random.choice(colors) for flower in flowers}

#
print(flower_color_dict)
