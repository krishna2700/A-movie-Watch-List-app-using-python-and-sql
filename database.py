import datetime
import sqlite3

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

CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    branch_name TEXT NOT NULL,
    parent_task_id INTEGER,
    created_at REAL NOT NULL,
    is_initial_task INTEGER DEFAULT 1,
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id)
);"""

INSERT_TASK = "INSERT INTO tasks (task_name, branch_name, parent_task_id, created_at, is_initial_task) VALUES (?, ?, ?, ?, ?)"
SELECT_ALL_TASKS = "SELECT * FROM tasks ORDER BY created_at DESC;"
SELECT_INITIAL_TASKS = "SELECT * FROM tasks WHERE is_initial_task = 1 ORDER BY created_at DESC;"
SELECT_TASK_BY_ID = "SELECT * FROM tasks WHERE id = ?;"
SELECT_FOLLOW_UP_TASKS = "SELECT * FROM tasks WHERE parent_task_id = ?;"

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.execute(CREATE_TASKS_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))


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


def add_task(task_name, branch_name, parent_task_id=None, is_initial_task=True):
    with connection:
        created_at = datetime.datetime.now().timestamp()
        connection.execute(
            INSERT_TASK, (task_name, branch_name, parent_task_id, created_at, 1 if is_initial_task else 0)
        )
        return connection.execute("SELECT last_insert_rowid()").fetchone()[0]


def get_all_tasks():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_TASKS)
        return cursor.fetchall()


def get_initial_tasks():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_INITIAL_TASKS)
        return cursor.fetchall()


def get_task_by_id(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_TASK_BY_ID, (task_id,))
        return cursor.fetchone()


def get_follow_up_tasks(parent_task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_FOLLOW_UP_TASKS, (parent_task_id,))
        return cursor.fetchall()
