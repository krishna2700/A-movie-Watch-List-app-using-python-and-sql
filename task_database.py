import sqlite3
import json
from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    STOPPED = "stopped"

class AgentStatus(Enum):
    IDLE = "idle"
    RUNNING = "running"
    STOPPED = "stopped"
    PAUSED = "paused"

# Database schema
CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    parent_task_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id)
);"""

CREATE_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'idle',
    task_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(task_id) REFERENCES tasks(id)
);"""

CREATE_TASK_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS task_agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'running',
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stopped_at TIMESTAMP,
    FOREIGN KEY(task_id) REFERENCES tasks(id),
    FOREIGN KEY(agent_id) REFERENCES agents(id),
    UNIQUE(task_id, agent_id)
);"""

CREATE_TASK_INDEX = """CREATE INDEX IF NOT EXISTS idx_task_status ON tasks(status);"""
CREATE_PARENT_TASK_INDEX = """CREATE INDEX IF NOT EXISTS idx_parent_task ON tasks(parent_task_id);"""
CREATE_AGENT_STATUS_INDEX = """CREATE INDEX IF NOT EXISTS idx_agent_status ON agents(status);"""

# SQL Queries
INSERT_TASK = """INSERT INTO tasks (title, description, status, parent_task_id) 
                 VALUES (?, ?, ?, ?)"""
UPDATE_TASK_STATUS = """UPDATE tasks SET status = ?, updated_at = CURRENT_TIMESTAMP 
                        WHERE id = ?"""
UPDATE_TASK_COMPLETED = """UPDATE tasks SET status = ?, completed_at = ?, updated_at = CURRENT_TIMESTAMP 
                           WHERE id = ?"""
SELECT_TASK_BY_ID = """SELECT * FROM tasks WHERE id = ?"""
SELECT_MAIN_TASKS = """SELECT * FROM tasks WHERE parent_task_id IS NULL"""
SELECT_FOLLOWUP_TASKS = """SELECT * FROM tasks WHERE parent_task_id = ?"""
SELECT_ALL_TASKS = """SELECT * FROM tasks ORDER BY created_at DESC"""

INSERT_AGENT = """INSERT INTO agents (name, status, task_id) VALUES (?, ?, ?)"""
UPDATE_AGENT_STATUS = """UPDATE agents SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?"""
UPDATE_AGENT_TASK = """UPDATE agents SET task_id = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?"""
SELECT_AGENT_BY_ID = """SELECT * FROM agents WHERE id = ?"""
SELECT_AGENTS_BY_TASK = """SELECT a.* FROM agents a 
                           JOIN task_agents ta ON a.id = ta.agent_id 
                           WHERE ta.task_id = ? AND ta.status = 'running'"""
SELECT_ALL_AGENTS = """SELECT * FROM agents"""

INSERT_TASK_AGENT = """INSERT OR REPLACE INTO task_agents (task_id, agent_id, status) 
                       VALUES (?, ?, ?)"""
UPDATE_TASK_AGENT_STATUS = """UPDATE task_agents SET status = ?, 
                              stopped_at = CASE WHEN ? = 'stopped' THEN CURRENT_TIMESTAMP ELSE stopped_at END
                              WHERE task_id = ? AND agent_id = ?"""
SELECT_TASK_AGENTS = """SELECT ta.*, a.name as agent_name FROM task_agents ta 
                        JOIN agents a ON ta.agent_id = a.id 
                        WHERE ta.task_id = ?"""

connection = sqlite3.connect("tasks.db", check_same_thread=False)
connection.row_factory = sqlite3.Row

def create_tables():
    """Initialize database tables"""
    with connection:
        connection.execute(CREATE_TASKS_TABLE)
        connection.execute(CREATE_AGENTS_TABLE)
        connection.execute(CREATE_TASK_AGENTS_TABLE)
        connection.execute(CREATE_TASK_INDEX)
        connection.execute(CREATE_PARENT_TASK_INDEX)
        connection.execute(CREATE_AGENT_STATUS_INDEX)

# Task operations
def add_task(title, description="", parent_task_id=None):
    """Add a new task (main or followup)"""
    status = TaskStatus.PENDING.value
    with connection:
        cursor = connection.execute(INSERT_TASK, (title, description, status, parent_task_id))
        return cursor.lastrowid

def update_task_status(task_id, status):
    """Update task status"""
    if status == TaskStatus.COMPLETED.value:
        with connection:
            connection.execute(UPDATE_TASK_COMPLETED, (status, datetime.now(), task_id))
    else:
        with connection:
            connection.execute(UPDATE_TASK_STATUS, (status, task_id))

def get_task(task_id):
    """Get task by ID"""
    cursor = connection.execute(SELECT_TASK_BY_ID, (task_id,))
    row = cursor.fetchone()
    return dict(row) if row else None

def get_main_tasks():
    """Get all main tasks (no parent)"""
    cursor = connection.execute(SELECT_MAIN_TASKS)
    return [dict(row) for row in cursor.fetchall()]

def get_followup_tasks(parent_task_id):
    """Get all followup tasks for a parent task"""
    cursor = connection.execute(SELECT_FOLLOWUP_TASKS, (parent_task_id,))
    return [dict(row) for row in cursor.fetchall()]

def get_all_tasks():
    """Get all tasks"""
    cursor = connection.execute(SELECT_ALL_TASKS)
    return [dict(row) for row in cursor.fetchall()]

# Agent operations
def add_agent(name, task_id=None):
    """Add a new agent"""
    status = AgentStatus.IDLE.value
    with connection:
        cursor = connection.execute(INSERT_AGENT, (name, status, task_id))
        return cursor.lastrowid

def update_agent_status(agent_id, status):
    """Update agent status"""
    with connection:
        connection.execute(UPDATE_AGENT_STATUS, (status, agent_id))

def assign_agent_to_task(agent_id, task_id):
    """Assign agent to task"""
    with connection:
        connection.execute(UPDATE_AGENT_TASK, (task_id, agent_id))
        connection.execute(INSERT_TASK_AGENT, (task_id, agent_id, 'running'))

def get_agent(agent_id):
    """Get agent by ID"""
    cursor = connection.execute(SELECT_AGENT_BY_ID, (agent_id,))
    row = cursor.fetchone()
    return dict(row) if row else None

def get_agents_for_task(task_id):
    """Get all running agents for a task"""
    cursor = connection.execute(SELECT_AGENTS_BY_TASK, (task_id,))
    return [dict(row) for row in cursor.fetchall()]

def get_all_agents():
    """Get all agents"""
    cursor = connection.execute(SELECT_ALL_AGENTS)
    return [dict(row) for row in cursor.fetchall()]

# Task-Agent relationship operations
def pause_agent_on_task(task_id, agent_id):
    """Pause a specific agent on a task"""
    with connection:
        connection.execute(UPDATE_TASK_AGENT_STATUS, ('stopped', 'stopped', task_id, agent_id))
        connection.execute(UPDATE_AGENT_STATUS, (AgentStatus.PAUSED.value, agent_id))

def pause_all_agents_on_task(task_id):
    """Pause all agents working on a task"""
    agents = get_agents_for_task(task_id)
    with connection:
        for agent in agents:
            pause_agent_on_task(task_id, agent['id'])

def resume_agent_on_task(task_id, agent_id):
    """Resume a paused agent on a task"""
    with connection:
        connection.execute(UPDATE_TASK_AGENT_STATUS, ('running', 'running', task_id, agent_id))
        connection.execute(UPDATE_AGENT_STATUS, (AgentStatus.RUNNING.value, agent_id))

def get_task_agents(task_id):
    """Get all agents assigned to a task with their status"""
    cursor = connection.execute(SELECT_TASK_AGENTS, (task_id,))
    return [dict(row) for row in cursor.fetchall()]

def start_task_with_agents(task_id, agent_ids):
    """Start a task and assign multiple agents to it"""
    # Update task status to in_progress
    update_task_status(task_id, TaskStatus.IN_PROGRESS.value)
    
    # Assign all agents
    for agent_id in agent_ids:
        assign_agent_to_task(agent_id, task_id)
        update_agent_status(agent_id, AgentStatus.RUNNING.value)

def complete_task(task_id):
    """Complete a task and update all agents"""
    agents = get_agents_for_task(task_id)
    
    with connection:
        # Mark task as completed
        update_task_status(task_id, TaskStatus.COMPLETED.value)
        
        # Update all agents to idle
        for agent in agents:
            connection.execute(UPDATE_TASK_AGENT_STATUS, ('stopped', 'stopped', task_id, agent['id']))
            update_agent_status(agent['id'], AgentStatus.IDLE.value)

def get_task_status_with_agents(task_id):
    """Get task status along with agent information"""
    task = get_task(task_id)
    if not task:
        return None
    
    task_agents = get_task_agents(task_id)
    
    # Determine actual status based on agents
    running_agents = [ta for ta in task_agents if ta['status'] == 'running']
    stopped_agents = [ta for ta in task_agents if ta['status'] == 'stopped']
    
    result = {
        'task': task,
        'agents': task_agents,
        'running_agents': running_agents,
        'stopped_agents': stopped_agents,
        'agent_count': len(task_agents),
        'running_count': len(running_agents),
        'stopped_count': len(stopped_agents)
    }
    
    return result

def restart_followup_task(task_id):
    """Restart a followup task when it begins (reset status from parent's completed)"""
    task = get_task(task_id)
    if task and task['parent_task_id']:
        # Reset status to pending when followup task starts
        update_task_status(task_id, TaskStatus.PENDING.value)
