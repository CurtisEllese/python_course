# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_arithmetic_progression(elem1, elem_diff, elem_amount):
    res_list = [elem1]
    for n in range(elem_amount - 1):
        res_list.append(res_list[n] + elem_diff)
    return res_list



first_elem = int(input("Введите первый элемент арифметической прогрессии: "))
difference_of_elements = int(input("Введите разность элементов арифметической прогрессии: "))
elements_amount = int(input("Введите количество элементов арифметической прогрессии: "))

arithmetic_progression_list = fill_arithmetic_progression(first_elem, difference_of_elements, elements_amount)

print(arithmetic_progression_list)
