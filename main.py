from tkinter import *
from tkinter import messagebox
from leaderboard import show_leaderboard
import logic
import database
import time

# UI Color Palette (Cyber Dark Theme)
BG_COLOR = "#1e1e2e"       
FRAME_BG = "#252538"       
TEXT_MAIN = "#cdd6f4"      
ACCENT_BLUE = "#89b4fa"    
ACCENT_GREEN = "#a6e3a1"   
MINE_COLOR = "#f38ba8"     
BTN_UNREVEALED = "#45475a" 

root = Tk()
root.title("Open Source Minesweeper")
root.geometry("600(x)800".replace("(x)", "x")) # Standard geometry dimensions
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Tracking states
backend_board = logic.create_board()
buttons_grid = []
start_time = None
game_active = False
score_counter = 0
total_safe_tiles = (logic.ROWS * logic.COLS) - logic.MINES

def start_game_timer():
    global start_time, game_active, score_counter
    if not game_active:
        start_time = time.time()
        game_active = True
        score_counter = 0
        update_timer_label()

def update_timer_label():
    if game_active and start_time:
        elapsed = int(time.time() - start_time)
        timer_label.config(text=f"⏱️ TIME: {elapsed}s")
        root.after(1000, update_timer_label)

def on_click(r, c):
    global score_counter, game_active
    player = player_name.get().strip()
    if not player:
        messagebox.showwarning("Name Required", "Please enter your Player Name before starting the game!")
        return

    # Initialize timer on the first click
    if not game_active and start_time is None:
        start_game_timer()

    value = backend_board[r][c]
    btn = buttons_grid[r][c]
    
    # Ignore clicking already opened buttons
    if btn["state"] == "disabled":
        return

    if value == -1:
        # Game Over - Hit a mine
        game_active = False
        elapsed_time = int(time.time() - start_time) if start_time else 0
        btn.config(text="💣", bg=MINE_COLOR, fg="#000000", disabledforeground="#000000")
        reveal_all_mines()
        
        # Save score even upon losing what they earned!
        database.save_score(player, score_counter, elapsed_time)
        messagebox.showerror("BOOM!", f"Game Over, {player}!\nScore: {score_counter}\nTime: {elapsed_time}s")
        reset_game()
    else:
        # Safe tile revealed
        score_counter += 10
        score_label.config(text=f"⭐ SCORE: {score_counter}")
        
        if value == 0:
            btn.config(text="", bg="#313244", state="disabled")
        else:
            colors = ["", "#89b4fa", "#a6e3a1", "#f38ba8", "#cba6f7", "#fab387", "#74c7ec", "#94e2d5", "#f9e2af"]
            btn.config(text=str(value), bg="#313244", fg=colors[value], disabledforeground=colors[value], font=("Helvetica", 12, "bold"), state="disabled")
        
        # Check Win Condition
        opened_tiles = 0
        for row in buttons_grid:
            for b in row:
                if b["state"] == "disabled":
                    opened_tiles += 1
                    
        if opened_tiles == total_safe_tiles:
            game_active = False
            elapsed_time = int(time.time() - start_time)
            # Big bonus score for complete survival
            score_counter += 500
            score_label.config(text=f"⭐ SCORE: {score_counter}")
            reveal_all_mines()
            
            database.save_score(player, score_counter, elapsed_time)
            messagebox.showinfo("VICTORY! 🎉", f"Incredible job {player}!\nYou cleared the minefield!\nFinal Score: {score_counter}\nTime: {elapsed_time}s")
            reset_game()

def reveal_all_mines():
    for r in range(logic.ROWS):
        for c in range(logic.COLS):
            if backend_board[r][c] == -1:
                buttons_grid[r][c].config(text="💣", bg=MINE_COLOR, fg="#000000")

def reset_game():
    global backend_board, start_time, game_active, score_counter
    backend_board = logic.create_board()
    start_time = None
    game_active = False
    score_counter = 0
    score_label.config(text="⭐ SCORE: 0")
    timer_label.config(text="⏱️ TIME: 0s")
    for r in range(logic.ROWS):
        for c in range(logic.COLS):
            buttons_grid[r][c].config(text="", bg=BTN_UNREVEALED, state="normal", relief="raised")

# --- UI Layout Design ---

title_label = Label(root, text="MINESWEEPER", font=("Helvetica", 26, "bold"), bg=BG_COLOR, fg=ACCENT_BLUE)
title_label.pack(pady=(25, 5))

input_frame = Frame(root, bg=BG_COLOR)
input_frame.pack(pady=5)

name_label = Label(input_frame, text="PLAYER NAME", font=("Helvetica", 10, "bold"), bg=BG_COLOR, fg=TEXT_MAIN)
name_label.pack()

player_name = Entry(
    input_frame, width=24, font=("Helvetica", 12), bg="#313244", fg=TEXT_MAIN,
    insertbackground=TEXT_MAIN, bd=0, highlightthickness=2, highlightbackground="#45475a",
    highlightcolor=ACCENT_BLUE, justify="center"
)
player_name.pack(pady=8, ipady=4)
player_name.insert(0, "Player1")

# Stats Readout Frame
stats_frame = Frame(root, bg=BG_COLOR)
stats_frame.pack(pady=5)

score_label = Label(stats_frame, text="⭐ SCORE: 0", font=("Helvetica", 12, "bold"), bg=BG_COLOR, fg="#fab387")
score_label.pack(side=LEFT, padx=20)

timer_label = Label(stats_frame, text="⏱️ TIME: 0s", font=("Helvetica", 12, "bold"), bg=BG_COLOR, fg=ACCENT_GREEN)
timer_label.pack(side=RIGHT, padx=20)

leaderboard_button = Button(
    root, text="🏆 View Leaderboard", font=("Helvetica", 11, "bold"), bg=FRAME_BG, fg="#f5c2e7",
    activebackground="#f5c2e7", activeforeground=BG_COLOR, bd=0, cursor="hand2", width=20, pady=6,
    command=show_leaderboard
)
leaderboard_button.pack(pady=10)

game_frame = Frame(root, bg=FRAME_BG, padx=10, pady=10, relief="flat")
game_frame.pack(pady=10)

# Build Grid
for r in range(logic.ROWS):
    row_btns = []
    for c in range(logic.COLS):
        btn = Button(
            game_frame, text="", width=3, height=1, font=("Helvetica", 14, "bold"),
            bg=BTN_UNREVEALED, activebackground="#585b70", bd=1, relief="raised",
            command=lambda row=r, col=c: on_click(row, col)
        )
        btn.grid(row=r, column=c, padx=2, pady=2)
        row_btns.append(btn)
    buttons_grid.append(row_btns)

root.mainloop()