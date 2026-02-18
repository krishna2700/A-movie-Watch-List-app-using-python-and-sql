# Movie Watchlist App

A command-line application for managing your movie watchlist using Python and SQLite.

## Features

- **Add Movies**: Add movies with titles and release dates to your watchlist
- **View Movies**: View all movies or filter by upcoming releases
- **User Management**: Create user accounts to track individual viewing habits
- **Watch Tracking**: Mark movies as watched and associate them with users
- **Search Functionality**: Search for movies by partial title matching
- **Database Persistence**: All data is stored in an SQLite database

## Requirements

- Python 3.8+
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - uses Python standard library only!

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - Display movies with future release dates
3. **View all movies** - Display complete movie list
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - Show all movies watched by a specific user
6. **Add user to the app** - Create a new user account
7. **Search for a movie** - Find movies by partial title
8. **Exit** - Close the application

## Database Schema

### Movies Table
- `id` (INTEGER PRIMARY KEY): Unique movie identifier
- `title` (TEXT): Movie title
- `release_timestamp` (REAL): Unix timestamp of release date

### Users Table
- `username` (TEXT PRIMARY KEY): Unique username

### Watched Table
- `user_username` (TEXT): Foreign key to users
- `movie_id` (INTEGER): Foreign key to movies

## Project Structure

```
.
├── app.py           # Main application with CLI interface
├── database.py      # Database operations and SQL queries
├── data.db          # SQLite database file (created on first run)
└── README.md        # This file
```

## Example Workflow

1. Start the app: `python app.py`
2. Add a user: Select option `6`, enter username
3. Add a movie: Select option `1`, enter title and date (format: dd-mm-YYYY)
4. Mark as watched: Select option `4`, enter username and movie ID
5. View watched movies: Select option `5`, enter username

## Date Format

When adding movies, use the format: `dd-mm-YYYY` (e.g., `25-12-2026`)

If no date is provided, the current date will be used.

## Database File

The application creates a SQLite database file named `data.db` in the project directory. This file persists all your data between sessions.

## Features in Detail

### Upcoming Movies
Movies are considered "upcoming" if their release date is in the future. The app automatically filters based on the current date.

### Search
Search is case-insensitive and matches partial titles. For example, searching "matrix" will find "The Matrix", "Matrix Reloaded", etc.

### Index Optimization
The database includes an index on the release timestamp for faster querying of upcoming movies.

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.
