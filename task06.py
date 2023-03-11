# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

num = input("Введите номер билета: ")

num1 = int(num[0:3])
num2 = int(num[3:6])

sum1 = (num1 // 100) + (num1 // 10 % 10) + (num1 % 10)
sum2 = (num2 // 100) + (num2 // 10 % 10) + (num2 % 10)

if sum1 == sum2:
    print(f"{num} -> yes")
else:
    print(f"{num} -> no")