#Задание 1
def print_quote():
    print('"Don\'t let the noise of others\' opinions')
    print('drown out your own inner voice."')
    print('Steve Jobs')

print_quote()
#Задание 2
def numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

numbers(3, 10)
#Задание 3
def draw_line(length, direction, symbol):
    if direction == 'gozizontal':
        print(symbol * length)
    elif direction == 'vertical':
        for _ in range(length):
            print(symbol)
    else:
        print("Неверное направление. Используйте 'gozizontal' или 'vertical'.")

draw_line(5, 'gozizontal', '*')
draw_line(3, 'vertical', '|')
#Задание 4
def max_of_four(a, b, c, d):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    if d > max_num:
        max_num = d
    return max_num

print(max_of_four(3, 7, 2, 5))
#Задание 5
def sum_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

print(sum_in_range(1, 5))
#Задание 6
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
#Задание 7
def is_lucky_number(number):
    if 100000 <= number <= 999999:
        digits = [int(d) for d in str(number)]
        return sum(digits[:3]) == sum(digits[3:])
    else:
        return False

print(is_lucky_number(123420))
print(is_lucky_number(723422))