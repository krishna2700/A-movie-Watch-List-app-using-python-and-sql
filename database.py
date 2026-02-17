import datetime
import sqlite3

# --- Table Creation ---

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
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('personal', 'team')),
    owner_username TEXT NOT NULL,
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

CREATE_WORKSPACE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS workspace_watched (
    workspace_id INTEGER,
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(workspace_id) REFERENCES workspaces(id),
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

# --- Indexes ---

CREATE_RELEASE_INDEX = """CREATE INDEX IF NOT EXISTS movies_release_idx ON movies (release_timestamp);"""

# --- Movie Queries ---

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""

# --- User Queries ---

INSERT_USER = "INSERT INTO users (username, last_workspace_id) VALUES (?, ?)"
SELECT_USER = "SELECT * FROM users WHERE username = ?;"
UPDATE_LAST_WORKSPACE = "UPDATE users SET last_workspace_id = ? WHERE username = ?;"

# --- Workspace Queries ---

INSERT_WORKSPACE = "INSERT INTO workspaces (name, type, owner_username) VALUES (?, ?, ?)"
SELECT_USER_WORKSPACES = """
    SELECT DISTINCT w.* FROM workspaces w
    LEFT JOIN workspace_members wm ON w.id = wm.workspace_id
    WHERE w.owner_username = ? OR wm.username = ?
    ORDER BY w.type ASC, w.name ASC;
"""
SELECT_WORKSPACE_BY_ID = "SELECT * FROM workspaces WHERE id = ?;"

# --- Workspace Members Queries ---

INSERT_WORKSPACE_MEMBER = "INSERT OR IGNORE INTO workspace_members (workspace_id, username) VALUES (?, ?)"
SELECT_WORKSPACE_MEMBERS = """
    SELECT username FROM workspace_members WHERE workspace_id = ?;
"""

# --- Workspace Movies Queries ---

INSERT_WORKSPACE_MOVIE = "INSERT INTO workspace_movies (workspace_id, movie_id) VALUES (?, ?)"
SELECT_WORKSPACE_MOVIES = """
    SELECT m.* FROM movies m
    JOIN workspace_movies wm ON m.id = wm.movie_id
    WHERE wm.workspace_id = ?;
"""
SELECT_WORKSPACE_UPCOMING_MOVIES = """
    SELECT m.* FROM movies m
    JOIN workspace_movies wm ON m.id = wm.movie_id
    WHERE wm.workspace_id = ? AND m.release_timestamp > ?;
"""
SEARCH_WORKSPACE_MOVIES = """
    SELECT m.* FROM movies m
    JOIN workspace_movies wm ON m.id = wm.movie_id
    WHERE wm.workspace_id = ? AND m.title LIKE ?;
"""

# --- Workspace Watched Queries ---

INSERT_WORKSPACE_WATCHED = "INSERT INTO workspace_watched (workspace_id, user_username, movie_id) VALUES (?, ?, ?)"
SELECT_WORKSPACE_WATCHED = """
    SELECT m.* FROM movies m
    JOIN workspace_watched ww ON m.id = ww.movie_id
    WHERE ww.workspace_id = ? AND ww.user_username = ?;
"""

# --- Watched (legacy) ---

INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM users
JOIN watched ON users.username = watched.user_username
JOIN movies ON watched.movie_id = movies.id
WHERE users.username = ?;"""

# --- Connection ---

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_WORKSPACES_TABLE)
        connection.execute(CREATE_WORKSPACE_MEMBERS_TABLE)
        connection.execute(CREATE_WORKSPACE_MOVIES_TABLE)
        connection.execute(CREATE_WORKSPACE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
    _migrate_users_table()


def _migrate_users_table():
    """Add last_workspace_id column to users table if it doesn't exist (migration)."""
    with connection:
        cursor = connection.cursor()
        cursor.execute("PRAGMA table_info(users);")
        columns = [col[1] for col in cursor.fetchall()]
        if "last_workspace_id" not in columns:
            connection.execute("ALTER TABLE users ADD COLUMN last_workspace_id INTEGER;")


# --- Movie Functions ---

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


def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()


# --- User Functions ---

def add_user(username):
    """Add a new user and auto-create their personal workspace."""
    with connection:
        connection.execute(INSERT_USER, (username, None))
        # Create personal workspace
        connection.execute(INSERT_WORKSPACE, (f"{username}'s Workspace", "personal", username))
        cursor = connection.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        workspace_id = cursor.fetchone()[0]
        # Add user as member of their own personal workspace
        connection.execute(INSERT_WORKSPACE_MEMBER, (workspace_id, username))
        # Set personal workspace as the default last workspace
        connection.execute(UPDATE_LAST_WORKSPACE, (workspace_id, username))
        return workspace_id


def get_user(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (username,))
        return cursor.fetchone()


def user_exists(username):
    return get_user(username) is not None


# --- Workspace Functions ---

def create_team_workspace(name, owner_username):
    """Create a team workspace and add the owner as a member."""
    with connection:
        connection.execute(INSERT_WORKSPACE, (name, "team", owner_username))
        cursor = connection.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        workspace_id = cursor.fetchone()[0]
        connection.execute(INSERT_WORKSPACE_MEMBER, (workspace_id, owner_username))
        return workspace_id


def get_user_workspaces(username):
    """Get all workspaces a user owns or is a member of."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER_WORKSPACES, (username, username))
        return cursor.fetchall()


def get_workspace(workspace_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WORKSPACE_BY_ID, (workspace_id,))
        return cursor.fetchone()


def add_workspace_member(workspace_id, username):
    """Add a user to a team workspace."""
    with connection:
        connection.execute(INSERT_WORKSPACE_MEMBER, (workspace_id, username))


def get_workspace_members(workspace_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WORKSPACE_MEMBERS, (workspace_id,))
        return [row[0] for row in cursor.fetchall()]


def update_last_workspace(username, workspace_id):
    """Update the user's last visited workspace so it persists across sessions."""
    with connection:
        connection.execute(UPDATE_LAST_WORKSPACE, (workspace_id, username))


def get_last_workspace(username):
    """Get the user's last visited workspace. Returns workspace row or None."""
    user = get_user(username)
    if user and user[1] is not None:
        return get_workspace(user[1])
    return None


# --- Workspace-Scoped Movie Functions ---

def add_movie_to_workspace(workspace_id, title, release_timestamp):
    """Add a movie and associate it with the current workspace."""
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))
        cursor = connection.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        movie_id = cursor.fetchone()[0]
        connection.execute(INSERT_WORKSPACE_MOVIE, (workspace_id, movie_id))
        return movie_id


def get_workspace_movies(workspace_id, upcoming=False):
    """Get movies belonging to a specific workspace."""
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_WORKSPACE_UPCOMING_MOVIES, (workspace_id, today_timestamp))
        else:
            cursor.execute(SELECT_WORKSPACE_MOVIES, (workspace_id,))
        return cursor.fetchall()


def search_workspace_movies(workspace_id, search_term):
    """Search movies within a specific workspace."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_WORKSPACE_MOVIES, (workspace_id, f"%{search_term}%"))
        return cursor.fetchall()


def watch_movie_in_workspace(workspace_id, username, movie_id):
    """Mark a movie as watched within a workspace."""
    with connection:
        connection.execute(INSERT_WORKSPACE_WATCHED, (workspace_id, username, movie_id))
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_workspace_watched_movies(workspace_id, username):
    """Get watched movies for a user within a specific workspace."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WORKSPACE_WATCHED, (workspace_id, username))
        return cursor.fetchall()


# Legacy function kept for backward compatibility
def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()
