import datetime
import database


welcome = "Welcome to the watchlist app!"


def get_menu(workspace_name):
    return f"""
--- Current Workspace: [{workspace_name}] ---

Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Add watched movie.
5) View watched movies.
6) Search for a movie.
7) Switch workspace.
8) Create team workspace.
9) Add member to team workspace.
10) View workspace members.
11) Exit.

Your selection: """


def prompt_login():
    """Prompt user to login or register. Returns (username, workspace)."""
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    if not username:
        print("Username cannot be empty!")
        return prompt_login()

    if database.user_exists(username):
        print(f"Welcome back, {username}!")
        # Retrieve the last visited workspace
        workspace = database.get_last_workspace(username)
        if workspace:
            ws_type = "Personal" if workspace[2] == "personal" else "Team"
            print(f"Restoring your last workspace: {workspace[1]} ({ws_type})")
        else:
            # Fallback: find their personal workspace
            workspaces = database.get_user_workspaces(username)
            workspace = workspaces[0] if workspaces else None
            if workspace:
                database.update_last_workspace(username, workspace[0])
                print(f"Opening your personal workspace: {workspace[1]}")
            else:
                print("Error: No workspace found. Please contact support.")
                return prompt_login()
    else:
        register = input("User not found. Register as new user? (y/n): ").strip().lower()
        if register == "y":
            database.add_user(username)
            print(f"User '{username}' created with a personal workspace!")
            workspace = database.get_last_workspace(username)
        else:
            print("Goodbye!")
            return None, None

    return username, workspace


def prompt_add_movie(workspace_id):
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    movie_id = database.add_movie_to_workspace(workspace_id, title, release_timestamp)
    print(f"Movie '{title}' added to workspace (ID: {movie_id}).")


def print_movie_list(heading, movies):
    print(f"\n-- {heading} movies --")
    if not movies:
        print("No movies found.")
    else:
        for movie in movies:
            movie_date = datetime.datetime.fromtimestamp(movie[2])
            human_date = movie_date.strftime("%b %d %Y")
            print(f"  {movie[0]}: {movie[1]} (on {human_date})")
    print("----\n")


def prompt_watch_movie(workspace_id, username):
    movie_id = input("Movie ID: ").strip()
    if not movie_id.isdigit():
        print("Invalid movie ID!")
        return
    database.watch_movie_in_workspace(workspace_id, username, int(movie_id))
    print("Movie marked as watched!")


def prompt_search_movies(workspace_id):
    search_term = input("Enter partial movie title: ")
    return database.search_workspace_movies(workspace_id, search_term)


def prompt_switch_workspace(username):
    """Show available workspaces and let user switch. Returns new workspace or None."""
    workspaces = database.get_user_workspaces(username)
    if not workspaces:
        print("No workspaces available.")
        return None

    print("\n--- Your Workspaces ---")
    for ws in workspaces:
        ws_type = "Personal" if ws[2] == "personal" else "Team"
        print(f"  {ws[0]}) {ws[1]} ({ws_type}) - Owner: {ws[3]}")
    print("---")

    choice = input("Enter workspace ID to switch to (or press Enter to cancel): ").strip()
    if not choice or not choice.isdigit():
        print("Cancelled.")
        return None

    workspace_id = int(choice)
    # Verify user has access to this workspace
    valid_ids = [ws[0] for ws in workspaces]
    if workspace_id not in valid_ids:
        print("You don't have access to that workspace!")
        return None

    workspace = database.get_workspace(workspace_id)
    if workspace:
        database.update_last_workspace(username, workspace_id)
        ws_type = "Personal" if workspace[2] == "personal" else "Team"
        print(f"Switched to workspace: {workspace[1]} ({ws_type})")
    return workspace


def prompt_create_team_workspace(username):
    """Create a new team workspace."""
    name = input("Team workspace name: ").strip()
    if not name:
        print("Workspace name cannot be empty!")
        return None

    workspace_id = database.create_team_workspace(name, username)
    print(f"Team workspace '{name}' created (ID: {workspace_id}).")
    # Automatically switch to the new workspace
    workspace = database.get_workspace(workspace_id)
    database.update_last_workspace(username, workspace_id)
    print(f"Switched to new team workspace: {name}")
    return workspace


def prompt_add_member(workspace_id, workspace):
    """Add a member to the current team workspace."""
    if workspace[2] != "team":
        print("You can only add members to team workspaces!")
        return

    member_username = input("Username to add: ").strip()
    if not member_username:
        print("Username cannot be empty!")
        return

    if not database.user_exists(member_username):
        print(f"User '{member_username}' does not exist!")
        return

    members = database.get_workspace_members(workspace_id)
    if member_username in members:
        print(f"User '{member_username}' is already a member!")
        return

    database.add_workspace_member(workspace_id, member_username)
    print(f"User '{member_username}' added to workspace '{workspace[1]}'.")


def prompt_view_members(workspace_id, workspace):
    """View members of the current workspace."""
    members = database.get_workspace_members(workspace_id)
    ws_type = "Personal" if workspace[2] == "personal" else "Team"
    print(f"\n--- Members of '{workspace[1]}' ({ws_type}) ---")
    for member in members:
        owner_tag = " (owner)" if member == workspace[3] else ""
        print(f"  - {member}{owner_tag}")
    print("---\n")


# --- Main App ---

print(welcome)
database.create_tables()

username, current_workspace = prompt_login()

if username is None:
    exit()

# current_workspace is a tuple: (id, name, type, owner_username)
workspace_id = current_workspace[0]
workspace_name = current_workspace[1]

while (user_input := input(get_menu(workspace_name))) != "11":
    if user_input == "1":
        prompt_add_movie(workspace_id)

    elif user_input == "2":
        movies = database.get_workspace_movies(workspace_id, upcoming=True)
        print_movie_list("Upcoming", movies)

    elif user_input == "3":
        movies = database.get_workspace_movies(workspace_id)
        print_movie_list("All", movies)

    elif user_input == "4":
        prompt_watch_movie(workspace_id, username)

    elif user_input == "5":
        movies = database.get_workspace_watched_movies(workspace_id, username)
        if movies:
            print_movie_list("Watched", movies)
        else:
            print("No watched movies in this workspace yet!")

    elif user_input == "6":
        movies = prompt_search_movies(workspace_id)
        if movies:
            print_movie_list("Movies found", movies)
        else:
            print("Found no movies for that search term!")

    elif user_input == "7":
        new_workspace = prompt_switch_workspace(username)
        if new_workspace:
            current_workspace = new_workspace
            workspace_id = current_workspace[0]
            workspace_name = current_workspace[1]

    elif user_input == "8":
        new_workspace = prompt_create_team_workspace(username)
        if new_workspace:
            current_workspace = new_workspace
            workspace_id = current_workspace[0]
            workspace_name = current_workspace[1]

    elif user_input == "9":
        prompt_add_member(workspace_id, current_workspace)

    elif user_input == "10":
        prompt_view_members(workspace_id, current_workspace)

    else:
        print("Invalid input, please try again!")

print("Goodbye!")
