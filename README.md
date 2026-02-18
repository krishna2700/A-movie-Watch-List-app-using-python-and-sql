# Movie Watchlist App (Python + SQLite)

Simple command-line watchlist app that stores movies, users, and watched history
in a local SQLite database. The app lets you add upcoming releases, mark movies
as watched, and search by title.

## Features

- Add movies with release dates
- List all or upcoming movies
- Create users and mark movies as watched
- View watched movies per user
- Search by partial title

## Requirements

- Python 3.10+

## Getting Started

1. Run the app:

   ```bash
   python app.py
   ```

2. Follow the menu prompts to add movies, users, and watched history.

The app creates `data.db` automatically in the project root.

## Project Structure

- `app.py`: CLI flow and user prompts
- `database.py`: SQLite queries and helpers
- `data.db`: Local SQLite database (auto-generated)

## Notes

- Release dates use the format `dd-mm-YYYY`.
- Upcoming movies are determined relative to today.
