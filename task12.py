# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2 
# 5 6 -> 2 3 

sum_of_numbers = int(input("Введите сумму чисел: "))
product_of_numbers = int(input("Введите произведение чисел: "))

num1 = 1
num2 = 1
while sum_of_numbers != num1 + num2 and product_of_numbers != num1 * num2:
    if product_of_numbers != (sum_of_numbers - num2) * num2:
        num2 += 1
    if num1 != sum_of_numbers - num2:
        num1 += 1

print(num1, num2)