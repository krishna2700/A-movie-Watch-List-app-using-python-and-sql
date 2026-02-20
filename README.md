# Movie Watchlist App

A simple command-line movie watchlist application built with Python and SQLite.

## Overview

This application allows users to manage their movie watchlist with features to add movies, track release dates, mark movies as watched, and search through the collection.

## Features

- **Add Movies**: Add new movies with titles and release dates
- **View Movies**: Browse all movies or filter by upcoming releases
- **Track Watched Movies**: Mark movies as watched and view your watch history
- **User Management**: Create and manage multiple user accounts
- **Search**: Find movies by partial title match
- **Release Date Tracking**: Automatically track upcoming vs past releases

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - the app uses Python standard library only.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

The application presents an interactive menu with the following options:

1. **Add new movie** - Enter a movie title and release date
2. **View upcoming movies** - Display movies with future release dates
3. **View all movies** - Show complete movie list
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Create a new user account
7. **Search for a movie** - Find movies by partial title
8. **Exit** - Close the application

## Database Structure

The application uses SQLite with three main tables:

- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Manages user accounts (username)
- **watched**: Tracks which users have watched which movies

## File Structure

- `app.py` - Main application with user interface and menu system
- `database.py` - Database operations and SQL queries
- `data.db` - SQLite database file (created automatically)

## Example Workflow

1. Start the app and create a user (option 6)
2. Add movies to your watchlist (option 1)
3. View upcoming releases (option 2)
4. Mark movies as watched (option 4)
5. Check your watch history (option 5)

## Notes

- Release dates use dd-mm-YYYY format
- If no date is provided when adding a movie, today's date is used
- The database is created automatically on first run
- All data persists between sessions in `data.db`
