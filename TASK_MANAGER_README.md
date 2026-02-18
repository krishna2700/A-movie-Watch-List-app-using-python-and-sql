# Multi-Agent Task Manager

A comprehensive task management system with multi-agent support, designed to handle main tasks, followup tasks, and agent status tracking with pause/resume functionality.

## Features

### 1. Task Management
- **Main Tasks**: Create independent tasks that can be tracked and managed
- **Followup Tasks**: Create tasks that are linked to a parent task
- **Status Tracking**: Automatic status updates based on agent activity
  - `Pending`: Task not yet started
  - `In Progress`: Task is actively being worked on by agents
  - `Completed`: Task has been finished
  - `Stopped`: Task has been paused (all agents stopped)

### 2. Multi-Agent Support
- Assign multiple agents to a single task
- Track individual agent status
- Display agent icons in the UI with status indicators
- Show which agents are currently working on a task

### 3. Agent Status Management
- **Running**: Agent is actively working on a task (🤖)
- **Stopped/Paused**: Agent has been paused (⏸️)
- **Idle**: Agent is not assigned to any task

### 4. Pause/Resume Functionality
- **Pause All Agents**: Stop all agents working on a task
- **Pause Specific Agents**: Select individual agents to pause while others continue
- **Resume Agents**: Restart paused agents to continue work
- **Visual Indicators**: Stopped agents show with pause icon (⏸️)

### 5. Followup Task Status Reset
When a followup task is created after the main task is completed:
- The followup task starts with `Pending` status
- When agents are assigned and the task begins, status changes to `In Progress`
- This ensures followup tasks don't inherit the "Completed" status from the parent

### 6. Agent Icon Display Logic
The system implements smart agent icon display:
- **When task is In Progress**: Shows running agent icons
- **When task is Stopped**: Shows stopped agent icons with count
- **Multiple agents**: Displays up to 5 agent icons, then "+X more" for additional agents
- **Hover tooltips**: Shows agent names when hovering over icons

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the web application:
```bash
python3 web_app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Command Line Demo

Run the demonstration script to see all features in action:
```bash
python3 task_manager.py
```

This will:
1. Create a main task
2. Start it with multiple agents
3. Pause specific agents
4. Pause all agents
5. Complete the main task
6. Create and start a followup task
7. Demonstrate selective agent pausing

### Web Interface

1. **Create a Task**:
   - Enter task title and optional description
   - Select parent task (for followup) or leave empty for main task
   - Click "Create Task"

2. **Start a Task**:
   - Click "Start Task" button
   - Enter comma-separated agent names (e.g., "Agent-Alpha, Agent-Beta")
   - Task status changes to "In Progress"

3. **Pause Agents**:
   - Click the "⏸️ Pause" button
   - Choose to pause all agents or select specific ones
   - Task shows "Stopped" status if all agents are paused

4. **Resume Agents**:
   - Click the "▶️ Resume" button
   - Select which agents to resume
   - Task returns to "In Progress" status

5. **Complete a Task**:
   - Click "✅ Complete" button
   - All agents are stopped and task is marked as completed

## Architecture

### Database Schema

#### Tasks Table
- `id`: Primary key
- `title`: Task name
- `description`: Task details
- `status`: Current status (pending/in_progress/completed/stopped)
- `parent_task_id`: Reference to parent task (for followups)
- `created_at`, `updated_at`, `completed_at`: Timestamps

#### Agents Table
- `id`: Primary key
- `name`: Agent name
- `status`: Current status (idle/running/stopped/paused)
- `task_id`: Currently assigned task
- `created_at`, `updated_at`: Timestamps

#### Task_Agents Table (Junction)
- `task_id`: Reference to task
- `agent_id`: Reference to agent
- `status`: Agent status on this specific task
- `started_at`, `stopped_at`: Timestamps

### API Endpoints

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks?main_only=true` - Get only main tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/:id` - Get specific task
- `POST /api/tasks/:id/start` - Start task with agents
- `POST /api/tasks/:id/pause` - Pause agents on task
- `POST /api/tasks/:id/resume` - Resume paused agents
- `POST /api/tasks/:id/complete` - Mark task as completed
- `GET /api/agents` - Get all agents
- `GET /api/tasks/:id/agents` - Get agents for specific task

## Key Features Implemented

### 1. Followup Task Status Reset ✅
When a main task is completed and a followup task is created:
```python
def restart_followup_task(task_id):
    """Restart a followup task when it begins (reset status from parent's completed)"""
    task = get_task(task_id)
    if task and task['parent_task_id']:
        # Reset status to pending when followup task starts
        update_task_status(task_id, TaskStatus.PENDING.value)
```

### 2. Selective Agent Pausing ✅
Users can pause individual agents or all agents:
```python
def pause_agents(self, task_id, agent_ids=None):
    """
    Pause specific agents or all agents on a task
    agent_ids: list of agent IDs to pause, or None to pause all
    """
    if agent_ids is None:
        # Pause all agents
        db.pause_all_agents_on_task(task_id)
    else:
        # Pause specific agents
        for agent_id in agent_ids:
            db.pause_agent_on_task(task_id, agent_id)
```

### 3. Smart Status Display ✅
Status shows what's actually happening:
- "In Progress (Agent-Alpha, Agent-Beta)" - Shows which agents are running
- "Stopped (2 agents)" - Shows how many agents are stopped
- Agent icons display with appropriate status indicators

### 4. Multi-Agent Icon Logic ✅
```python
def _format_agent_icons(self, status):
    """
    Format agent icons for display
    - If 2 agents stopped, show both icons with "Stopped" status
    - Show only running agents when in progress
    - Limit display to prevent clutter
    """
```

## Examples

### Example 1: Main Task with Multiple Agents
```
Task #1: Implement User Authentication
Status: In Progress (Agent-Alpha, Agent-Beta, Agent-Gamma) 🤖🤖🤖
  - Agent-Alpha: running 🤖
  - Agent-Beta: running 🤖
  - Agent-Gamma: running 🤖
```

### Example 2: Paused Agents
```
Task #1: Implement User Authentication
Status: Stopped (3 agents) ⏸️⏸️⏸️
  - Agent-Alpha: stopped ⏸️
  - Agent-Beta: stopped ⏸️
  - Agent-Gamma: stopped ⏸️
```

### Example 3: Partial Pause
```
Task #1: Implement User Authentication
Status: In Progress (Agent-Gamma) 🤖
  - Agent-Alpha: stopped ⏸️
  - Agent-Beta: stopped ⏸️
  - Agent-Gamma: running 🤖
```

### Example 4: Followup Task
```
Task #1: Implement User Authentication
   Status: Completed

  └─ Task #2: Add Password Reset Feature
     Status: In Progress (Agent-Delta, Agent-Epsilon) 🤖🤖
       - Agent-Delta: running 🤖
       - Agent-Epsilon: running 🤖
```

## Files

- `task_database.py`: Database schema and operations
- `task_manager.py`: Business logic and task management
- `web_app.py`: Flask web application and REST API
- `templates/index.html`: Web interface
- `static/styles.css`: UI styling
- `requirements.txt`: Python dependencies

## Testing

Run the demo to verify all functionality:
```bash
python3 task_manager.py
```

Expected output shows:
- ✅ Task creation
- ✅ Multi-agent assignment
- ✅ Status updates
- ✅ Selective pausing
- ✅ Complete task workflow
- ✅ Followup task handling
- ✅ Agent icon display

## Troubleshooting

### Database locked error
If you get a database locked error, remove the database file and restart:
```bash
rm tasks.db
python3 web_app.py
```

### Agents not showing
Make sure to assign agents when starting a task. You can't pause agents if none are assigned.

### Status not updating
The web interface auto-refreshes every 5 seconds. If status isn't updating, check the browser console for errors.
