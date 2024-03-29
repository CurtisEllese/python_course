# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

num = int(input("Введите натуральное число больше 1: "))
while num < 1:
    num = int(input("Введите натуральное число больше 1: "))

count = 3
f1 = f2 = 1

while num > f2:
    f1, f2 = f2, f2 + f1
    count += 1
print(count if num == f2 else -1)