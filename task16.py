# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

amount_of_elems = int(input("Введите размер списка: "))
entered_list = list()

for item in range(amount_of_elems):
    entered_item = int(input(f"Введите {item} элемент списка: "))
    entered_list.append(entered_item)
print(entered_list)

search_num = int(input("Введите число, которое нужно найти: "))
count = 0
for item in entered_list:
    if search_num == item:
        count += 1

print(f"Число {search_num} встречается {count} раз(a)")