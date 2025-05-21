#zadanie1:
#!/usr/bin/python
# -*- coding: utf-8 -*-
def filter_file():
    #читаем заперщенные слова
    with open('bad_words.txt', 'r', encoding='utf-8') as f:
        bad_words = [word.strip() for word in f.readlines()]

    # Читаем исходный файл
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Удаляем запрещённые слова
    for word in bad_words:
        text = text.replace(word, '***')

    # Записываем результат
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(text)

filter_file()
#zadanie2:

#zadanie3:

#zadanie4:
