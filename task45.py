# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 10**5. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:   Вывод:
# 300     220 284


def sum_div(num):
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    return sum_


k = 300
for num_1 in range(2, k + 1):
    num_2 = sum_div(num_1)
    sum_num_2 = sum_div(num_2)
    if (num_1 < num_2) and (sum_num_2 == num_1):
        print(num_1, num_2)

# import datetime

# a = datetime.datetime.now()

# def sum_divide(num):
#     sum_div, i = 1, 2
#     while i*i < num:
#         if num % i == 0:
#             sum_div += i
#             sum_div += (num // i)
#         i += 1
#     return sum_div


# number = int(input("Введите число: "))
# while number > 10 ** 5:
#     number = int(input("Введите число, не превышающее 10^5: "))

# res_list = []

# for i in range(1, number + 1):
#     j = sum_divide(i)
#     if i < j < number and i == sum_divide(j):
#         res_list.append((i, j))

# print(res_list)
# print(datetime.datetime.now() - a)

# import datetime

# a = datetime.datetime.now()

# def fill_list_order_nums(num):
#     res_list = list()
#     for i in range(1, num + 1):
#         res_list.append(i)
#     return res_list

# def find_amicable_numbers(list1):
#     num1 = 0
#     num2 = 0
#     sum1 = 0
#     sum2 = 0
#     res_list = []
#     for i in list1:
#         for div1 in range(1, i):
#             num1 = i
#             if i % div1 == 0:
#                 sum1 += div1
#         if sum1 in list1:
#             num2 = sum1
#             for div2 in range(1, num2):
#                 if num2 % div2 == 0:
#                     sum2 += div2
#             if num1 == sum2 and num2 == sum1 and not num1 == num2 and (num2, num1) not in res_list:
#                 res_list.append((num1, num2))
#                 sum1 = sum2 = 0
#             else:
#                 sum1 = sum2 = 0        
#         else:
#             sum1 = sum2 = 0
#     return res_list
            

# number = int(input("Введите число: "))
# while number > 10 ** 5:
#     number = int(input("Введите число, не превышающее 10^5: "))

# ordered_list = fill_list_order_nums(number)
# print(find_amicable_numbers(ordered_list))
# print(datetime.datetime.now() - a)