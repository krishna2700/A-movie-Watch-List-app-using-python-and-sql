# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to manage their movie collections, track what they've watched, and discover upcoming releases.

## Features

- **Add Movies**: Add new movies to your watchlist with title and release date
- **View Movies**: Browse all movies or filter by upcoming releases
- **Track Watched Movies**: Mark movies as watched and view your watch history
- **User Management**: Support for multiple users with individual watchlists
- **Search**: Search for movies by partial title matching
- **Database Storage**: Persistent storage using SQLite with indexed queries for performance

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies are required - the app uses Python standard library only.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

When you start the app, you'll see a menu with the following options:

1. **Add new movie** - Add a movie with title and release date (format: dd-mm-YYYY)
2. **View upcoming movies** - See all movies with future release dates
3. **View all movies** - Display complete movie list
4. **Add watched movie** - Mark a movie as watched by a specific user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

### Example Workflow

```
1. Add a user: Select option 6, enter username
2. Add movies: Select option 1, enter movie details
3. Mark as watched: Select option 4, enter username and movie ID
4. View history: Select option 5, enter username to see watched movies
```

## Database Schema

The application uses three main tables:

- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Stores registered usernames
- **watched**: Junction table linking users to watched movies

## Project Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (auto-generated)
└── README.md       # This file
```

## License

This project is open source and available for educational purposes.
