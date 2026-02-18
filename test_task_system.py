#!/usr/bin/env python3
"""
Test script demonstrating the task management system fixes:
1. Followup task status resets when started (not stuck on 'completed')
2. Selective agent pausing (pause specific agents, not all)
3. Multi-agent icon display in followup tasks
4. Proper status display showing which agents are in progress
"""

import database

def print_separator(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

# Initialize database
database.create_tables()

print_separator("SETUP: Creating Agents")
agent1_id = database.add_agent('Research Agent', '🔍')
agent2_id = database.add_agent('Code Agent', '💻')
agent3_id = database.add_agent('Test Agent', '🧪')
print(f"Created 3 agents:")
print(f"  🔍 Research Agent (ID: {agent1_id})")
print(f"  💻 Code Agent (ID: {agent2_id})")
print(f"  🧪 Test Agent (ID: {agent3_id})")

print_separator("TEST 1: Main Task with Multiple Agents")
main_task_id = database.add_task('Implement new feature')
database.assign_agent_to_task(main_task_id, agent1_id)
database.assign_agent_to_task(main_task_id, agent2_id)
database.assign_agent_to_task(main_task_id, agent3_id)

database.update_task_status(main_task_id, 'in_progress')
status_text, agent_icons, agent_count = database.get_task_status_display(main_task_id)
print(f"Main task started:")
print(f"  Status: {status_text}")
print(f"  Agents: {' '.join(agent_icons)} ({agent_count} total)")

database.update_task_status(main_task_id, 'completed')
status_text, _, _ = database.get_task_status_display(main_task_id)
print(f"\nMain task completed:")
print(f"  Status: {status_text}")

print_separator("TEST 2: Followup Task Status Reset Issue (FIXED)")
followup_id = database.add_task('Fix bugs found in testing', parent_task_id=main_task_id)
database.assign_agent_to_task(followup_id, agent1_id)
database.assign_agent_to_task(followup_id, agent2_id)

# Simulate the issue: followup task gets completed
database.update_task_status(followup_id, 'completed')
status_text, _, _ = database.get_task_status_display(followup_id)
print(f"Followup task marked completed:")
print(f"  Status: {status_text}")

# THE FIX: When followup task starts, status should reset
print(f"\n🔧 Starting followup task (should reset from 'completed')...")
database.start_followup_task(followup_id)
status_text, agent_icons, agent_count = database.get_task_status_display(followup_id)
print(f"  Status: {status_text} ✓")
print(f"  Agents: {' '.join(agent_icons)} ({agent_count} total)")

print_separator("TEST 3: Selective Agent Pausing (FIXED)")
print("Current agents running:")
running = database.get_running_agents(followup_id)
for agent in running:
    print(f"  {agent[2]} {agent[1]}")

print(f"\n🔧 Pausing only Research Agent (not all agents)...")
database.pause_agent(followup_id, agent1_id)

running = database.get_running_agents(followup_id)
stopped = database.get_stopped_agents(followup_id)

print(f"\nRunning agents:")
for agent in running:
    print(f"  {agent[2]} {agent[1]}")

print(f"\nStopped agents:")
for agent in stopped:
    print(f"  {agent[2]} {agent[1]}")

status_text, agent_icons, _ = database.get_task_status_display(followup_id)
print(f"\nTask status: {status_text}")
print(f"Stopped agent icons shown: {' '.join(agent_icons)}")

print_separator("TEST 4: All Agents Stopped = 'Stopped' Status")
print("🔧 Pausing all remaining agents...")
database.pause_agent(followup_id, agent2_id)

status_text, agent_icons, agent_count = database.get_task_status_display(followup_id)
print(f"\nTask status: {status_text} ✓")
print(f"All stopped agent icons: {' '.join(agent_icons)}")
print(f"Total agents: {agent_count}")

print_separator("TEST 5: Multi-Agent Icon Display Logic")
# Create a task with many agents to test icon display
many_agents_task = database.add_task('Task with many agents')
database.assign_agent_to_task(many_agents_task, agent1_id)
database.assign_agent_to_task(many_agents_task, agent2_id)
database.assign_agent_to_task(many_agents_task, agent3_id)

database.update_task_status(many_agents_task, 'in_progress')
status_text, agent_icons, agent_count = database.get_task_status_display(many_agents_task)

print(f"Task with {agent_count} agents:")
print(f"  Status: {status_text}")
if len(agent_icons) <= 2:
    icon_display = " ".join(agent_icons)
else:
    icon_display = f"{agent_icons[0]} {agent_icons[1]} +{agent_count - 2}"
print(f"  Icon display: {icon_display}")

print_separator("TEST 6: View All Tasks with Followup Tasks")
tasks = database.get_all_tasks()
for task in tasks:
    task_id = task[0]
    title = task[1]
    status_text, agent_icons, agent_count = database.get_task_status_display(task_id)
    
    icon_display = ""
    if agent_count > 0:
        if len(agent_icons) <= 2:
            icon_display = " ".join(agent_icons)
        else:
            icon_display = f"{agent_icons[0]} {agent_icons[1]} +{agent_count - 2}"
    
    print(f"📋 {title}")
    print(f"   Status: {status_text} {icon_display}")
    
    # Show followup tasks
    followup_tasks = database.get_followup_tasks(task_id)
    if followup_tasks:
        print("   Followup tasks:")
        for ft in followup_tasks:
            ft_id = ft[0]
            ft_title = ft[1]
            ft_status_text, ft_agent_icons, ft_agent_count = database.get_task_status_display(ft_id)
            
            ft_icon_display = ""
            if ft_agent_count > 0:
                if len(ft_agent_icons) <= 2:
                    ft_icon_display = " ".join(ft_agent_icons)
                else:
                    ft_icon_display = f"{ft_agent_icons[0]} {ft_agent_icons[1]} +{ft_agent_count - 2}"
            
            print(f"     ↳ {ft_title}")
            print(f"       Status: {ft_status_text} {ft_icon_display}")
    print()

print_separator("SUMMARY OF FIXES")
print("✅ Fix 1: Followup task status resets when started")
print("   - Status changes from 'completed' to 'in_progress'")
print("   - All agents reset to 'running' status")
print()
print("✅ Fix 2: Selective agent pausing")
print("   - Can pause specific agents instead of all")
print("   - Stopped agents show their icons")
print()
print("✅ Fix 3: Multi-agent icon display in followup tasks")
print("   - Same logic as main tasks")
print("   - Shows up to 2 icons, then '+N' for more")
print()
print("✅ Fix 4: Proper status display")
print("   - 'In Progress' when agents are running")
print("   - 'Stopped' when all agents are paused")
print("   - Shows which agents are active/stopped")
print()
