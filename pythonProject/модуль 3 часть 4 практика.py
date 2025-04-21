#Задание 1
size = int(input("Введите сторону квадрата:"))
for i in range(size):
    print("*" * size)
#Задание 2
width = int(input("Введите ширину прямоугольника:"))
hight = int(input("Введите высоту прямоугольника"))
for i in range(hight):
    print("*" * width)
#Задание 3
size = int(input("Введите размер стороны квадрата:"))
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")
#Задание 4
height = int(input('Введите высоту прямоугольника: '))
width = int(input('Введити ширину прямоугольника: '))
for i in range(1, height + 1):
    if i == 1 or i == height:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')