from traceback import print_tb

print("Hello world!!!")
#Функция для печати текста и его вывода в консоль
# name = input("Введите ваше имя:")
# age = input("Введите ваш возраст:")
# print("Привет,", name , ", Тебе", age , ' лет')

# #Калькулятор
# value1 = int(input("Введите первую переменную: "))
# value2 = int(input("Введите вторую переменную: "))
# print(f"{value1} + {value2} = {value1 + value2}")#сумма элементов
# #string - тип данных для текста
# #int - тип данных для целочисленных чисел
# #float - тип данных с плавающей точкой
# #bool - тип данных логический, True? False
# print(f"{value1} - {value2} = {value1 - value2}")
# print(f"{value1} * {value2} = {value1 * value2}")
# print(f"{value1} / {value2} = {value1 / value2}")
# print(f"{value1} // {value2} = {value1 // value2}")
# print(f"{value1} % {value2} = {value1 % value2}")
# print(f"{value1} ** {value2} = {value1 ** value2}")
# print("*" * 11)
# #Проверка и сравнение данных
# print(value1 > value2)
# print(value1 < value2)
# print(value1 == value2)
# print(value1 == 'Hello World!!!')#проверка на ревенство
# print(value1 != 'Hello World!!!')#проверка на неравенство
# print("hello" > "hello world")

#Пользователь вводит с клавиатуры три числа необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.

# value_number = int(input("Введите число 1: "))
# value_number2 = int(input("Введите число 2: "))
# value_number3 = int(input("Введите число 3: "))
# sum = value_number + value_number2 + value_number3
# proz = value_number * value_number2 * value_number3
# print(f"sum: {sum}")
# print(f"proz: {proz}")

#Пользователь вводит с клавиатуры три числа.
#Первое чило ЗП
#Второе число сумма ежемесяного платежа
#Третье число задолжность за коммунальные услуги
#Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат

# value_number = int(input("Введите зарплату: "))
# value_number2 = int(input("Введите платеж по кредиту: "))
# value_number3 = int(input("Введите комуналка: "))
# result = value_number - value_number2 - value_number3
# print(f" ЗП: {value_number}, \n Платеж: {value_number2}, \n Коммуналка: {value_number3}"
#     f" \n Остаток: {result}")

#Экранирование символов
#Вызов спец символа \ для создания команды вставки символа
# \\ - добавляет обратный слеш
# \" - добавляет двойные кавычки
# \' - добавляет одиночные кавычки
# \n - переход на новую строку
# \t - вставка 3х пробелов
# \b - удаление пред. символа
# string = "Фраза для работы со строкой"
# print(value_number, string, value_number2, value_number3, sep="*\n")
# #sep - это строка между значениями, для вставки, между значениями элементов вывода print
# #end - это вставка символа в конце строки, вместо \n
# print(value_number, string, value_number2, value_number3, end="***")

#Выведите на экран надпись To be or not to be на разных строках. Пример вывода:
#To be
#           or not
#                       to be

# print("To be")
# print("\t\t or not")
# print("\t\t\t\t\t to be")
#
# print("To be \n \t\t or not \n \t\t\t\t\t to be")
# print("To be", "\n", "or not", "\n" "to be")

#Пользователь вводит с клавиатуры три цифры.
#Например, если с клавиатуры введено 1, 5, 7.
#Тогда нужно сформировать число 157.

# value_number = int(input("Введите цифру 1:"))
# value_number2 = int(input("Введите цифру 2:"))
# value_number3 = int(input("Введите цифру 3:"))
# print(value_number, value_number2, value_number3)

# a = int(input("Введите цифру 1:"))
# b = int(input("Введите цифру 2:"))
# c = int(input("Введите цифру 3:"))
# print(a*100+b*10+c)
# print(str(a)+str(b)+str(c))
# print(str(a)+str(b)+str(c), sep='')

# Пользователь вводит с клавиатуры число, стостящее из четырех цифр.
# Требуется найти произведение цифр
# Например, если с клавитуры введено 1324,
# Тогда результат произведения 1*3*2*3*4=24.
# a = int(input("Введите цифру:"))
# print( (a//1000)*((a//100)%10)*((a//10)%10)*(a % 10))
# a = input("Введите цифру:")
# print(int(a[0])*int(a[1])*int(a[2])*int(a[3]))
# Строки и их свойства
string = "my name is AaA"
print(type(string)) # Проверка типа данных
print(string + string) # Сложение строк
print(string * 4) # Умножение строк
print(string.capitalize()) #Приводит первую букву в верхний регистр
print(string.lower()) #Приводит все символы в нижний регистр
print(string.swapcase()) #Меняет текущий регист буквы на противоположный
print(string.title()) #Преобразует первые буквы всех слов в верхний регист
print(string.upper()) #Преобразует все буквы в верхний регистр
print(string.count( x="my",start=0,end=5)) #Подсчитывает количество элементов в строке
print(string.endswith("!")) #Проверяет заканчивает ли строка подстрокой
print(string.startswith("!")) #Проверяет начинается ли строка подстрокой
print(string.find("is")) #Ищет подстроку в строке слево на право
print(string.rfind("AaA")) #Ищет подстроку в строке право на слево
#Возвращает первое вхождение(индекс) подстроки
print(string.index("AaA")) #Ищет подстроку в строке слево на право
print(string.rindex("AaA")) #Ищет подстроку в строке право на слево
#Возвращает первое вхождение(индекс) подстроки, если элемента нет, будет ошибка
