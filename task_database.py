import sqlite3
import json
from datetime import datetime
import os

# Database connection - use /tmp for sandbox environments
db_path = os.path.join('/tmp', 'tasks.db')
connection = None

def get_connection():
    """Get or create database connection"""
    global connection
    if connection is None:
        connection = sqlite3.connect(db_path, check_same_thread=False)
    return connection

# SQL Statements
CREATE_TASKS_TABLE = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    parent_task_id INTEGER,
    FOREIGN KEY(parent_task_id) REFERENCES tasks(id) ON DELETE CASCADE
);"""

CREATE_AGENTS_TABLE = """CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    icon TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(task_id) REFERENCES tasks(id) ON DELETE CASCADE
);"""

CREATE_TASK_STATUS_HISTORY = """CREATE TABLE IF NOT EXISTS task_status_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    old_status TEXT,
    new_status TEXT NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(task_id) REFERENCES tasks(id) ON DELETE CASCADE
);"""


def create_tables():
    """Initialize database tables"""
    conn = get_connection()
    with conn:
        conn.execute(CREATE_TASKS_TABLE)
        conn.execute(CREATE_AGENTS_TABLE)
        conn.execute(CREATE_TASK_STATUS_HISTORY)


def add_task(content, parent_task_id=None):
    """Add a new task or follow-up task"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (content, status, parent_task_id) VALUES (?, ?, ?)",
            (content, 'pending', parent_task_id)
        )
        task_id = cursor.lastrowid
        # Log status change
        cursor.execute(
            "INSERT INTO task_status_history (task_id, old_status, new_status) VALUES (?, ?, ?)",
            (task_id, None, 'pending')
        )
        return task_id


def add_agent_to_task(task_id, agent_name, agent_icon):
    """Add an agent to a task"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO agents (task_id, name, icon, status) VALUES (?, ?, ?, ?)",
            (task_id, agent_name, agent_icon, 'active')
        )
        return cursor.lastrowid


def update_task_status(task_id, new_status):
    """Update task status with history tracking"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        # Get current status
        cursor.execute("SELECT status FROM tasks WHERE id = ?", (task_id,))
        result = cursor.fetchone()
        if result:
            old_status = result[0]
            # Update task status
            completed_at = datetime.now() if new_status == 'completed' else None
            cursor.execute(
                "UPDATE tasks SET status = ?, completed_at = ? WHERE id = ?",
                (new_status, completed_at, task_id)
            )
            # Log status change
            cursor.execute(
                "INSERT INTO task_status_history (task_id, old_status, new_status) VALUES (?, ?, ?)",
                (task_id, old_status, new_status)
            )
            # If task status changes to in_progress, restart follow-up tasks if they were completed
            if new_status == 'in_progress':
                cursor.execute(
                    "UPDATE tasks SET status = 'pending', completed_at = NULL WHERE parent_task_id = ? AND status = 'completed'",
                    (task_id,)
                )
            return True
        return False


def update_agent_status(agent_id, new_status):
    """Update individual agent status (active, stopped, paused)"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE agents SET status = ? WHERE id = ?",
            (new_status, agent_id)
        )
        return cursor.rowcount > 0


def pause_agents(task_id, agent_ids):
    """Pause specific agents for a task"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        placeholders = ','.join(['?'] * len(agent_ids))
        cursor.execute(
            f"UPDATE agents SET status = 'stopped' WHERE task_id = ? AND id IN ({placeholders})",
            [task_id] + agent_ids
        )
        return cursor.rowcount


def get_task_agents(task_id):
    """Get all agents for a specific task"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, icon, status FROM agents WHERE task_id = ? ORDER BY id",
            (task_id,)
        )
        agents = []
        for row in cursor.fetchall():
            agents.append({
                'id': row[0],
                'name': row[1],
                'icon': row[2],
                'status': row[3]
            })
        return agents


def get_task_with_details(task_id):
    """Get task with all its agents and status"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, content, status, created_at, completed_at, parent_task_id FROM tasks WHERE id = ?",
            (task_id,)
        )
        task_row = cursor.fetchone()
        if not task_row:
            return None
        
        agents = get_task_agents(task_id)
        
        # Determine display status based on agents
        display_status = task_row[2]  # default to task status
        stopped_agents = [a for a in agents if a['status'] == 'stopped']
        active_agents = [a for a in agents if a['status'] == 'active']
        
        # Build status display info
        status_info = {
            'status': display_status,
            'agents': agents,
            'stopped_agents': stopped_agents,
            'active_agents': active_agents,
            'display_icons': [],
            'display_text': display_status.capitalize()
        }
        
        # If agents are stopped, show their icons
        if stopped_agents:
            status_info['display_icons'] = [a['icon'] for a in stopped_agents]
            status_info['display_text'] = 'Stopped'
        elif display_status == 'in_progress' and agents:
            # Show active agent icons when in progress
            status_info['display_icons'] = [a['icon'] for a in active_agents[:2]]  # Show up to 2 icons
            if len(active_agents) > 2:
                status_info['display_text'] = f"In Progress ({len(active_agents)} agents)"
            else:
                status_info['display_text'] = "In Progress"
        
        return {
            'id': task_row[0],
            'content': task_row[1],
            'status': task_row[2],
            'created_at': task_row[3],
            'completed_at': task_row[4],
            'parent_task_id': task_row[5],
            'status_info': status_info
        }


def get_followup_tasks(parent_task_id):
    """Get all follow-up tasks for a parent task"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM tasks WHERE parent_task_id = ? ORDER BY created_at",
            (parent_task_id,)
        )
        followup_tasks = []
        for row in cursor.fetchall():
            task = get_task_with_details(row[0])
            if task:
                followup_tasks.append(task)
        return followup_tasks


def get_all_tasks():
    """Get all main tasks (no parent)"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM tasks WHERE parent_task_id IS NULL ORDER BY created_at DESC"
        )
        tasks = []
        for row in cursor.fetchall():
            task = get_task_with_details(row[0])
            if task:
                task['followups'] = get_followup_tasks(row[0])
                tasks.append(task)
        return tasks


def start_followup_task(followup_task_id):
    """Start a follow-up task - resets status if it was completed"""
    conn = get_connection()
    with conn:
        cursor = conn.cursor()
        # Get current status
        cursor.execute("SELECT status, parent_task_id FROM tasks WHERE id = ?", (followup_task_id,))
        result = cursor.fetchone()
        if result:
            current_status = result[0]
            parent_id = result[1]
            
            # If it was completed, reset to in_progress
            if current_status == 'completed':
                update_task_status(followup_task_id, 'in_progress')
                # Also reset agent statuses
                cursor.execute(
                    "UPDATE agents SET status = 'active' WHERE task_id = ?",
                    (followup_task_id,)
                )
            elif current_status == 'pending':
                update_task_status(followup_task_id, 'in_progress')
            
            return True
        return False
