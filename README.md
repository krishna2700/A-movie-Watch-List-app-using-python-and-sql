# Movie Watchlist App

A command-line application built with Python and SQLite for managing your movie watchlist. Track movies you want to watch, mark them as watched, and search through your collection.

## Features

- Add new movies with release dates
- View upcoming movies (releases after today)
- View all movies in your watchlist
- Mark movies as watched
- View watched movies by user
- Multi-user support
- Search movies by partial title match
- SQLite database for persistent storage

## Requirements

- Python 3.x
- SQLite3 (included with Python standard library)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - the app uses Python standard library modules only.

## Usage

Run the application:
```bash
python3 app.py
```

### Menu Options

When you start the app, you'll see a menu with the following options:

1. **Add new movie** - Add a movie to your watchlist with title and release date
2. **View upcoming movies** - Display all movies with release dates in the future
3. **View all movies** - Display your complete movie collection
4. **Add watched movie** - Mark a movie as watched by a specific user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

### Example Workflow

1. First, add a user:
   - Select option 6
   - Enter a username

2. Add movies to your watchlist:
   - Select option 1
   - Enter movie title
   - Enter release date (format: dd-mm-YYYY) or press Enter for today's date

3. Mark a movie as watched:
   - Select option 4
   - Enter your username
   - Enter the movie ID (shown when viewing movies)

4. Search for movies:
   - Select option 7
   - Enter part of the movie title

## Database Structure

The application uses SQLite with three tables:

- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Stores registered usernames
- **watched**: Junction table linking users to movies they've watched

## Files

- `app.py` - Main application with user interface and menu logic
- `database.py` - Database operations and SQL queries
- `data.db` - SQLite database file (created automatically on first run)

## Features in Detail

### Date Handling
- Dates are stored as Unix timestamps for easy comparison
- Displayed in human-readable format (e.g., "Jan 15 2024")
- Default to today's date if not specified

### Search Functionality
- Case-insensitive partial matching
- Returns all movies containing the search term

### Multi-user Support
- Multiple users can track their own watched movies
- Shared movie database across all users

## License

This project is available for educational purposes.
