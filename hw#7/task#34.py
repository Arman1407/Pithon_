# Задача 34
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Пример:

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да    

# Вывод: Парам пам-пам  
# Вывод: Пам парам


def poem(phrase):
    phrase_str = phrase.lower().split()
    lower_letter = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    summa_letter = lower_letter(phrase_str[0])
    if all([lower_letter(i) == summa_letter for i in phrase_str]):
        return 'Парам пам-пам'
    return 'Пам парам'

poem_ = input('Введите стихотворение Винни-Пуха: ')
print(poem(poem_))