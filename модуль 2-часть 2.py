#Задание 1
value_number = int(input("Введите время в секундах с начала дня: "))

total_seconds = 24 * 60 * 60

if value_number < 0 or value_number >= total_seconds:
    print("Ошибка! Введите число от 0 до 86399.")
else:
    remaining_seconds = total_seconds - value_number
    hours = remaining_seconds // 3600
    minutes = (remaining_seconds % 3600) // 60
    seconds = remaining_seconds % 60
    print(f"До полуночи осталось: {hours} часов, {minutes} минут, {seconds} секунд")
#Задание 2
import math

value_number = float(input("Введите диаметр окружности: "))

radius = value_number / 2
print("Выберите действие:")
print("1 - Посчитать площадь")
print("2 - Посчитать периметр")
choice = input("Введите 1 или 2: ")

if choice == "1":
    area = math.pi * radius ** 2
    print(f"Площадь окружности: {area:.2f}")
elif choice == "2":
    perimeter = 2 * math.pi * radius
    print(f"Периметр окружности: {perimeter:.2f}")
else:
    print("Ошибка! Введите 1 или 2.")
#Задание 3
price = float(input("Введите стоимость одной приставки: "))
quantity = int(input("Введите количество приставок: "))
discount = float(input("Введите процент скидки: "))

print("Выберите действие:")
print("1 - Посчитать сумму заказа со скидкой")
print("2 - Посчитать стоимость одной приставки со скидкой")
choice = input("Введите 1 или 2: ")

if choice == "1":
    total = (price * quantity) * (1 - discount / 100)
    print(f"Сумма заказа со скидкой: {total:.2f}")
elif choice == "2":
    discounted_price = price * (1 - discount / 100)
    print(f"Цена одной приставки со скидкой: {discounted_price:.2f}")
else:
    print("Ошибка! Введите 1 или 2.")
#Задание 4
size_gb = float(input("Введите размер файла в ГБ: "))
speed_bps = float(input("Введите скорость интернета в битах/с: "))

size_bits = size_gb * 8 * 1024 ** 3
time_seconds = size_bits / speed_bps

print("Выберите единицу времени:")
print("1 - Часы")
print("2 - Минуты")
print("3 - Секунды")
choice = input("Введите 1, 2 или 3: ")

if choice == "1":
    print(f"Время загрузки: {time_seconds / 3600:.2f} часов")
elif choice == "2":
    print(f"Время загрузки: {time_seconds / 60:.2f} минут")
elif choice == "3":
    print(f"Время загрузки: {time_seconds:.2f} секунд")
else:
    print("Ошибка! Введите 1, 2 или 3.")
#Задание 5
value_number = int(input("Введите текущий час (0-23): "))

if 0 <= value_number < 6:
    print("Good Night")
elif 6 <= value_number < 13:
    print("Good Morning")
elif 13 <= value_number < 17:
    print("Good Day")
elif 17 <= value_number <= 23:
    print("Good Evening")
else:
    print("Ошибка! Введите число от 0 до 23.")