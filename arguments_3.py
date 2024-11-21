def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))