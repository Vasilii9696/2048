import random

import os



# Инициализация игровой доски

def initialize_game():

    board = [[0] * 4 for _ in range(4)]

    add_new_tile(board)

    add_new_tile(board)

    return board



# Добавление новой плитки

def add_new_tile(board):

    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]

    if empty_cells:

        i, j = random.choice(empty_cells)

        board[i][j] = random.choice([2, 4])



# Поворот доски на 90 градусов

def rotate_board(board):

    return [list(row) for row in zip(*board[::-1])]



# Сжатие плиток

def compress(board):

    new_board = [[0] * 4 for _ in range(4)]

    for i in range(4):

        pos = 0

        for j in range(4):

            if board[i][j] != 0:

                new_board[i][pos] = board[i][j]

                pos += 1

    return new_board



# Объединение плиток

def merge(board):

    for i in range(4):

        for j in range(3):

            if board[i][j] == board[i][j + 1] and board[i][j] != 0:

                board[i][j] *= 2

                board[i][j + 1] = 0

    return board



# Ход игрока

def move_left(board):

    new_board = compress(board)

    new_board = merge(new_board)

    new_board = compress(new_board)

    return new_board



def move_right(board):

    board = rotate_board(rotate_board(board))

    board = move_left(board)

    board = rotate_board(rotate_board(board))

    return board



def move_up(board):

    board = rotate_board(rotate_board(rotate_board(board)))

    board = move_left(board)

    board = rotate_board(board)

    return board



def move_down(board):

    board = rotate_board(board)

    board = move_left(board)

    board = rotate_board(rotate_board(rotate_board(board)))

    return board



# Отображение доски

def display_board(board):

    os.system('cls' if os.name == 'nt' else 'clear')

    for row in board:

        print('\t'.join(map(str, row)))

        print()



# Проверка окончания игры

def check_game_over(board):

    for i in range(4):

        for j in range(4):

            if board[i][j] == 0:

                return False

            if i < 3 and board[i][j] == board[i + 1][j]:

                return False

            if j < 3 and board[i][j] == board[i][j + 1]:

                return False

    return True



# Основной цикл игры

def play_game():

    board = initialize_game()

    while True:

        display_board(board)

        move = input("Введите ход (W, A, S, D): ").upper()

        if move == 'W':

            board = move_up(board)

        elif move == 'A':

            board = move_left(board)

        elif move == 'S':

            board = move_down(board)

        elif move == 'D':

            board = move_right(board)

        else:

            print("Некорректный ввод, попробуйте снова.")

            continue



        add_new_tile(board)

        if check_game_over(board):

            display_board(board)

            print("Игра окончена!")

            break



if __name__ == "__main__":

    play_game()

