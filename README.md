# Movie Watch List App

A command-line movie watchlist application built with **Python** and **SQLite**. Track movies, manage users, and keep a record of what you've watched.

## Features

- **Add movies** with title and release date
- **View upcoming movies** that haven't been released yet
- **View all movies** in the database
- **Mark movies as watched** per user
- **View watched movies** for a specific user
- **User management** — add users to the app
- **Search movies** by partial title match

## Project Structure

```
├── app.py          # Main application entry point (CLI menu)
├── database.py     # SQLite database layer (queries, connection)
├── data.db         # SQLite database file
└── README.md
```

## Prerequisites

- Python 3.7+

No external dependencies are required — the app uses only the Python standard library (`sqlite3`, `datetime`).

## Getting Started

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Run the application**

   ```bash
   python app.py
   ```

   The database tables are created automatically on first run.

## Usage

When you start the app you will see an interactive menu:

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
```

| Option | Description |
|--------|-------------|
| **1** | Add a movie by entering its title and release date (`dd-mm-YYYY`). If no date is provided, today's date is used. |
| **2** | List all movies with a release date in the future. |
| **3** | List every movie in the database. |
| **4** | Mark a movie as watched by providing a username and movie ID. |
| **5** | View all movies a specific user has watched. |
| **6** | Register a new user by username. |
| **7** | Search for movies by a partial title match. |
| **8** | Exit the application. |

## Database Schema

The app uses three SQLite tables:

**movies**

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER (PK) | Auto-incremented movie ID |
| `title` | TEXT | Movie title |
| `release_timestamp` | REAL | Unix timestamp of the release date |

**users**

| Column | Type | Description |
|--------|------|-------------|
| `username` | TEXT (PK) | Unique username |

**watched**

| Column | Type | Description |
|--------|------|-------------|
| `user_username` | TEXT (FK → users) | Username reference |
| `movie_id` | INTEGER (FK → movies) | Movie ID reference |

## License

This project is provided as-is for educational purposes.
