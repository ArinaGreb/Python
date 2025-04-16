#for (Условие):
    #Операция:
# for i in range(10,100):
#     print("*" * i)
#     i = 2
# sum = 0
# value = int(input("Введите число для ввода данных:"))
# for i in range(value):
#     sum = sum + int(input("Введите число:"))
#     print(i)
# del(i)
# # print(i)
# print(f'умма чисел пользователя: {sum}')
# for i in range(10):
#     print('%' * i, end=' ')
#     for j in range(10):
#         print("*", end=' ')
    # print('\n')


#Цикл while
#while (Условия):
    #программа, инструкции
# while True:
#     try:
#         age = int(input("Введите свой возраст: "))
#     except valueError:
#         print("Введите корректное значение!")
#         continue #завершает текущую иттерацию, игнорирует внутренний код и начинает новый виток цикла
#     break #используется как точка выхода из цикла
# print(f"Вы ввели свой возраст - {age}, вы старый")
# i = 0
# while i <= 10:
#     print(i**2)
#     i += 1
# f = 1
# valueUser = int(input("Введите значение для факториала:"))
# i = 1
# while i <= valueUser:
#     f *= i
#     print(f"Шаг{i} значение факториала:{f}")
#     i += 1
# print(f"Ваш факториал равен: {f}")
#проверка строки на палиндром через цикл while
stringUser = input("Введите строку для проверки:")
# А роза упала на лапу Азора
# а буду я у дуба
i = len(stringUser) -1
strA = ''
while i <= 0:
    strA += stringUser[i]
if strA == stringUser:
    print("Строка палиндром")
else:
    print("Строка - не палиндром")
strA = ''
for i in stringUser:
    strA += i + strA
if strA == stringUser:
    print()
if stringUser == stringUser[::-1]:
    print("Строка палиндром!")
#метод среза строки
#stringA = "Hello world"
# a = stringA[6] #'w'
# b = string[0:5]# 'Hello'
# c = stringA[0:5:2] #'Hlo'
# d = stringA[0:5:-1] #'olleH'
#stringB = " ".join(reversed(stringA))
#stringC = ",".join(reversed(stringA)) #'o,l,l,e,H'
#stringB = " ".split(reversed(stringA))
