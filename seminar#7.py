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
# map

# nums = list('1233456789')
# print(nums)

# for i in range(len(nums)):
#     nums[i] = int(nums[i])
# print(nums)

# ИЛИ

# nums = list(map(int, nums))

# print(nums)           # список
# print(*nums)          # цифры

# nums = list(map(lambda x: str(x) if x % 2 == 0 else x, nums))
# print(nums)

#################################

# zip

# n = list('123654879756')
# m = list ('khkbkjnihnjk')

# new_list = []
# for i in range(len(n)):
#     new_list.append((n[i], m[i]))

# new_list = list(zip_longest(n, m, fillvalue= 'ПУСТО'))
# print(new_list)

#####################################

# enumerate

# Задача

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




# list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     # Функция для вычисления площади эллипса по полуосям a и b
#     def ellipse_area(a, b):
#         return 3.14 * a * b  # Приближенное значение числа π

#     max_orbita = max * (ellipse_area(a, b) for a, b in list_of_orbits) 
#     n = next((a, b) for a, b in list_of_orbits if ellipse_area a, b == max_arena)
#     return (n)



# import random

# print(planets := [(random.randint(1,10), random.randint(1, 10)) for _ in range(10)])

# planets = list(filter(lambda x: x[0] != x[1], planets))
# print(planets)

# print(max(planets, key = lambda x: x[0]*x[1]))





# Задача №51.
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




