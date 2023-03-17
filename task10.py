# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# Input: 5 -> 1 0 1 1 0
# Output: 2

num_coins = int(input("Введите количество монет: "))

tail_side = 0
head_side = 1
tail_count = 0
head_count = 0
for i in range(num_coins):
    coin = int(input("Введите сторону монеты: "))
    if coin == tail_side:
        tail_count += 1
    if coin == head_side:
        head_count += 1

if tail_count < head_count:
    print(f"Нужно перевернуть {tail_count} монетки")
if head_count < tail_count:
    print(f"Нужно перевернуть {head_count} монетки")
else:
    print(f"Нужно перевернуть {head_count} монетки")
