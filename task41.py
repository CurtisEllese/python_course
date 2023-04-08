# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# Ввод:         Ввод:
# 5             5
# 1 2 3 4 5     1 5 1 5 1

# Вывод:        Вывод:
# 0             2

def check_less_adjacent(list1):
    count = 0
    for item in range(1, len(list1) - 1):
        if list1[item - 1] < list1[item] > list1[item + 1]:
            count += 1
    return count

def fill_list(list_len, text="Введите элемент списка: "):
    res_list = list()
    for item in range(list_len):
        res_list.append(int(input(text)))
    return res_list

list_length = int(input("Введите длину списка: "))
input_list = fill_list(list_length)
print(input_list)

print(check_less_adjacent(input_list))