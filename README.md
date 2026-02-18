# 🎬 Movie Watchlist App

A command-line movie watchlist application built with **Python** and **SQLite**. Track movies, manage users, mark films as watched, and search your collection — all from the terminal.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Database Schema](#-database-schema)
- [How It Works](#-how-it-works)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| **Add Movies** | Add new movies with a title and release date to your collection |
| **View Upcoming** | See movies with release dates in the future |
| **View All Movies** | Browse your entire movie library |
| **Mark as Watched** | Associate watched movies with specific users |
| **View Watched List** | See all movies a particular user has watched |
| **User Management** | Register new users to the app |
| **Search** | Search for movies by partial title match |

---

## 🛠 Tech Stack

- **Language:** Python 3.11+
- **Database:** SQLite 3 (via Python's built-in `sqlite3` module)
- **Dependencies:** None — uses only the Python standard library

---

## 📁 Project Structure

```
movie-watchlist/
├── app.py          # Main application entry point & CLI menu
├── database.py     # Database connection, queries, and helper functions
├── data.db         # SQLite database file (auto-created on first run)
└── README.md       # Project documentation
```

| File | Purpose |
|---|---|
| `app.py` | Handles user interaction through a text-based menu. Collects input, formats output, and delegates data operations to `database.py`. |
| `database.py` | Manages the SQLite database — creates tables, inserts records, and runs queries. All SQL statements are defined as constants for clarity. |
| `data.db` | The SQLite database file storing all movies, users, and watched records. Automatically created when the app runs for the first time. |

---

## 📌 Prerequisites

- **Python 3.11** or higher installed on your system
- No additional packages or virtual environments required

Verify your Python version:

```bash
python3 --version
```

---

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/movie-watchlist-app.git
   cd movie-watchlist-app
   ```

2. **Run the application:**

   ```bash
   python3 app.py
   ```

   That's it — no dependencies to install. The SQLite database (`data.db`) is created automatically on the first run.

---

## 🎮 Usage

When you launch the app, you'll see an interactive menu:

```
Welcome to the watchlist app!

Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.

Your selection:
```

### Menu Options

| Option | Action | Required Input |
|---|---|---|
| `1` | Add a new movie | Movie title, release date (`dd-mm-YYYY`) |
| `2` | View upcoming movies | — |
| `3` | View all movies | — |
| `4` | Mark a movie as watched | Username, Movie ID |
| `5` | View a user's watched movies | Username |
| `6` | Register a new user | Username |
| `7` | Search for a movie | Partial or full movie title |
| `8` | Exit the application | — |

> **Note:** When adding a movie, if you leave the release date blank, it defaults to today's date.

---

## 🗄 Database Schema

The app uses three SQLite tables:

### `movies`

| Column | Type | Description |
|---|---|---|
| `id` | `INTEGER` (PK) | Auto-incrementing unique movie identifier |
| `title` | `TEXT` | The movie title |
| `release_timestamp` | `REAL` | Unix timestamp of the release date |

### `users`

| Column | Type | Description |
|---|---|---|
| `username` | `TEXT` (PK) | Unique username |

### `watched`

| Column | Type | Description |
|---|---|---|
| `user_username` | `TEXT` (FK → `users.username`) | The user who watched the movie |
| `movie_id` | `INTEGER` (FK → `movies.id`) | The movie that was watched |

### Indexes

- `movies_release_idx` — Index on `movies.release_timestamp` for faster upcoming movie queries.

### Entity Relationship

```
┌──────────┐       ┌───────────┐       ┌──────────┐
│  users   │       │  watched  │       │  movies  │
├──────────┤       ├───────────┤       ├──────────┤
│ username │◄──────│ user_     │       │ id       │
│  (PK)   │       │ username  │       │  (PK)    │
└──────────┘       │ movie_id  │──────►│ title    │
                   └───────────┘       │ release_ │
                                       │ timestamp│
                                       └──────────┘
```

---

## ⚙ How It Works

1. **Startup** — `app.py` prints a welcome message and calls `database.create_tables()` to ensure all tables and indexes exist.
2. **Menu Loop** — The app enters a `while` loop using Python's walrus operator (`:=`), continuously prompting the user until they select option `8`.
3. **Data Layer** — All database interactions go through `database.py`, which uses parameterized queries to prevent SQL injection.
4. **Date Handling** — Dates are stored as Unix timestamps (`REAL`) and converted to human-readable format (`%b %d %Y`) for display.
5. **Search** — Movie search uses SQLite's `LIKE` operator with wildcards for partial title matching.

---

## 📝 Examples

### Adding a Movie

```
Your selection: 1
Movie title: The Matrix Resurrections
Release date (dd-mm-YYYY): 22-12-2021
```

### Viewing All Movies

```
Your selection: 3
-- All movies --
1: The Matrix Resurrections (on Dec 22 2021)
2: Dune Part Two (on Mar 01 2024)
----
```

### Registering a User and Marking a Movie as Watched

```
Your selection: 6
Username: alice

Your selection: 4
Username: alice
Movie ID: 1
```

### Viewing Watched Movies

```
Your selection: 5
Username: alice
-- Watched movies --
1: The Matrix Resurrections (on Dec 22 2021)
----
```

### Searching for a Movie

```
Your selection: 7
Enter partial movie title: matrix
-- Movies found movies --
1: The Matrix Resurrections (on Dec 22 2021)
----
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add: description of your change"
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** describing your changes

### Ideas for Contributions

- Add movie ratings or reviews
- Implement movie categories/genres
- Add a "recommend a movie" feature
- Create a web-based frontend (Flask/Django)
- Add data export (CSV/JSON)
- Write unit tests for `database.py`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with Python 🐍 and SQLite 💾
</p>
