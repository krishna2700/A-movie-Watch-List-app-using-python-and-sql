# Movie Watchlist App

Command-line watchlist app built with Python and SQLite. Track upcoming releases, mark movies as watched, and search your list.

## Features

- Add movies with release dates
- View upcoming or all movies
- Track watched movies per user
- Search by partial title

## Requirements

- Python 3.10+

## Getting Started

Run the app from the project root:

```bash
python app.py
```

Follow the on-screen menu to add users and manage your watchlist. The app stores data in `data.db` in the project root.

## Project Structure

- `app.py` - CLI interface and menu
- `database.py` - SQLite data access layer
- `data.db` - SQLite database file
