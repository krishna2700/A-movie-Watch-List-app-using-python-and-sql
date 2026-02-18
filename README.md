# Movie Watchlist App

A command-line Python application for managing your movie watchlist, powered by SQLite.

## Features

- **Add Movies** — Add new movies with a title and release date.
- **View Upcoming Movies** — See movies that haven't been released yet.
- **View All Movies** — Browse your full movie catalog.
- **Mark as Watched** — Track which movies each user has watched.
- **User Management** — Add users to the app.
- **Search** — Search for movies by partial title.

## Requirements

- Python 3.7+
- SQLite (bundled with Python)

## Usage

```bash
python app.py
```

You will be presented with an interactive menu:

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

## Project Structure

```
├── app.py         # CLI interface and menu logic
├── database.py    # SQLite database operations
└── data.db        # SQLite database file (auto-created)
```

## Database Schema

| Table     | Description                          |
|-----------|--------------------------------------|
| `movies`  | Stores movie titles and release dates |
| `users`   | Stores usernames                     |
| `watched` | Tracks which user watched which movie |
