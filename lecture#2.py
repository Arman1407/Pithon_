# СПИСКИ

##############
# Способы создания списков

# list_1 = []           # пустой список
# list_1 = list()       # пустой список
# print(list_1)

# list_1 = [1, 2, 3, 5] # заполненный список
# print(list_1)

# list_1 = [1, 2, 3, 5] # заполненный список
# print(*list_1)        # вывод списка только из цифр
# print(len(list_1))    # Размер списка
# print(list_1[2])      # Указывает цифру в списке по номеру индекса
# print(list_1[-1])     # Указывает цифру в списке по номеру индекса

##############
# Работа с циклами, функциями

# for i in list_1:
#     print(i)


# list_1 = [1, 2, 3, 5]
# print(list_1)
# list_1.append(8)           # Добавляет цифру(значение) в список
# print(list_1)
# list_1.append(85)           # Добавляет цифру(значение) в список
# print(list_1)


# list_1 = []               # С помощью цикла добавляем значения
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

################
# Функции в списках

######
# Удаление и добавление элемента списка

# Удаление последнего элемента списка
# list_1 = [1, 2, 3, 5]

# print(list_1.pop())          # удалили 5, так же функция pop и возвращает последний элемент
# print(list_1)                # 1, 2 , 3 - осталось

# print(list_1.pop())          # удалили 3
# print(list_1)                # 1,2 - осталось

# print(list_1.pop())          # удалили 2
# print(list_1)                # 1 - осталось

######
# Удаление конкретного элемента из списка

# list_1 = [1, 2, 3, 5]

# print(list_1.pop(1))  # удалили 1 индекс- цифру 2
# print(list_1)         # 1, 3, 5  - осталось

######
# Добавление элемента на нужную позицию

# list_1 = [1, 2, 3, 5]

# print(list_1.insert(2, 11)) # добавили 11 на 2 позицию
# print(list_1)               # 1, 2, 11, 3, 5 - получилось


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list[0])              # выводится 1 элемент
# print(list[1])              # выводится 2 элемент
# print(list[len(list)-1])    # выводится последний элемент
# print(list[-1])             # выводится последний элемент
# print(list[-5])             # выводится пятый элемент с конца
# print(list[:])              # выводится весь список
# print(list[:2])             # выводится список с начала и до 1 элемента, последний элемент не берем
# print(list[len(list)-2:])   # выводится 2 последних элемента списка
# print(list[2:9])            # выводится элементы со 2 по 9 списка, последний элемент не берем
# print(list[6:-18])          # выводится пустой список
# print(list[0:len(list):6])  # выводится элементы с шагом 6
# print(list[::6])            # выводится элементы с шагом 6

#################
#################
# КОРТЕЖИ
# нельзя изменить элементы внутри них

# t = ()                  # пустой кортеж
# print(type(t))

# t = (1, 3, 5,)          # кортеж со значениями/ в конце обязательно запятая
# print(type(t))

###########
# Преобразование списка в кортеж

# v = [1, 2, 5]       # список
# print(v)
# print(type(v))

# v = tuple(v)        #  кортеж
# print(v)
# print(type(v))

###########
# Разделение кортежа

# a, b, c = v
# print(a,b,c)

# t = (1, 2, 3, 4, 5,)
# for i in t:                 # кортеж
#     print(i)

# for i in range(len(t)):     # список
#     print(t[i])

################
################
# СЛОВАРИ

# d = {}      # пустой словарь
# d = dict()  # пустой словарь

# d['q'] = 'qwerty'
# print(d)                # {'q': 'qwerty'} - где q - это ключ, по обращению к нему получим : qwerty

# d['w'] = 'werty'
# print(d)                # {'q': 'qwerty', 'w': 'werty'} - в словаре 2 значения с 2 ключами

# print(d['q'])           # qwerty - выводится значение

########
# Пример
# slovo = {}
# slovo = {'qw': '12', 'as': '34', 'zx': '56', 'er': '78'}
# print(slovo)        # {'qw': '12', 'as': '34', 'zx': '56', 'er': '78'} - получается
#print(slovo['er'])  # 78

# удаление элемента
# del slovo['as']
# print(slovo)     # {'qw': '12', 'zx': '56', 'er': '78'}, 'as': '34' - удалено

# for item in slovo:
    # print(item)       
        # выводит все ключи
        # qw
        # as
        # zx
        # er

    # print('{}: {}'.format(item, slovo[item]))   
        # format - выводит все ключи со значениями
        # qw: 12
        # as: 34
        # zx: 56
        # er: 78


########
# Пример
# slovo = {'qw': '12', 'as': '34', 'zx': '56', 'er': '78'}
# print(slovo.items())    # dict_items([('qw', '12'), ('as', '34'), ('zx', '56'), ('er', '78')]) 
                        # список состоящий из кортежей, которые состоят из ключа и значения

# for (k, v) in slovo.items():
    # print(k,v)
        # выводит все ключи со значениями
        # qw: 12
        # as: 34
        # zx: 56
        # er: 78

#################
#################
# МНОЖЕСТВА

# g = set()               #  пустое множество

# colors = {'red', 'green', 'blue'}
# print(colors)               # {'blue', 'green', 'red'}

# colors.add('red')       # add - добавляет новое значение
# print(colors)               # {'blue', 'green', 'red'}
# # colors.add('gray')
# # print(colors)             # {'gray', 'blue', 'green', 'red'}

# colors.remove('red')    # remove - удаляет выбранное значение
# print(colors)               # {'blue', 'green'}

# colors.discard('red')   # discard - проверяет множество, если есть выбранное значение (red) - удаляет, нет - оставляет как есть
# print(colors)               # {'green', 'blue'}

# colors.clear()          # clear - удаляет все элементы множества
# print(colors)               # set()

##############
# Опреции со множествами

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy()                # с = {1, 2, 3, 5, 8} копирует множество а
# u = a.union(b)              # u = {1, 2, 3, 5, 8, 13, 21} объединяет оба множества  в одно
# i = a.intersection(b)       # i = {2, 5, 8} пересечение, оставляет в новом множестве одинаковые элементы
# dl = a.difference(b)        # d1 = {1, 3} разность множеств a - b
# dr = b.difference(a)        # dr = {13, 21} разность множеств b - a
# q = a.union(b).difference(a.intersection(b))  # 1. находим пересечение a, b: 2. объединяем два множества a, b: 3. из обединенного мноржества вычитем множество полученное при пересечении
# #       2.          3.          1.       - действия

##############
# Замороженное множество

# a = {1, 3, 6}

# b = frozenset(a)    # замороженное множество, оно не изменно
# print(b)            # frozenset({1, 3, 6})

################
################
# КОЛЛЕКЦИИ ДАННЫХ

# Тип коллекции

# Обобщение свойств встроенных коллекций в сводной таблице

# Тип коллекции	    #  Изменяемость	    # Индексированность	# Уникальность	# Как создаем
#############################################################################################
# Список            #                   #                   #               #    []         #
# (list)	        #       да	        #        да	        #      нет	    #    list()     #
#                   #                   #                   #               #               #        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                    
# Кортеж            #                   #                   #               #    (),        #
# (tuple)	        #       нет	        #        да	        #      нет	    #    tuple()    #
#                   #                   #                   #               #               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Строка            #                   #                   #               #     ''        #
# (string)	        #       нет	        #        да	        #      нет	    #     " "       #
#                   #                   #                   #               #               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Множество         #                   #                   #               #  {elml, elm2} #
# (set)	            #       да	        #        нет	    #      да	    #     set()     #
#                   #                   #                   #               #               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Неизменное        #                   #                   #               #               #
# множество         #      нет          #        нет        #      да       #  frozenset()  #
# (frozenset)	    #       	        #       	        #               #               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Словарь           #    + элементы     #                   #   + элементы  # {}            #
# (dict)	        #    - ключи        #        нет        #   + ключи     # {key: value,} #
#                   #    + значения     #                   #   - значения  # dict()        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     	       	                   

	
#############################################################################################

# List Comprehension - Генератор списка

# Задача 1
# Создать список чисел от 1 до 100

# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)               # Выводит список от 1 дот 100 [1, 2, 3, ........99, 100]

# # или можно так

# list_1 = [i for i in range(1, 101)]


# # Задача 2
# # Создать список четных чисел от 1 до 100 (кортежи)

# list_1 = [i for i in range(1, 101) if i % 2 == 0]


# # Задача 3
# # Создать пары к числам от 1 до 100

# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# list_1 = [(i, i*i) for i in range(1, 101) if i % 2 == 0]  # кортеж из числа и его квадрата


# Задача 4
# Умножить каждый нечетный элемент списка от 1 до 10 на 2

# list_1 = [i * 2 for i in range(10) if i % 2 ]
# print(list_1)















































