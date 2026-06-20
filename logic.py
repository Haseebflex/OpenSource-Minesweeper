import random

ROWS = 9
COLS = 9
MINES = 10

def create_board():
    # 1. Create a clean, empty 9x9 board filled with 0s
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
   
    # 2. Randomly place 10 mines (-1 represents a mine)
    count = 0
    while count < MINES:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        if board[r][c] != -1:
            board[r][c] = -1
            count += 1
           
    # 3. Calculate the numbers for safe cells (how many mines touch them)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == -1:
                continue
           
            # Check all 8 surrounding cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == -1:
                        board[r][c] += 1
                       
    return board

def get_neighbors(r, c):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                neighbors.append((nr, nc))
    return neighbors

def get_neighbors(r, c):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                neighbors.append((nr, nc))
    return neighbors



