"""
Task Manager Application with Multi-Agent Support
Handles main tasks, followup tasks, and agent status management
"""

import task_database as db
from datetime import datetime

class TaskManager:
    def __init__(self):
        db.create_tables()
    
    def create_main_task(self, title, description=""):
        """Create a new main task"""
        task_id = db.add_task(title, description, parent_task_id=None)
        print(f"Created main task #{task_id}: {title}")
        return task_id
    
    def create_followup_task(self, parent_task_id, title, description=""):
        """Create a followup task for a main task"""
        # Verify parent task exists
        parent = db.get_task(parent_task_id)
        if not parent:
            raise ValueError(f"Parent task #{parent_task_id} does not exist")
        
        task_id = db.add_task(title, description, parent_task_id=parent_task_id)
        print(f"Created followup task #{task_id}: {title} (parent: #{parent_task_id})")
        return task_id
    
    def start_task(self, task_id, agent_names):
        """Start a task with specified agents"""
        task = db.get_task(task_id)
        if not task:
            raise ValueError(f"Task #{task_id} does not exist")
        
        # If this is a followup task starting, reset its status
        if task['parent_task_id']:
            db.restart_followup_task(task_id)
        
        # Create or get agents
        agent_ids = []
        for name in agent_names:
            agent_id = db.add_agent(name, task_id)
            agent_ids.append(agent_id)
        
        # Start task with agents
        db.start_task_with_agents(task_id, agent_ids)
        print(f"Started task #{task_id} with {len(agent_ids)} agent(s)")
        
        return self.get_task_status(task_id)
    
    def pause_agents(self, task_id, agent_ids=None):
        """
        Pause specific agents or all agents on a task
        agent_ids: list of agent IDs to pause, or None to pause all
        """
        task = db.get_task(task_id)
        if not task:
            raise ValueError(f"Task #{task_id} does not exist")
        
        if agent_ids is None:
            # Pause all agents
            db.pause_all_agents_on_task(task_id)
            db.update_task_status(task_id, db.TaskStatus.STOPPED.value)
            print(f"Paused all agents on task #{task_id}")
        else:
            # Pause specific agents
            for agent_id in agent_ids:
                db.pause_agent_on_task(task_id, agent_id)
            
            # Check if all agents are now stopped
            status = self.get_task_status(task_id)
            if status['running_count'] == 0 and status['stopped_count'] > 0:
                db.update_task_status(task_id, db.TaskStatus.STOPPED.value)
            
            print(f"Paused {len(agent_ids)} agent(s) on task #{task_id}")
        
        return self.get_task_status(task_id)
    
    def resume_agents(self, task_id, agent_ids):
        """Resume specific paused agents"""
        task = db.get_task(task_id)
        if not task:
            raise ValueError(f"Task #{task_id} does not exist")
        
        for agent_id in agent_ids:
            db.resume_agent_on_task(task_id, agent_id)
        
        # Update task status back to in_progress
        db.update_task_status(task_id, db.TaskStatus.IN_PROGRESS.value)
        print(f"Resumed {len(agent_ids)} agent(s) on task #{task_id}")
        
        return self.get_task_status(task_id)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        task = db.get_task(task_id)
        if not task:
            raise ValueError(f"Task #{task_id} does not exist")
        
        db.complete_task(task_id)
        print(f"Completed task #{task_id}")
        
        return self.get_task_status(task_id)
    
    def get_task_status(self, task_id):
        """Get detailed status of a task including agent information"""
        status = db.get_task_status_with_agents(task_id)
        if not status:
            raise ValueError(f"Task #{task_id} does not exist")
        
        return status
    
    def get_task_display_info(self, task_id):
        """
        Get display information for a task including:
        - Current status
        - Agent icons to display
        - Status label
        """
        status = self.get_task_status(task_id)
        task = status['task']
        
        display_info = {
            'task_id': task_id,
            'title': task['title'],
            'status': task['status'],
            'is_followup': task['parent_task_id'] is not None,
            'parent_task_id': task['parent_task_id'],
            'agents': []
        }
        
        # Build agent display list
        for agent in status['agents']:
            display_info['agents'].append({
                'id': agent['agent_id'],
                'name': agent['agent_name'],
                'status': agent['status'],
                'icon': self._get_agent_icon(agent['agent_name'], agent['status'])
            })
        
        # Determine status display
        if task['status'] == db.TaskStatus.COMPLETED.value:
            display_info['status_label'] = 'Completed'
            display_info['status_color'] = 'green'
        elif task['status'] == db.TaskStatus.STOPPED.value:
            display_info['status_label'] = f"Stopped ({status['stopped_count']} agents)"
            display_info['status_color'] = 'red'
        elif task['status'] == db.TaskStatus.IN_PROGRESS.value:
            if status['running_count'] > 0:
                agent_names = [a['agent_name'] for a in status['running_agents']]
                display_info['status_label'] = f"In Progress ({', '.join(agent_names)})"
                display_info['status_color'] = 'blue'
            else:
                display_info['status_label'] = 'In Progress'
                display_info['status_color'] = 'blue'
        else:
            display_info['status_label'] = 'Pending'
            display_info['status_color'] = 'gray'
        
        # Show agent icons
        display_info['agent_icons_display'] = self._format_agent_icons(status)
        
        return display_info
    
    def _get_agent_icon(self, agent_name, status):
        """Get icon representation for an agent"""
        # Simple icon representation (could be emoji or icon class)
        status_icons = {
            'running': '🤖',
            'stopped': '⏸️',
            'paused': '⏸️'
        }
        return status_icons.get(status, '🤖')
    
    def _format_agent_icons(self, status):
        """
        Format agent icons for display
        - If 2 agents stopped, show both icons with "Stopped" status
        - Show only running agents when in progress
        - Limit display to prevent clutter
        """
        icons = []
        
        # Show stopped agents if task is stopped
        if status['task']['status'] == db.TaskStatus.STOPPED.value:
            for agent in status['stopped_agents'][:5]:  # Limit to 5
                icons.append({
                    'name': agent['agent_name'],
                    'icon': '⏸️',
                    'status': 'stopped'
                })
            if status['stopped_count'] > 5:
                icons.append({
                    'name': f'+{status["stopped_count"] - 5} more',
                    'icon': '⏸️',
                    'status': 'stopped'
                })
        
        # Show running agents if task is in progress
        elif status['task']['status'] == db.TaskStatus.IN_PROGRESS.value:
            for agent in status['running_agents'][:5]:  # Limit to 5
                icons.append({
                    'name': agent['agent_name'],
                    'icon': '🤖',
                    'status': 'running'
                })
            if status['running_count'] > 5:
                icons.append({
                    'name': f'+{status["running_count"] - 5} more',
                    'icon': '🤖',
                    'status': 'running'
                })
        
        return icons
    
    def list_tasks(self, show_followups=True):
        """List all tasks with their status"""
        main_tasks = db.get_main_tasks()
        
        result = []
        for task in main_tasks:
            task_info = self.get_task_display_info(task['id'])
            result.append(task_info)
            
            if show_followups:
                followups = db.get_followup_tasks(task['id'])
                for followup in followups:
                    followup_info = self.get_task_display_info(followup['id'])
                    result.append(followup_info)
        
        return result
    
    def print_task_tree(self):
        """Print a tree view of all tasks"""
        main_tasks = db.get_main_tasks()
        
        for task in main_tasks:
            info = self.get_task_display_info(task['id'])
            self._print_task_line(info, indent=0)
            
            # Print followup tasks
            followups = db.get_followup_tasks(task['id'])
            for followup in followups:
                followup_info = self.get_task_display_info(followup['id'])
                self._print_task_line(followup_info, indent=2)
    
    def _print_task_line(self, info, indent=0):
        """Print a single task line with formatting"""
        prefix = " " * indent + ("└─ " if indent > 0 else "")
        
        # Agent icons
        agent_display = ""
        if info['agent_icons_display']:
            icons = [a['icon'] for a in info['agent_icons_display']]
            agent_display = " " + "".join(icons)
        
        print(f"{prefix}Task #{info['task_id']}: {info['title']}")
        print(f"{' ' * (indent + 3)}Status: {info['status_label']}{agent_display}")
        
        if info['agents']:
            for agent in info['agents']:
                print(f"{' ' * (indent + 3)}  - {agent['name']}: {agent['status']} {agent['icon']}")
        print()


def demo():
    """Demonstration of the task manager system"""
    tm = TaskManager()
    
    print("=== Creating Main Task ===")
    task1 = tm.create_main_task("Implement User Authentication", "Add login and signup features")
    
    print("\n=== Starting Task with Multiple Agents ===")
    tm.start_task(task1, ["Agent-Alpha", "Agent-Beta", "Agent-Gamma"])
    
    print("\n=== Current Task Status ===")
    tm.print_task_tree()
    
    print("=== Pausing Specific Agents ===")
    status = tm.get_task_status(task1)
    agents_to_pause = [status['agents'][0]['agent_id'], status['agents'][1]['agent_id']]
    tm.pause_agents(task1, agents_to_pause)
    
    print("\n=== After Pausing 2 Agents ===")
    tm.print_task_tree()
    
    print("=== Pausing All Agents ===")
    tm.pause_agents(task1)  # Pause all
    
    print("\n=== After Pausing All Agents ===")
    tm.print_task_tree()
    
    print("=== Completing Main Task ===")
    tm.complete_task(task1)
    
    print("\n=== Creating and Starting Followup Task ===")
    followup1 = tm.create_followup_task(task1, "Add Password Reset Feature")
    tm.start_task(followup1, ["Agent-Delta", "Agent-Epsilon"])
    
    print("\n=== Full Task Tree ===")
    tm.print_task_tree()
    
    print("=== Pausing One Agent in Followup ===")
    followup_status = tm.get_task_status(followup1)
    tm.pause_agents(followup1, [followup_status['agents'][0]['agent_id']])
    
    print("\n=== Final Status ===")
    tm.print_task_tree()


if __name__ == "__main__":
    demo()
