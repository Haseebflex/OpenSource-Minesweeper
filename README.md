Markdown
# Open Source Minesweeper

A classic Minesweeper game built with Python using the **Tkinter** GUI library and **SQLite** for local database management. This project demonstrates modular desktop application development, relational database integration, and collaborative open-source workflows.

---

## 🚀 Features

* **Main Dashboard:** Clean Tkinter interface with a user profile name input field.
* **Dynamic Minesweeper Grid:** Interactive central gameplay frame designed for modular component rendering.
* **Real-time Leaderboard:** Dedicated pop-up UI window that fetches and displays the **Top 10 Players** directly from an SQLite database.
* **Modular Architecture:** Cleanly separated UI, game logic, and database storage modules to allow team-wide parallel development.

---

## 📂 Project Architecture

The project is structured into independent Python modules to facilitate team collaboration:

* `main.py` - The primary application entry point. Handles the root window, player name acquisition, and holds the `game_frame` canvas container.
* `leaderboard.py` - Manages the leaderboard pop-up window interface and handles formatting the list rows.
* `database.py` - *Backend module* (handled by team members) responsible for SQLite database connections, data insertions, and high-score queries.
* `logic.py` - *Game engine module* (handled by team members) managing cell states, mine allocation grids, and win/loss checking.

---

## 🔧 Installation & Setup

Ensure you have Python 3.x installed on your operating system before proceeding.

### 1. Clone the Project
```bash
git clone [https://github.com/YOUR_USERNAME/minesweeper.git](https://github.com/YOUR_USERNAME/minesweeper.git)
cd minesweeper

2. Install Dependencies
This project relies on Python's built-in libraries (tkinter and sqlite3). Any external requirements can be installed via:

Bash
pip install -r requirements.txt
3. Run the Application
Bash
python main.py
📊 Database Connectivity Preview
The leaderboard module reads from the database and processes records expecting a tuple layout corresponding to:
Username | Score: [Score] | Time: [Time]s

👥 Team Members
Muhammad Haseeb (F2024105186)

Hira Tayyab (F2024105196)

Maram Khalid (F2024105271)

📄 License
This project is developed for academic evaluation as a semester assignment. Distributed under the MIT License.