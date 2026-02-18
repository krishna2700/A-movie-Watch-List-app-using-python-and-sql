"""
UI Helper Functions for Task and Agent Status Display

This module provides helper functions for rendering task status
and agent information in the frontend UI.
"""

import database


def get_task_display_info(task_id):
    """
    Get comprehensive task display information including status and agents.

    Returns a dictionary with all information needed for UI rendering:
    - status: The display status (stopped, in_progress, completed, pending)
    - status_label: Human-readable status label
    - agent_icons: List of agent icons to display
    - agent_info: Detailed agent information
    - show_pulse: Whether to show pause/pulse icon
    """
    status_info = database.get_task_status_with_agents(task_id)
    if not status_info:
        return None

    display_status = status_info['status']
    active_agents = status_info['active_agents']
    stopped_agents = status_info['stopped_agents']

    # Determine status label
    status_labels = {
        'pending': 'Pending',
        'in_progress': 'In Progress',
        'completed': 'Completed',
        'stopped': 'Stopped'
    }
    status_label = status_labels.get(display_status, 'Unknown')

    # Collect agent icons for display
    agent_icons = []
    if active_agents:
        # Show first 2 active agent icons
        for agent in active_agents[:2]:
            if agent[3]:  # agent_icon
                agent_icons.append(agent[3])

    if stopped_agents and not active_agents:
        # If all agents stopped, show stopped agent icons
        for agent in stopped_agents[:2]:
            if agent[3]:  # agent_icon
                agent_icons.append(agent[3])

    # Build detailed agent info
    agent_details = []
    for agent in active_agents:
        agent_details.append({
            'id': agent[0],
            'name': agent[2],
            'icon': agent[3],
            'status': 'running',
            'can_pause': True
        })

    for agent in stopped_agents:
        agent_details.append({
            'id': agent[0],
            'name': agent[2],
            'icon': agent[3],
            'status': 'stopped',
            'can_pause': False
        })

    # Show pulse icon when there are active agents
    show_pulse = len(active_agents) > 0

    return {
        'task_id': task_id,
        'title': status_info['title'],
        'status': display_status,
        'status_label': status_label,
        'agent_icons': agent_icons,
        'agent_count': len(agent_details),
        'active_count': len(active_agents),
        'stopped_count': len(stopped_agents),
        'agents': agent_details,
        'show_pulse': show_pulse,
        'is_followup': status_info['is_followup']
    }


def format_status_badge(task_id):
    """
    Format status badge HTML/text representation.

    For in_progress tasks: Shows which agents are running
    For stopped tasks: Shows 'Stopped' with stopped agent icons
    """
    info = get_task_display_info(task_id)
    if not info:
        return "Unknown"

    status = info['status']

    if status == 'stopped':
        # Show "Stopped" with stopped agent icons
        icons = ' '.join(info['agent_icons'][:2])
        return f"Stopped {icons}"

    elif status == 'in_progress':
        # Show "In Progress" with active agent info
        if info['active_count'] == 1:
            agent_name = info['agents'][0]['name']
            agent_icon = info['agents'][0]['icon']
            return f"In Progress: {agent_icon} {agent_name}"
        elif info['active_count'] > 1:
            icons = ' '.join(info['agent_icons'])
            return f"In Progress: {icons} ({info['active_count']} agents)"
        else:
            return "In Progress"

    elif status == 'completed':
        return "Completed"

    elif status == 'pending':
        return "Pending"

    return status.title()


def get_pause_menu_items(task_id):
    """
    Get menu items for the pause dropdown.

    Returns a list of agents that can be paused with their details.
    Used when user clicks the pulse icon to show selective pause options.
    """
    info = get_task_display_info(task_id)
    if not info:
        return []

    menu_items = []

    # Add option to pause all active agents
    if info['active_count'] > 1:
        menu_items.append({
            'type': 'pause_all',
            'label': 'Pause All Agents',
            'icon': '⏸️',
            'agents': [a for a in info['agents'] if a['status'] == 'running']
        })

    # Add individual agent pause options
    for agent in info['agents']:
        if agent['status'] == 'running':
            menu_items.append({
                'type': 'pause_single',
                'agent_id': agent['id'],
                'label': f"Pause {agent['name']}",
                'icon': agent['icon'],
                'agent_name': agent['name']
            })

    return menu_items


def should_reset_followup_status(task_id):
    """
    Check if a follow-up task status should be reset when starting.

    Returns True if this is a follow-up task that was previously completed
    and should be reset to in_progress when work starts again.
    """
    task = database.get_task(task_id)
    if not task:
        return False

    is_followup = task[7]  # is_followup column
    status = task[3]  # status column

    # Reset if it's a follow-up task that was completed
    return is_followup and status == 'completed'


def format_agent_list_for_ui(task_id):
    """
    Format agent list for UI display.

    Returns formatted string showing agent status:
    - "Agent1 🔧, Agent2 🎨" for multiple agents
    - "Agent1 🔧 (+ 2 stopped)" if some agents are stopped
    """
    info = get_task_display_info(task_id)
    if not info or not info['agents']:
        return ""

    parts = []

    # Show active agents
    for agent in info['agents'][:2]:
        if agent['status'] == 'running':
            parts.append(f"{agent['name']} {agent['icon']}")

    # Show stopped count if any
    if info['stopped_count'] > 0:
        if parts:
            parts.append(f"(+ {info['stopped_count']} stopped)")
        else:
            # All stopped
            for agent in info['agents'][:2]:
                parts.append(f"{agent['name']} {agent['icon']}")

    return ', '.join(parts)


# Example usage
if __name__ == "__main__":
    # This would typically be called from a web framework or UI layer
    print("UI Helper Functions Demo")
    print("=" * 60)

    # Create sample data
    database.create_tables()
    task_id = database.add_task("Sample Task", "Test task", status='in_progress')
    agent1 = database.add_agent(task_id, "Backend Agent", "🔧", "running")
    agent2 = database.add_agent(task_id, "Frontend Agent", "🎨", "running")

    # Get display info
    info = get_task_display_info(task_id)
    print(f"\nTask Display Info:")
    print(f"  Title: {info['title']}")
    print(f"  Status: {info['status_label']}")
    print(f"  Agent Icons: {' '.join(info['agent_icons'])}")
    print(f"  Show Pulse: {info['show_pulse']}")

    # Format status badge
    badge = format_status_badge(task_id)
    print(f"\nStatus Badge: {badge}")

    # Get pause menu
    menu = get_pause_menu_items(task_id)
    print(f"\nPause Menu Items:")
    for item in menu:
        print(f"  - {item['label']} {item.get('icon', '')}")

    # Format agent list
    agent_list = format_agent_list_for_ui(task_id)
    print(f"\nAgent List: {agent_list}")

    # Pause one agent
    print("\n--- After Pausing One Agent ---")
    database.pause_agent(agent1)

    badge = format_status_badge(task_id)
    print(f"Status Badge: {badge}")

    agent_list = format_agent_list_for_ui(task_id)
    print(f"Agent List: {agent_list}")

    # Pause all agents
    print("\n--- After Pausing All Agents ---")
    database.pause_agent(agent2)

    badge = format_status_badge(task_id)
    print(f"Status Badge: {badge}")
    print(f"Status: {get_task_display_info(task_id)['status']}")
