# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- Add new movies with release dates
- View upcoming movies (movies with future release dates)
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

When you start the app, you'll see the following menu:

```
1) Add new movie
2) View upcoming movies
3) View all movies
4) Add watched movie
5) View watched movies
6) Add user to the app
7) Search for a movie
8) Exit
```

### Adding a Movie

1. Select option `1`
2. Enter the movie title
3. Enter the release date in `dd-mm-YYYY` format (or press Enter to use today's date)

### Adding a User

1. Select option `6`
2. Enter a username

### Marking a Movie as Watched

1. Select option `4`
2. Enter the username
3. Enter the movie ID (you can find this by viewing all movies)

### Viewing Watched Movies

1. Select option `5`
2. Enter the username to see all movies that user has watched

### Searching for Movies

1. Select option `7`
2. Enter a partial movie title (case-insensitive search)

## Database Structure

The application uses SQLite with three tables:

### movies
- `id` (INTEGER PRIMARY KEY): Unique movie identifier
- `title` (TEXT): Movie title
- `release_timestamp` (REAL): Release date as Unix timestamp

### users
- `username` (TEXT PRIMARY KEY): Unique username

### watched
- `user_username` (TEXT): Foreign key to users table
- `movie_id` (INTEGER): Foreign key to movies table

An index is created on `release_timestamp` for optimized queries on upcoming movies.

## Project Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## Example Workflow

1. Start the app: `python app.py`
2. Add a user: Select `6`, enter "John"
3. Add a movie: Select `1`, enter "Inception", enter "16-07-2010"
4. Mark as watched: Select `4`, enter "John", enter movie ID
5. View watched movies: Select `5`, enter "John"

## License

This project is open source and available for educational purposes.
