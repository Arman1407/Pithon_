# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:

# k = 'ноутбук'
# 12


# Вариант1 
diction = {'АВЕИНОРСТAEIOULNSTR': 1, 'ДКЛМПУDG': 2,
           'БГЁЬЯBCMP': 3, 'ЙЫFHVWY': 4, 'ЖЗХЦЧK': 5, 'ШЭЮJX': 8, 'ФЩЪQZ': 10}

def scrabble(letter):
    for key in diction:
        if letter in key:
            return diction.get(key)

input_word = input("Введите слово: ").upper()

print(f"Вы набрали {sum(map(scrabble, input_word))} очков.")

# Вариант 2
alpha = {'AEIOULNSTRАВЕИНОРСТ': 1,              # создали словари
         'DGДКЛМПУ': 2,
         'BCMPБГЁЬЯ': 3,
         'FHVWYЙЫ': 4,
         'KЖЗХЦЧ': 5,
         'JXШЭЮ': 8,
         'QZФЩЪ': 10}

word = input('Введите слово: ')
total = 0
for char in word.upper():
    for letters, score in alpha.items():
        if char in letters:
            total += score
print(f'Слово {word} весит {total} очков')

# Вариант 3
alpha = {'AEIOULNSTRАВЕИНОРСТ': 1,              # создали словари
         'DGДКЛМПУ': 2,
         'BCMPБГЁЬЯ': 3,
         'FHVWYЙЫ': 4,
         'KЖЗХЦЧ': 5,
         'JXШЭЮ': 8,
         'QZФЩЪ': 10}

word = input('Введите слово: ')
total = 0
new_alpha = {}
for letters, score in alpha.items():
    new_alpha.update(dict.fromkeys(letters, score)) # разбивает строку словаря на отдельные словари - {'a': '1', 'e': '1', 'i': '1', 'o': '1', 'u': '1', 'l': '1', 'n': '1', 's': '1', 't': '1', 'r': '1', и т.д.

for char in word.upper():            # upper - переводит в регистр 
    total += new_alpha.get(char)



print(f'Слово {word} весит {total} очков')