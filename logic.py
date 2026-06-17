import random

ROWS = 9
COLS = 9
MINES = 10

def create_board():

    board = []

    for i in range(ROWS):
        row = []

        for j in range(COLS):
            row.append(0)

        board.append(row)

    return board


def place_mines(board):

    count = 0

    while count < MINES:

        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)

        if board[r][c] != -1:
            board[r][c] = -1
            count += 1

    return board
