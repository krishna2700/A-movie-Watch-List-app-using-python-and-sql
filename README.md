# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite. This app allows users to manage their movie lists, track watched movies, and search through their collection.

## Features

- Add new movies with release dates
- View upcoming movies
- View all movies in the database
- Mark movies as watched by user
- View watched movies per user
- Add multiple users to the app
- Search for movies by title
- SQLite database for persistent storage

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

When you start the app, you'll see the following menu:

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - See all movies releasing in the future
3. **View all movies** - Display all movies in the database
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

## Database Structure

The app uses three main tables:

### Movies Table
- `id`: Primary key (auto-incrementing)
- `title`: Movie title
- `release_timestamp`: Unix timestamp of release date

### Users Table
- `username`: Primary key

### Watched Table
- `user_username`: Foreign key to users
- `movie_id`: Foreign key to movies

## Example Workflow

1. Start the app: `python app.py`
2. Add a user (option 6)
3. Add movies (option 1)
4. Mark movies as watched (option 4)
5. View your watched list (option 5)

## File Structure

```
.
├── app.py          # Main application with CLI menu
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## License

This project is open source and available under the MIT License.