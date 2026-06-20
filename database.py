import sqlite3

def init_db():
    """Creates the database and table if they don't exist yet."""
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
    conn.close()

def save_score(name, score, time_taken):
    """Saves the player's final game score and time taken to the database."""
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leaderboard(player_name,score,time_taken) VALUES(?,?,?)",
        (name, score, time_taken)
    )
    conn.commit()
    conn.close()

def get_scores():
    """Fetches the top 10 scores, sorting by highest score first, then fastest time."""
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT player_name,score,time_taken
    FROM leaderboard
    ORDER BY score DESC,time_taken ASC
    LIMIT 10
    """)
    results = cursor.fetchall()
    conn.close()
    return results

# Automatically build table layout on launch
init_db()