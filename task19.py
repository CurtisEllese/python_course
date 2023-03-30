# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5]
k = int(input("Введите число сдвига: "))
for i in range(k % len(list_1)):
    list_1.insert(0, list_1.pop(-1))
print(list_1)

# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Введите число сдвига: "))
# while k > 0:
#     list_1.insert(0, list_1.pop(-1))
#     k -= 1
# print(list_1)

# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Введите число сдвига: "))
# list_2 = list()
# for i in range(len(list_1)):
#     list_2.insert(i, list_1[i - k])

# print(list_2)

# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Введите число сдвига: ")) % len(list_1)

# print(list_1[k:] + list_1[:k])
