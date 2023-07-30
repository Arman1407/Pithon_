# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# 5



# from random import randint

# print(lst := [randint(-5, 5) for _ in range(1, 11)])
# n = int(input(f'Введите число: '))
# m = lst[0]
# for i in lst:
#     if m(i - n) < m(i):
#         m = m(i)
#         print(m)


# # Вариант с последовательным массивом.

# def input_fill_list(size):
#     new_list = []
#     for i in range(size):
#         new_list.append(int(input("Введите натуральное число: ")))
#     return new_list

# # # Рандом
# import random

# def random_fill_list(size):
#     new_list = []
#     for i in range(size):
#         new_list.append(random.randint(1, 10))
#     return new_list


list_size = int(input("Введите размер массива: "))
find_num = int(input("Введите искомое значение: "))

# Вариант через цикл
my_list = input_fill_list(list_size)
# my_list = random_fill_list(list_size)

closest_num = my_list[0]
for i in my_list:
    if abs(i-find_num) <= abs(closest_num-find_num):
        closest_num = i
   

# print(f"В массиве :{my_list} ближайшее число к: {find_num} является: {closest_num}.")

# # Вариант через min
# my_list = random_fill_list(list_size)
# print(f"В массиве :{my_list} ближайшее число к: {find_num} является: {min(my_list, key=lambda x: abs(x-find_num))}.")