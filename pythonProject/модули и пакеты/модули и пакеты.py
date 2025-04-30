import  math as mt, sys
from confing import *
from platform import platform,machine, processor, system, version
#print(mt.pi)
#print(user_value)

#for name in dir(mt):
    #print(name, end='\t')
# print(system())
# print(version())
# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print(machine())
# print(processor())
#
# def plus(c, d):
#     return f"{c}+{d}={c+d} \n"
#     pass
# def minus(a,b):
#     return f"{a}-{b}={a-b} \n"
#     pass
# def delet(a,b):
#     return f"{a}/{b}={a / b} \n"
#     pass
# def umnoj(a,b):
#     return f"{a}*{b}={a * b} \n"
#     pass
# def calcul(a,b):
#     a = int(input("Value1:"))
#     b = int(input("Value2:"))
#     print(plus(a,b))
#    umnoj(a,b)
#    delet(a,b)
#    minus(a,b)
#MAIN

# if __name__=="__main__":
#     calcul()

#Задание 1 Напишите функцию, которая отображает: "Не сравнивайте себя ни с кем. Это оскорбительно в первую очередь для вас!"
#Билл Гейтс
def print_f():
    print("Не сравнивайте себя ни с кем."
          "Это оскорбительно в первую очередь для вас! \n Билл Гейтс")
print_f()
#Задание 2 Напишите функцию, которая принимает два числа в качетсве параметра и отображает все четные числа между ними.
def print_f():
    if a > b:
        a,b = b,a
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i,end=' ')
value1 = int(input())
value2 = int(input())
chet(value1, value2)
#Задание 3 