#Файл - это всего лишь набор данных представленных в виде последовательности битов на ПК, информация хранится в куче
# данных(сттруктура данных) и имеет название "Имя файла"
# В пайтоне есть 2 типа данных:
# 1. текстовые *.txt *.rtf
# 2. бинарные *.bin
# Последовательность операций:
# 1. открытие файла
# 2. выполнение операций(чтение, запись)
# 3. закрытие потока

f = open('test.txt', 'r')
# r - только для чтения
# w - только для записи. если файла нет, он его создаст
# rb - только для чтения(бинарный файл)
# wb - только для записи(бинарный файл)
# r+ - для чтения и записи
# a - открытие файла для редактирования. так же создает новый файл, если он не найден
# rb +, wb+, a+, ab, ab+
# print(*f) # * - распаковка любого типа данных
# f.close() #закрытие потока работы с файлом
#
# f = open('test.txt', 'r')
# try:
#     print(*f)
# finally:
#     f.close()
#
# with open('test.txt','r') as f:
#     print(f.read(10)) #чтение определенного кол-во символов
#     print(f.readLine(0)) #функция работы со строками
#     print(f.readLine(1))
#     print(f.readLines(2))
#     # print(*f)
# width open("practic.txt","w") as f:
#     f.write("Per aspera ad astra")
# with open("practic.txt","r") as f:
#     print(f.readlines())
# file.fileno() - проверка целостности файла
# file.flush() - очистка буфера обмена файла(поток)
# file.isatty() - возвращает True, если файл закреплен для
# file.next() - возвращает след. строку из файла
# file.seek - устанавливает текущую позицию указателя в файле
# file.seekable() - проверяет доступ к файлу, случайный доступ
# file.tell() - возвращает текущую позицию в файле
# file.truncate() - уменьшает размер файла, если n указана, то файл обрезается до n-байта, если нет - то
# до текущей позиции
# file.writelines() - добавляет последовательность строк в файлах
import os
#os.rename('test.txt', 'test123.txt')
#Пример реализации приложения "Шпионаж".
def file_collector(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files":[]}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result['dirs'].append(dir)
        for file in filenames:
            result['files'].append(file)
    f = open("collector.txt",'w')
    f.write("*"*4+f"Directories"+"*"*4)
    for dir in result['dirs']:
        f.write(f'\n {dir}\n')
    f.write("*" * 4 + f"Files" + "*" * 4)
    for file in result['files']:
        f.write(f'\n {file}\n')
    f.close()
path='C:\\Users\\Mp\\Downloads\\Список литературы'
file_collector(path)