board = list(range(1, 10))


def grid(board):
    for i in range(3):
        print(board[0 + i * 3], " ", board[1 + i * 3], " ", board[2 + i * 3])
        print(" " * 13)


def player_turn(player_check):
    valid = False
    while not valid:
        player_answer = input("Укажите ячейку " + player_check)
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Введите число от 1 до 9")
            continue
        if player_answer > 0 and player_answer < 10:
            if str(board[player_answer - 1]) not in "X0":
                board[player_answer - 1] = player_check
                valid = True
            else:
                print("Эта клетка уже занята.")
        else:
            print("Некоректный ввод. Введите число от 1 до 9")


def check_win(board):
    win_coord = (
                 (0, 1, 2), (3, 4, 5),
                 (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)
                 )
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    count = 0
    win = False
    while not win:
        grid(board)
        if count % 2 == 0:
            player_turn("X")
        else:
            player_turn("0")
        count += 1
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "Выиграл.")
                win = True
                break
        if count == 9:
            print("Ничья.")
            break
    grid(board)


main(board)

while True:
    while True:
        answer = str(input('Нажмите Enter, чтобы начать заново. (Enter/n): '))
        if answer in ('', 'n'):
            break
        print("Некорректный ввод.")
    if answer == '':
        board = list(range(1, 10))
        main(board)
    else:
        break