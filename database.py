import datetime
import sqlite3
from contextlib import contextmanager
import threading

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

_local = threading.local()

@contextmanager
def get_connection():
    if not hasattr(_local, 'connection') or _local.connection is None:
        _local.connection = sqlite3.connect("data.db", check_same_thread=False, timeout=30.0)
        _local.connection.execute("PRAGMA journal_mode=WAL")
        _local.connection.execute("PRAGMA synchronous=NORMAL")
        _local.connection.execute("PRAGMA cache_size=-64000")

    try:
        yield _local.connection
    except Exception:
        _local.connection.rollback()
        raise
    else:
        _local.connection.commit()


def create_tables():
    with get_connection() as conn:
        conn.execute(CREATE_MOVIES_TABLE)
        conn.execute(CREATE_USERS_TABLE)
        conn.execute(CREATE_WATCHED_TABLE)
        conn.execute(CREATE_RELEASE_INDEX)


def add_movie(title, release_timestamp):
    with get_connection() as conn:
        conn.execute(INSERT_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with get_connection() as conn:
        cursor = conn.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def add_user(username):
    with get_connection() as conn:
        conn.execute(INSERT_USER, (username,))


def watch_movie(username, movie_id):
    with get_connection() as conn:
        conn.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(search_term):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()
