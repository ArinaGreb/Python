#Задание 1
tuple1 = (1, 2, 3, 4)
tuple2 = (2, 3, 4, 5)
tuple3 = (3, 4, 5, 6)

common_elements = []
for num in tuple1:
    if num in tuple2 and num in tuple3:
        common_elements.append(num)

print("Элементы, которые есть во всех кортежах:", common_elements)
#Задание 2 
from collections import defaultdict

tuple1 = (1, 2, 3, 4)
tuple2 = (2, 3, 4, 5)
tuple3 = (3, 4, 5, 6)

count_dict = defaultdict(int)
for num in tuple1 + tuple2 + tuple3:
    count_dict[num] += 1

unique_elements = [num for num, count in count_dict.items() if count == 1]

print("Уникальные элементы:", unique_elements)
#Задание 3 
tuple1 = (1, 2, 3, 4)
tuple2 = (1, 5, 3, 7)
tuple3 = (1, 8, 3, 9)

common_elements_same_position = []
min_length = min(len(tuple1), len(tuple2), len(tuple3))

for i in range(min_length):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        common_elements_same_position.append(tuple1[i])

print("Элементы на одинаковых позициях во всех кортежах:", common_elements_same_position)