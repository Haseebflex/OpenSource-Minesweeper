Markdown
# Contribution & Collaboration Guide

Welcome to the team! This document outlines the git workflow, codebase structure, and integration specifications for our Minesweeper semester project. Please review these rules before writing or merging code to prevent conflicts.

---

## 🛠️ Branching Strategy

To keep the stable code secure on the `main` branch, all members must develop features on separate, isolated branches:

1. **Pull the latest project state** from the remote repository before making code changes:
```bash
   git pull origin main

   1: Create your feature branch using a descriptive component tag:
   Bash
   # Examples:
   git checkout -b feature/database-backend
   git checkout -b feature/game-logic

   🧩 Inter-Module Integration Specs
Because our project is highly modular, please conform strictly to the following architectural agreements to ensure our components seamlessly hook together:

1. Database Integration (database.py)
The file must export a function named get_scores().

get_scores() must return a list of tuples sorted by performance, containing exactly three items per player row: (str(username), int(score), int(time_in_seconds)).

2. UI Container Hooks (main.py & leaderboard.py)
The core game logic component must draw its grid buttons inside the pre-allocated game_frame Tkinter Frame object exported by main.py.

To keep presentation consistent across systems, do not modify the static application window configurations (700x700 layout dimensions, resizable = False).

📝 Code Requirements & Conventions
Variable Naming: Write explicit, clear naming definitions for Tkinter widgets (e.g., use leaderboard_button instead of generic names like button1).

State Integrity: Keep database mutations safe. Avoid accessing data records raw outside of dedicated methods inside database.py.

Clean Commits: Provide clear messages detailing what changes were introduced so your teammates can follow along smoothly in the commit history.

Recommended pattern: git commit -m "Fix: updated data padding layout in leaderboard window lines"

🚀 Submitting Pull Requests (PRs)
Push your local feature branch to the central GitHub repository.

Open a Pull Request targeting the main branch.

Assign a team member to review the implementation and verify that nothing breaks before finalizing the merge.