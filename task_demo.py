import datetime
import database

def print_task_status(task_id, label="Task Status"):
    """Print task status with agent information"""
    status_info = database.get_task_status_with_agents(task_id)
    if status_info:
        print(f"\n{label}:")
        print(f"  Task ID: {status_info['task_id']}")
        print(f"  Title: {status_info['title']}")
        print(f"  Display Status: {status_info['status']}")
        print(f"  Actual Status: {status_info['actual_status']}")
        print(f"  Is Follow-up: {status_info['is_followup']}")

        if status_info['active_agents']:
            print(f"  Active Agents ({len(status_info['active_agents'])}):")
            for agent in status_info['active_agents']:
                print(f"    - {agent[2]} ({agent[3]}) - {agent[4]}")

        if status_info['stopped_agents']:
            print(f"  Stopped Agents ({len(status_info['stopped_agents'])}):")
            for agent in status_info['stopped_agents']:
                print(f"    - {agent[2]} ({agent[3]}) - {agent[4]}")


def demo_task_workflow():
    """Demonstrate task and follow-up task workflow with status updates"""
    print("=" * 60)
    print("TASK MANAGEMENT DEMO - Status Updates & Agent Tracking")
    print("=" * 60)

    # Create tables
    database.create_tables()

    # Scenario 1: Main task with follow-up
    print("\n--- SCENARIO 1: Main Task with Follow-up ---")

    # Create main task
    main_task_id = database.add_task(
        "Implement User Authentication",
        "Add login and registration functionality",
        status='pending'
    )
    print(f"\n1. Created main task (ID: {main_task_id})")
    print_task_status(main_task_id, "Initial Status")

    # Start main task with agents
    database.update_task_status(main_task_id, 'in_progress')
    agent1_id = database.add_agent(main_task_id, "Backend Agent", "🔧", "running")
    agent2_id = database.add_agent(main_task_id, "Frontend Agent", "🎨", "running")
    print("\n2. Started main task with 2 agents")
    print_task_status(main_task_id, "Status with Active Agents")

    # Complete main task
    database.update_task_status(main_task_id, 'completed')
    print("\n3. Completed main task")
    print_task_status(main_task_id, "Completed Status")

    # Create follow-up task
    followup_task_id = database.add_task(
        "Add Password Reset Feature",
        "Implement forgot password flow",
        status='pending',
        parent_task_id=main_task_id,
        is_followup=True
    )
    print(f"\n4. Created follow-up task (ID: {followup_task_id})")
    print_task_status(followup_task_id, "Follow-up Initial Status")

    # Mark follow-up as completed initially
    database.update_task_status(followup_task_id, 'completed')
    print("\n5. Marked follow-up as completed")
    print_task_status(followup_task_id, "Follow-up Completed")

    # Start follow-up task (THIS IS THE BUG FIX - status should update)
    print("\n6. Starting follow-up task (status should change from 'completed' to 'in_progress')")
    database.update_task_status(followup_task_id, 'in_progress')
    followup_agent1 = database.add_agent(followup_task_id, "Email Agent", "📧", "running")
    followup_agent2 = database.add_agent(followup_task_id, "Database Agent", "💾", "running")
    print_task_status(followup_task_id, "Follow-up Restarted Status")

    # Scenario 2: Selective agent pause
    print("\n\n--- SCENARIO 2: Selective Agent Pause ---")

    task2_id = database.add_task(
        "Build API Endpoints",
        "Create REST API for the application",
        status='in_progress'
    )

    api_agent1 = database.add_agent(task2_id, "Auth API Agent", "🔐", "running")
    api_agent2 = database.add_agent(task2_id, "Data API Agent", "📊", "running")
    api_agent3 = database.add_agent(task2_id, "Upload API Agent", "📤", "running")

    print(f"\n1. Created task with 3 agents (ID: {task2_id})")
    print_task_status(task2_id, "All Agents Running")

    # Pause selective agents
    print("\n2. Pausing 2 out of 3 agents")
    database.pause_agent(api_agent1)
    database.pause_agent(api_agent2)
    print_task_status(task2_id, "Status with Partial Pause")

    # Pause all agents
    print("\n3. Pausing all agents")
    database.pause_agent(api_agent3)
    print_task_status(task2_id, "Status with All Stopped (shows 'stopped')")

    # Scenario 3: Multi-agent icon display
    print("\n\n--- SCENARIO 3: Multi-Agent Icon Display ---")

    task3_id = database.add_task(
        "Implement Dashboard",
        "Create analytics dashboard",
        status='in_progress'
    )

    dash_agent1 = database.add_agent(task3_id, "Chart Agent", "📈", "running")
    dash_agent2 = database.add_agent(task3_id, "Widget Agent", "🎯", "running")

    status_info = database.get_task_status_with_agents(task3_id)
    print(f"\n1. Task with 2 active agents:")
    print(f"   Status: {status_info['status']}")
    print(f"   Agent Icons: ", end="")
    for agent in status_info['active_agents']:
        print(f"{agent[3]} ", end="")
    print(f"\n   Agent Count: {status_info['agent_count']}")

    # Stop one agent
    database.pause_agent(dash_agent1)
    status_info = database.get_task_status_with_agents(task3_id)
    print(f"\n2. After stopping one agent:")
    print(f"   Status: {status_info['status']}")
    print(f"   Active Icons: ", end="")
    for agent in status_info['active_agents']:
        print(f"{agent[3]} ", end="")
    print(f"\n   Stopped Icons: ", end="")
    for agent in status_info['stopped_agents']:
        print(f"{agent[3]} ", end="")
    print(f"\n   Total Agent Count: {status_info['agent_count']}")

    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    demo_task_workflow()
