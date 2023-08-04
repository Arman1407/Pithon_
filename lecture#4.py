# В данном примере показывается, что функция "f" может заменяться фенкцией "a" с такими же свойствами

# def f(x):
#     return x*x

# a = f
# print(a(5))
# print(f(5))     

###############################

# # передача функции в другуют функцию с переменными

# # с одной переменной
# def calk1(a):
#     return a + a

# def calk2(a):
#     return a * a

# def math(op, x):
#     print(op(x))\
    
# math(calk1, 6)
# math(calk2, 5)

# # с двумя переменнымми
# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))
    
# math(calk1, 6, 7)
# math(calk2, 5, 8)

#############################

# # lambda - 

# # def calk2(a, b):
# #     return a * b

# def math(op, x, y):
#     print(op(x, y))

# # def calk1(a, b):
# #     return a + b
# # ИЛИ
# # calk1 = lambda a, b: a + b     # вставили "lambda a, b: a + b" в функцию "math(calk1, 5, 8)" вместо "calk1"

# math(lambda a, b: a + b, 5, 8)
# math(lambda a, b: a * b, 6, 7)

# Задача
# В списке хранятся числа. Нужно выбрать тотлько четные числа составить список пар (число; квадрат числа).

# from random import randint
# print(lst := [randint(1, 50) for i in range(int(input("Введите кол-во элементов списка: ")))])

# res = list()
# for i in lst:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

# ИЛИ

# def select(f, col):
#     return [f(i) for i in col]

# def where(f, col):
#     return [i for i in col if f(i)]

# from random import randint
# data = [randint(1, 50) for i in range(int(input("Введите кол-во элементов списка: ")))]

# res = select(int, data)
# print(res)
# res = where(lambda i: i % 2 == 0, res)
# print(res)
# res = list(select(lambda i: (i, i ** 2), res))
# print(res)

####################################################

# map - функция которая передает другую функцию и другой объект

# list1 = [x for x in range(1, 20)]
# print(list1)

# list1 = list(map(lambda x: x + 10, list1))
# print(list1)

# Задача
# С клавиатуры вводятся числа, в качестве разделителя - пробел. Этот набор чисел считывается как строка. 
# Как превратить list строк в list чисел?

# data = '15 58 65 74 59 62 31 20 15 48 48'

# data = list(map(int, data.split()))
# print(data)

#######
# Заменим функцию 'select' на 'map'

# def where(f, col):
#     return [i for i in col if f(i)]

# from random import randint
# data = [randint(1, 50) for i in range(int(input("Введите кол-во элементов списка: ")))]

# res = map(int, data)
# print(res)
# res = where(lambda i: i % 2 == 0, res)
# print(res)
# res = list(map(lambda i: (i, i ** 2), res))
# print(res)

#################################################

# filter - функция фильтрации

# data = [45, 87, 6, 5, 85, 94]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

#########
# Заменим функцию 'where' на 'filter'

# def where(f, col):
#     return [i for i in col if f(i)]

# from random import randint
# data = [randint(1, 50) for i in range(int(input("Введите кол-во элементов списка: ")))]

# res = map(int, data)
# print(res)
# res = filter(lambda i: i % 2 == 0, res)
# print(res)
# res = list(map(lambda i: (i, i ** 2), res))
# print(res)

#################################################

# zip - функция котроая возвращает кортежи из элементов входных данных

# qwe = ['q', 'w', 'e', 'r', 't']
# asd = [1, 2, 3, 4, 5, 6, 7]
# zxc = ['1q', '2w', '3e']
# qaz = list(zip(qwe, asd, zxc))
# print(qaz)                      # [('q', 1, '1q'), ('w', 2, '2w'), ('e', 3, '3e')] - берется по самому короткому значению

################################################

# enumerate - функция возвращает новый объект и кортеж из индекса и элементов входных данных, т.е нумерует набор данных

# list_1 = ['qwe', 'asd', 'zxc']
# data = list(enumerate(list_1))
# print(data)                         # [(0, 'qwe'), (1, 'asd'), (2, 'zxc')]

###############################################

# Файлы

# а - открытие для добавления данных
#     - позволяет дописать в имеющийся файл
#     - если файла нет, он будет создан автоматически и внего начнется запись

# r - открытие для чтения данных
#     - позволяет читать данные из файла
#     - если файла нет, выдаст ошибку

# w - открытие для записи данных
#     - записывает данные и создает файл, если его не существует
 
# w+ - 
#     - открывает файл для записи и читет из него
#     - если файла нет, будет создан

# r+ - 
#     - открывает файл для чтения и дописывает в него
#     - если файла нет, выдаст ошибку




