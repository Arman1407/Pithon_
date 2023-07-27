# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# def fill_list(size):
#     new_list = []
#     for i in range(size):
#         new_list.append(int(input("Enter number: ")))
    # return new_list


import random
def fill_list(element):
    new_list = []
    for i in range(element):
        new_list.append(random.randint(1, 20))
    return new_list


first_set = int(input("Введите количество элементов в 1 наборе: "))
n = fill_list(first_set)
print(n)
second_set = int(input("Введите количество элементов во 2 наборе: "))
m = fill_list(second_set)
print(m)

print(f"Sorted list: {sorted(set(n + m))}")