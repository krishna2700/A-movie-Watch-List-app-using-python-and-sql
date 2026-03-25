# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- Add new movies with release dates
- View upcoming movies (releases after today)
- View all movies in the database
- User management system
- Track watched movies per user
- Search movies by partial title match
- SQLite database with indexed queries for performance

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - the app uses Python's standard library.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

The application provides an interactive menu with the following options:

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - Shows movies with release dates in the future
3. **View all movies** - Displays all movies in the database
4. **Add watched movie** - Mark a movie as watched by a specific user
5. **View watched movies** - See all movies a user has watched
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

### Example Workflow

1. Start the app: `python app.py`
2. Add a user (option 6)
3. Add movies to the watchlist (option 1)
4. View upcoming movies (option 2)
5. Mark movies as watched (option 4)
6. View your watched movies (option 5)

## Database Schema

The application uses three tables:

### movies
- `id` (INTEGER PRIMARY KEY)
- `title` (TEXT)
- `release_timestamp` (REAL)

### users
- `username` (TEXT PRIMARY KEY)

### watched
- `user_username` (TEXT, Foreign Key to users)
- `movie_id` (INTEGER, Foreign Key to movies)

## Project Structure

```
.
├── app.py           # Main application with CLI interface
├── database.py      # Database operations and SQL queries
├── data.db          # SQLite database file (auto-created)
└── README.md        # This file
```

## Technical Details

- Date format for input: `dd-mm-YYYY` (e.g., 25-12-2024)
- Dates are stored as Unix timestamps for efficient querying
- Database includes an index on `release_timestamp` for optimized upcoming movie queries
- Uses Python's walrus operator (`:=`) for clean input handling

## License

This project is open source and available for educational purposes.