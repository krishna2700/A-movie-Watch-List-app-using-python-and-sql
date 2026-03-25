# Movie Watchlist App (Python + SQLite)

Simple command-line app to manage movies, users, and watched history using SQLite.

## Features

- Add movies with optional release dates
- View all or upcoming movies
- Track watched movies per user
- Search movies by partial title

## Project Structure

- `app.py`: CLI entrypoint and menu handling
- `database.py`: SQLite data access helpers
- `data.db`: SQLite database file (created/updated at runtime)

## Requirements

- Python 3.10+

## Run

```bash
python app.py
```

Follow the on-screen menu to add users, add movies, and mark movies as watched.

## Notes

- Dates are entered as `dd-mm-YYYY`. If blank, today’s date is used.
- The database is stored locally in `data.db`.
