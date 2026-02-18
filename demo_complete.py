#!/usr/bin/env python3
"""
Complete demonstration of the Multi-Agent Task Manager
Shows all features including:
1. Main task creation
2. Followup task creation after main task completion
3. Multi-agent assignment
4. Selective agent pausing
5. Status updates and display
6. Agent icon logic
"""

import task_manager as tm
import task_database as db
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def pause_for_user():
    """Wait for user to press Enter"""
    input("\nPress Enter to continue...")

def main():
    # Initialize clean database
    if os.path.exists('tasks.db'):
        os.remove('tasks.db')
    
    manager = tm.TaskManager()
    
    clear_screen()
    print("=" * 80)
    print(" " * 20 + "MULTI-AGENT TASK MANAGER DEMO")
    print("=" * 80)
    print("\nThis demo will demonstrate all key features:")
    print("  1. Main task creation and multi-agent assignment")
    print("  2. Selective agent pausing (pause icon feature)")
    print("  3. Task completion and followup task creation")
    print("  4. Followup task status reset and agent management")
    print("  5. Smart agent icon display logic")
    pause_for_user()
    
    # ============================================================================
    # PART 1: Main Task with Multiple Agents
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 1: Creating Main Task with Multiple Agents")
    print("=" * 80)
    
    print("\n📋 Creating main task: 'Implement User Authentication'")
    task1 = manager.create_main_task(
        "Implement User Authentication",
        "Add login, signup, and session management"
    )
    
    print(f"✅ Task #{task1} created successfully!")
    print("\n📊 Current status:")
    manager.print_task_tree()
    pause_for_user()
    
    # ============================================================================
    # PART 2: Starting Task with Agents
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 2: Starting Task with 3 Agents")
    print("=" * 80)
    
    print("\n🚀 Starting task with agents: Alpha, Beta, Gamma")
    manager.start_task(task1, ["Agent-Alpha", "Agent-Beta", "Agent-Gamma"])
    
    print("\n📊 Status after starting (all agents running):")
    manager.print_task_tree()
    
    print("\n💡 Notice:")
    print("  - Status shows 'In Progress' with all agent names")
    print("  - Three running agent icons (🤖) are displayed")
    print("  - Each agent shows individual status")
    pause_for_user()
    
    # ============================================================================
    # PART 3: Selective Agent Pausing (Key Feature)
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 3: Selective Agent Pausing (Pause Icon Feature)")
    print("=" * 80)
    
    print("\n⏸️  Pausing 2 out of 3 agents (Alpha and Beta)")
    print("   This demonstrates the selective pause feature!")
    
    status = manager.get_task_status(task1)
    agents_to_pause = [
        status['agents'][0]['agent_id'],  # Agent-Alpha
        status['agents'][1]['agent_id']   # Agent-Beta
    ]
    manager.pause_agents(task1, agents_to_pause)
    
    print("\n📊 Status after pausing 2 agents:")
    manager.print_task_tree()
    
    print("\n💡 Key observations:")
    print("  ✓ Status still shows 'In Progress' (because Gamma is still running)")
    print("  ✓ Shows '(Agent-Gamma)' - only the running agent")
    print("  ✓ Stopped agents show pause icon (⏸️)")
    print("  ✓ Running agent shows robot icon (🤖)")
    pause_for_user()
    
    # ============================================================================
    # PART 4: Pausing All Agents
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 4: Pausing All Agents")
    print("=" * 80)
    
    print("\n⏸️  Pausing ALL remaining agents")
    manager.pause_agents(task1)  # Pause all
    
    print("\n📊 Status after pausing all agents:")
    manager.print_task_tree()
    
    print("\n💡 Key observations:")
    print("  ✓ Status changed to 'Stopped (3 agents)'")
    print("  ✓ All three pause icons (⏸️) are displayed")
    print("  ✓ Task is effectively paused but not completed")
    pause_for_user()
    
    # ============================================================================
    # PART 5: Completing Main Task
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 5: Completing Main Task")
    print("=" * 80)
    
    print("\n✅ Marking task as completed")
    manager.complete_task(task1)
    
    print("\n📊 Status after completion:")
    manager.print_task_tree()
    
    print("\n💡 Key observations:")
    print("  ✓ Status shows 'Completed'")
    print("  ✓ All agents are stopped")
    print("  ✓ Main task is now finished")
    pause_for_user()
    
    # ============================================================================
    # PART 6: Creating Followup Task (Critical Feature)
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 6: Creating Followup Task (Status Reset Feature)")
    print("=" * 80)
    
    print("\n📋 Creating followup task: 'Add Password Reset Feature'")
    print("   Parent task (#1) is completed, but followup should start fresh!")
    
    followup1 = manager.create_followup_task(
        task1,
        "Add Password Reset Feature",
        "Implement email-based password reset"
    )
    
    print(f"\n✅ Followup task #{followup1} created successfully!")
    print("\n📊 Current status:")
    manager.print_task_tree()
    
    print("\n💡 Key observation:")
    print("  ✓ Followup task starts with 'Pending' status")
    print("  ✓ NOT inherited 'Completed' status from parent")
    print("  ✓ This is the status reset feature in action!")
    pause_for_user()
    
    # ============================================================================
    # PART 7: Starting Followup Task with New Agents
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 7: Starting Followup Task with Different Agents")
    print("=" * 80)
    
    print("\n🚀 Starting followup task with agents: Delta, Epsilon")
    manager.start_task(followup1, ["Agent-Delta", "Agent-Epsilon"])
    
    print("\n📊 Full task tree:")
    manager.print_task_tree()
    
    print("\n💡 Key observations:")
    print("  ✓ Main task remains 'Completed'")
    print("  ✓ Followup task is 'In Progress' with new agents")
    print("  ✓ Each task maintains independent agent sets")
    print("  ✓ Tree structure shows parent-child relationship")
    pause_for_user()
    
    # ============================================================================
    # PART 8: Selective Pause in Followup Task
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 8: Demonstrating Selective Pause in Followup Task")
    print("=" * 80)
    
    print("\n⏸️  Pausing only Agent-Delta (1 out of 2 agents)")
    followup_status = manager.get_task_status(followup1)
    manager.pause_agents(followup1, [followup_status['agents'][0]['agent_id']])
    
    print("\n📊 Final status:")
    manager.print_task_tree()
    
    print("\n💡 Key observations:")
    print("  ✓ Followup task still 'In Progress' (Epsilon running)")
    print("  ✓ Shows '(Agent-Epsilon)' - only active agent")
    print("  ✓ Delta shows pause icon (⏸️)")
    print("  ✓ Same multi-agent logic works in followup tasks!")
    pause_for_user()
    
    # ============================================================================
    # PART 9: Creating Second Followup Task
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print("PART 9: Multiple Followup Tasks")
    print("=" * 80)
    
    print("\n📋 Creating second followup task: 'Add Two-Factor Authentication'")
    followup2 = manager.create_followup_task(
        task1,
        "Add Two-Factor Authentication",
        "Implement TOTP-based 2FA"
    )
    
    print("\n🚀 Starting with 4 agents to show icon limit feature")
    manager.start_task(followup2, [
        "Agent-Zeta",
        "Agent-Eta",
        "Agent-Theta",
        "Agent-Iota"
    ])
    
    print("\n📊 Complete task tree:")
    manager.print_task_tree()
    
    print("\n💡 Key observations:")
    print("  ✓ Multiple followup tasks under same parent")
    print("  ✓ Each followup maintains independent status")
    print("  ✓ Icon display shows up to 5 agents (currently 4)")
    pause_for_user()
    
    # ============================================================================
    # SUMMARY
    # ============================================================================
    clear_screen()
    print("\n" + "=" * 80)
    print(" " * 25 + "DEMO SUMMARY")
    print("=" * 80)
    
    print("\n✅ ALL FEATURES SUCCESSFULLY DEMONSTRATED:")
    print("\n1. ✓ Multi-Agent Task Management")
    print("   - Created tasks with multiple agents")
    print("   - Each agent tracked individually")
    
    print("\n2. ✓ Selective Agent Pausing (PAUSE ICON FEATURE)")
    print("   - Paused individual agents while others continued")
    print("   - Paused all agents on a task")
    print("   - Proper status updates based on agent states")
    
    print("\n3. ✓ Followup Task Status Reset")
    print("   - Followup tasks start with 'Pending' status")
    print("   - Don't inherit parent's 'Completed' status")
    print("   - Status properly updates when followup starts")
    
    print("\n4. ✓ Agent Icon Display Logic")
    print("   - Running agents show 🤖 icon")
    print("   - Stopped agents show ⏸️ icon")
    print("   - Status label shows active agent names")
    print("   - 'Stopped (X agents)' when all paused")
    
    print("\n5. ✓ Multi-Agent Icon Logic in Followups")
    print("   - Same pause/resume logic works in followup tasks")
    print("   - Independent agent management per task")
    print("   - Clear visual distinction between running/stopped")
    
    print("\n" + "=" * 80)
    print("\n📊 Final state of all tasks:")
    print("=" * 80)
    manager.print_task_tree()
    
    print("\n" + "=" * 80)
    print("Demo completed! Database saved as 'tasks.db'")
    print("Run 'python3 web_app.py' to see the web interface")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
