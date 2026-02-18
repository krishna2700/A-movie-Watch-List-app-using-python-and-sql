# Movie Watch List App

A Python-based movie watch list application using SQLite database to manage movies and track watched movies for users.

## Features

- Add new movies to the watchlist
- View upcoming movies
- View all movies
- Track watched movies per user
- Add users to the app
- Search for movies by title
- SQLite database for data persistence

## Requirements

- Python 3.x
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - uses only Python standard library.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - Display movies with release dates in the future
3. **View all movies** - Display all movies in the database
4. **Add watched movie** - Mark a movie as watched for a user
5. **View watched movies** - Display all movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Search movies by partial title match
8. **Exit** - Exit the application

## Project Structure

```
.
├── app.py          # Main application file with user interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created automatically)
└── README.md       # This file
```

## Database Schema

### Movies Table
- `id` (INTEGER PRIMARY KEY)
- `title` (TEXT)
- `release_timestamp` (REAL)

### Users Table
- `username` (TEXT PRIMARY KEY)

### Watched Table
- `user_username` (TEXT) - Foreign key to users
- `movie_id` (INTEGER) - Foreign key to movies

## Examples

### Adding a Movie
```
Movie title: The Matrix
Release date (dd-mm-YYYY): 31-03-1999
```

### Adding a User
```
Username: john_doe
```

### Marking a Movie as Watched
```
Username: john_doe
Movie ID: 1
```

## License

This project is open source and available for educational purposes.
