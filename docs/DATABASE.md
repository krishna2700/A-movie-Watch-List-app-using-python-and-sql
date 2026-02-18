# Database Documentation

This document describes the database module (`database.py`) and its functionality.

## Overview

The `database.py` module handles all database operations for the Movie Watch List application. It uses SQLite3 for data persistence and provides functions for managing movies, users, and watched movie records.

## Database Connection

The module establishes a connection to `data.db` SQLite database file:
```python
connection = sqlite3.connect("data.db")
```

## Functions

### `create_tables()`
Creates all necessary database tables if they don't exist:
- `movies` table
- `users` table
- `watched` table
- `movies_release_idx` index on release_timestamp

**Usage:**
```python
database.create_tables()
```

### `add_movie(title, release_timestamp)`
Adds a new movie to the database.

**Parameters:**
- `title` (str): Movie title
- `release_timestamp` (float): Release date as Unix timestamp

**Usage:**
```python
import datetime
release_date = datetime.datetime(1999, 3, 31)
database.add_movie("The Matrix", release_date.timestamp())
```

### `get_movies(upcoming=False)`
Retrieves movies from the database.

**Parameters:**
- `upcoming` (bool): If True, returns only movies with release dates in the future

**Returns:**
- List of tuples: `(id, title, release_timestamp)`

**Usage:**
```python
all_movies = database.get_movies()
upcoming_movies = database.get_movies(upcoming=True)
```

### `add_user(username)`
Adds a new user to the database.

**Parameters:**
- `username` (str): Unique username

**Usage:**
```python
database.add_user("john_doe")
```

### `watch_movie(username, movie_id)`
Records that a user has watched a movie.

**Parameters:**
- `username` (str): Username who watched the movie
- `movie_id` (int): ID of the movie watched

**Usage:**
```python
database.watch_movie("john_doe", 1)
```

### `get_watched_movies(username)`
Retrieves all movies watched by a specific user.

**Parameters:**
- `username` (str): Username to query

**Returns:**
- List of tuples: `(id, title, release_timestamp)`

**Usage:**
```python
watched = database.get_watched_movies("john_doe")
```

### `search_movies(search_term)`
Searches for movies by partial title match.

**Parameters:**
- `search_term` (str): Partial movie title to search for

**Returns:**
- List of tuples: `(id, title, release_timestamp)`

**Usage:**
```python
results = database.search_movies("Matrix")
```

## Database Schema

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

### Index
```sql
CREATE INDEX IF NOT EXISTS movies_release_idx ON movies (release_timestamp);
```

## Error Handling

The module uses context managers (`with connection:`) to ensure transactions are properly committed. However, it does not include explicit error handling for:
- Duplicate usernames
- Invalid movie IDs
- Database connection errors

Consider adding try-except blocks in production code.

## Performance Considerations

- An index is created on `release_timestamp` to optimize queries for upcoming movies
- All database operations use parameterized queries to prevent SQL injection
- Transactions are automatically committed using context managers
