#есть стопка оладий различного радиуса. Единственная операция, проводимая с ними - между двумя любыми оладьями
# просовываем лопатку и меняем порядок оладий на обратный
# Необходимо за минимальное количесвто операций таких отсортировать снизу вверх по убыванию радиуса оладья.
# def pancakes_sort(mass):
#     def find_largest_index(mass, n):
#         i = 0
#         for j in range(n):
#             if mass[j] > mass[i]:
#                 i = j
#         return i
#     def flip(mass, k):
#         return  mass[:k][::-1] + mass[k:]
#     result = []
#     n = len(mass)
#     while n > 1:
#         i = find_largest_index(mass, n)
#         if i < n - 1:
#             mass = flip(mass, i+1)
#             result.append(i+1)
#             mass = flip(mass, n)
#             result.append(n)
#         n -= 1
#     return result
# pancakes = [3, 1, 4, 5, 9, 6, 4, 3, 6, 4, 3, 6, 2, 4, 7]
# oper = pancakes_sort(pancakes)
# print(f"Оладья: {pancakes}")
# print(f"Операции: {oper}")
#МОДУЛЬ 7 сортировка и посик часть 3
#1
list1 = [3, 5, 7]
list2 = [2, 4, 6]
list3 = [1, 9, 8]
list4 = [0, 10, 11]

total_list = list1 + list2 + list3 + list4

print("Объединенный список:", total_list)

sort_order = input("Как отсортировать список? (возрастание/убывание): ")

if sort_order.lower() == "возрастание":
    total_list.sort()
    print("Отсортированный по возрастанию список:", total_list)
elif sort_order.lower() == "убывание":
    total_list.sort(reverse=True)
    print("Отсортированный по убыванию список:", total_list)
else:
    print("Неверный ввод, список остался без сортировки:", total_list)
search_value = int(input("Введите значение для поиска: "))
found = False
for i in range(len(total_list)):
    if total_list[i] == search_value:
        print(f"Значение {search_value} найдено на позиции {i}")
        found = True
        break

if not found:
    print(f"Значение {search_value} не найдено в списке")
#2
list1 = [3, 5, 7, 8]
list2 = [2, 4, 6, 11, 15]
list3 = [1, 9, 8]
list4 = [0, 10, 11]

total_list = list1 + list2 + list3 + list4
elements_counts = Counter(total_list)
unique_elements = [elem for elem, count in element_counts.items() if count == 1]
print("Уникальные элементы:", unique_elements)
sort_order = input("Введите порядок сортировки (asc или desc): ").strip().lower()
if sort_order == "asc":
    unique_elements.sort()
elif sort_order == "desc":
    unique_elements.sort(reverse=True)
else:
    print("Неверный ввод, сортирую по возрастанию.")
unique_elements.sort()

print("Отсортированный список:", unique_elements)
def binary_search(arr, x, ascending=True):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        if ascending:
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] > x:
                left = mid + 1
            else:
                right = mid - 1
    return -1

user_value = int(input("Введите число для поиска: "))
is_ascending = sort_order == "asc"
result_index = binary_search(unique_elements, user_value, is_ascending)

if result_index != -1:
    print(f"Число {user_value} найдено на позиции {result_index}.")
else:
    print(f"Число {user_value} не найдено в списке.")
