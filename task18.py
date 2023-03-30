# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

amount_of_elems = int(input("Введите размер списка: "))
entered_list = list()

for item in range(amount_of_elems):
    entered_item = int(input(f"Введите {item} элемент списка: "))
    entered_list.append(entered_item)
print(entered_list)

search_num = int(input("Введите число, близкое значение к которому нужно найти: "))
min_range = abs(search_num - entered_list[0])
close_value = entered_list[0]

for item in range(len(entered_list)):
    if abs(search_num - entered_list[item]) < min_range:
        close_value = entered_list[item]
        min_range = abs(search_num - entered_list[item])
print(close_value)