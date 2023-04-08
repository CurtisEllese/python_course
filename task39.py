# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Ввод: 
# - 7
# - 3 1 3 4 2 4 12
# - 6
# - 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

def check_el_not_in_list(list1, list2):
    res_list = list()
    for item in list1:
        if item not in list2:
            res_list.append(item)
    return res_list

def fill_list(list_len, text="Введите элемент списка: "):
    res_list = list()
    for item in range(list_len):
        res_list.append(int(input(text)))
    return res_list

first_list_len = int(input("Введите длину первого списка: "))
first_list = fill_list(first_list_len)
print(first_list)

second_list_len = int(input("Введите длину второго списка: "))
second_list = fill_list(second_list_len)
print(second_list)

print(check_el_not_in_list(first_list, second_list))