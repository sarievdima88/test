"""
def my_sum(arg_1, arg_2,):
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


# позиционные параметры
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))


# именованные параметры
def second_func(var_2, var_1, var_3):
    print(f"Dima - {var_2}; Erdem - {var_1}; Nikolay - {var_3}")

second_func(var_1=10, var_2=20, var_3=30)




def s_calc():
    try:
        r_val = float(input("Укажите радиус: "))
        h_val = float(input("Укажите высоту: "))
    except ValueError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return s_side, s_full, s_circle


s_side_val, s_circle, s_full_val = s_calc()
print(f"Площадь боковой пов-ти - {s_side_val};Площадь цилиндра - {s_circle} Полная площадь - {s_full_val}")

def my_func(*args):
    return

print(my_func(el_1=10, el_2=20, el_3="text"))

my_func = lambda p_1, p_2: p_1 + p_2

print(my_func(2, 5))
print(my_func("abra", "kadabra"))

print((lambda p_1, p_2: p_1 + p_2)(2, 5))
print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))

new_func = lambda *args: args
print(new_func(10, 20, 30, 40))

# f = lambda x: x ** 2

print((lambda x: x / 2)(4))

print(ord("G"))
print(chr(71))
print(len("abrakadabra12"))

print(abs(4.0))
print(round(4,4600))
print(divmod(9, 2))
print(pow(16, 2))

iter_obj = [20, 2, 5, 100]
print(sum(iter_obj))
iter_obj = (20, 2, 5, 100)
print(sum(iter_obj))
iter_obj = {20, 2, 5, 100}
print(sum(iter_obj))
"""
print(list(range(10)))
print(tuple(range(10)))
