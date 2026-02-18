import datetime
import os
import sqlite3

# Use absolute path to ensure the same DB is used regardless of working directory
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db")

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL,
    image BLOB
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

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, image) VALUES (?, ?, ?)"
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

UPDATE_MOVIE_IMAGE = "UPDATE movies SET image = ? WHERE id = ?;"
SELECT_MOVIE_IMAGE = "SELECT id, title, image FROM movies WHERE id = ?;"

connection = sqlite3.connect(DB_PATH)


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        _migrate_add_image_column()


def _migrate_add_image_column():
    """Add image column to existing movies table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(movies);")
    columns = [row[1] for row in cursor.fetchall()]
    if "image" not in columns:
        connection.execute("ALTER TABLE movies ADD COLUMN image BLOB;")


def add_movie(title, release_timestamp, image=None):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp, image))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()


def add_movie_image(movie_id, image_data):
    """Store image binary data for a movie."""
    with connection:
        connection.execute(UPDATE_MOVIE_IMAGE, (image_data, movie_id))


def get_movie_image(movie_id):
    """Retrieve image binary data for a movie. Returns (id, title, image_blob) or None."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_MOVIE_IMAGE, (movie_id,))
        return cursor.fetchone()
