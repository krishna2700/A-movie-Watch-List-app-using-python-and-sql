# Movie Watchlist App

A command-line application built with Python and SQLite for managing your movie watchlist. Track movies you want to watch, mark them as watched, and search through your collection.

## Features

- **Add Movies**: Add new movies to your watchlist with release dates
- **View Movies**: See all movies or filter by upcoming releases
- **Track Watched Movies**: Mark movies as watched and view your watch history
- **User Management**: Support for multiple users with individual watchlists
- **Search Functionality**: Search for movies by partial title match
- **Database Indexing**: Optimized queries with indexed release dates

## Project Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## Database Schema

### Tables

**movies**
- `id` (INTEGER PRIMARY KEY): Unique movie identifier
- `title` (TEXT): Movie title
- `release_timestamp` (REAL): Release date as Unix timestamp

**users**
- `username` (TEXT PRIMARY KEY): Unique username

**watched**
- `user_username` (TEXT): Foreign key to users table
- `movie_id` (INTEGER): Foreign key to movies table

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/krishna2700/A-movie-Watch-List-app-using-python-and-sql.git
cd A-movie-Watch-List-app-using-python-and-sql
```

2. No additional dependencies required - uses Python standard library only!

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

1. **Add new movie**: Add a movie with title and release date (format: dd-mm-YYYY)
2. **View upcoming movies**: Display movies with future release dates
3. **View all movies**: Display complete movie list
4. **Add watched movie**: Mark a movie as watched for a specific user
5. **View watched movies**: See all movies watched by a user
6. **Add user to the app**: Register a new user
7. **Search for a movie**: Find movies by partial title match
8. **Exit**: Close the application

### Example Workflow

```
Welcome to the watchlist app!
Please select one of the following options:
1) Add new movie.
...
Your selection: 6
Username: john

Your selection: 1
Movie title: The Matrix
Release date (dd-mm-YYYY): 31-03-1999

Your selection: 3
-- All movies --
1: The Matrix (on Mar 31 1999)
----

Your selection: 4
Username: john
Movie ID: 1

Your selection: 5
Username: john
-- Watched movies --
1: The Matrix (on Mar 31 1999)
----
```

## Features in Detail

### Date Handling
- Dates are stored as Unix timestamps for efficient querying
- Input format: dd-mm-YYYY
- Display format: Mon DD YYYY (e.g., Mar 31 1999)
- If no date is provided, defaults to current date

### Search
- Case-insensitive partial matching
- Searches within movie titles
- Returns all matching results

### Database Optimization
- Index on `release_timestamp` for faster upcoming movie queries
- Foreign key constraints ensure data integrity
- Automatic table creation on first run

## Technical Details

### Database Connection
- Uses SQLite3 with a persistent connection
- Database file: `data.db`
- Automatic table and index creation

### Error Handling
- Invalid menu selections are caught and reported
- Database operations use context managers for safe transactions

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project to demonstrate Python and SQL integration.
