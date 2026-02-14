# Movie Watch List App

A command-line movie watchlist application built with Python and SQLite. Track movies, manage users, and keep a record of what you've watched.

## Features

- **Add Movies** — Store movies with their release dates
- **View Upcoming Movies** — See movies with future release dates
- **View All Movies** — Browse the full movie catalog
- **Mark Movies as Watched** — Track which movies each user has seen
- **User Management** — Add users to the app
- **Search** — Find movies by partial title match

## Prerequisites

- Python 3.6+

No external dependencies are required. The app uses Python's built-in `sqlite3` module.

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/A-movie-Watch-List-app-using-python-and-sql.git
   cd A-movie-Watch-List-app-using-python-and-sql
   ```

2. **Run the application**

   ```bash
   python app.py
   ```

   The database file (`data.db`) is created automatically on first run.

## Usage

When you start the app you are presented with an interactive menu:

```
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
| **2** | List all movies whose release date is in the future. |
| **3** | List every movie in the database. |
| **4** | Mark a movie as watched by providing a username and movie ID. |
| **5** | View all movies a specific user has watched. |
| **6** | Register a new user by username. |
| **7** | Search for movies by a partial title match. |
| **8** | Exit the application. |

## Database Schema

The app creates three tables in `data.db`:

### `movies`

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER (PK) | Auto-incremented movie ID |
| `title` | TEXT | Movie title |
| `release_timestamp` | REAL | Release date stored as a Unix timestamp |

### `users`

| Column | Type | Description |
|--------|------|-------------|
| `username` | TEXT (PK) | Unique username |

### `watched`

| Column | Type | Description |
|--------|------|-------------|
| `user_username` | TEXT (FK → users) | Username of the viewer |
| `movie_id` | INTEGER (FK → movies) | ID of the watched movie |

An index (`movies_release_idx`) is created on `movies.release_timestamp` for efficient upcoming-movie queries.

## Project Structure

```
.
├── app.py          # CLI interface and menu logic
├── database.py     # SQLite database queries and connection
├── data.db         # SQLite database (auto-created)
└── README.md
```
