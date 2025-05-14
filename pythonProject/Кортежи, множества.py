#Кортеж - неизменяемая структура данных, кот. По своему подобию похожа на список. Список - неизменяемый тип данных
# [1,2,3]
# a = [1,2,3]
# a [1] = 5
# print(a)
# b = (1,2,3)
# b [1] = 15 #ошибка TypeError
#print(b)
#Плюсы:
# 1) экономия места
# 2) в процессе работы, данные в безопасности
# 3) выше производительность программы
from itertools import islice

a = (1,2,3)
print(type(a))
print(a[1])
del a

lst = [1,2,3,4,5]
print(type(lst))
print(lst)
tpl = tuple(lst)
print(type(tpl))
print(tpl)

# Обратно в список
lst2 = list(tpl)
print(type(lst2))
print(lst2)

# Словари (dict)
dictionari = {
    "Персона": "Человек",
    "Марафон": "Гонка бегунов длиной около 26 миль",
    "Айфон": 15,
}

dictionari2 = {
    (1, 1/2, 0.2): "Кортежи могут быть ключами",
    1: "Целые числа могут быть ключами",
    "бежать": "СТРОКИ ТОЖЕ",
}

# Не работают нехэшируемые типы данных
dictionari3 = {True: 'yes', 1: 'no', 1.0: 'maybe'}

# Работа со словарями
d = {}
d = {'dick_key': 'dict_value'}
d = dict(short='dict', lond='dictionary')
d['index'] = 20
d = dict.fromkeys(['a', 'b'], 100)

key_list = ['marvel', 'dc']
value_list = ['Spiderman', 'Flash']
superhero_list = dict(zip(key_list, value_list))

d = {i: i**2 for i in range(10)}
print(d)

dictionari4 = {"Марафон": 26}
print(dictionari4['Марафон'])

story_dict = {"Сто":100, "Двести":200,"Триста":300}
for key in story_dict:
    print(key)
for key,value in story_dict.item():
    print(key, value)
#Сортировка
people = {3:'jim',
          4:'olga',
          5:'ivan',
          6:'kirill'}
print(sorted(people))
#Если задача состоит в том что словарь слишком большой а вам нужно лишь его часть вам поможем метод islice()
nd = dict(islice(people.items(), 0, 3))
print(nd)
#dict to list
people_list =[]
for key, value in people.items():
    temp = [key, value]
    people_list.append(temp)
# p_l = [[key,value] for key, value in people.items()]

#множества(set) - контейнер не повторяющиеся элементы в случайном порядке
# создание множества
s = set()
print(type(s))
s = set('hello')
#{'h','e','l','o'}
s = {i **2 for i in range(10)}
print(s)
#методы set
# len() #проверка принадлежностей
#s.isdisjoint(other) - истина, если set и other
#не имеют общих элементов
#set == other - проверка всех элемнтов множества на пересечении с другим множеством
# s.issubset(other) - проверка принадлежности можества
#s.issubset(other) - проверка 2множества на вхождение в 1
# # s.uion(other,...) #объединение нескольких множеств
# s.intersection(other) - пересечение множеств
# s.difference - множество элементов, уникальных в 2х множеств
# s.symmetric_difference() - уникальные встречающиеся элементы
# s.copy()
# s.update(other)
# s.intersection_update(other)
# s.simmetric_difference_update(other)
# s.add(item) - добавление элемента
# s.remove(item)- удаление
# s.discard(item) - удаление элемента если он есть в множестве
# s.pop() - удалаяет случайный элемент
# s.clear() - очистка множества

#задача инвестора
our_products = {"Apple","Tesla","DNS"}
range_of_company1 = {"Samsung","Sony"}
range_of_company2 = {"Apple","BMW","IBM"}
range_of_company3 = {"BMW","Tesla","DNS","Ferrary"}
print("Акции которые уже у нас есть в 3х списках:")
print(our_products.intersection(range_of_company1))
print(our_products.intersection(range_of_company2))
print(our_products.intersection(range_of_company3))
#Противоположная задача
print("Акции которых нет у нас в 3х списках:")
print(our_products.difference(range_of_company1))
print(our_products.difference(range_of_company2))
print(our_products.difference(range_of_company3))
#Разница в товарах
print("Разница в 3х списках:")
print(our_products.symmetric_difference(range_of_company1))
print(our_products.symmetric_difference(range_of_company2))
print(our_products.symmetric_difference(range_of_company3))
fronzenset_product = frozenset(our_products) #замороженный портфель
#Пример 2 "Журнал Юзера"
my_dict = {"Никита":{
                    "tel": "12345678910",
                    "ok":"ok.ru/nikita41"
                    },
            "Marina":{
                    "tel": "12345678910",
                    "ok": "ok.ru/marina10"
            },
            "Max":{
                    "tel": "12345678910",
                    "ok": "ok.ru/max100"
            },
}
user = my_dict[input("Введите имя пользователя:")][input("Что конкретно? -->")]
print(user)

