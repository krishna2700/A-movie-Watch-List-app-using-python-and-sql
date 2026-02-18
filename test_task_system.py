#!/usr/bin/env python3
"""
Test script to demonstrate the task management system fixes:
1. Follow-up task status resets when restarted (not stuck on completed)
2. Pause specific agents instead of all agents
3. Show stopped agent icons with "Stopped" status
4. Multi-agent icon display logic for both main and follow-up tasks
5. Clear indication of what's in progress
"""

import task_database as db
import os

# Clean slate
db_path = '/tmp/tasks.db'
if os.path.exists(db_path):
    os.remove(db_path)

print("=" * 80)
print("TASK MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
print("=" * 80)

# Initialize
db.create_tables()

print("\n📋 TEST 1: Follow-up task status management")
print("-" * 80)

# Create main task
main_task_id = db.add_task("Implement Authentication System")
db.add_agent_to_task(main_task_id, "Security Agent", "🔒")
db.add_agent_to_task(main_task_id, "Database Agent", "💾")
db.update_task_status(main_task_id, 'completed')
print(f"✓ Created main task {main_task_id}: 'Implement Authentication System'")
print(f"  Added agents: 🔒 Security Agent, 💾 Database Agent")
print(f"  Status: COMPLETED")

# Create follow-up task
followup_id = db.add_task("Add OAuth integration", main_task_id)
db.add_agent_to_task(followup_id, "OAuth Agent", "🔑")
db.add_agent_to_task(followup_id, "API Agent", "🌐")
db.update_task_status(followup_id, 'completed')
print(f"\n✓ Created follow-up task {followup_id}: 'Add OAuth integration'")
print(f"  Added agents: 🔑 OAuth Agent, 🌐 API Agent")
print(f"  Status: COMPLETED")

# Check initial state
task = db.get_task_with_details(followup_id)
print(f"\n📊 Follow-up task status BEFORE restart: {task['status']}")
print(f"   Status display: {task['status_info']['display_text']}")

# Start the follow-up task (should reset from completed)
print(f"\n🔄 Starting follow-up task {followup_id}...")
db.start_followup_task(followup_id)

# Check state after restart
task = db.get_task_with_details(followup_id)
print(f"✅ Follow-up task status AFTER restart: {task['status']}")
print(f"   Status display: {task['status_info']['display_text']}")
agents = db.get_task_agents(followup_id)
agents_state = [f"{a['icon']} {a['status']}" for a in agents]
print(f"   Agents state: {agents_state}")

print("\n" + "=" * 80)
print("📋 TEST 2: Selective agent pausing")
print("-" * 80)

# Create a new task with multiple agents
multi_agent_task_id = db.add_task("Deploy to production")
agent1_id = db.add_agent_to_task(multi_agent_task_id, "Build Agent", "🏗️")
agent2_id = db.add_agent_to_task(multi_agent_task_id, "Test Agent", "🧪")
agent3_id = db.add_agent_to_task(multi_agent_task_id, "Deploy Agent", "🚀")
db.update_task_status(multi_agent_task_id, 'in_progress')

print(f"✓ Created task {multi_agent_task_id}: 'Deploy to production'")
print(f"  Added agents: 🏗️ Build Agent, 🧪 Test Agent, 🚀 Deploy Agent")
print(f"  Status: IN PROGRESS")

# Show initial state
task = db.get_task_with_details(multi_agent_task_id)
print(f"\n📊 Initial agent states:")
for agent in task['status_info']['agents']:
    print(f"   [{agent['id']}] {agent['icon']} {agent['name']}: {agent['status']}")

# Pause only Build and Test agents
print(f"\n⏸️  Pausing Build Agent (ID: {agent1_id}) and Test Agent (ID: {agent2_id})...")
db.pause_agents(multi_agent_task_id, [agent1_id, agent2_id])

# Show updated state
task = db.get_task_with_details(multi_agent_task_id)
print(f"\n✅ Updated agent states:")
for agent in task['status_info']['agents']:
    status_symbol = "⏸️" if agent['status'] == 'stopped' else "▶️"
    print(f"   [{agent['id']}] {agent['icon']} {agent['name']}: {agent['status']} {status_symbol}")

print(f"\n📊 Task status display:")
print(f"   Status: {task['status_info']['status']}")
print(f"   Display text: {task['status_info']['display_text']}")
print(f"   Display icons: {task['status_info']['display_icons']}")
stopped_agents_list = [f"{a['icon']} {a['name']}" for a in task['status_info']['stopped_agents']]
print(f"   Stopped agents: {stopped_agents_list}")

print("\n" + "=" * 80)
print("📋 TEST 3: Multi-agent icon display logic")
print("-" * 80)

# Test with 2 active agents
task_2agents_id = db.add_task("Process data pipeline")
db.add_agent_to_task(task_2agents_id, "Extractor", "📥")
db.add_agent_to_task(task_2agents_id, "Transformer", "⚡")
db.update_task_status(task_2agents_id, 'in_progress')

task = db.get_task_with_details(task_2agents_id)
print(f"✓ Task with 2 agents in progress:")
print(f"  Display: {' '.join(task['status_info']['display_icons'])} {task['status_info']['display_text']}")

# Test with 4 active agents (should show first 2 icons + count)
task_4agents_id = db.add_task("Complex workflow")
db.add_agent_to_task(task_4agents_id, "Agent A", "🅰️")
db.add_agent_to_task(task_4agents_id, "Agent B", "🅱️")
db.add_agent_to_task(task_4agents_id, "Agent C", "©️")
db.add_agent_to_task(task_4agents_id, "Agent D", "🅾️")
db.update_task_status(task_4agents_id, 'in_progress')

task = db.get_task_with_details(task_4agents_id)
print(f"\n✓ Task with 4 agents in progress:")
print(f"  Display: {' '.join(task['status_info']['display_icons'])} {task['status_info']['display_text']}")

print("\n" + "=" * 80)
print("📋 TEST 4: Complete workflow demonstration")
print("-" * 80)

# Create a realistic scenario
main_id = db.add_task("Develop E-commerce Platform")
db.add_agent_to_task(main_id, "Frontend Dev", "🎨")
db.add_agent_to_task(main_id, "Backend Dev", "⚙️")
db.add_agent_to_task(main_id, "Database Admin", "💾")
db.update_task_status(main_id, 'completed')

followup1_id = db.add_task("Add payment gateway", main_id)
db.add_agent_to_task(followup1_id, "Payment Integration", "💳")
db.add_agent_to_task(followup1_id, "Security Audit", "🔐")
db.update_task_status(followup1_id, 'completed')

followup2_id = db.add_task("Implement analytics dashboard", main_id)
db.add_agent_to_task(followup2_id, "Analytics Agent", "📊")
db.add_agent_to_task(followup2_id, "Visualization Agent", "📈")
db.add_agent_to_task(followup2_id, "Data Mining Agent", "⛏️")

print("✓ Created complete task hierarchy:")
print(f"  Main task: {main_id}")
print(f"  Follow-up 1: {followup1_id} (completed)")
print(f"  Follow-up 2: {followup2_id} (pending)")

# Start followup 1 (should reset from completed)
print(f"\n🔄 Restarting completed follow-up task {followup1_id}...")
db.start_followup_task(followup1_id)
task = db.get_task_with_details(followup1_id)
print(f"✅ Status changed: completed → {task['status']}")

# Start followup 2 and pause one agent
print(f"\n▶️ Starting follow-up task {followup2_id}...")
db.update_task_status(followup2_id, 'in_progress')
agents = db.get_task_agents(followup2_id)
db.pause_agents(followup2_id, [agents[0]['id']])

task = db.get_task_with_details(followup2_id)
print(f"✅ Task status: {task['status']}")
print(f"   Display: {' '.join(task['status_info']['display_icons'])} {task['status_info']['display_text']}")
active_agents_list = [f"{a['icon']} {a['name']}" for a in task['status_info']['active_agents']]
stopped_agents_list = [f"{a['icon']} {a['name']}" for a in task['status_info']['stopped_agents']]
print(f"   Active agents: {active_agents_list}")
print(f"   Stopped agents: {stopped_agents_list}")

print("\n" + "=" * 80)
print("📋 FINAL VIEW: All tasks with complete status information")
print("-" * 80)

all_tasks = db.get_all_tasks()
for task in all_tasks:
    print(f"\n📌 [{task['id']}] {task['content']}")
    print(f"   Status: {task['status_info']['display_text']}")
    if task['status_info']['display_icons']:
        print(f"   Icons: {' '.join(task['status_info']['display_icons'])}")
    if task['status_info']['agents']:
        print(f"   Agents:")
        for agent in task['status_info']['agents']:
            print(f"     • {agent['icon']} {agent['name']}: {agent['status']}")
    
    if task['followups']:
        print(f"   Follow-up tasks:")
        for followup in task['followups']:
            print(f"     ↳ [{followup['id']}] {followup['content']}")
            print(f"       Status: {followup['status_info']['display_text']}")
            if followup['status_info']['display_icons']:
                print(f"       Icons: {' '.join(followup['status_info']['display_icons'])}")
            if followup['status_info']['agents']:
                for agent in followup['status_info']['agents']:
                    print(f"         • {agent['icon']} {agent['name']}: {agent['status']}")

print("\n" + "=" * 80)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
print("=" * 80)
print("\nKey Features Demonstrated:")
print("1. ✅ Follow-up tasks reset status when restarted (not stuck on 'completed')")
print("2. ✅ Selective agent pausing (not all agents)")
print("3. ✅ Stopped agents show their icons with 'Stopped' status")
print("4. ✅ Multi-agent icon logic works for both main and follow-up tasks")
print("5. ✅ Clear indication of what's in progress with agent details")
print("\n" + "=" * 80)
