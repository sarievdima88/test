"""
def my_sum(arg_1, arg_2):
    return arg_1 + arg_2


print(my_sum(20, 30))
print(my_sum("abra", "kadabra"))


def summ(a, b):
    c = a + b
    return c


res = summ(5, 10)
print(res)


def my_func():
    pass


print(my_func())


def s_calc():
    r_val = float(input("Укажите радиус: "))
    h_val = float(input("Укажите высоту: "))
    # площадь боковой поверхности цилиндра:
    s_side = 2 * 3.14 * r_val * h_val
    # площадь одного основания цилиндра:
    s_circle = 3.14 * r_val ** 2
    # полная площадь цилиндра:
    s_full = s_side + 2 * s_circle
    return s_full


s_val = s_calc()
print(s_val)


def average(a, b, c, d):
    sum = a + b + c + d
    return sum / 4


a = 8
b = 4
c = -12
result = average(a, b, c, 10)
print(result)

z=15
def local (x):
    y=10
    print('x= {}, y={}, z={}'.format(x,y,z))
local(5)

"""


# позиционные параметры
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))


# именованные параметры
def second_func(var_2, var_1, var_3):
    print(f"Dima - {var_2}; Erdem - {var_1}; Nikolay - {var_3}")

second_func(var_1=10, var_2=20, var_3=30)