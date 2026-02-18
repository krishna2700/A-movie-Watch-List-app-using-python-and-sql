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
    title TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    parent_task_id INTEGER,
    created_at REAL,
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id)
);"""

CREATE_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    icon TEXT NOT NULL
);"""

CREATE_TASK_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS task_agents (
    task_id INTEGER,
    agent_id INTEGER,
    status TEXT DEFAULT 'running',
    FOREIGN KEY(task_id) REFERENCES tasks(id),
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    PRIMARY KEY(task_id, agent_id)
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

INSERT_TASK = "INSERT INTO tasks (title, status, parent_task_id, created_at) VALUES (?, ?, ?, ?)"
UPDATE_TASK_STATUS = "UPDATE tasks SET status = ? WHERE id = ?"
SELECT_TASK = "SELECT * FROM tasks WHERE id = ?"
SELECT_ALL_TASKS = "SELECT * FROM tasks WHERE parent_task_id IS NULL ORDER BY created_at DESC;"
SELECT_FOLLOWUP_TASKS = "SELECT * FROM tasks WHERE parent_task_id = ? ORDER BY created_at DESC;"

INSERT_AGENT = "INSERT INTO agents (name, icon) VALUES (?, ?)"
SELECT_AGENT = "SELECT * FROM agents WHERE id = ?"
SELECT_ALL_AGENTS = "SELECT * FROM agents;"

INSERT_TASK_AGENT = "INSERT INTO task_agents (task_id, agent_id, status) VALUES (?, ?, ?)"
UPDATE_TASK_AGENT_STATUS = "UPDATE task_agents SET status = ? WHERE task_id = ? AND agent_id = ?"
SELECT_TASK_AGENTS = """SELECT agents.*, task_agents.status 
FROM agents 
JOIN task_agents ON agents.id = task_agents.agent_id 
WHERE task_agents.task_id = ?;"""
SELECT_RUNNING_AGENTS = """SELECT agents.* 
FROM agents 
JOIN task_agents ON agents.id = task_agents.agent_id 
WHERE task_agents.task_id = ? AND task_agents.status = 'running';"""
SELECT_STOPPED_AGENTS = """SELECT agents.* 
FROM agents 
JOIN task_agents ON agents.id = task_agents.agent_id 
WHERE task_agents.task_id = ? AND task_agents.status = 'stopped';"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        connection.execute(CREATE_TASKS_TABLE)
        connection.execute(CREATE_AGENTS_TABLE)
        connection.execute(CREATE_TASK_AGENTS_TABLE)


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
def add_task(title, parent_task_id=None):
    """Add a new task or followup task"""
    with connection:
        cursor = connection.cursor()
        created_at = datetime.datetime.now().timestamp()
        cursor.execute(INSERT_TASK, (title, 'pending', parent_task_id, created_at))
        return cursor.lastrowid


def update_task_status(task_id, status):
    """Update task status"""
    with connection:
        connection.execute(UPDATE_TASK_STATUS, (status, task_id))


def get_task(task_id):
    """Get a specific task"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_TASK, (task_id,))
        return cursor.fetchone()


def get_all_tasks():
    """Get all main tasks (not followup tasks)"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_TASKS)
        return cursor.fetchall()


def get_followup_tasks(parent_task_id):
    """Get all followup tasks for a parent task"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_FOLLOWUP_TASKS, (parent_task_id,))
        return cursor.fetchall()


def start_followup_task(task_id):
    """
    Start a followup task - resets status from completed to in_progress
    This is the key fix: when followup tasks start, status should reset
    """
    with connection:
        # Reset task status to in_progress
        connection.execute(UPDATE_TASK_STATUS, ('in_progress', task_id))
        
        # Reset all agents to running status
        cursor = connection.cursor()
        cursor.execute("UPDATE task_agents SET status = 'running' WHERE task_id = ?", (task_id,))


# Agent management functions
def add_agent(name, icon):
    """Add a new agent"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_AGENT, (name, icon))
        return cursor.lastrowid


def get_agent(agent_id):
    """Get a specific agent"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_AGENT, (agent_id,))
        return cursor.fetchone()


def get_all_agents():
    """Get all agents"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_AGENTS)
        return cursor.fetchall()


# Task-Agent relationship functions
def assign_agent_to_task(task_id, agent_id, status='running'):
    """Assign an agent to a task"""
    with connection:
        connection.execute(INSERT_TASK_AGENT, (task_id, agent_id, status))


def pause_agent(task_id, agent_id):
    """Pause a specific agent for a task"""
    with connection:
        connection.execute(UPDATE_TASK_AGENT_STATUS, ('stopped', task_id, agent_id))


def resume_agent(task_id, agent_id):
    """Resume a specific agent for a task"""
    with connection:
        connection.execute(UPDATE_TASK_AGENT_STATUS, ('running', task_id, agent_id))


def get_task_agents(task_id):
    """Get all agents assigned to a task with their status"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_TASK_AGENTS, (task_id,))
        return cursor.fetchall()


def get_running_agents(task_id):
    """Get all running agents for a task"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_RUNNING_AGENTS, (task_id,))
        return cursor.fetchall()


def get_stopped_agents(task_id):
    """Get all stopped agents for a task"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_STOPPED_AGENTS, (task_id,))
        return cursor.fetchall()


def get_task_status_display(task_id):
    """
    Get display information for task status including agent icons
    Returns: (status_text, agent_icons, agent_count)
    """
    task = get_task(task_id)
    if not task:
        return ("Unknown", [], 0)
    
    status = task[2]  # status column
    running_agents = get_running_agents(task_id)
    stopped_agents = get_stopped_agents(task_id)
    
    # Determine status text
    if status == 'completed':
        status_text = 'Completed'
    elif status == 'pending':
        status_text = 'Pending'
    elif status == 'in_progress':
        if len(running_agents) == 0 and len(stopped_agents) > 0:
            # All agents stopped
            status_text = 'Stopped'
        else:
            status_text = 'In Progress'
    else:
        status_text = status.title()
    
    # Get agent icons
    agent_icons = []
    if len(stopped_agents) > 0:
        # Show stopped agent icons
        agent_icons = [agent[2] for agent in stopped_agents]  # icon column
    elif len(running_agents) > 0:
        # Show running agent icons
        agent_icons = [agent[2] for agent in running_agents]  # icon column
    
    agent_count = len(running_agents) + len(stopped_agents)
    
    return (status_text, agent_icons, agent_count)
