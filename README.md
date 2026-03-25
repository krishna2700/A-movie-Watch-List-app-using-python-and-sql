# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- Add new movies with release dates
- View upcoming movies (releases after today)
- View all movies in the database
- Create user accounts
- Mark movies as watched by specific users
- View watched movies per user
- Search for movies by partial title match

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies are required as the app uses only Python standard library modules.

## Usage

Run the application:

```bash
python app.py
```

### Menu Options

When you run the app, you'll see the following menu:

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - See all movies with future release dates
3. **View all movies** - Display the complete movie list
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Create a new user account
7. **Search for a movie** - Find movies by partial title search
8. **Exit** - Close the application

## Database Schema

The application uses three tables:

### Movies Table
- `id` (INTEGER PRIMARY KEY)
- `title` (TEXT)
- `release_timestamp` (REAL)

### Users Table
- `username` (TEXT PRIMARY KEY)

### Watched Table
- `user_username` (TEXT, Foreign Key to users)
- `movie_id` (INTEGER, Foreign Key to movies)

## File Structure

- `app.py` - Main application with user interface and menu logic
- `database.py` - Database operations and SQL queries
- `data.db` - SQLite database file (created automatically)

## Example Workflow

1. Start the app and add a user
2. Add movies to your watchlist
3. View upcoming movies to see what's releasing soon
4. Mark movies as watched after viewing them
5. Search for specific movies in your collection

## License

This project is open source and available for educational purposes.
