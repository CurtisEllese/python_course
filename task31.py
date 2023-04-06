# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

def fibo(number):
    if number in [1, 2]:
        return 1
    return fibo(number - 1) + fibo(number - 2)

num = int(input("Введите число: "))
print(fibo(num))
