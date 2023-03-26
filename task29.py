# Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность). Все числа вводит пользователь.

i = int(input("Введите число: "))
max_num = i
while i != 0:
    if i > max_num:
        max_num = i
    i = int(input("Введите число: "))
print(max_num)

# numbers_list = []
# flag = True

# while flag:
#     num = int(input("Введите число: "))
#     if num == 0:
#         flag = False
#     else:
#         numbers_list.append(num)

# max_num = numbers_list[0]
# for num in numbers_list:
#     if num > max_num:
#         max_num = num

# print(f"Наибольшее число списка {numbers_list} --> {max_num}")