

board = [' '] * 9
player = 'x'
winner = None
game_running = True
winlist = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
#список комбинаций для победы
#вывод игрового поля
print("Добро пожаловать в игру: Крестики-Нолики!")
print("Играем на поле с выбором клеток: ")
print("1 | 2 | 3")
print("-"*9)
print("4 | 5 | 6")
print("-"*9)
print("7 | 8 | 9")
print("-"*9)
print("Удачи и хорошей игры!\n","*"*11)
#Игровой процесс
while game_running:
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("-" * 9)
    #ход игрока
    print(f"Ход игрока: {player}")
    while True:
        try:
            position = int(input("Выберите позицию для хода(1-9):")) - 1
            if 0 <= position <= 8 and board[position] == ' ':
                break
            else:
                print("Некоректный ход. Обдумайте еще раз!")
        except ValueError:
            print("Попробуйте ввести число от 1-9!!!")
    board[position] = player
    #проверка на победителя!
    for combo in winlist:
        if (board[combo[0]] == board[combo[1]] == board[combo[2]] != ' '):
            winner = player
            game_running = False
            break
    #проверка на ничью
    if ' ' not in board:
        game_running = False
    if player == 'x':
        player = 'o'
    else:
        player = 'x'

#вывести на финальную доску
print("Финальная доска:")
print(f"{board[0]} | {board[1]} | {board[2]}")
print("-" * 9)
print(f"{board[3]} | {board[4]} | {board[5]}")
print("-" * 9)
print(f"{board[6]} | {board[7]} | {board[8]}")
print("-" * 9)
if winner:
    print(f"Победил игрок {winner}")
else:
    print("Игра закончилась ничьей!!!")
print("Приходите к нам еще!")