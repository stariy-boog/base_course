
name = "Ivan Gavryushkin"


m_upper = "_".join(name) + "_"
ascii_upper = [ord(char) for char in m_upper.upper()]


m_lower = "_".join(name) + "_"
ascii_lower = [ord(char) for char in m_lower.lower()]


max_upper = max(ascii_upper)
min_upper = min(ascii_upper)

max_lower = max(ascii_lower)
min_lower = min(ascii_lower)


print("Наибольшее значение верхнего ригистра ", max_upper) #verxniy
print("Наименьшее значение нижнего регистра ", min_upper)# nizniy

print("Наибольшее значение верхниго ", max_lower)#verxniy
print("Наименьшее значение нижнего ", min_lower)# nizniy
