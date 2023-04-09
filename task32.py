# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_index_in_range(min_v, max_v, list_):
    res_list = []
    for i in range(len(list_)):
        if min_v <= list_[i] <= max_v:
            res_list.append(i)
    return res_list


min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

index_list = find_index_in_range(min_value, max_value, list1)
print(index_list)