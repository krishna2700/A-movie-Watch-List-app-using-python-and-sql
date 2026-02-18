#!/usr/bin/env python3
"""
Task Management System with Multi-Agent Support
Handles main tasks, follow-up tasks, and agent status tracking
"""

import task_database as db
from datetime import datetime

# Initialize database
db.create_tables()


def display_task(task, indent=0):
    """Display a task with its status and agents"""
    prefix = "  " * indent
    status_info = task['status_info']
    
    # Build status display
    status_display = status_info['display_text']
    if status_info['display_icons']:
        icons_str = " ".join(status_info['display_icons'])
        status_display = f"{icons_str} {status_display}"
    
    print(f"{prefix}[{task['id']}] {task['content']}")
    print(f"{prefix}    Status: {status_display}")
    
    # Show agents if any
    if status_info['agents']:
        agents_display = ", ".join([
            f"{a['icon']} {a['name']} ({a['status']})" 
            for a in status_info['agents']
        ])
        print(f"{prefix}    Agents: {agents_display}")
    
    # Show follow-up tasks
    if 'followups' in task and task['followups']:
        print(f"{prefix}    Follow-up tasks:")
        for followup in task['followups']:
            display_task(followup, indent + 2)
    
    print()


def add_new_task():
    """Add a new main task"""
    content = input("Task content: ")
    task_id = db.add_task(content)
    print(f"✓ Task created with ID: {task_id}")
    
    # Ask if agents should be added
    add_agents = input("Add agents to this task? (y/n): ").lower()
    if add_agents == 'y':
        while True:
            agent_name = input("Agent name (or press Enter to finish): ")
            if not agent_name:
                break
            agent_icon = input(f"Icon for {agent_name} (emoji): ")
            db.add_agent_to_task(task_id, agent_name, agent_icon)
            print(f"✓ Agent {agent_icon} {agent_name} added")
    
    return task_id


def add_followup_task():
    """Add a follow-up task to an existing task"""
    parent_id = int(input("Parent task ID: "))
    content = input("Follow-up task content: ")
    task_id = db.add_task(content, parent_id)
    print(f"✓ Follow-up task created with ID: {task_id}")
    
    # Ask if agents should be added
    add_agents = input("Add agents to this follow-up task? (y/n): ").lower()
    if add_agents == 'y':
        while True:
            agent_name = input("Agent name (or press Enter to finish): ")
            if not agent_name:
                break
            agent_icon = input(f"Icon for {agent_name} (emoji): ")
            db.add_agent_to_task(task_id, agent_name, agent_icon)
            print(f"✓ Agent {agent_icon} {agent_name} added")
    
    return task_id


def update_status():
    """Update task status"""
    task_id = int(input("Task ID: "))
    print("\nAvailable statuses:")
    print("1) pending")
    print("2) in_progress")
    print("3) completed")
    print("4) stopped")
    
    choice = input("Select status (1-4): ")
    status_map = {
        '1': 'pending',
        '2': 'in_progress',
        '3': 'completed',
        '4': 'stopped'
    }
    
    if choice in status_map:
        new_status = status_map[choice]
        if db.update_task_status(task_id, new_status):
            print(f"✓ Task {task_id} status updated to: {new_status}")
            
            # Special handling for follow-up tasks starting
            task = db.get_task_with_details(task_id)
            if task and task['parent_task_id'] and new_status == 'in_progress':
                print("  → Follow-up task status reset from completed (if applicable)")
        else:
            print("✗ Task not found")
    else:
        print("✗ Invalid choice")


def pause_task_agents():
    """Pause specific agents for a task"""
    task_id = int(input("Task ID: "))
    
    # Get all agents for this task
    agents = db.get_task_agents(task_id)
    if not agents:
        print("✗ No agents found for this task")
        return
    
    print("\nAgents for this task:")
    for agent in agents:
        print(f"  [{agent['id']}] {agent['icon']} {agent['name']} - Status: {agent['status']}")
    
    # Get agent IDs to pause
    agent_ids_input = input("\nEnter agent IDs to pause (comma-separated): ")
    try:
        agent_ids = [int(x.strip()) for x in agent_ids_input.split(',')]
        count = db.pause_agents(task_id, agent_ids)
        print(f"✓ Paused {count} agent(s)")
        
        # Show updated task
        task = db.get_task_with_details(task_id)
        if task:
            print("\nUpdated task status:")
            display_task(task)
    except ValueError:
        print("✗ Invalid agent IDs")


def start_followup():
    """Start a follow-up task (resets status if completed)"""
    followup_id = int(input("Follow-up task ID: "))
    if db.start_followup_task(followup_id):
        print(f"✓ Follow-up task {followup_id} started/restarted")
        task = db.get_task_with_details(followup_id)
        if task:
            display_task(task)
    else:
        print("✗ Follow-up task not found")


def view_all_tasks():
    """View all tasks with their follow-ups and agents"""
    tasks = db.get_all_tasks()
    if not tasks:
        print("No tasks found")
        return
    
    print("\n" + "=" * 80)
    print("ALL TASKS")
    print("=" * 80)
    for task in tasks:
        display_task(task)


def demo_scenario():
    """Create a demo scenario to showcase the features"""
    print("\n🎭 Creating demo scenario...")
    
    # Create main task
    main_task_id = db.add_task("Build new feature: User Dashboard")
    db.add_agent_to_task(main_task_id, "Frontend Agent", "🎨")
    db.add_agent_to_task(main_task_id, "Backend Agent", "⚙️")
    db.update_task_status(main_task_id, 'completed')
    print(f"✓ Created main task {main_task_id} with 2 agents (completed)")
    
    # Create follow-up task
    followup_id = db.add_task("Add dark mode support", main_task_id)
    db.add_agent_to_task(followup_id, "UI Agent", "🎨")
    db.add_agent_to_task(followup_id, "Theme Agent", "🌙")
    db.update_task_status(followup_id, 'completed')
    print(f"✓ Created follow-up task {followup_id} with 2 agents (completed)")
    
    # Now when we start the follow-up, it should reset status
    print("\n📍 Simulating follow-up task restart...")
    db.start_followup_task(followup_id)
    
    # Pause one agent
    agents = db.get_task_agents(followup_id)
    if agents:
        db.pause_agents(followup_id, [agents[0]['id']])
        print(f"✓ Paused agent: {agents[0]['icon']} {agents[0]['name']}")
    
    print("\n" + "=" * 80)
    print("DEMO RESULT - Task with stopped agent:")
    print("=" * 80)
    task = db.get_task_with_details(main_task_id)
    display_task(task)


def main():
    """Main menu"""
    menu = """
╔════════════════════════════════════════════════════════╗
║         Task Management with Multi-Agent Support        ║
╚════════════════════════════════════════════════════════╝

1) Add new task
2) Add follow-up task
3) Update task status
4) Pause specific agents
5) Start/restart follow-up task
6) View all tasks
7) Run demo scenario
8) Exit

Your choice: """

    while True:
        choice = input(menu).strip()
        
        if choice == '1':
            add_new_task()
        elif choice == '2':
            add_followup_task()
        elif choice == '3':
            update_status()
        elif choice == '4':
            pause_task_agents()
        elif choice == '5':
            start_followup()
        elif choice == '6':
            view_all_tasks()
        elif choice == '7':
            demo_scenario()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
