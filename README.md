# Movie Watchlist App

A command-line application for managing your movie watchlist. Track movies you want to watch, mark them as watched, and search through your collection.

## Features

- Add movies with release dates
- View upcoming movies
- View all movies in your watchlist
- Track multiple users
- Mark movies as watched per user
- Search movies by title
- SQLite database for persistent storage

## Requirements

- Python 3.8+
- SQLite3 (included with Python)

## Installation

1. Clone this repository
2. No additional dependencies required - uses Python standard library only

## Usage

Run the application:

```bash
python app.py
```

### Menu Options

1. **Add new movie** - Add a movie to your watchlist with a release date
2. **View upcoming movies** - See movies with future release dates
3. **View all movies** - Display your entire movie collection
4. **Add watched movie** - Mark a movie as watched for a specific user
5. **View watched movies** - See all movies watched by a user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

## Database Schema

The application uses three tables:

- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Stores registered usernames
- **watched**: Junction table linking users to movies they've watched

## Example Workflow

1. Add a user: Select option 6 and enter a username
2. Add movies: Select option 1 and enter movie details
3. Mark movies as watched: Select option 4, enter username and movie ID
4. View your watched movies: Select option 5 and enter your username

## Data Storage

All data is stored in `data.db` SQLite database file, which is created automatically on first run.
