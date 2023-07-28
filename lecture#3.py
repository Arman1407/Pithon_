# def - так обозначается функция/процедура. Сколько значений функция принимает, столько и отдаёт.
#                                           Соответственно и наоборот

# Пример:

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# sum_numbers(5) # 1 + 2 + 3 + 4 + 5 = 15

# ИЛИ
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5)) # 1 + 2 + 3 + 4 + 5 = 15

# ИЛИ
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# a = sum_numbers(5)
# print(a) # 1 + 2 + 3 + 4 + 5 = 15

####################

# def sum_str(*args):      #  *args - объединяет неограниченное число аргументов в одну строку
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'w', 'e', 'r', 't', 'y'))
# # print(sum_str(1, 2, 3)) # выдается ошибкой, т.к. вводится тип - int, а не str
# print(sum_str('1', '2', '3'))


# Модуль - это файл в котором находятся определенные функции

# Пример
# import modul1             # импортирует из фйла  modul1
# print(modul1.max1(5, 9))  # указывается файл и функция


# ИЛИ можно вывести так

# from modul1 import max1
# print(max1(5, 9))


# ИЛИ можно вывести из файла все функции

# from modul1 import *
# print(max1(5, 9))


# ИЛИ можно переимновать на время работы название функции

# import modul1 as m1
# print(m1.max1(5, 9))

###############

# Рекурсия - функция, вызывающая сама себя

# Выводим число Фибоначчи через рекурсию

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))

# print(list_1)

###########################

# Сортировки

# Быстрая сортировка

# def fast(arrya):
#     if len(arrya) <= 1:
#         return arrya
#     else:
#         pivot = arrya[0]
#     less = [i for i in arrya[1:] if i <= pivot]
#     more = [i for i in arrya[1:] if i > pivot]
#     return fast(less) + [pivot] + fast(more)

# print(fast([1, 52, 3, 14, 98, 20, 8, 6, 54, 87, 63, 24]))



# Сортировка слиянием

# def merg(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merg(left)
#         merg(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [1, 5, 54, 69, 25, 32, 6, 87, 41, 23, 54, 21, 9, 7]
# merg(list1)
# print(list1)