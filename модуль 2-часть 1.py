#Задание 1
value_number1 = float(input("Введите первое число: "))
value_number2 = float(input("Введите второе число: "))
value_number3 = float(input("Введите третье число: "))

print("Выберите операцию:")
print("1 - Сумма")
print("2 - Произведение")
choice = input("Введите 1 или 2: ")

if choice == "1":
    result = value_number1 + value_number2 + value_number3
    print(f"Сумма чисел: {result}")
elif choice == "2":
    result = value_number1 * value_number2 * value_number3
    print(f"Произведение чисел: {result}")
else:
    print("Неверный выбор операции! Введите 1 или 2.")
#Задание 2
value_number1 = float(input("Введите первое число: "))
value_number2 = float(input("Введите второе число: "))
value_number3 = float(input("Введите третье число: "))

print("Выберите операцию:")
print("1 - Максимум")
print("2 - Минимум")
print("3 - Среднее")
choice = input("Введите 1, 2 или 3: ")

if choice == "1":
    result = max(value_number1, value_number2, value_number3)
    print(f"Максимальное число: {result}")
elif choice == "2":
    result = min(value_number1, value_number2, value_number3)
    print(f"Минимальное число: {result}")
elif choice == "3":
    result = (value_number1 + value_number2 + value_number3) / 3
    print(f"Среднеарифметическое: {result}")
else:
    print("Неверный выбор операции! Введите 1, 2 или 3.")
#Задание 3
meters = float(input("Введите количество метров: "))

print("Выберите единицу измерения:")
print("1 - Мили")
print("2 - Дюймы")
print("3 - Ярды")
choice = input("Введите 1, 2 или 3: ")

if choice == "1":
    miles = meters * 0.000621371
    print(f"{meters} метров = {miles} миль")
elif choice == "2":
    inches = meters * 39.3701
    print(f"{meters} метров = {inches} дюймов")
elif choice == "3":
    yards = meters * 1.09361
    print(f"{meters} метров = {yards} ярдов")
else:
    print("Неверный выбор! Введите 1, 2 или 3.")