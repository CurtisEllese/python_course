# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Input: 5
# Output: 120

num = int(input("Введите натуральное число: "))
while num < 0:
    num = int(input("Введите целое неотрицательное число: "))

factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(factorial)