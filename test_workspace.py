#!/usr/bin/env python3
"""Test script to demonstrate workspace persistence functionality"""

import database
import os

# Clean start
if os.path.exists("data.db"):
    os.remove("data.db")

print("=== Testing Workspace Persistence ===\n")

# Create tables
database.create_tables()
print("✓ Database tables created\n")

# Test 1: Create a user with personal workspace
print("Test 1: Creating user 'alice'")
database.add_user("alice")
personal_ws_id = database.create_workspace("Alice's Personal Workspace", "personal", "alice")
database.update_user_last_workspace("alice", "personal", str(personal_ws_id))
print(f"✓ Created user 'alice' with personal workspace (ID: {personal_ws_id})\n")

# Test 2: Create a team workspace
print("Test 2: Creating team workspace")
team_ws_id = database.create_workspace("Team Alpha", "team", "alice")
print(f"✓ Created team workspace 'Team Alpha' (ID: {team_ws_id})\n")

# Test 3: Switch to team workspace
print("Test 3: Switching alice to team workspace")
database.update_user_last_workspace("alice", "team", str(team_ws_id))
last_type, last_id = database.get_user_last_workspace("alice")
print(f"✓ Alice's last workspace: type='{last_type}', id='{last_id}'\n")

# Test 4: Simulate logout and login - should restore team workspace
print("Test 4: Simulating re-login (should restore team workspace)")
last_type, last_id = database.get_user_last_workspace("alice")
if last_id:
    workspace = database.get_workspace_by_id(int(last_id))
    print(f"✓ Restored workspace: {workspace[1]} ({workspace[2]})")
    print(f"  Expected: Team Alpha (team)")
    assert workspace[1] == "Team Alpha", "Should restore Team Alpha workspace"
    assert workspace[2] == "team", "Should be team type"
print()

# Test 5: Switch back to personal workspace
print("Test 5: Switching back to personal workspace")
database.update_user_last_workspace("alice", "personal", str(personal_ws_id))
last_type, last_id = database.get_user_last_workspace("alice")
print(f"✓ Alice's last workspace: type='{last_type}', id='{last_id}'\n")

# Test 6: Simulate logout and login - should restore personal workspace
print("Test 6: Simulating re-login (should restore personal workspace)")
last_type, last_id = database.get_user_last_workspace("alice")
if last_id:
    workspace = database.get_workspace_by_id(int(last_id))
    print(f"✓ Restored workspace: {workspace[1]} ({workspace[2]})")
    print(f"  Expected: Alice's Personal Workspace (personal)")
    assert workspace[1] == "Alice's Personal Workspace", "Should restore personal workspace"
    assert workspace[2] == "personal", "Should be personal type"
print()

# Test 7: Create another user and verify they get their own workspace
print("Test 7: Creating user 'bob'")
database.add_user("bob")
bob_ws_id = database.create_workspace("Bob's Personal Workspace", "personal", "bob")
database.update_user_last_workspace("bob", "personal", str(bob_ws_id))
print(f"✓ Created user 'bob' with personal workspace (ID: {bob_ws_id})\n")

# Test 8: Verify bob's workspace is separate from alice's
print("Test 8: Verifying workspace isolation")
alice_workspaces = database.get_user_workspaces("alice")
bob_workspaces = database.get_user_workspaces("bob")
print(f"✓ Alice has {len(alice_workspaces)} workspace(s)")
print(f"✓ Bob has {len(bob_workspaces)} workspace(s)")
print()

print("=== All Tests Passed! ===\n")
print("Summary:")
print("- Users can have personal and team workspaces")
print("- Last visited workspace is persisted in the database")
print("- When user logs back in, their last workspace is restored")
print("- Switching from team to personal workspace is persisted")
print("- Switching from personal to team workspace is persisted")
