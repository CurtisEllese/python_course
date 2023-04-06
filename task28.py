# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

def recursive_sum(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    return recursive_sum(num1 - 1, num2 + 1)

res = recursive_sum(first_num, second_num)
print(res)