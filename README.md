# Movie Watchlist App

A Python-based command-line application for managing personal movie watchlists. This app allows users to add movies, track what they've watched, and search through their movie collection.

## Features

- Add new movies with release dates
- View upcoming movies
- View all movies in the database
- Mark movies as watched
- View watched movies by user
- Add users to the app
- Search for movies by title
- SQLite database for persistent storage

## Requirements

- Python 3.7+
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. No additional dependencies required - the app uses Python's built-in libraries.

## Usage

Run the application:
```bash
python app.py
```

The app will display a menu with the following options:

1. **Add new movie** - Enter a movie title and release date
2. **View upcoming movies** - See movies with future release dates
3. **View all movies** - Display all movies in the database
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Create a new user account
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

## Database Structure

The app uses three SQLite tables:

- **movies** - Stores movie information (id, title, release_timestamp)
- **users** - Stores user accounts (username)
- **watched** - Links users to movies they've watched (user_username, movie_id)

## File Structure

- `app.py` - Main application logic and user interface
- `database.py` - Database operations and schema definitions
- `data.db` - SQLite database file (created automatically)

## Example Workflow

1. Run the app with `python app.py`
2. Add a user (option 6)
3. Add some movies (option 1)
4. View all movies (option 3)
5. Mark movies as watched (option 4)
6. View your watched movies (option 5)

## Contributing

Feel free to submit issues and pull requests to improve the application.