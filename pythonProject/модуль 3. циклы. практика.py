#Задание 1
#Показать таблицу умножения для числа, введенного
#пользователем. Например, если пользователь вводит
#число 7, нужно показать:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
value_user = int(input("Введите число:"))
for i in range(1, 10):
       result = value_user * i
       print(f"{value_user} * {i} = {result}")

# Задание 2 Написать программу – конвертер валют. Реализовать
# общение с пользователем через меню.
print("Конвертер валют")
USD = 82.14
EURO = 92.22
BYN = 26.52
while True:
    value_user = float(input("Выберите количество рублей для перевода:"))
    print("1.USD \n2.EURO \n3.BYN \n0 выход")  # BYN
    user_choice = int(input("Ваш выбор: "))
    if (1 == user_choice):
        print(f"USD {value_user / 82.14}")
    elif (2 == user_choice):
        print(f"EURO {value_user / 92.22}")
    elif (3 == user_choice):
        print(f"BYN {value_user / 26.52}")
    elif (0 == user_choice):
        break
#Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
#программа просит пользователя повторно ввести число,
#и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
#восклицательными знаками. Например:
#1 2 3 !4! 5 6 7

lower = int(input ("Введите 1 границу диапазона: "))
upp = int(input ("Введите 2 границу диапазона: "))

while True:
    value_number = int(input ("Введите число  "))
    if lower <= value_number <= upp:
        break
    print(f"Число {value_number} не входит в диапазон. Введите число от lower до upp")
for i in range (lower, upp + 1):
    if i == value_number:
        print(f"!{i}!", end = " ")
    else:
        print(i, end = " ")
#Задание 4
import random
import datetime

print("Добро пожаловать в игру <Угадай число!>")
print("Правила очень просты: ты пытаешься угадать число от 1 до 500, я даю тебе подсказки!")
print("*"*11)
user_choice_count = 0
user_choice_time = datetime.datetime.now() #текущее время
print(f"Начало игры в {user_choice_time}")
random_value = random.randint(1, 500)
# #randint - функция для выбора
# #случайного числа в интервале
while True:
    user_choice_count += 1
    value_user = int(input("Введите предполагаемое число:"))
    if value_user == random_value:
        print("Вы угадали число! Поздравляю!")
        break
    elif value_user < random_value:
        print("Ваше число меньше загаданного")
    elif value_user > random_value:
        print("Ваше число больше загаданного")
    print("*"*11)
delta_time = datetime.datetime.now() - user_choice_time
print(f"Статистика: \n Попыток ->{user_choice_count} \n Время->{delta_time}")
