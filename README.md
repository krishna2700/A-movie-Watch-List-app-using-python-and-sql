# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- **Add Movies**: Add new movies to your watchlist with title and release date
- **View Movies**: Browse all movies or filter by upcoming releases
- **Track Watched Movies**: Mark movies as watched and associate them with users
- **User Management**: Create and manage multiple users
- **Search Functionality**: Search for movies by partial title matching
- **SQLite Database**: Persistent storage with optimized indexing

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - the app uses Python standard library only!

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

When you run the app, you'll see the following menu:

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

### Example Workflow

1. **Create a user**:
   - Select option `6`
   - Enter a username

2. **Add a movie**:
   - Select option `1`
   - Enter movie title
   - Enter release date in format `dd-mm-YYYY` (or press Enter for today's date)

3. **View upcoming movies**:
   - Select option `2`
   - See all movies with release dates in the future

4. **Mark a movie as watched**:
   - Select option `4`
   - Enter your username
   - Enter the movie ID (shown when viewing movies)

5. **View your watched movies**:
   - Select option `5`
   - Enter your username
   - See all movies you've marked as watched

6. **Search for movies**:
   - Select option `7`
   - Enter partial movie title
   - See matching results

## Database Schema

The application uses three main tables:

### Movies Table
- `id`: INTEGER PRIMARY KEY
- `title`: TEXT
- `release_timestamp`: REAL

### Users Table
- `username`: TEXT PRIMARY KEY

### Watched Table
- `user_username`: TEXT (Foreign Key to users)
- `movie_id`: INTEGER (Foreign Key to movies)

## File Structure

```
.
├── app.py          # Main application logic and user interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## Database Features

- Automatic table creation on first run
- Indexed release timestamps for optimized queries
- Foreign key constraints for data integrity
- Support for multiple users tracking the same movies

## Date Format

All dates should be entered in `dd-mm-YYYY` format (e.g., `25-12-2024` for December 25, 2024).

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.
