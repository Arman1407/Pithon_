# Задача 1.
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(8))

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

#################

# Задача
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1



# from random import randint
# print(list_1 := [randint(1, 5) for _ in range(10)])

# max1 = max(list_1)
# print(max1)
# for i in range(len(list_1)):
#     if max1 == list_1[i]:
#         list_1[i] = 1

# print(list_1)

##############
# https://www.youtube.com/channel/UCCC7ihYh4SNQZj26adlk2Kg
##############

# Задача 1

# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# def is_prime(num: int) -> bool:
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for dev in range(3, num // 2 + 1, 2):
#         if num % dev == 0:
#             return False
#     return True

# print(is_prime(12))
# print(is_prime(13))

#####################

# Задача
# 1. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.
# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).


# def index(n):
#     if n < 1:
#         return
#     i = int(input(f'Введите число: '))
#     index(n - 1)
#     print(i, end = ' ')

# n = int(input(f'Введите количество элементов: '))
# index(n)

#######################

# def index(n):
#     if n < 1:
#         return ''
#     i = input()
#     return index(n - 1) + ' ' + i

# num = int(input('Введите количество элементов: '))
# print(index(num))