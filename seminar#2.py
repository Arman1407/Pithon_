# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# # 1 вариант
# n = int(input('n =    '))
# i = 1
# f = 1
# while i <= n:
#     f = f  * i
#     i += 1
# print(f)

 # 2 вариант
# n = int(input('Введите число:    '))

# f = 1

# while n > 0:
#     f *= n
#     n -= 1

# print(f)



# # Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# # Если А не является числом Фибоначчи, выведите число -1.

# number = int(input('Введите число: '))

# fibo_prev = 0
# fibo_cur = 1
# index = 1

# while fibo_cur < number:
#     fibo_prev, fibo_cur = fibo_cur, fibo_prev + fibo_cur
#     index += 1
# if fibo_cur == number:
#     print(f'Число {number} идет {index} числом в последовательности Фибоначчи')
# else:
#     print(-1)


# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# from random import randint

# # print(randint(1,30000))

# # 1 вариант 
# n = int(input ('Введите общее колличество'))
# m = 0
# min1 = 30001
# max2 = 0
# while m < n:
#     mass=randint(1,30000)
#     print(mass)
#     if max2 < mass:
#         max2 = mass
#     if min1 > mass:
#         min1 = mass
#     m+=1
# print(f'Максимальный вес арбуза:{max2},Минимальный вес арбуза:{min1}')

# # 2 вариант

# from random import randint

# count_wm = int(input('Введите количество арбузов: '))

# max_wm = float('-inf') # max бесконечность
# min_wm = float('inf')  # min бесконечность
# print(f'Перед вами {count_wm} арбузов:')
# for _ in range(count_wm):
#     current_wm = randint(1000, 30000)
#     print(current_wm, end=' ')
#     if max_wm < current_wm:
#         max_wm = current_wm
#     if min_wm > current_wm:
#         min_wm = current_wm
# print(f'\nСамый тяжелый арбуз - {max_wm} гр\nСамый легкий арбуз - {min_wm} гр')


# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней 
# длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.

# from random import randint

# days = int(input('Введите количество дней: '))
# max_len, count, temp = 0, 0, 0

# for _ in range(days):
#     temp += randint(-3, 3)
#     print(temp, end=' ')
#     if temp > 0:
#         count += 1
#         if count > max_len:
#             max_len = count
#     else:
#         count = 0

# print(f'\nМаксимальное количество теплых дней подряд - {max_len} дней')








