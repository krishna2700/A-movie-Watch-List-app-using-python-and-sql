# Movie Watch List App

A command-line movie watchlist application built with Python and SQLite. Track movies, manage users, and keep a record of what you've watched.

## Features

- **Add Movies** — Add movies with a title and release date.
- **View Upcoming Movies** — See movies with a future release date.
- **View All Movies** — Browse every movie in the database.
- **Mark Movies as Watched** — Associate watched movies with a user.
- **View Watched Movies** — See all movies a specific user has watched.
- **User Management** — Add users to the app.
- **Search Movies** — Search for movies by partial title match.

## Requirements

- Python 3.7+

No external dependencies are required. The app uses only the Python standard library (`sqlite3`, `datetime`).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/A-movie-Watch-List-app-using-python-and-sql.git
   cd A-movie-Watch-List-app-using-python-and-sql
   ```

2. Run the application:

   ```bash
   python app.py
   ```

   The SQLite database (`data.db`) is created automatically on first run.

## Usage

When you start the app you will see an interactive menu:

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

### Menu Options

| Option | Description |
|--------|-------------|
| **1** | Add a new movie by entering a title and release date (`dd-mm-YYYY`). If no date is provided, today's date is used. |
| **2** | Display all movies with a release date in the future. |
| **3** | Display every movie stored in the database. |
| **4** | Mark a movie as watched by providing a username and movie ID. |
| **5** | View all movies a specific user has watched. |
| **6** | Register a new user by entering a username. |
| **7** | Search for movies by entering a partial title. |
| **8** | Exit the application. |

## Database Schema

The app uses an SQLite database (`data.db`) with three tables:

### `movies`

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER (PK) | Auto-incrementing movie ID |
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
├── app.py          # CLI entry point and menu logic
├── database.py     # Database connection, queries, and helper functions
├── data.db         # SQLite database (auto-created on first run)
└── README.md       # Project documentation
```

## License

This project is provided as-is for educational purposes.
