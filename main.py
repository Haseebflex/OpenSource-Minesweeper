from tkinter import *
from leaderboard import show_leaderboard

root = Tk()

root.title("Open Source Minesweeper")
root.geometry("700x700")
root.resizable(False, False)

title_label = Label(
    root,
    text="OPEN SOURCE MINESWEEPER",
    font=("Arial",20,"bold")
)

title_label.pack(pady=20)

name_label = Label(
    root,
    text="Player Name"
)

name_label.pack()

player_name = Entry(
    root,
    width=30
)

player_name.pack(pady=10)

leaderboard_button = Button(
    root,
    text="Leaderboard",
    width=20,
    command=show_leaderboard
)

leaderboard_button.pack(pady=10)

game_frame = Frame(
    root,
    width=450,
    height=450,
    bg="lightgray"
)

game_frame.pack(pady=20)

root.mainloop()