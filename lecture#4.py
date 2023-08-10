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

# map - функция которая применяет функцию к объекту и самй объект

# list1 = [x for x in range(1, 20)]
# print(list1)

# list1 = list(map(lambda x: x + 10, list1))
# print(list1)

# Задача
# С клавиатуры вводятся числа, в качестве разделителя - пробел. Этот набор чисел считывается как строка. 
# Как превратить list строк в list чисел?

# data = '15 58 65 74 59 62 31 20 15 48 48'     # строка
# print(data)

# data = data.split()        #  преобразует строку в список строк
# print(data)

# data = list(map(int, data.split()))  # преобразует строку в список из чисел
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
# res = filter(lambda i: i % 2 == 0, res)
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

# w - открытие для записи данных (перзаписывает т.е. стирает старое и добавляет новое)
#     - записывает данные и создает файл, если его не существует
 
# w+ - 
#     - открывает файл для записи и читет из него
#     - если файла нет, будет создан

# r+ - 
#     - открывает файл для чтения и дописывает в него
#     - если файла нет, выдаст ошибку

# # создание файла
# file = open('new.txt', 'a', encoding='UTF-8')  # encoding='UTF-8' - переводит в кириллицу, new.txt - название файла
# file.write('pole, russkoe pole\n')             # записывает строку: 'pole, russkoe pole' - это заносим в файл в виде строки
# file.close()                                   # закрывает работу с файлом

# \n и \t - переносят запись на новую строчку. 

# # чтение файл а
# # read
# file = open('new.txt', 'r', encoding='UTF-8')
# data = file.read()  # read - показывает в консоли одну строку      
# file.close()    
# print(data)         # pole, russkoe pole
# print(data.__repr__())  # показывает текст как он есть, т.е. одной строкой - 'pole, russkoe pole\npole, russkoe pole\n\tpole, russkoe pole\n\tpole, russkoe pole\n'
# print(data.split('\n')) # возвращает список строк - ['pole, russkoe pole', 'pole, russkoe pole', '\tpole, russkoe pole', '\tpole, russkoe pole', '']

# # readline
# file = open('new.txt', 'r', encoding='UTF-8')
# data1 = file.readline()  # read - считывает информацию построчно      
# data2 = file.readline()
# data3 = file.readline()
# data4 = file.readline()
# file.close()    
# print(data1[:-1])           # pole, russkoe pole \\\\\\ [:-1] - удаляет пустую строку между строками
# print(data2)                # pole, russkoe pole  

# print(data3)                    # pole, russkoe pole

# print(data4)                    # pole, russkoe pole

# # readlines
# file = open('new.txt', 'r', encoding='UTF-8')
# data = file.readlines()  # read - показывает список строк   ['pole, russkoe pole\n', 'pole, russkoe pole\n', '\tpole, russkoe pole\n', '\tpole, russkoe pole\n']
# file.close()  
# data = list(map(lambda x: x.strip(), data))  # убирает слэши: ['pole, russkoe pole', 'pole, russkoe pole', 'pole, russkoe pole', 'pole, russkoe pole']
# print(data)     

# data[1] = 'FFFFFFFFFFFFFFFFF'
# data = '\n'.join(data)              # возвращает слэши

# file = open('new.txt', 'w', encoding='UTF-8')
# file.write(data)
# file.close()

############
# # контекстный менеджер
# with open('new.txt', 'w', encoding='UTF-8') as file:   # закрывает файл автоматически, когда выходим из тела контекстного менеджера, т.е. из отступа
#     file.write(data)

# Примеры работы с файлами

## 1
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')        # здесь указываем режим в котором будем работать
#                         # a -  откроет новый файл в формате  'txt'
# data.writelines(colors)             # записывает в файл данные - colors
# data.close()                        # запускает код

## 2
# удаляет старые записи в файле и добавляет новые

# with open('file.txt', 'w') as data:  # открывает файл с именем: data
#     data.write('line 1\n')
#     data.write('line 2\n')

## 3
# режим чтения

# path = 'file.txt'
# data = open('file.txt', 'r') # окрывем файл в режиме чтения - r
# for line in data:             # проходимся по всему файлу
#     print(line)               # печатаем файл
# data.close()                  # закрываем файл