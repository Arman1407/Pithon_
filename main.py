# Комментирование кода

"""n = 5

m = 5.36

k = 'no'"""

#print(n,m,k)
"""

# Компилляция

print(n,' - ', m, ' - ',k)

print(f"{n} - {m} - {k}")

print("{} - {} - {}".format(n))
"""


# print('Введите число:  ')
# a = input()
# b = input('Введите число:  ')

# n = 5.65
# print(n)
# print(type(n))

# n = int(n)
# print(n)
# print(type(n))

# n = str(n)
# print(n)
# print(type(n))

# Вывод арифметической операции

# c = 1
# print(c)
# print(type(c))

# c = bool(c)
# print(c)
# print(type(c))

# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)


# Округление

# n = 5.3695
# m = 6.32458
# print(round(n*m, 5))

# Действия повторения

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 6 # iter = iter / 6
# iter //= 7 # iter = iter // 7
# iter %= 8 # iter = iter % 8
# iter **= 9 # iter = iter ** 9

# Логические операции

# n = 1  > 4
# print(n)

# n = 1 < 4 and 5 > 2
# print(n)

# n = 1 == 2
# print(n)

# n = 1 != 2
# print(n)

# n = 'qaz'
# m = 'qaz'
# print(n == m)

# n = 1 < 3 < 5 < 8
# print(n)

# Условия: if, elif (else if), else

# name = input('Введите имя: ')
# if name == 'Маша':
#     print('Ура, это же Маша!')
# elif name == 'Марина':
#     print('Марина, вот так сюрприз.')
# elif name == 'Светлана':
#     print('Светы - ты вне конкурса')
# else:
#     print('И тебе не хворать, ', name)


# Цикл while, while else
    
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('yes')
#     print('no')
# print(i)


# Метод флажка (без команды break)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i+= 1


# Цикл for, функция range()

# p = range(5) # 0 1 2 3 4
# p = range(2, 5) # 2 3 4 начинают с 2, 5 - последний элемент который не включают
# p = range(0, -5) # ------
# P = range(1, 10, 2) # 1 3 5 7    начинают с 1, до 10 не включая 10, 2 - это шаг
# p = range(100, 0, -20) # 100 80 60 40 20 начинают со 100 до 0, -20 - это шаг
# p = range(100, 0, -20) # range(100, 0, -20)
# for i in p:
#     print(i)

# Цикл for со значениями str
# 1

# a = 'qazwsx'

# for i in a:
#     print(i)

# 2

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "+"
#     print(line)

# Работа с текстом

# text = 'Работа не Волк, в лес не убежит'
# print(len(text)) # определяет размер строки(количество элементов
# print('волк' in text) # определяет наличие символов в строке
# print(text.lower()) # переводит все в нижний регистр
# print(text.upper()) # переводит все в верзний регистр
# print(text.replace('лес', 'ЛЕС'))


# Работа с символами в строках

text = 'Работа не Волк, в лес не убежиТ'

# print(text[0]) #  так можно выводить каждый символ, и т.д.
# print(text[:]) # выводит всю строку
# print(text[:2]) # выводит первые два символа строки
# print(text[len(text)-2:]) # выводит последние два символа строки
# print(text[2:9]) # задает отрезок
# print(text[0:len(text):2]) # выводит символы с заданным шагом от 1 до последнего символа
# print(text[::2]) # выводит символы с заданным шагом от 1 до последнего символа

# text = text[2:9] + text[-5] + text[:2] # складывает разные части из элементов строки
# print(text)