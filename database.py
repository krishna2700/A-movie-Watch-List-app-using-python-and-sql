import datetime
import sqlite3

# ──────────────────────────────────────────────
# Movie Watchlist Tables (existing)
# ──────────────────────────────────────────────

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

# ──────────────────────────────────────────────
# Task & Agent Management Tables
# ──────────────────────────────────────────────

# Statuses: Pending, In Progress, Completed, Stopped
CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'Pending',
    created_at REAL NOT NULL
);"""

# Follow-up tasks linked to a parent task
# Key fix: status resets to 'Pending' and transitions to 'In Progress' when started
CREATE_FOLLOWUP_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS followup_tasks (
    id INTEGER PRIMARY KEY,
    parent_task_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'Pending',
    created_at REAL NOT NULL,
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id)
);"""

# Available agents
CREATE_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    icon TEXT NOT NULL DEFAULT '🤖'
);"""

# Agents assigned to main tasks with per-agent status
# agent_status: Running, Stopped, Completed
CREATE_TASK_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS task_agents (
    id INTEGER PRIMARY KEY,
    task_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    agent_status TEXT NOT NULL DEFAULT 'Running',
    FOREIGN KEY(task_id) REFERENCES tasks(id),
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    UNIQUE(task_id, agent_id)
);"""

# Agents assigned to follow-up tasks with per-agent status
CREATE_FOLLOWUP_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS followup_agents (
    id INTEGER PRIMARY KEY,
    followup_task_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    agent_status TEXT NOT NULL DEFAULT 'Running',
    FOREIGN KEY(followup_task_id) REFERENCES followup_tasks(id),
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    UNIQUE(followup_task_id, agent_id)
);"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        # Movie tables
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)
        # Task & agent tables
        connection.execute(CREATE_TASKS_TABLE)
        connection.execute(CREATE_FOLLOWUP_TASKS_TABLE)
        connection.execute(CREATE_AGENTS_TABLE)
        connection.execute(CREATE_TASK_AGENTS_TABLE)
        connection.execute(CREATE_FOLLOWUP_AGENTS_TABLE)


# ──────────────────────────────────────────────
# Movie Watchlist Functions (existing)
# ──────────────────────────────────────────────

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


# ──────────────────────────────────────────────
# Agent Management
# ──────────────────────────────────────────────

def add_agent(name, icon="🤖"):
    with connection:
        connection.execute(
            "INSERT OR IGNORE INTO agents (name, icon) VALUES (?, ?)",
            (name, icon),
        )


def get_all_agents():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM agents;")
        return cursor.fetchall()


def get_agent_by_id(agent_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM agents WHERE id = ?;", (agent_id,))
        return cursor.fetchone()


# ──────────────────────────────────────────────
# Task Management
# ──────────────────────────────────────────────

def create_task(title, description=""):
    with connection:
        now = datetime.datetime.now().timestamp()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, 'Pending', ?)",
            (title, description, now),
        )
        return cursor.lastrowid


def get_all_tasks():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC;")
        return cursor.fetchall()


def get_task_by_id(task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?;", (task_id,))
        return cursor.fetchone()


def update_task_status(task_id, status):
    with connection:
        connection.execute(
            "UPDATE tasks SET status = ? WHERE id = ?;",
            (status, task_id),
        )


def start_task(task_id):
    """Start a task — sets status to 'In Progress' and all assigned agents to 'Running'."""
    with connection:
        connection.execute(
            "UPDATE tasks SET status = 'In Progress' WHERE id = ?;", (task_id,)
        )
        connection.execute(
            "UPDATE task_agents SET agent_status = 'Running' WHERE task_id = ?;",
            (task_id,),
        )


def complete_task(task_id):
    """Complete a task — sets status to 'Completed' and all agents to 'Completed'."""
    with connection:
        connection.execute(
            "UPDATE tasks SET status = 'Completed' WHERE id = ?;", (task_id,)
        )
        connection.execute(
            "UPDATE task_agents SET agent_status = 'Completed' WHERE task_id = ?;",
            (task_id,),
        )


# ──────────────────────────────────────────────
# Assign Agents to Tasks
# ──────────────────────────────────────────────

def assign_agent_to_task(task_id, agent_id):
    with connection:
        connection.execute(
            "INSERT OR IGNORE INTO task_agents (task_id, agent_id, agent_status) VALUES (?, ?, 'Running')",
            (task_id, agent_id),
        )


def get_task_agents(task_id):
    """Get all agents assigned to a main task with their status."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT agents.id, agents.name, agents.icon, task_agents.agent_status
               FROM task_agents
               JOIN agents ON task_agents.agent_id = agents.id
               WHERE task_agents.task_id = ?;""",
            (task_id,),
        )
        return cursor.fetchall()


def stop_agent_on_task(task_id, agent_id):
    """Stop (pause) a specific agent on a task. Then recompute task status."""
    with connection:
        connection.execute(
            "UPDATE task_agents SET agent_status = 'Stopped' WHERE task_id = ? AND agent_id = ?;",
            (task_id, agent_id),
        )
    _recompute_task_status(task_id)


def resume_agent_on_task(task_id, agent_id):
    """Resume a stopped agent on a task. Then recompute task status."""
    with connection:
        connection.execute(
            "UPDATE task_agents SET agent_status = 'Running' WHERE task_id = ? AND agent_id = ?;",
            (task_id, agent_id),
        )
    _recompute_task_status(task_id)


def _recompute_task_status(task_id):
    """
    Recompute the overall task status based on individual agent statuses:
    - All agents Completed  → task = Completed
    - All agents Stopped    → task = Stopped
    - Any agent Running     → task = In Progress
    """
    agents = get_task_agents(task_id)
    if not agents:
        return

    statuses = [a[3] for a in agents]

    if all(s == "Completed" for s in statuses):
        update_task_status(task_id, "Completed")
    elif all(s == "Stopped" for s in statuses):
        update_task_status(task_id, "Stopped")
    else:
        update_task_status(task_id, "In Progress")


# ──────────────────────────────────────────────
# Follow-up Task Management
# ──────────────────────────────────────────────

def create_followup_task(parent_task_id, title, description=""):
    """Create a follow-up task under a parent. Always starts as 'Pending'."""
    with connection:
        now = datetime.datetime.now().timestamp()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO followup_tasks (parent_task_id, title, description, status, created_at) VALUES (?, ?, ?, 'Pending', ?)",
            (parent_task_id, title, description, now),
        )
        return cursor.lastrowid


def get_followup_tasks(parent_task_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM followup_tasks WHERE parent_task_id = ? ORDER BY created_at;",
            (parent_task_id,),
        )
        return cursor.fetchall()


def get_followup_task_by_id(followup_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM followup_tasks WHERE id = ?;", (followup_id,)
        )
        return cursor.fetchone()


def update_followup_status(followup_id, status):
    with connection:
        connection.execute(
            "UPDATE followup_tasks SET status = ? WHERE id = ?;",
            (status, followup_id),
        )


def start_followup_task(followup_id):
    """
    KEY FIX: When a follow-up task starts, its status is RESET to 'In Progress'
    regardless of what it was before (fixes the bug where it stayed 'Completed').
    All assigned agents are also reset to 'Running'.
    """
    with connection:
        connection.execute(
            "UPDATE followup_tasks SET status = 'In Progress' WHERE id = ?;",
            (followup_id,),
        )
        connection.execute(
            "UPDATE followup_agents SET agent_status = 'Running' WHERE followup_task_id = ?;",
            (followup_id,),
        )


def complete_followup_task(followup_id):
    """Complete a follow-up task and all its agents."""
    with connection:
        connection.execute(
            "UPDATE followup_tasks SET status = 'Completed' WHERE id = ?;",
            (followup_id,),
        )
        connection.execute(
            "UPDATE followup_agents SET agent_status = 'Completed' WHERE followup_task_id = ?;",
            (followup_id,),
        )


# ──────────────────────────────────────────────
# Assign Agents to Follow-up Tasks
# ──────────────────────────────────────────────

def assign_agent_to_followup(followup_id, agent_id):
    with connection:
        connection.execute(
            "INSERT OR IGNORE INTO followup_agents (followup_task_id, agent_id, agent_status) VALUES (?, ?, 'Running')",
            (followup_id, agent_id),
        )


def get_followup_agents(followup_id):
    """Get all agents assigned to a follow-up task with their status."""
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT agents.id, agents.name, agents.icon, followup_agents.agent_status
               FROM followup_agents
               JOIN agents ON followup_agents.agent_id = agents.id
               WHERE followup_agents.followup_task_id = ?;""",
            (followup_id,),
        )
        return cursor.fetchall()


def stop_agent_on_followup(followup_id, agent_id):
    """Stop (pause) a specific agent on a follow-up task. Then recompute status."""
    with connection:
        connection.execute(
            "UPDATE followup_agents SET agent_status = 'Stopped' WHERE followup_task_id = ? AND agent_id = ?;",
            (followup_id, agent_id),
        )
    _recompute_followup_status(followup_id)


def resume_agent_on_followup(followup_id, agent_id):
    """Resume a stopped agent on a follow-up task. Then recompute status."""
    with connection:
        connection.execute(
            "UPDATE followup_agents SET agent_status = 'Running' WHERE followup_task_id = ? AND agent_id = ?;",
            (followup_id, agent_id),
        )
    _recompute_followup_status(followup_id)


def _recompute_followup_status(followup_id):
    """
    Recompute follow-up task status from agent statuses — same logic as main tasks:
    - All agents Completed  → Completed
    - All agents Stopped    → Stopped  (shows stopped agent icons)
    - Any agent Running     → In Progress
    """
    agents = get_followup_agents(followup_id)
    if not agents:
        return

    statuses = [a[3] for a in agents]

    if all(s == "Completed" for s in statuses):
        update_followup_status(followup_id, "Completed")
    elif all(s == "Stopped" for s in statuses):
        update_followup_status(followup_id, "Stopped")
    else:
        update_followup_status(followup_id, "In Progress")


# ──────────────────────────────────────────────
# Display Helpers — Multi-Agent Icon Logic
# ──────────────────────────────────────────────

def format_agent_icons(agents, status_filter=None):
    """
    Build a display string of agent icons.
    If status_filter is provided, only include agents matching that status.
    Returns e.g. '🤖🤖' for 2 agents, or '🤖' for 1.
    """
    if status_filter:
        filtered = [a for a in agents if a[3] == status_filter]
    else:
        filtered = agents
    return "".join(a[2] for a in filtered)


def format_task_status_display(task_id, is_followup=False):
    """
    Build a full status display string for a task or follow-up task.
    Shows status + agent icons + per-agent breakdown.

    Examples:
      'In Progress 🤖🤖  [Agent-A: Running, Agent-B: Running]'
      'Stopped 🤖🤖  [Agent-A: Stopped, Agent-B: Stopped]'
      'In Progress 🤖  [Agent-A: Running] | Stopped: 🤖 [Agent-B: Stopped]'
    """
    if is_followup:
        task = get_followup_task_by_id(task_id)
        agents = get_followup_agents(task_id)
    else:
        task = get_task_by_id(task_id)
        agents = get_task_agents(task_id)

    if not task:
        return "Task not found"

    status = task[3] if not is_followup else task[4]

    if not agents:
        return f"{status} (no agents assigned)"

    running_agents = [a for a in agents if a[3] == "Running"]
    stopped_agents = [a for a in agents if a[3] == "Stopped"]
    completed_agents = [a for a in agents if a[3] == "Completed"]

    parts = [status]

    # Show icons for the dominant status group
    if status == "Stopped":
        icons = format_agent_icons(agents, "Stopped")
        parts.append(f" {icons}")
        agent_names = ", ".join(a[1] for a in stopped_agents)
        parts.append(f" [{agent_names}]")
    elif status == "In Progress":
        # Show running agent icons prominently
        running_icons = format_agent_icons(agents, "Running")
        parts.append(f" {running_icons}")
        running_names = ", ".join(f"{a[1]}: Running" for a in running_agents)
        parts.append(f" [{running_names}]")
        # Also show stopped agents if any
        if stopped_agents:
            stopped_icons = format_agent_icons(agents, "Stopped")
            stopped_names = ", ".join(a[1] for a in stopped_agents)
            parts.append(f" | Stopped: {stopped_icons} [{stopped_names}]")
    elif status == "Completed":
        icons = format_agent_icons(agents, "Completed")
        parts.append(f" {icons}")
        agent_names = ", ".join(a[1] for a in completed_agents)
        parts.append(f" [{agent_names}]")
    else:
        # Pending or other
        all_icons = format_agent_icons(agents)
        parts.append(f" {all_icons}")

    return "".join(parts)
