# Database Schema Documentation

## Overview

The Movie Watchlist App uses SQLite3 as its database engine. The schema consists of three main tables with foreign key relationships to maintain data integrity.

## Tables

### movies

Stores information about movies in the watchlist.

```sql
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);
```

**Columns:**
- `id` (INTEGER PRIMARY KEY): Auto-incrementing unique identifier for each movie
- `title` (TEXT): The title of the movie
- `release_timestamp` (REAL): Unix timestamp representing the movie's release date

**Indexes:**
- `movies_release_idx`: Index on `release_timestamp` for optimized date-based queries

### users

Stores user accounts for the application.

```sql
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);
```

**Columns:**
- `username` (TEXT PRIMARY KEY): Unique username identifier

### watched

Junction table that tracks which users have watched which movies.

```sql
CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
```

**Columns:**
- `user_username` (TEXT): References `users.username`
- `movie_id` (INTEGER): References `movies.id`

**Foreign Keys:**
- `user_username` → `users(username)`
- `movie_id` → `movies(id)`

## Entity Relationship Diagram

```
┌─────────────────┐
│     users       │
├─────────────────┤
│ username (PK)   │
└────────┬────────┘
         │
         │ 1:N
         │
┌────────▼────────┐
│    watched      │
├─────────────────┤
│ user_username   │◄─────┐
│ movie_id        │      │
└────────┬────────┘      │
         │               │ N:1
         │ N:1           │
         │               │
┌────────▼────────┐      │
│     movies      │──────┘
├─────────────────┤
│ id (PK)         │
│ title           │
│ release_timestamp│
└─────────────────┘
```

## Query Operations

### Prepared Statements

The application uses parameterized queries to prevent SQL injection:

1. **INSERT_MOVIE**: Add a new movie
   ```sql
   INSERT INTO movies (title, release_timestamp) VALUES (?, ?)
   ```

2. **SELECT_ALL_MOVIES**: Retrieve all movies
   ```sql
   SELECT * FROM movies;
   ```

3. **SELECT_UPCOMING_MOVIES**: Get movies releasing after a specific date
   ```sql
   SELECT * FROM movies WHERE release_timestamp > ?;
   ```

4. **INSERT_USER**: Add a new user
   ```sql
   INSERT INTO users (username) VALUES (?)
   ```

5. **INSERT_WATCHED_MOVIE**: Mark a movie as watched by a user
   ```sql
   INSERT INTO watched (user_username, movie_id) VALUES (?, ?)
   ```

6. **SELECT_WATCHED_MOVIES**: Get all movies watched by a specific user
   ```sql
   SELECT movies.*
   FROM users
   JOIN watched ON users.username = watched.user_username
   JOIN movies ON watched.movie_id = movies.id
   WHERE users.username = ?;
   ```

7. **SEARCH_MOVIE**: Search movies by partial title match
   ```sql
   SELECT * FROM movies WHERE title LIKE ?;
   ```

## Performance Optimizations

### Indexes

The application creates an index on the `release_timestamp` column to optimize queries that filter by date:

```sql
CREATE INDEX IF NOT EXISTS movies_release_idx ON movies (release_timestamp);
```

This improves performance when:
- Retrieving upcoming movies
- Filtering movies by release date
- Sorting movies chronologically

## Database File

- **Filename**: `data.db`
- **Location**: Root directory of the application
- **Creation**: Automatically created on first run via `create_tables()` function

## Connection Management

The application maintains a single connection to the database:

```python
connection = sqlite3.connect("data.db")
```

All database operations use context managers (`with connection:`) to ensure:
- Automatic transaction commits on success
- Automatic rollbacks on errors
- Proper resource cleanup

## Data Integrity

### Foreign Key Constraints

Foreign keys ensure:
- A watched movie must reference an existing movie ID
- A watched entry must reference an existing username
- Referential integrity between tables

### Primary Keys

- `movies.id`: Auto-incrementing integer ensures unique movie identifiers
- `users.username`: Text-based primary key prevents duplicate usernames

## Timestamp Format

Movie release dates are stored as Unix timestamps (REAL type):
- **Storage**: Floating-point number representing seconds since epoch (1970-01-01)
- **Input Format**: `dd-mm-YYYY` (converted to timestamp)
- **Display Format**: `Mon DD YYYY` (e.g., "Jan 15 2025")

**Conversion Example:**
```python
# Input: "15-01-2025"
release_timestamp = datetime.datetime.strptime("15-01-2025", "%d-%m-%Y").timestamp()
# Stored: 1736899200.0

# Display
movie_date = datetime.datetime.fromtimestamp(1736899200.0)
human_date = movie_date.strftime("%b %d %Y")
# Output: "Jan 15 2025"
```

## Schema Initialization

The `create_tables()` function in `database.py` initializes the schema:

```python
def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
```

This function:
- Creates tables if they don't exist (idempotent)
- Sets up foreign key relationships
- Creates performance indexes
- Is called automatically on application startup
