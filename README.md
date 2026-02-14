# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite.

## Features

- Add new movies with release dates
- View all movies or only upcoming releases
- Track watched movies per user
- User management
- Search movies by title
- SQLite database for persistent storage

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

No additional dependencies required - uses Python standard library.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

1. Add new movie - Add a movie with title and release date
2. View upcoming movies - See movies releasing after today
3. View all movies - List all movies in the database
4. Add watched movie - Mark a movie as watched for a specific user
5. View watched movies - See all movies watched by a user
6. Add user to the app - Register a new user
7. Search for a movie - Find movies by partial title match
8. Exit - Close the application

## Database Schema

### Movies Table
- `id` (INTEGER PRIMARY KEY)
- `title` (TEXT)
- `release_timestamp` (REAL)

### Users Table
- `username` (TEXT PRIMARY KEY)

### Watched Table
- `user_username` (TEXT, FOREIGN KEY)
- `movie_id` (INTEGER, FOREIGN KEY)

## Project Structure

- `app.py` - Main application with user interface and menu logic
- `database.py` - Database operations and SQL queries
- `data.db` - SQLite database file (created on first run)

## Example Workflow

1. Start the app: `python app.py`
2. Add a user (option 6)
3. Add movies (option 1)
4. Mark movies as watched (option 4)
5. View your watched movies (option 5)

## Testing

This is a test README file created for demonstration purposes.