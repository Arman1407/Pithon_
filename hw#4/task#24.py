# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


# # Вариант 1
# import random

# def berries(size):
#     new_list = []
#     for i in range(size):
#         new_list.append(random.randint(1, 10))
#     return new_list

# size = int(input("Введите количество кустов: "))
# bush = berries(size)
# print(f"Количество ягод на кустах: {bush}")
# if size <= 3:
#     print(sum(bush))
# else:
#     result = 0
#     for i in range(size):
#         summ = bush[i-1] + bush[i] + bush[(i+1) % size]
#         if summ > result: 
#             result = summ
#             temp = (i-1, i, (i+1) % size)
#     print(f"Максимально модуль сможет собрать ягод в количестве - {result} шт.")

# # Вариант 1
# import random

# print(bushes := [random.randint(1,20) for _ in range(10)])

# sum_berries = []

# for i in range(len(bushes)):
#     sum_berries.append(bushes[(i-1)%len(bushes)] + bushes[i] + bushes[(i+1)%len(bushes)])

# print(max(sum_berries))

# # Вариант 3
# import random

# print(bushes := [random.randint(1,20) for _ in range(10)])

# sum_berries = []

# for i in range(len(bushes)):
#     if i ==0:
#         sum_berries.append(bushes[-1] + bushes[0] + bushes[1])
#     elif i == len(bushes)-1:
#         sum_berries.append(bushes[-2] + bushes[-1] + bushes[0])
#     else:
#         sum_berries.append(bushes[i-1] + bushes[i] + bushes[i+1])

# print(max(sum_berries))