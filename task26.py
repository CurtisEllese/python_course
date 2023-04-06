# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponentiation(num1, num2):
    if num2 == 1:
        return num1
    return num1 * exponentiation(num1, num2 - 1)

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

res = exponentiation(first_num, second_num)
print(res)