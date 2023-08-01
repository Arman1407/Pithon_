# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6

import random
print(lst := [random.randint(0, 100) for _ in range(10)])
print(n := int(input('Введите число: ')))
if n in lst:
    print(f'Число {n} встречается в массиве {lst.count(n)} раз')
else:
    figure = 0
    closely = float('inf')
    for i in lst:
        if closely > abs(n - i):
            closely = abs(n - i)
            figure = i
    print(f'Близкое число к {n} это {figure}')


