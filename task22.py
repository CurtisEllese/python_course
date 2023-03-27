# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пример: 
# -- 5
# -- 5
# -- 4 6 8 10 2
# -- 3 9 6 1 2
# 2 6 

len_of_first_selection = int(input("Введите длину первого множества: "))
len_of_second_selection = int(input("Введите длину второго множества: "))
first_selection_of_nums = list()
second_selection_of_nums = list()

while len(first_selection_of_nums) < len_of_first_selection:
    first_selection_of_nums.append(int(input("Введите значение первого множества: ")))

while len(second_selection_of_nums) < len_of_second_selection:
    second_selection_of_nums.append(int(input("Введите значение второго множества: ")))

first_selection_of_nums = set(first_selection_of_nums)
second_selection_of_nums = set(second_selection_of_nums)

sorted_intersection_list = sorted(first_selection_of_nums.intersection(second_selection_of_nums))

print(sorted_intersection_list)
