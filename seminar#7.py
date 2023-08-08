# lambda

# def summa(a, b):
#     result = a + b
#     return result
# # ИЛИ
# lambda a, b: a + b

########
# def key_sort(a):
#     return a[1]
# # ИЛИ
# lst = [(1,2), (3,4), (2,5)]
# print(max(lst, key=lambda x: x[1]))

#########################
# map - принимает функцию и коллекцию и применяет эту функцию к коллекции

# nums = list('1234567890')
# print(nums)

# for i in range(len(nums)):
#     nums[i] = int(nums[i])
# print(nums)

# # ИЛИ

# nums = list(map(int, nums))
# print(nums)           # список

# print(*nums)          # цифры

# nums = list(map(lambda x: x**2, nums))
# print(nums)
# nums = list(map(lambda x: str(x) if x % 2 == 0 else x, nums)) # четные цыфры стали строками, нечетный - цифрами
# print(nums)

# Введение цифр через пробел

# nums = input('Введите числа через пробел: ')
# nums = list(map(int, nums.split()))              # список чисел только из вводимых чисел
# print(nums)

# nums = list(map(int, filter(lambda x: x.isdigit(), nums.split())))   # выводит те значения где только цифры
# print(nums)

# nums = list(map(int, filter(lambda x: x.isdigit(), nums)))   # выводит список цифр из любых вводимых значений
# print(nums)
#################################

# zip

# n = list('123654879756')
# m = list ('khkbkjnihnjk')

# new_list = []                     # [('1', 'k'), ('2', 'h'), ('3', 'k'), ('6', 'b'), ('5', 'k'), ('4', 'j'), ('8', 'n'), ('7', 'i'), ('9', 'h'), ('7', 'n'), ('5', 'j'), ('6', 'k')]
# for i in range(len(n)):
#     new_list.append((n[i], m[i]))
# print(new_list)

# # ИЛИ 

# new_list = list(zip(n, m))       # [('1', 'k'), ('2', 'h'), ('3', 'k'), ('6', 'b'), ('5', 'k'), ('4', 'j'), ('8', 'n'), ('7', 'i'), ('9', 'h'), ('7', 'n'), ('5', 'j'), ('6', 'k')]
# print(new_list)

##############
# n = list('12345')
# m = list ('khkbkjnghj')
# k = list('@#$%^&*')

# new_list = list(zip(n, m, k))     # [('1', 'k', '@'), ('2', 'h', '#'), ('3', 'k', '$'), ('4', 'b', '%'), ('5', 'k', '^')] - берет минимальный список: это - n
# print(new_list)

# # если необходимо пройти по длине всех списков
# from itertools import zip_longest

# n = list('12345')
# m = list ('khkbkjnghj')
# k = list('@#$%^&*')

# new_list = list(zip_longest(n, m, k))     # [('1', 'k', '@'), ('2', 'h', '#'), ('5', 'k', '^'), (None, 'j', '&'), (None, 'n', '*'), (None, 'g', None), (None, 'h', None), (None, 'j', None)]
# print(new_list)

# # вместо 'None'  можно подставить любое другое слово
# new_list = list(zip_longest(n, m, k, fillvalue= 'НЕТ'))    # [('1', 'k', '@'), ('2', 'h', '#'), ('5', 'k', '^'), ('НЕТ', 'j', '&'), ('НЕТ', 'n', '*'), ('НЕТ', 'h', 'НЕТ'), ('НЕТ', 'j', 'НЕТ')]
# print(new_list)

#####################################

# enumerate

# list_1 = list('GHJKLASDFG')
# for i in enumerate(list_1):
#     print(i)

# (0, 'G')
# (1, 'H')
# (2, 'J')
# (3, 'K')
# (4, 'L')
# (5, 'A')
# (6, 'S')
# (7, 'D')
# (8, 'F')
# (9, 'G')

# ИЛИ записать 
# list_1 = list('GHJKLASDFG')
# for i, item in enumerate(list_1):
#     print(i, item)

# 0 G
# 1 H
# 2 J
# 3 K
# 4 L
# 5 A
# 6 S
# 7 D
# 8 F
# 9 G

# ИЛИ указать с какого элемента начинаем
# list_1 = list('GHJKLASDFG')
# for i, item in enumerate(list_1, 10):
#     print(i, item)

# 10 G
# 11 H
# 12 J
# 13 K
# 14 L
# 15 A
# 16 S
# 17 D
# 18 F
# 19 G

# Задача 47

# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Ответ: transformation = lambda a: a

# Задача 49
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна


# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# # Вариант 1
# from random import randint
# lst = [(randint(1, 10), randint(1, 10)) for i in range(10)]

# def find_farthest_orbit(orbits):
#     list_res = []
#     for i,j in orbits:
#         if i != j:
#             S = i * j
#             list_res.append(S)
#     max_s = max(list_res)

#     res = orbits[list_res.index(max_s)]
#     return res

# print(lst)
# print(find_farthest_orbit(lst))

# # Вариант 2
# def find_farthest_orbit(orbits):
#     orbits = list(filter(lambda x: x[0] != x[1], orbits))
#     square = list(map(lambda x: x[0] * x[1], orbits))
#     for i in range(len(square)):
#         if square[i] == max(square):
#             return orbits[i]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# # Вариант 3
# import random
# print(lst := [(random.randint(1, 10), random. randint(1, 10)) for _ in range(10)])
# print(lst := list(filter(lambda x: x[0] != x[1], lst)))
# print(max(lst, key=lambda x: x[0] * x[1]))

# # Примеры
# w = ['qwert', 'asdfghj', 'zxc', 'poiu', 'lkjhg']
# print(max(w, key=len))                      # asdfghj - самое длинное
# print(min(w, key=len))                      # zxc - самое короткое
# print(sorted(w, key = len))                 # ['zxc', 'poiu', 'qwert', 'lkjhg', 'asdfghj']
# print(sorted(w, key = len, reverse = True)) # ['asdfghj', 'qwert', 'lkjhg', 'poiu', 'zxc']


# Задача 51.
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.
# Ввод:                                               Вывод:
# values = [0, 2, 10, 6]                              same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


# # Вариант 1
# def same_by(func, array):
#     if len(array) == 0:
#         return True
#     buf = list(map(func, array))
#     if len(list(filter(lambda x: x == buf[0], buf))) == len(buf):
#         return True
#     return False

# values = [0, 3, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# # Вариант 2
# def same_by(fun, lost):
#     return len(set(map(fun, lost))) < 2

# values = [0, 4, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')