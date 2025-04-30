#Задание 1
value_number = input("Введите шестизначное число: ")

if len(value_number) != 6 or not value_number.isdigit():
    print("Ошибка! Введите именно шестизначное число.")
else:
    first_part = int(value_number[0]) + int(value_number[1]) + int(value_number[2])
    second_part = int(value_number[3]) + int(value_number[4]) + int(value_number[5])
    
    if first_part == second_part:
        print("Это счастливое число!")
    else:
        print("Это несчастливое число.")
#Задание 2
value_number = input("Введите шестизначное число: ")

if len(value_number) != 6 or not value_number.isdigit():
    print("Ошибка! Введите именно шестизначное число.")
else:
    digits = list(value_number)
    digits[1], digits[4] = digits[4], digits[1]
    new_number = ''.join(digits)
    print("Новое число:", new_number)
#Задание 3
value_number = int(input("Введите номер месяца (1-12): "))

if value_number < 1 or value_number > 12:
    print("Ошибка! Введите число от 1 до 12.")
else:
    if value_number == 12 or value_number <= 2:
        print("Winter")
    elif 3 <= value_number <= 5:
        print("Spring")
    elif 6 <= value_number <= 8:
        print("Summer")
    else:
        print("Autumn")