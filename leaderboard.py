from tkinter import *
from database import get_scores

def show_leaderboard():
    leaderboard_window = Toplevel()
    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("400x450")
    leaderboard_window.configure(bg="#1e1e2e")
    leaderboard_window.resizable(False, False)

    # Header Title
    Label(
        leaderboard_window,
        text="🏆 TOP 10 PLAYERS 🏆",
        font=("Helvetica", 18, "bold"),
        bg="#1e1e2e",
        fg="#f5c2e7"
    ).pack(pady=20)

    # Frame wrapper for clean list display
    list_frame = Frame(leaderboard_window, bg="#252538")
    list_frame.pack(pady=10, padx=25, fill="both", expand=True)

    scores = get_scores()

    if len(scores) == 0:
        Label(
            list_frame,
            text="No scores available yet.\nBe the first to win!",
            font=("Helvetica", 12, "italic"),
            bg="#252538",
            fg="#a6adc8"
        ).pack(pady=50)
    else:
        # Table Headers
        header = Frame(list_frame, bg="#252538")
        header.pack(fill="x", padx=15, pady=(10, 5))
        
        Label(header, text="Player", font=("Helvetica", 11, "bold"), bg="#252538", fg="#89b4fa").pack(side=LEFT)
        Label(header, text="Time", font=("Helvetica", 11, "bold"), bg="#252538", fg="#a6e3a1").pack(side=RIGHT, padx=(0, 10))
        Label(header, text="Score", font=("Helvetica", 11, "bold"), bg="#252538", fg="#fab387").pack(side=RIGHT, padx=30)
        
        # Divider Line
        Canvas(list_frame, height=2, bg="#45475a", highlightthickness=0).pack(fill="x", padx=15, pady=5)

        # Print out the leaderboard entries mapping to player[0], player[1], player[2]
        for i, player in enumerate(scores):
            row = Frame(list_frame, bg="#252538")
            row.pack(fill="x", padx=15, pady=6)
            
            lbl_name = Label(row, text=f"{i+1}.  {player[0]}", font=("Helvetica", 11), bg="#252538", fg="#cdd6f4")
            lbl_name.pack(side=LEFT)
            
            lbl_time = Label(row, text=f"{player[2]}s", font=("Helvetica", 11, "bold"), bg="#252538", fg="#a6e3a1")
            lbl_time.pack(side=RIGHT)
            
            lbl_score = Label(row, text=f"{player[1]}", font=("Helvetica", 11, "bold"), bg="#252538", fg="#fab387")
            lbl_score.pack(side=RIGHT, padx=45)