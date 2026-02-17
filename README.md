# 🎬 Movie Watch List App

A command-line movie watchlist application built with **Python** and **SQLite**.

Track movies you want to watch, mark them as watched, and search your collection — all from the terminal.

## Features

- **Add movies** with a title and release date
- **View upcoming movies** that haven't been released yet
- **View all movies** in the database
- **Mark movies as watched** per user
- **View watched movies** for a specific user
- **Multi-user support** — add users and track watched lists independently
- **Search movies** by partial title match
- **Persistent storage** using a local SQLite database (`data.db`)

## Requirements

- Python 3.7+

No external dependencies — uses only the Python standard library (`sqlite3`, `datetime`).

## Project Structure

```
├── app.py          # CLI menu and user interaction logic
├── database.py     # SQLite database connection, schema, and queries
├── data.db         # SQLite database file (created automatically on first run)
└── README.md
```

## Getting Started

### Run the app

```bash
python app.py
```

### Menu Options

```
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Add watched movie.
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
```

## Usage Examples

**Add a movie:**

```
Your selection: 1
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010
```

> Leave the release date blank to default to today's date.

**Add a user:**

```
Your selection: 6
Username: alice
```

**Mark a movie as watched:**

```
Your selection: 4
Username: alice
Movie ID: 1
```

**Search for a movie:**

```
Your selection: 7
Enter partial movie title: incep
```

## Database Schema

| Table     | Columns                                          | Description                        |
|-----------|--------------------------------------------------|------------------------------------|
| `movies`  | `id` (PK), `title`, `release_timestamp`          | Stores all movies                  |
| `users`   | `username` (PK)                                  | Stores registered users            |
| `watched` | `user_username` (FK), `movie_id` (FK)            | Tracks which user watched which movie |

An index on `movies.release_timestamp` is created for efficient upcoming-movie queries.

## License

This project is open source and available for personal and educational use.
