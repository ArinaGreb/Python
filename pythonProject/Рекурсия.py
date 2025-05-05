# from random import random
#
#
# def factorial(n):
#     if n == 0:
#         return n * factorial(n-1)
#
#
# print(factorial(6))
#Рекрусиваня функция для нахождения степени числа
# def klad(a,n):
#     if n == 0:
#         return 1
#     else:
#         return a*klad(a,n-1)
# a = int(input())
# n = int(input())
# print(klad(a,n))
#функция вычисляет сумму элементов между a,b
# def sum(a,b):
#     if a==b:
#         return a
#     return a + sum(a+1,b)
#функция, которая выводит N звезд в ряд N задает пользователь
# def f4(N):
#     if N==0:
#         return "*"
#     return "*" + f4(N-1)
#функция, которая принимает список из 100 случайных элементов, находит позицию с которой начинается последовательность
#из 10 чисел, сумма которых минимальна.
import random
def f5(random_list, tek_pos=0,min_sum=1000, pos_sum=-1):
    #проврка на конец списка
    if tek_pos > len(random_list) - 10:
        return pos_sum
    tek_sum = sum(random_list[tek_pos:tek_pos+10])
    #если текущая сумма меньше минимальной суммы, обновляем ее и запоминаем позицию.
    if tek_sum < min_sum:
        min_sum = tek_sum
        pos_sum = tek_pos
    return f5(random_list,tek_pos+1,min_sum, pos_sum) #рекрусия
#MAIN
random_list = [random.randit(1,100) for i in range(100)] #список случайных чисел
print(f"Начальный список:{random_list}")
print("Позиция мин.суммы:"+f5(random_list))
print(f"Сумма: {random_list[a : a + 10]}")



