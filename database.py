import datetime
import sqlite3
import threading
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

# Thread-local storage for database connections
_thread_local = threading.local()

def get_connection():
    """Get or create a connection for the current thread."""
    if not hasattr(_thread_local, 'connection'):
        _thread_local.connection = sqlite3.connect("data.db", check_same_thread=False, timeout=5.0)
        # Enable WAL mode for better concurrent access
        _thread_local.connection.execute("PRAGMA journal_mode=WAL")
    return _thread_local.connection

@contextmanager
def get_db():
    """Context manager for database connections."""
    conn = get_connection()
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    else:
        conn.commit()


def create_tables():
    with get_db() as conn:
        conn.execute(CREATE_MOVIES_TABLE)
        conn.execute(CREATE_USERS_TABLE)
        conn.execute(CREATE_WATCHED_TABLE)
        conn.execute(CREATE_RELEASE_INDEX)


def add_movie(title, release_timestamp):
    with get_db() as conn:
        conn.execute(INSERT_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with get_db() as conn:
        cursor = conn.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def add_user(username):
    with get_db() as conn:
        conn.execute(INSERT_USER, (username,))


def watch_movie(username, movie_id):
    with get_db() as conn:
        conn.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(search_term):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()
