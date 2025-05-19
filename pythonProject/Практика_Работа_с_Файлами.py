#Модуль 5 файлы Часть 1
#zadanie 1
with open('test.txt','w') as f:
    f.write("banana mango me the math mango-banana")

buffer = ''
with open('test.txt','r') as f:
    buffer = f.readline()
print(buffer)
buffer_list = buffer.split(" ")
print(buffer_list)
with open("test_result.txt",'w') as f:
    for i in range(len(buffer_list)-1):
        if len(buffer_list[i]) < 7:
            f.writelines(buffer_list)
#zadanie 2
with open('text_result.txt', f) as f:
    with open('new_text_result.txt','w') as fi:
        fi.write(r.readLines())
#zadanie 3
with open('input.txt', 'r') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    for line in reversed(lines):
        f.write(line)
#zadanie 4
with open('input.txt', 'r') as f:
    lines = f.readlines()
last_non_comma = -1
for i, line in enumerate(lines):
    if ',' not in line:
        last_non_comma = i
if last_non_comma != -1:
    lines.insert(last_non_comma + 1, '************\n')
else:
    lines.append('************\n')
with open('output.txt', 'w') as f:
    f.writelines(lines)
#zadanie 5
c = input()[0]
with open('input.txt', 'r') as f:
    words = f.read().split()
count = sum(1 for word in words if word.start(c))
print(count)
#zadanie 6
with open('input.txt', 'r') as f:
    lines = f.readlines()
with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line.replace('*', '&').replace('&', '*'))
#zadanie 7
arr = ["line1", "line2", "line3"]
with open('output.txt', 'w') as f:
    for line in arr:
        f.write(line + '\n')
#zadanie 8
arr = ["line1", "line2", "line3"]
with open('output.txt', 'w') as f:
    for line in arr:
        f.write(line + '\n')
#zadanie 9
with open('input.txt', 'r') as f:
    text = f.read()
print(len(text))
#zadanie 10
with open('input.txt', 'r') as f:
    lines = f.readlines()
print(len(lines))