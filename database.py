import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    last_workspace_id INTEGER
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

CREATE_WORKSPACES_TABLE = """CREATE TABLE IF NOT EXISTS workspaces (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT CHECK(type IN ('personal', 'team')),
    owner_username TEXT,
    FOREIGN KEY(owner_username) REFERENCES users(username)
);"""

CREATE_WORKSPACE_MEMBERS_TABLE = """CREATE TABLE IF NOT EXISTS workspace_members (
    workspace_id INTEGER,
    username TEXT,
    PRIMARY KEY(workspace_id, username),
    FOREIGN KEY(workspace_id) REFERENCES workspaces(id),
    FOREIGN KEY(username) REFERENCES users(username)
);"""

CREATE_WORKSPACE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS workspace_movies (
    workspace_id INTEGER,
    movie_id INTEGER,
    PRIMARY KEY(workspace_id, movie_id),
    FOREIGN KEY(workspace_id) REFERENCES workspaces(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
INSERT_USER = "INSERT INTO users (username, last_workspace_id) VALUES (?, NULL)"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM users
JOIN watched ON users.username = watched.user_username
JOIN movies ON watched.movie_id = movies.id
WHERE users.username = ?;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""
CREATE_RELEASE_INDEX = """CREATE INDEX IF NOT EXISTS movies_release_idx ON movies (release_timestamp);"""

# Workspace queries
INSERT_WORKSPACE = "INSERT INTO workspaces (name, type, owner_username) VALUES (?, ?, ?)"
INSERT_WORKSPACE_MEMBER = "INSERT OR IGNORE INTO workspace_members (workspace_id, username) VALUES (?, ?)"
INSERT_WORKSPACE_MOVIE = "INSERT OR IGNORE INTO workspace_movies (workspace_id, movie_id) VALUES (?, ?)"

SELECT_USER_WORKSPACES = """
SELECT workspaces.* FROM workspaces
LEFT JOIN workspace_members ON workspaces.id = workspace_members.workspace_id
WHERE workspaces.owner_username = ? OR workspace_members.username = ?
GROUP BY workspaces.id;"""

SELECT_WORKSPACE_BY_ID = "SELECT * FROM workspaces WHERE id = ?;"

SET_LAST_WORKSPACE = "UPDATE users SET last_workspace_id = ? WHERE username = ?;"
GET_LAST_WORKSPACE = "SELECT last_workspace_id FROM users WHERE username = ?;"

SELECT_WORKSPACE_MOVIES = """
SELECT movies.* FROM movies
JOIN workspace_movies ON movies.id = workspace_movies.movie_id
WHERE workspace_movies.workspace_id = ?;"""

SELECT_WORKSPACE_UPCOMING_MOVIES = """
SELECT movies.* FROM movies
JOIN workspace_movies ON movies.id = workspace_movies.movie_id
WHERE workspace_movies.workspace_id = ? AND movies.release_timestamp > ?;"""

SELECT_WORKSPACE_WATCHED_MOVIES = """
SELECT movies.* FROM movies
JOIN watched ON movies.id = watched.movie_id
JOIN workspace_movies ON movies.id = workspace_movies.movie_id
WHERE watched.user_username = ? AND workspace_movies.workspace_id = ?;"""

SEARCH_WORKSPACE_MOVIES = """
SELECT movies.* FROM movies
JOIN workspace_movies ON movies.id = workspace_movies.movie_id
WHERE workspace_movies.workspace_id = ? AND movies.title LIKE ?;"""

SELECT_USER = "SELECT * FROM users WHERE username = ?;"

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_WORKSPACES_TABLE)
        connection.execute(CREATE_WORKSPACE_MEMBERS_TABLE)
        connection.execute(CREATE_WORKSPACE_MOVIES_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        # Ensure last_workspace_id column exists for older databases
        try:
            connection.execute("ALTER TABLE users ADD COLUMN last_workspace_id INTEGER;")
        except sqlite3.OperationalError:
            pass  # Column already exists


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))
        cursor = connection.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        return cursor.fetchone()[0]


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


def get_user(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (username,))
        return cursor.fetchone()


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


# --- Workspace functions ---

def create_workspace(name, ws_type, owner_username):
    """Create a workspace and add the owner as a member. Returns workspace id."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_WORKSPACE, (name, ws_type, owner_username))
        workspace_id = cursor.lastrowid
        connection.execute(INSERT_WORKSPACE_MEMBER, (workspace_id, owner_username))
        return workspace_id


def create_personal_workspace(username):
    """Create the default personal workspace for a user and set it as last active."""
    workspace_id = create_workspace(f"{username}'s Workspace", "personal", username)
    set_last_workspace(username, workspace_id)
    return workspace_id


def add_workspace_member(workspace_id, username):
    """Add a user to a team workspace."""
    with connection:
        connection.execute(INSERT_WORKSPACE_MEMBER, (workspace_id, username))


def get_user_workspaces(username):
    """Get all workspaces a user has access to (personal + team)."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER_WORKSPACES, (username, username))
        return cursor.fetchall()


def get_workspace_by_id(workspace_id):
    """Get a workspace by its id."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WORKSPACE_BY_ID, (workspace_id,))
        return cursor.fetchone()


def set_last_workspace(username, workspace_id):
    """Persist the last active workspace for a user."""
    with connection:
        connection.execute(SET_LAST_WORKSPACE, (workspace_id, username))


def get_last_workspace(username):
    """Retrieve the last active workspace id for a user. Returns workspace_id or None."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_LAST_WORKSPACE, (username,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None


def add_movie_to_workspace(workspace_id, movie_id):
    """Link a movie to a workspace."""
    with connection:
        connection.execute(INSERT_WORKSPACE_MOVIE, (workspace_id, movie_id))


def get_workspace_movies(workspace_id, upcoming=False):
    """Get movies belonging to a workspace."""
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_WORKSPACE_UPCOMING_MOVIES, (workspace_id, today_timestamp))
        else:
            cursor.execute(SELECT_WORKSPACE_MOVIES, (workspace_id,))
        return cursor.fetchall()


def get_workspace_watched_movies(username, workspace_id):
    """Get watched movies within a specific workspace."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WORKSPACE_WATCHED_MOVIES, (username, workspace_id))
        return cursor.fetchall()


def search_workspace_movies(workspace_id, search_term):
    """Search movies within a specific workspace."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_WORKSPACE_MOVIES, (workspace_id, f"%{search_term}%"))
        return cursor.fetchall()
