# Задача 12

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.



S = int(input('Введите сумму 2-х чисел: '))
P = int(input('Введите произведение этих чисел: '))

x = 0
y = 0


for x in range(S):
    for y in range(P):
        if x + y == S and x * y == P:
            print(f'x = {x}, y = {y}')





















