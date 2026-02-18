# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- ✨ **Add Movies**: Add new movies with release dates to your watchlist
- 📅 **Track Upcoming Movies**: View movies that haven't been released yet
- 👀 **View All Movies**: Browse your entire movie collection
- ✅ **Mark as Watched**: Record when you've watched a movie
- 📊 **User Management**: Support for multiple users with individual watch histories
- 🔍 **Search Functionality**: Find movies by partial title match
- 💾 **SQLite Database**: Persistent storage with indexed queries for performance

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd movie-watchlist-app
```

2. No additional dependencies required! The app uses only Python standard library modules.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

When you start the app, you'll see the following menu:

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
```

### Workflow Example

1. **Create a user first**:
   - Select option `6`
   - Enter your username

2. **Add a movie**:
   - Select option `1`
   - Enter movie title
   - Enter release date in format `dd-mm-YYYY` (or press Enter for today's date)

3. **View upcoming movies**:
   - Select option `2`
   - See all movies with future release dates

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

The application uses SQLite with three main tables:

### Movies Table
```sql
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);
```

### Users Table
```sql
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);
```

### Watched Table
```sql
CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
```

### Indexes
- Release date index for optimized upcoming movies queries

## Project Structure

```
.
├── app.py           # Main application with CLI interface
├── database.py      # Database operations and SQL queries
├── data.db          # SQLite database file (created on first run)
└── README.md        # This file
```

## Key Functions

### app.py
- `prompt_add_movie()`: Add a new movie with release date
- `print_movie_list()`: Display formatted list of movies
- `prompt_watch_movie()`: Record a watched movie for a user
- `prompt_get_watched_movies()`: Retrieve user's watched movies
- `prompt_add_user()`: Create a new user
- `prompt_search_movies()`: Search for movies by title

### database.py
- `create_tables()`: Initialize database schema
- `add_movie()`: Insert new movie record
- `get_movies()`: Retrieve all or upcoming movies
- `add_user()`: Create new user
- `watch_movie()`: Record watched movie
- `get_watched_movies()`: Get watched movies for a user
- `search_movies()`: Search movies by partial title

## Date Format

The app uses `dd-mm-YYYY` format for date input (e.g., `25-12-2026` for December 25, 2026).

Internally, dates are stored as Unix timestamps for easy comparison and sorting.

## Example Session

```
Welcome to the watchlist app!
Please select one of the following options:
1) Add new movie.
...
Your selection: 6
Username: john

Your selection: 1
Movie title: Dune: Part Three
Release date (dd-mm-YYYY): 15-05-2026

Your selection: 2
-- Upcoming movies --
1: Dune: Part Three (on May 15 2026)
---- 

Your selection: 4
Username: john
Movie ID: 1

Your selection: 5
Username: john
-- Watched movies --
1: Dune: Part Three (on May 15 2026)
---- 

Your selection: 8
```

## Future Enhancements

Potential features to add:
- Movie ratings and reviews
- Categories/genres
- Export watchlist to CSV/JSON
- Movie recommendations
- Integration with movie APIs (TMDb, OMDb)
- Web interface
- Watchlist sharing between users

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Created as a learning project for Python and SQL database operations.
