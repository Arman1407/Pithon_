# Задача 17

# Дан список чисел. Определите, сколько в нем встречается различных чисел.


# from random import randint

# print(lst := [randint(-5, 5) for _ in range(1, 11)])

# print(len(set(lst)))



# Задача 19

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.

# from random import randint

# # 1 вариант
# print(lst := [randint(-5, 5) for _ in range(1, 11)])
# shift = int(input('Введите сдвиг: '))
# print(lst[-shift:] + lst[:-shift])

# # 2 вариант
# for i in range(shift):
#     lst.insert(0, lst.pop())
# print(lst)

# # 3 вариант
# list1 = []
# for i in range(len(lst)):
#     list1.append(lst[(i - shift) % len(lst)])
# print(list1)

 
# new_list = []
# for i in range(100):
#     print(lst[i%len(lst)])


# Задача 21
# Напишите программу для печати всех уникальных значений в словаре.
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# nset = set()
# for dct in list_1:
#     print(*dct.values()) # показывает значения
#     print(*dct.keys())   # показывает ключи
# print(*list_1) # распоковывает список состоящий из словарей


# Задача 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)


# nums = [1, 2, 3, 1, 2]
# count = 0
# for i in range(1, len(nums)):
#     if nums[i - 1] < nums[i]:
#         count += 1
# print(count)

# # или

# from random import randint

# print(lst := [randint(-5, 5) for i in range(8)])
# count = 0

# for i in range(len(lst)-1):
#     if lst[i] < lst[i+1]:
#         count += 1
# print(count)







