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

CREATE_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);"""

CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    agent_id INTEGER NOT NULL,
    parent_task_id INTEGER,
    branch_id INTEGER,
    created_at REAL,
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id),
    FOREIGN KEY(branch_id) REFERENCES branches(id)
);"""

CREATE_BRANCHES_TABLE = """CREATE TABLE IF NOT EXISTS branches (
    id INTEGER PRIMARY KEY,
    task_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    created_at REAL,
    FOREIGN KEY(task_id) REFERENCES tasks(id)
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

INSERT_AGENT = "INSERT INTO agents (name, description) VALUES (?, ?)"
SELECT_ALL_AGENTS = "SELECT * FROM agents;"
SELECT_AGENT_BY_ID = "SELECT * FROM agents WHERE id = ?;"

INSERT_TASK = """INSERT INTO tasks (title, description, agent_id, parent_task_id, branch_id, created_at)
VALUES (?, ?, ?, ?, ?, ?);"""
SELECT_ALL_TASKS = "SELECT * FROM tasks;"
SELECT_TASK_BY_ID = "SELECT * FROM tasks WHERE id = ?;"
SELECT_TASKS_BY_PARENT = "SELECT * FROM tasks WHERE parent_task_id = ?;"

INSERT_BRANCH = "INSERT INTO branches (task_id, name, description, created_at) VALUES (?, ?, ?, ?)"
SELECT_BRANCHES_BY_TASK = "SELECT * FROM branches WHERE task_id = ?;"
SELECT_BRANCH_BY_ID = "SELECT * FROM branches WHERE id = ?;"

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.execute(CREATE_AGENTS_TABLE)
        connection.execute(CREATE_BRANCHES_TABLE)
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


# --- Agent functions ---

def add_agent(name, description):
    with connection:
        connection.execute(INSERT_AGENT, (name, description))


def get_agents():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_AGENTS)
        return cursor.fetchall()


def get_agent_by_id(agent_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_AGENT_BY_ID, (agent_id,))
        return cursor.fetchone()


# --- Task functions ---

def add_task(title, description, agent_id, parent_task_id=None, branch_id=None):
    with connection:
        created_at = datetime.datetime.today().timestamp()
        connection.execute(
            INSERT_TASK, (title, description, agent_id, parent_task_id, branch_id, created_at)
        )


def get_tasks():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_TASKS)
        return cursor.fetchall()


def get_task_by_id(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_TASK_BY_ID, (task_id,))
        return cursor.fetchone()


def get_follow_up_tasks(parent_task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_TASKS_BY_PARENT, (parent_task_id,))
        return cursor.fetchall()


# --- Branch functions ---

def add_branch(task_id, name, description):
    with connection:
        created_at = datetime.datetime.today().timestamp()
        connection.execute(INSERT_BRANCH, (task_id, name, description, created_at))


def get_branches_for_task(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_BRANCHES_BY_TASK, (task_id,))
        return cursor.fetchall()


def get_branch_by_id(branch_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_BRANCH_BY_ID, (branch_id,))
        return cursor.fetchone()
