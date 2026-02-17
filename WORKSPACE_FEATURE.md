# Workspace Persistence Feature

## Overview
This feature implements workspace persistence for the movie watchlist application, allowing users to work in both personal and team workspaces. The application now remembers which workspace a user was last using and automatically restores it when they log back in.

## Key Features

### 1. **Workspace Types**
- **Personal Workspace**: Each user gets their own personal workspace by default
- **Team Workspace**: Users can create and join team workspaces for collaboration

### 2. **Workspace Persistence**
- When a user selects a workspace (personal or team), that selection is saved to the database
- Upon re-login or revisit, the user's last active workspace is automatically restored
- If the user was in a team workspace, they return to that team workspace
- If the user was in their personal workspace, they return to their personal workspace

### 3. **User Experience**
- Login required on app start
- Automatic workspace restoration based on last session
- Easy workspace switching via menu option
- Ability to create new workspaces

## Database Schema Changes

### Modified Tables

#### `users` table
```sql
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    last_workspace_type TEXT DEFAULT 'personal',  -- NEW
    last_workspace_id TEXT                        -- NEW
);
```

### New Tables

#### `workspaces` table
```sql
CREATE TABLE workspaces (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('personal', 'team')),
    owner_username TEXT,
    FOREIGN KEY(owner_username) REFERENCES users(username)
);
```

#### `workspace_members` table
```sql
CREATE TABLE workspace_members (
    workspace_id INTEGER,
    username TEXT,
    FOREIGN KEY(workspace_id) REFERENCES workspaces(id),
    FOREIGN KEY(username) REFERENCES users(username),
    PRIMARY KEY(workspace_id, username)
);
```

## New Database Functions

### Workspace Management
- `create_workspace(name, workspace_type, owner_username)` - Create a new workspace
- `get_user_workspaces(username)` - Get all workspaces accessible to a user
- `get_workspace_by_id(workspace_id)` - Get workspace details by ID
- `add_workspace_member(workspace_id, username)` - Add a member to a team workspace

### Persistence Functions
- `update_user_last_workspace(username, workspace_type, workspace_id)` - Save user's current workspace
- `get_user_last_workspace(username)` - Retrieve user's last active workspace

## Application Flow

### 1. **First Time User**
```
1. User starts app
2. Prompted to login
3. User creates new account (option 6)
4. Personal workspace automatically created
5. User is logged in with personal workspace active
```

### 2. **Returning User - Last Used Personal Workspace**
```
1. User starts app
2. User logs in with username
3. System retrieves last workspace (personal)
4. Personal workspace is restored
5. Message: "Restored your last workspace: [Name] (personal)"
```

### 3. **Returning User - Last Used Team Workspace**
```
1. User starts app
2. User logs in with username
3. System retrieves last workspace (team)
4. Team workspace is restored
5. Message: "Restored your last workspace: [Name] (team)"
```

### 4. **Switching Workspaces**
```
1. User selects option 8 (Switch workspace)
2. System displays all available workspaces
3. User enters workspace ID
4. System switches to selected workspace
5. Last workspace preference is updated in database
```

## Menu Options

The application menu has been updated:

```
1) Add new movie
2) View upcoming movies
3) View all movies
4) Add watched movie
5) View watched movies
6) Add user to the app
7) Search for a movie
8) Switch workspace          [NEW]
9) Create workspace          [NEW]
10) Exit
```

## Usage Examples

### Creating a Team Workspace
```
Your selection: 9
Enter workspace name: Marketing Team
Enter workspace type (personal/team): team
Workspace 'Marketing Team' created successfully! (ID: 2)
Switch to this workspace now? (y/n): y
Switched to workspace: Marketing Team
```

### Switching Between Workspaces
```
Your selection: 8

-- Available Workspaces --
1: Alice's Personal Workspace (personal) 
2: Marketing Team (team) CURRENT
----

Enter workspace ID to switch to: 1
Switched to workspace: Alice's Personal Workspace (personal)
```

### Login with Workspace Restoration
```
Welcome to the watchlist app!

--- Login Required ---
Enter your username to login: alice

Welcome back, alice!
Restored your last workspace: Marketing Team (team)
```

## Testing

Run the automated test suite to verify workspace persistence:

```bash
python3 test_workspace.py
```

The test suite validates:
- User creation with personal workspace
- Team workspace creation
- Workspace switching (personal → team)
- Workspace persistence after simulated logout/login
- Workspace switching (team → personal)
- Workspace isolation between users

## Implementation Details

### Key Changes in `database.py`
- Added workspace-related SQL queries and table definitions
- Implemented lazy connection initialization with `get_connection()`
- Added functions for workspace CRUD operations
- Added functions for tracking user's last workspace

### Key Changes in `app.py`
- Added global variables for `current_workspace` and `current_user`
- Implemented `prompt_login()` for user authentication and workspace restoration
- Implemented `prompt_switch_workspace()` for workspace switching
- Implemented `prompt_create_workspace()` for creating new workspaces
- Modified `prompt_add_user()` to create default personal workspace
- Updated menu to include workspace options (8 and 9)
- Changed exit option from 8 to 10

## Migration Notes

**Important**: If you have an existing `data.db` file, you need to delete it and let the application recreate it with the new schema:

```bash
rm data.db
python3 app.py
```

This will create a fresh database with all the new workspace tables and columns.

## Future Enhancements

Potential improvements for this feature:
1. Add workspace member management (invite/remove users from team workspaces)
2. Implement workspace-scoped movie lists (movies visible only within a workspace)
3. Add workspace permissions (admin, member, viewer roles)
4. Implement workspace activity logs
5. Add workspace settings and customization options
