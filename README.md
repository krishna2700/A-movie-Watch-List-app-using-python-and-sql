# Movie Watchlist App

A command-line application for managing your movie watchlist built with Python and SQLite.

## Features

- Add movies with release dates
- View upcoming and all movies
- Track watched movies per user
- Multi-user support
- Search movies by title
- SQLite database for persistent storage

## Requirements

- Python 3.8+
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - uses Python standard library

## Usage

Run the application:
```bash
python app.py
```

## Menu Options

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - Display movies with future release dates
3. **View all movies** - Display all movies in the database
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - Display movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Search movies by partial title match
8. **Exit** - Close the application

## Database Structure

The application uses SQLite with three tables:

### Movies Table
- `id` (INTEGER PRIMARY KEY)
- `title` (TEXT)
- `release_timestamp` (REAL)

### Users Table
- `username` (TEXT PRIMARY KEY)

### Watched Table
- `user_username` (TEXT, Foreign Key)
- `movie_id` (INTEGER, Foreign Key)

## File Structure

- `app.py` - Main application with CLI interface
- `database.py` - Database operations and SQL queries
- `data.db` - SQLite database file (created on first run)

## Example Workflow

1. Start the app and add a user
2. Add movies with their release dates
3. View upcoming movies to plan what to watch
4. Mark movies as watched
5. View your watch history
6. Search for specific movies

## Date Format

When adding movies, use the date format: `dd-mm-YYYY` (e.g., 25-12-2026)

If no date is provided, the current date is used.

## License

This project is open source and available for educational purposes.
