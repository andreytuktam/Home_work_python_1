# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


x = 1
while x != 0:
    x = int(input("введите день недели: "))
    if x > 7 or x < 1:
        print("такого дня недели нет, введите значения от 1 до 7!")
    if x == 6 or x == 7:
        print("выходной!")
    else:
        print("работать!)")