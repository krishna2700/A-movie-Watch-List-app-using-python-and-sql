import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT DEFAULT 'Unknown',
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

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, genre) VALUES (?, ?, ?)"
SELECT_ALL_MOVIES = "SELECT * FROM movies ORDER BY release_timestamp DESC;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ? ORDER BY release_timestamp ASC;"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM users
JOIN watched ON users.username = watched.user_username
JOIN movies ON watched.movie_id = movies.id
WHERE users.username = ?;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ? ORDER BY release_timestamp DESC;"""
CREATE_RELEASE_INDEX = """CREATE INDEX IF NOT EXISTS movies_release_idx ON movies (release_timestamp);"""

CREATE_RATINGS_TABLE = """CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY,
    user_username TEXT,
    movie_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 10),
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""
INSERT_RATING = "INSERT INTO ratings (user_username, movie_id, rating) VALUES (?, ?, ?)"

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.execute(CREATE_RATINGS_TABLE)


def add_movie(title, release_timestamp, genre="Unknown"):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp, genre))


def rate_movie(username, movie_id, rating):
    with connection:
        connection.execute(INSERT_RATING, (username, movie_id, rating))


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


def get_movie_ratings(movie_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT AVG(rating), COUNT(*) FROM ratings WHERE movie_id = ?",
            (movie_id,),
        )
        return cursor.fetchone()
