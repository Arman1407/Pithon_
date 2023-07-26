# Задача 1
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# str = '123456789123456789456789789 '
# str = list(str)
# s = set(str)

# for i in s:
#     count = 0
#     for j in range(len(str)):
#         if str[j] == i and count > 0:
#             str[j] = f'{str[j]}_{count}'
#             count += 1
#         if str[j] == i:
#             count += 1

# print(str)


# или

# n = input('Введите стоку: ')
# s = {}
# # # total = []

# for i in n:
#     # if i in s:
#     #     s[i] += 1
#     # else:
#         # s[i] = 1
#     s[i] = s.get(i, 0) + 1
#     print(f'{i}' + (f'_{s[i]-1}' if s[i] > 1 else ''), end=' ')

# # print(s)

# # # total.append(f'{i}' + (f'_{s[i]-1}' if s[i] > 1 else ''), end=' ')

# # # print(*total)



# Задача 2
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# Пример
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# str = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells"""

# str = str.lower()
# str = str.replace('.','')
# print(str)

# str = list(str.split())
# str_set = set(str)

# print(str_set)
# print(len(str_set))



# Задача 3
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.


# # Ваня
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print (max_number)

# # Петя
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print (n)


# Арман
# n = int(input(f'Введите число: '))
# max_number =-1
# while n != 0:
#     n = int(input(f'Введиьте число: '))
#     if max_number < n:
#         max_number = n
# print(max_number)































