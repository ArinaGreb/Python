#задание1
def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        line_number = 1
        while True:
            line1 = file1.readline()
            line2 = file2.readline()
            
            if not line1 and not line2:
                print("Файлы идентичны.")
                break
                
            if line1 != line2:
                print(f"Несовпадение в строке {line_number}:")
                print(f"Файл 1: {line1.strip()}")
                print(f"Файл 2: {line2.strip()}")
                break
                
            line_number += 1

compare_files('file1.txt', 'file2.txt')

#задание2
def file_statistics(input_file, output_file):
    vowels = 'аеёиоуыэюяaeiou'
    consonants = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz'
    digits = '0123456789'
    
    char_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            for char in line.lower():
                char_count += 1
                if char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1
                elif char in digits:
                    digit_count += 1
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Количество символов: {char_count}\n")
        file.write(f"Количество строк: {line_count}\n")
        file.write(f"Количество гласных букв: {vowel_count}\n")
        file.write(f"Количество согласных букв: {consonant_count}\n")
        file.write(f"Количество цифр: {digit_count}\n")

file_statistics('input.txt', 'statistics.txt')

#задание3
def remove_last_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if lines:
        lines = lines[:-1]
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)

remove_last_line('input.txt', 'output.txt')

#задание4
def longest_line_length(filename):
    max_length = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_length = len(line.rstrip('\n'))
            if line_length > max_length:
                max_length = line_length
    return max_length

length = longest_line_length('text.txt')
print(f"Длина самой длинной строки: {length}")

#задание5
def count_word_occurrences(filename, target_word):
    count = 0
    target_word = target_word.lower()
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split()
            count += words.count(target_word)
    
    return count

word = input("Введите слово для поиска: ")
count = count_word_occurrences('text.txt', word)
print(f"Слово '{word}' встречается {count} раз(а) в файле.")

#задание6
def replace_word_in_file(input_file, output_file, old_word, new_word):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified_content = []
    for word in content.split():
        if word.lower() == old_word.lower():
            modified_content.append(new_word)
        else:
            modified_content.append(word)
    modified_content = ' '.join(modified_content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)

old_word = input("Введите слово для замены: ")
new_word = input("Введите слово для замены: ")
replace_word_in_file('input.txt', 'output.txt', old_word, new_word)
print("Замена выполнена успешно!")




