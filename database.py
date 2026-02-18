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
    id INTEGER PRIMARY KEY,
    title TEXT,
    status TEXT,
    followup_of INTEGER,
    created_at REAL,
    FOREIGN KEY(followup_of) REFERENCES tasks(id)
);"""

CREATE_TASK_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS task_agents (
    task_id INTEGER,
    agent_name TEXT,
    status TEXT,
    PRIMARY KEY (task_id, agent_name),
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
CREATE_TASK_FOLLOWUP_INDEX = """CREATE INDEX IF NOT EXISTS tasks_followup_idx ON tasks (followup_of);"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.execute(CREATE_TASKS_TABLE)
        connection.execute(CREATE_TASK_AGENTS_TABLE)
        connection.execute(CREATE_TASK_FOLLOWUP_INDEX)


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


def add_task(title, agent_names, followup_of=None):
    created_at = datetime.datetime.utcnow().timestamp()
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, status, followup_of, created_at) VALUES (?, ?, ?, ?)",
            (title, "in_progress", followup_of, created_at),
        )
        task_id = cursor.lastrowid
        for agent_name in agent_names:
            cursor.execute(
                "INSERT INTO task_agents (task_id, agent_name, status) VALUES (?, ?, ?)",
                (task_id, agent_name, "in_progress"),
            )
        return task_id


def add_followup_task(title, agent_names, parent_task_id):
    return add_task(title, agent_names, followup_of=parent_task_id)


def set_agent_status(task_id, agent_name, status):
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE task_agents SET status = ? WHERE task_id = ? AND agent_name = ?",
            (status, task_id, agent_name),
        )
        cursor.execute(
            "SELECT status FROM task_agents WHERE task_id = ?",
            (task_id,),
        )
        statuses = [row[0] for row in cursor.fetchall()]
        task_status = _derive_task_status(statuses)
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (task_status, task_id),
        )


def _derive_task_status(agent_statuses):
    if not agent_statuses:
        return "in_progress"
    normalized = [status for status in agent_statuses if status]
    if any(status == "in_progress" for status in normalized):
        return "in_progress"
    if all(status == "completed" for status in normalized):
        return "completed"
    if any(status == "stopped" for status in normalized):
        return "stopped"
    return "in_progress"


def complete_task(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE task_agents SET status = ? WHERE task_id = ?",
            ("completed", task_id),
        )
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            ("completed", task_id),
        )


def get_tasks_with_agents():
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, title, status, followup_of FROM tasks ORDER BY id"
        )
        tasks = cursor.fetchall()
        results = []
        for task_id, title, status, followup_of in tasks:
            cursor.execute(
                "SELECT agent_name, status FROM task_agents WHERE task_id = ? ORDER BY agent_name",
                (task_id,),
            )
            agents = cursor.fetchall()
            results.append(
                {
                    "id": task_id,
                    "title": title,
                    "status": status,
                    "followup_of": followup_of,
                    "agents": agents,
                }
            )
        return results
