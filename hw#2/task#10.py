# Задача 10 

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint

# n = int(input('Введите количество монет: '))

# eagle = 0
# tails = 0
# # countE = 0
# # countT = 0

# for i in range(n):
#     n = randint(0, 1)
#     print(n, end=' ')
#     if i != 1:                      
#         eagle += 1                  # почему не суммирует
#     else:
#         tails += 1                  # почему не суммирует
    
# print(min(f'\nнеобходимо перевернуть {eagle} "орлов", {tails} "решек"'))
   
#################

import random
n = int(input('Введите количество монет: '))
eagle = 0

for i in range(n):
    n = random.randint(0, 1)
    print(n, end=' ')
    eagle += n

print(f'\nНеобходимо перевернуть {1 if eagle < n // 2 + 1 else 0}')