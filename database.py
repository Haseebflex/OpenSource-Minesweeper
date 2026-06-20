import sqlite3

conn = sqlite3.connect("leaderboard.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leaderboard(
id INTEGER PRIMARY KEY AUTOINCREMENT,
player_name TEXT,
score INTEGER,
time_taken INTEGER
)
""")

conn.commit()


def save_score(name, score, time_taken):
    cursor.execute(
        "INSERT INTO leaderboard(player_name,score,time_taken) VALUES(?,?,?)",
        (name, score, time_taken)
    )
    conn.commit()


def get_scores():
    cursor.execute("""
    SELECT player_name,score,time_taken
    FROM leaderboard
    ORDER BY score DESC,time_taken ASC
    LIMIT 10
    """)
    return cursor.fetchall()