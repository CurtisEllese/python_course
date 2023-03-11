# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

num_horizontal = int(input("Введите число долек по горизонтали: "))
num_vertical = int(input("Введите число долек по горизонтали: "))
num_break_off = int(input("Введите число долек, которые нужно отломить: "))

if num_break_off == num_vertical or num_break_off == num_horizontal or num_break_off % num_horizontal == 0 or num_break_off % num_vertical == 0:
    print(f"{num_horizontal}; {num_vertical}; {num_break_off} --> yes")
else:
    print(f"{num_horizontal}; {num_vertical}; {num_break_off} --> no")
