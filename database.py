import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    last_workspace_type TEXT DEFAULT 'personal',
    last_workspace_id TEXT
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

CREATE_WORKSPACES_TABLE = """CREATE TABLE IF NOT EXISTS workspaces (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('personal', 'team')),
    owner_username TEXT,
    FOREIGN KEY(owner_username) REFERENCES users(username)
);"""

CREATE_WORKSPACE_MEMBERS_TABLE = """CREATE TABLE IF NOT EXISTS workspace_members (
    workspace_id INTEGER,
    username TEXT,
    FOREIGN KEY(workspace_id) REFERENCES workspaces(id),
    FOREIGN KEY(username) REFERENCES users(username),
    PRIMARY KEY(workspace_id, username)
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

INSERT_WORKSPACE = "INSERT INTO workspaces (name, type, owner_username) VALUES (?, ?, ?)"
SELECT_USER_WORKSPACES = """SELECT * FROM workspaces 
WHERE owner_username = ? OR id IN (SELECT workspace_id FROM workspace_members WHERE username = ?);"""
UPDATE_USER_LAST_WORKSPACE = "UPDATE users SET last_workspace_type = ?, last_workspace_id = ? WHERE username = ?"
SELECT_USER_LAST_WORKSPACE = "SELECT last_workspace_type, last_workspace_id FROM users WHERE username = ?"
SELECT_WORKSPACE_BY_ID = "SELECT * FROM workspaces WHERE id = ?"
INSERT_WORKSPACE_MEMBER = "INSERT INTO workspace_members (workspace_id, username) VALUES (?, ?)"

connection = None


def get_connection():
    global connection
    if connection is None:
        connection = sqlite3.connect("data.db")
    return connection


def create_tables():
    connection = get_connection()
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_WORKSPACES_TABLE)
        connection.execute(CREATE_WORKSPACE_MEMBERS_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)


def add_movie(title, release_timestamp):
    conn = get_connection()
    with conn:
        conn.execute(INSERT_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def add_user(username):
    conn = get_connection()
    with conn:
        conn.execute(INSERT_USER, (username,))


def watch_movie(username, movie_id):
    conn = get_connection()
    with conn:
        conn.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(search_term):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()


def create_workspace(name, workspace_type, owner_username):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_WORKSPACE, (name, workspace_type, owner_username))
        return cursor.lastrowid


def get_user_workspaces(username):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_USER_WORKSPACES, (username, username))
        return cursor.fetchall()


def update_user_last_workspace(username, workspace_type, workspace_id):
    conn = get_connection()
    with conn:
        conn.execute(UPDATE_USER_LAST_WORKSPACE, (workspace_type, workspace_id, username))


def get_user_last_workspace(username):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_USER_LAST_WORKSPACE, (username,))
        result = cursor.fetchone()
        return result if result else ('personal', None)


def get_workspace_by_id(workspace_id):
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_WORKSPACE_BY_ID, (workspace_id,))
        return cursor.fetchone()


def add_workspace_member(workspace_id, username):
    conn = get_connection()
    with conn:
        conn.execute(INSERT_WORKSPACE_MEMBER, (workspace_id, username))
