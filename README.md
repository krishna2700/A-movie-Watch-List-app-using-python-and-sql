# Movie Watchlist Application

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- **Add Movies**: Add new movies with title and release date
- **View Movies**: Browse all movies or filter by upcoming releases
- **User Management**: Create user accounts to track personal watchlists
- **Watch Tracking**: Mark movies as watched for specific users
- **Search**: Search for movies by partial title match
- **Database**: Persistent storage using SQLite

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd vercel/sandbox
```

2. No additional dependencies required - uses Python standard library only

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

When you run the application, you'll see the following menu:

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

### Workflow Example

1. **Create a user** (Option 6):
   - Enter your username when prompted

2. **Add movies** (Option 1):
   - Enter movie title
   - Enter release date in format: `dd-mm-YYYY` (or press Enter for today's date)

3. **View upcoming movies** (Option 2):
   - See all movies with release dates in the future

4. **Mark a movie as watched** (Option 4):
   - Enter your username
   - Enter the movie ID (shown when viewing movies)

5. **View your watched movies** (Option 5):
   - Enter your username to see all movies you've watched

6. **Search for movies** (Option 7):
   - Enter partial movie title to find matching movies

## Database Structure

The application uses SQLite with three main tables:

### Movies Table
- `id`: Primary key (auto-increment)
- `title`: Movie title (text)
- `release_timestamp`: Release date (Unix timestamp)

### Users Table
- `username`: Primary key (text)

### Watched Table
- `user_username`: Foreign key to users table
- `movie_id`: Foreign key to movies table

An index is created on `release_timestamp` for optimized upcoming movie queries.

## File Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database (created on first run)
└── README.md       # This file
```

## Technical Details

- **Date Handling**: Dates are stored as Unix timestamps for easy comparison
- **Input Format**: Release dates use `dd-mm-YYYY` format (e.g., `25-12-2026`)
- **Display Format**: Dates are displayed in human-readable format (e.g., `Dec 25 2026`)
- **Database Connection**: Single persistent connection used throughout the application
- **Transaction Management**: All database operations use context managers for safety

## Example Usage

```
Welcome to the watchlist app!
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.

Your selection: 1
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010

Your selection: 3
-- All movies --
1: Inception (on Jul 16 2010)
---- 
```

## Notes

- The database file (`data.db`) is created automatically on first run
- All dates are compared using Unix timestamps for accuracy
- Users must be created before marking movies as watched
- Movie IDs are displayed when viewing movies and are needed for marking them as watched

## License

This project is open source and available for educational purposes.
