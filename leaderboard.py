from tkinter import *
from database import get_scores

def show_leaderboard():

    leaderboard_window = Toplevel()

    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("400x300")

    Label(
        leaderboard_window,
        text="Top 10 Players",
        font=("Arial",16,"bold")
    ).pack(pady=10)

    scores = get_scores()

    if len(scores) == 0:
        Label(
            leaderboard_window,
            text="No scores available"
        ).pack()
    else:

        for player in scores:

            Label(
                leaderboard_window,
                text=f"{player[0]} | Score: {player[1]} | Time: {player[2]}s"
            ).pack()