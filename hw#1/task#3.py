# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# Пример:
# n = 385916 -> yes
# n = 123456 -> no

n = 385916

res =  (n//100000) + (n%100000)//10000 + (n%10000)//1000
res1 = (n%1000)//100 + (n%100)//10 + n%10

if(res != res1):
    print('no')
else:
    print('yes')


# или

ticket = input('Введите номер билета: ')
one = ticket[:3]
sec = ticket[3:]

one = int(one[0]) + int(one[1]) + int(one[2])
sec = int(sec[0]) + int(sec[1]) + int(sec[2])

print('yes' if one == sec else 'no')