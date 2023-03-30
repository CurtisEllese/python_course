# Задача №25. Напишите программу, которая принимает на вхд строку, и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string_list = 'a a a b c a a d c d d'.split()
counts_dict = dict()
count = 0

for i, val in enumerate(string_list):
    if val in counts_dict.keys():
        counts_dict[val] += 1
        count = counts_dict[val]
        string_list.pop(i)
        string_list.insert(i, f"{val}_{count}")
    else:
        counts_dict[val] = 1

print(string_list)