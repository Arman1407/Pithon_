# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# # Вариант 1
# import random

# print(first_set := set([random.randint(0, 20) for _ in range(10)]))
# print(second_set := set([random.randint(0, 20) for _ in range(10)]))

# print(sorted(set(first_set).intersection(set(second_set))))

# # Вариан 2
# import random

# print(first_set := [random.randint(0, 20) for _ in range(10)])
# print(second_set := [random.randint(0, 20) for _ in range(10)])

# print(sorted([item for item in first_set if item in second_set]))




# import random
# def fill_list(element):
#     new_list = []
#     for i in range(element):
#         new_list.append(random.randint(1, 20))
#     return new_list


# first_set = int(input("Введите количество элементов в 1 наборе: "))
# n = fill_list(first_set)
# print(n)
# print()
# second_set = int(input("Введите количество элементов во 2 наборе: "))
# m = fill_list(second_set)
# print(m)

# for i in n:
#     for j in m:
#         if i != j:
#             print(f"Новый набор по возрастанию: {sorted(set(n) + set(m))}")


