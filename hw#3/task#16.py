# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

## Вариант 1
# from random import randint

# print(lst := [randint(-5, 5) for _ in range(1, 11)])
# n = int(input(f'Введите число: '))
# count = 0
# for i in lst:
#        if i == n:
#         count += 1

# print(f'Число {n} встречается в массиве {count} раз')

## Вариант 2
# import random
# print(lst := [random.randint(-5, 5) for _ in range(10)])
# print(n := int(input('Введите число: ')))
# if n in lst:
#     print(f'Число {n} встречается в массиве {lst.count(n)} раз')
