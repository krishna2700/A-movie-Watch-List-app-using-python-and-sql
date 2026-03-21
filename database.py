import datetime
import sqlite3
from contextlib import contextmanager

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM users
JOIN watched ON users.username = watched.user_username
JOIN movies ON watched.movie_id = movies.id
WHERE users.username = ?;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""
CREATE_RELEASE_INDEX = """CREATE INDEX IF NOT EXISTS movies_release_idx ON movies (release_timestamp);"""

DB_PATH = "data.db"

@contextmanager
def get_connection():
    """Get a new database connection with thread-safe settings."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10.0)
    conn.execute("PRAGMA journal_mode=WAL")  # Enable Write-Ahead Logging for better concurrency
    try:
        yield conn
    finally:
        conn.close()


def create_tables():
    with get_connection() as connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.commit()


def add_movie(title, release_timestamp):
    with get_connection() as connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))
        connection.commit()


def get_movies(upcoming=False):
    with get_connection() as connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def add_user(username):
    with get_connection() as connection:
        connection.execute(INSERT_USER, (username,))
        connection.commit()


def watch_movie(username, movie_id):
    with get_connection() as connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))
        connection.commit()


def get_watched_movies(username):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(search_term):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()
