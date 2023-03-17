# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 6 8 

num = int(input("Введите число: "))

num_in_power = 1
while num_in_power < num:
    print(num_in_power, end=" ")
    num_in_power *= 2