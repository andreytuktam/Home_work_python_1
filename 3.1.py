# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

quarter = 1
while quarter != 0:
    quarter = int(input("введите номер четверти: "))
    if quarter == 1:
        print("x > 0, y > 0")
    elif quarter == 2:
        print("x < 0, y > 0")
    elif quarter == 3:
        print("x < 0, y < 0")
    elif quarter == 4:
        print("x > 0, y < 0")
 