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

CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    created_at REAL,
    updated_at REAL,
    parent_task_id INTEGER,
    is_followup BOOLEAN DEFAULT 0,
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id)
);"""

CREATE_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    agent_name TEXT NOT NULL,
    agent_icon TEXT,
    status TEXT DEFAULT 'running',
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

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.execute(CREATE_TASKS_TABLE)
        connection.execute(CREATE_AGENTS_TABLE)


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


# Task management functions
INSERT_TASK = """INSERT INTO tasks (title, description, status, created_at, updated_at, parent_task_id, is_followup)
                 VALUES (?, ?, ?, ?, ?, ?, ?)"""
UPDATE_TASK_STATUS = """UPDATE tasks SET status = ?, updated_at = ? WHERE id = ?"""
GET_TASK = """SELECT * FROM tasks WHERE id = ?"""
GET_FOLLOWUP_TASKS = """SELECT * FROM tasks WHERE parent_task_id = ? AND is_followup = 1"""
GET_ALL_TASKS = """SELECT * FROM tasks WHERE parent_task_id IS NULL"""

INSERT_AGENT = """INSERT INTO agents (task_id, agent_name, agent_icon, status, created_at) VALUES (?, ?, ?, ?, ?)"""
UPDATE_AGENT_STATUS = """UPDATE agents SET status = ? WHERE id = ?"""
GET_TASK_AGENTS = """SELECT * FROM agents WHERE task_id = ?"""
GET_ACTIVE_AGENTS = """SELECT * FROM agents WHERE task_id = ? AND status = 'running'"""
GET_STOPPED_AGENTS = """SELECT * FROM agents WHERE task_id = ? AND status = 'stopped'"""


def add_task(title, description, status='pending', parent_task_id=None, is_followup=False):
    with connection:
        now = datetime.datetime.now().timestamp()
        connection.execute(INSERT_TASK, (title, description, status, now, now, parent_task_id, is_followup))
        return connection.execute("SELECT last_insert_rowid()").fetchone()[0]


def update_task_status(task_id, status):
    with connection:
        now = datetime.datetime.now().timestamp()
        connection.execute(UPDATE_TASK_STATUS, (status, now, task_id))

        # When a followup task starts, reset its status from 'completed' to 'in_progress'
        task = get_task(task_id)
        if task and task[7]:  # is_followup
            if status in ['in_progress', 'pending']:
                # Also update all child followup tasks to reset from completed
                followup_tasks = get_followup_tasks(task_id)
                for ft in followup_tasks:
                    if ft[3] == 'completed':  # status column
                        connection.execute(UPDATE_TASK_STATUS, ('pending', now, ft[0]))


def get_task(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_TASK, (task_id,))
        return cursor.fetchone()


def get_followup_tasks(parent_task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_FOLLOWUP_TASKS, (parent_task_id,))
        return cursor.fetchall()


def get_all_tasks():
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_ALL_TASKS)
        return cursor.fetchall()


def add_agent(task_id, agent_name, agent_icon=None, status='running'):
    with connection:
        now = datetime.datetime.now().timestamp()
        connection.execute(INSERT_AGENT, (task_id, agent_name, agent_icon, status, now))
        return connection.execute("SELECT last_insert_rowid()").fetchone()[0]


def update_agent_status(agent_id, status):
    with connection:
        connection.execute(UPDATE_AGENT_STATUS, (status, agent_id))


def pause_agent(agent_id):
    update_agent_status(agent_id, 'stopped')


def get_task_agents(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_TASK_AGENTS, (task_id,))
        return cursor.fetchall()


def get_active_agents(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_ACTIVE_AGENTS, (task_id,))
        return cursor.fetchall()


def get_stopped_agents(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_STOPPED_AGENTS, (task_id,))
        return cursor.fetchall()


def get_task_status_with_agents(task_id):
    """
    Get task status with agent information.
    Returns a dict with status, active agents, and stopped agents.
    """
    task = get_task(task_id)
    if not task:
        return None

    active_agents = get_active_agents(task_id)
    stopped_agents = get_stopped_agents(task_id)

    status = task[3]  # status column

    # Determine display status based on agents
    if stopped_agents and not active_agents:
        display_status = 'stopped'
    elif active_agents:
        display_status = 'in_progress'
    else:
        display_status = status

    return {
        'task_id': task[0],
        'title': task[1],
        'status': display_status,
        'actual_status': status,
        'active_agents': active_agents,
        'stopped_agents': stopped_agents,
        'agent_count': len(active_agents) + len(stopped_agents),
        'is_followup': task[7]
    }
