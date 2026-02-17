# 🎬 Movie Watchlist App

A command-line movie watchlist application built with **Python** and **SQLite**. Track movies, manage users, and keep a personal watched history — all from your terminal.

## Features

- **Add Movies** — Store movies with their release dates.
- **View Upcoming Movies** — See movies that haven't been released yet.
- **View All Movies** — Browse the full movie catalog.
- **Mark as Watched** — Log movies you've watched per user.
- **View Watched Movies** — Check a user's watched history.
- **User Management** — Register users to track individual watchlists.
- **Search** — Find movies by partial title match.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language  | Python 3   |
| Database  | SQLite 3   |
| Storage   | `data.db` (local file) |

## Project Structure

```
├── app.py          # Main application entry point & CLI menu
├── database.py     # Database connection, queries & helper functions
├── data.db         # SQLite database file (auto-created on first run)
└── README.md
```

## Prerequisites

- **Python 3.7+** — No external dependencies required. The app uses only Python standard library modules (`sqlite3`, `datetime`).

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Run the application

```bash
python app.py
```

## Usage

On launch, you'll see an interactive menu:

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

| Option | Action | Details |
|--------|--------|---------|
| **1** | Add new movie | Enter a title and release date (`dd-mm-YYYY`). Defaults to today if left blank. |
| **2** | View upcoming movies | Lists movies with a release date in the future. |
| **3** | View all movies | Lists every movie in the database. |
| **4** | Add watched movie | Assign a movie (by ID) to a user's watched list. |
| **5** | View watched movies | Display all movies a specific user has watched. |
| **6** | Add user | Register a new username. |
| **7** | Search for a movie | Search by partial title (case-insensitive). |
| **8** | Exit | Quit the application. |

### Example Workflow

```
# 1. Register a user
Your selection: 6
Username: alice

# 2. Add a movie
Your selection: 1
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010

# 3. View all movies to get the movie ID
Your selection: 3
-- All movies --
1: Inception (on Jul 16 2010)
----

# 4. Mark it as watched
Your selection: 4
Username: alice
Movie ID: 1

# 5. View watched movies
Your selection: 5
Username: alice
-- Watched movies --
1: Inception (on Jul 16 2010)
----
```

## Database Schema

The app uses three SQLite tables:

### `movies`
| Column              | Type    | Description              |
|---------------------|---------|--------------------------|
| `id`                | INTEGER | Primary key (auto-increment) |
| `title`             | TEXT    | Movie title              |
| `release_timestamp` | REAL    | Unix timestamp of release date |

### `users`
| Column     | Type | Description          |
|------------|------|----------------------|
| `username` | TEXT | Primary key          |

### `watched`
| Column          | Type    | Description                        |
|-----------------|---------|------------------------------------|
| `user_username` | TEXT    | Foreign key → `users.username`     |
| `movie_id`      | INTEGER | Foreign key → `movies.id`         |

An index (`movies_release_idx`) is created on `movies.release_timestamp` for efficient upcoming movie queries.

## License

This project is open source and available under the [MIT License](LICENSE).
