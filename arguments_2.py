def my_func(a, b=0):
    x = 3 * a - b
    return x

# Так НЕЛЬЗЯ!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

def my_func(*args):
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))
print(my_func(3, 4, 8))