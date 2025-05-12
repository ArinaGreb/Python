import random
from time import perf_counter
from unittest.mock import right


# Пузырьковая сортировка
def bubble_sort(mass):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(mass) - 1):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
                swapped = True

# Сортировка выбором
def selection_sort(mass):
    for i in range(len(mass)):
        lowest_value_index = i
        for j in range(i + 1, len(mass)):
            if mass[j] < mass[lowest_value_index]:
                lowest_value_index = j
        mass[i], mass[lowest_value_index] = mass[lowest_value_index], mass[i]

# Сортировка вставками (исправлено)
def insert_sort(mass):
    for i in range(1, len(mass)):
        item_to_insert = mass[i]
        j = i - 1
        while j >= 0 and mass[j] > item_to_insert:
            mass[j + 1] = mass[j]  # исправлено { } на [ ]
            j -= 1
        mass[j + 1] = item_to_insert
# Пирамидальная сортировка - сортировка кучей. Работает как два выше написанных алгоритма.
# Преобразует втрой элемент списка в структуру двнных "куча"(hear), чтобы можно было эффективно определить самый
# большой элемент.
def heapify(mass, heap_size, root_index):
    largest = root_index
    left_child = (2*root_index) + 1
    right_child = (2 * root_index) + 2
    #Если левый поток корня - допустимый индекс, а элемент болше, чем текущий наибольший, обновляем элемент
    if left_child < heap_size and mass[left_child] > mass[largest]:
        largest = left_child

    if right_child < heap_size and mass[right_child] > mass[largest]:
        largest = right_child

    if largest != root_index:
        mass[root_index], mass[largest] = mass[largest], mass[root_index]
        heapify(mass, heap_size, largest)

def heap_sort(mass):
    n = len(mass)
    for i in range(n, -1, -1):
        heapify(mass, n, i)
    for i in range(n-1, 0, -1):
        mass[0], mass[i] = mass[i], mass[0]
        heapify(mass, i, 0)
#рекрусивная сортировка с методом случайного выбора опорного элемента(pivot)
def quick_sort_randomizer_inplace(mass):
    def partition(mass, low, high):
        pivot_index = random.randint(low, high)
        mass[pivot_index], mass[low] = mass[low], mass[pivot_index]
        pivot = mass[low]

        i = low + 1
        j = high
        while True:
            while i <= j and mass[i] <= pivot:
                i += 1
            while i <= j and mass[j] > pivot:
                j -= 1
            if i > j:
                break
            mass[i], mass[j], = mass[j], mass[i]
            i += 1
            j += 1
        mass[low], mass[j] = mass[j], mass[low]
        return j
#быстрая сортировка по умолчанию
def quickSort(mass):
    if len(mass) > 1:
        pivot = mass.pop()
        grtr_lst, egual_list, smlr_lst = [], [pivot], []
        for item in mass:
            if item == pivot:
                egual_list.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + egual_list + quickSort(grtr_lst))
    else:
        return mass
#сортировка методом Шелла
def shellSort(mass):
    n = len(mass)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = mass[i]
            j = i
            while j >= interval and mass[j-interval] > temp:
                mass[j] = mass[j - interval]
                j -= interval
            mass[j] = temp
        interval //= 2
    return mass
# MAIN
random_mass = [random.randint(1, 10) for _ in range(10)]
print("Сортировка Пузырьком:")
print(f"Исходный: {random_mass}")
bubble_sort(random_mass)
print(f"Отсортированный: {random_mass}")

random_mass = [random.randint(1, 10) for _ in range(10)]
print("\nСортировка Выбором:")
print(f"Исходный: {random_mass}")
selection_sort(random_mass)
print(f"Отсортированный: {random_mass}")

random_mass = [random.randint(1, 10) for _ in range(10)]
print("\nСортировка Вставками:")  # исправлено название
print(f"Исходный: {random_mass}")
insert_sort(random_mass)  # исправлено item_to_insert → insert_sort
print(f"Отсортированный: {random_mass}")



