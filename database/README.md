# Database Module Documentation

## Overview

The `database.py` module handles all database operations for the Movie Watch List application. It provides a clean interface for interacting with the SQLite database.

## File Location

`/database.py`

## Database Schema

### Tables

#### 1. Movies Table
```sql
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);
```

**Fields:**
- `id`: Auto-incrementing primary key
- `title`: Movie title (TEXT)
- `release_timestamp`: Unix timestamp of release date (REAL)

#### 2. Users Table
```sql
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);
```

**Fields:**
- `username`: Unique username (TEXT, PRIMARY KEY)

#### 3. Watched Table
```sql
CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
```

**Fields:**
- `user_username`: Foreign key to users table
- `movie_id`: Foreign key to movies table

### Indexes

- `movies_release_idx`: Index on `release_timestamp` for faster upcoming movie queries

## Functions

### `create_tables()`
Creates all necessary tables and indexes if they don't exist.

**Usage:**
```python
database.create_tables()
```

**Note:** Should be called once at application startup.

---

### `add_movie(title, release_timestamp)`
Adds a new movie to the database.

**Parameters:**
- `title` (str): Movie title
- `release_timestamp` (float): Unix timestamp of release date

**Usage:**
```python
import datetime
release_date = datetime.datetime(2024, 12, 25)
database.add_movie("New Movie", release_date.timestamp())
```

---

### `get_movies(upcoming=False)`
Retrieves movies from the database.

**Parameters:**
- `upcoming` (bool, optional): If True, returns only upcoming movies. Default: False

**Returns:**
- List of tuples: `[(id, title, release_timestamp), ...]`

**Usage:**
```python
# Get all movies
all_movies = database.get_movies()

# Get upcoming movies only
upcoming_movies = database.get_movies(upcoming=True)
```

---

### `add_user(username)`
Adds a new user to the database.

**Parameters:**
- `username` (str): Unique username

**Usage:**
```python
database.add_user("john_doe")
```

**Note:** Username must be unique (PRIMARY KEY constraint).

---

### `watch_movie(username, movie_id)`
Marks a movie as watched by a specific user.

**Parameters:**
- `username` (str): Username who watched the movie
- `movie_id` (int): ID of the movie watched

**Usage:**
```python
database.watch_movie("john_doe", 1)
```

---

### `get_watched_movies(username)`
Retrieves all movies watched by a specific user.

**Parameters:**
- `username` (str): Username to query

**Returns:**
- List of tuples: `[(id, title, release_timestamp), ...]` or empty list if no movies found

**Usage:**
```python
watched = database.get_watched_movies("john_doe")
```

---

### `search_movies(search_term)`
Searches for movies by partial title match.

**Parameters:**
- `search_term` (str): Partial movie title to search for

**Returns:**
- List of tuples: `[(id, title, release_timestamp), ...]` matching the search term

**Usage:**
```python
results = database.search_movies("inception")
# Returns movies with "inception" in the title (case-sensitive)
```

**Note:** Uses SQL LIKE operator with wildcards (`%search_term%`).

## Database Connection

The module uses a global SQLite connection:
```python
connection = sqlite3.connect("data.db")
```

The database file `data.db` is created automatically in the project root directory.

## Error Handling

The module uses context managers (`with connection:`) to ensure proper transaction handling. All database operations are wrapped in transactions for data integrity.

## Dependencies

- `sqlite3`: Python standard library for SQLite database operations
- `datetime`: Used for timestamp operations (imported but not directly used in this module)

## Best Practices

1. Always call `create_tables()` before using other functions
2. Handle duplicate username errors when adding users
3. Ensure movie_id exists before marking as watched
4. Use proper date formatting when converting timestamps
