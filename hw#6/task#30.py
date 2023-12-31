# Задача 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5, где  7 - первый элемент, 2 - шаг, 5 - количество элементов
# Вывод: 7 9 11 13 15

def ar_progres(a, n, d):
    progres = []
    for n in range(a):
        progres.append(a + n * d)
    return progres


a = int(input('Введите первое число арифметической прогрессии: '))
n = int(input('Укажите "шаг" арифметической прогресии: '))
d = int(input('Введите количество элементов арифметической прогрессии: '))

print(f'Арифметическая прогрессия {ar_progres(a, d, n)}')