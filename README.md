# Movie Watch List App

A command-line movie watchlist application built with Python and SQLite.

## Features

- **Add Movies** — Add new movies with a title and release date.
- **View Upcoming Movies** — See movies with a future release date.
- **View All Movies** — Browse every movie in the database.
- **Mark Movies as Watched** — Track which movies a user has watched.
- **View Watched Movies** — See all movies a specific user has watched.
- **User Management** — Add users to the app.
- **Search** — Search for movies by partial title.

## Requirements

- Python 3.7+

No external dependencies are needed — the app uses Python's built-in `sqlite3` and `datetime` modules.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the app:**

   ```bash
   python app.py
   ```

   The SQLite database (`data.db`) is created automatically on first run.

## Usage

When you start the app you'll see an interactive menu:

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

| Option | Description |
|--------|-------------|
| **1** | Add a new movie with a title and release date (defaults to today). |
| **2** | List movies whose release date is in the future. |
| **3** | List every movie in the database. |
| **4** | Mark a movie as watched by a user (requires username and movie ID). |
| **5** | View all movies a specific user has watched. |
| **6** | Register a new user. |
| **7** | Search movies by a partial title match. |
| **8** | Exit the application. |

### Example

```
Your selection: 1
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010

Your selection: 6
Username: alice

Your selection: 4
Username: alice
Movie ID: 1

Your selection: 5
Username: alice
-- Watched movies --
1: Inception (on Jul 16 2010)
----
```

## Project Structure

```
├── app.py          # CLI interface and menu logic
├── database.py     # SQLite database setup, queries, and helper functions
├── data.db         # SQLite database file (auto-generated)
└── README.md
```

## Database Schema

The app creates three tables:

- **movies** (`id`, `title`, `release_timestamp`) — Stores movie information.
- **users** (`username`) — Stores registered usernames.
- **watched** (`user_username`, `movie_id`) — Links users to the movies they've watched.

An index on `release_timestamp` is created for efficient upcoming-movie queries.

## License

This project is open source and available under the [MIT License](LICENSE).
