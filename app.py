import datetime
import database

welcome = "Welcome to the watchlist app!"

current_user = None
current_workspace = None  # (id, name, type, owner_username)


def get_menu():
    ws_name = current_workspace[1] if current_workspace else "None"
    ws_type = current_workspace[2] if current_workspace else ""
    ws_label = f"{ws_name} ({ws_type})"
    return f"""
--- Current Workspace: {ws_label} ---
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Add watched movie.
5) View watched movies.
6) Search for a movie.
7) Switch workspace.
8) Create a team workspace.
9) Invite user to current team workspace.
10) View all workspaces.
11) Exit.

Your selection: """


def prompt_login():
    """Login or register a user. Returns the username."""
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return prompt_login()

    user = database.get_user(username)
    if user is None:
        print(f"User '{username}' not found. Creating new account...")
        database.add_user(username)
        database.create_personal_workspace(username)
        print(f"Account created! A personal workspace has been set up for you.")
    else:
        print(f"Welcome back, {username}!")

    return username


def resolve_workspace(username):
    """Resolve which workspace to open for the user based on last visited."""
    last_ws_id = database.get_last_workspace(username)

    if last_ws_id is not None:
        workspace = database.get_workspace_by_id(last_ws_id)
        if workspace:
            ws_type = workspace[2]
            print(f"Resuming your last workspace: \"{workspace[1]}\" ({ws_type})")
            return workspace

    # Fallback: find or create personal workspace
    workspaces = database.get_user_workspaces(username)
    for ws in workspaces:
        if ws[2] == "personal" and ws[3] == username:
            database.set_last_workspace(username, ws[0])
            print(f"Opening your personal workspace: \"{ws[1]}\"")
            return ws

    # No personal workspace exists yet — create one
    ws_id = database.create_personal_workspace(username)
    workspace = database.get_workspace_by_id(ws_id)
    print(f"Created and opened your personal workspace: \"{workspace[1]}\"")
    return workspace


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    movie_id = database.add_movie(title, release_timestamp)
    database.add_movie_to_workspace(current_workspace[0], movie_id)
    print(f"Movie '{title}' added to workspace \"{current_workspace[1]}\".")


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("---- \n")


def prompt_watch_movie():
    movie_id = input("Movie ID: ")
    database.watch_movie(current_user, movie_id)
    print("Movie marked as watched!")


def prompt_get_watched_movies():
    return database.get_workspace_watched_movies(current_user, current_workspace[0])


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    return database.search_workspace_movies(current_workspace[0], search_term)


def prompt_switch_workspace():
    """Show all workspaces and let the user pick one. Persists the choice."""
    global current_workspace
    workspaces = database.get_user_workspaces(current_user)

    if not workspaces:
        print("You have no workspaces.")
        return

    print("\n--- Your Workspaces ---")
    for ws in workspaces:
        marker = " <-- current" if ws[0] == current_workspace[0] else ""
        print(f"  {ws[0]}) {ws[1]} ({ws[2]}){marker}")
    print()

    choice = input("Enter workspace ID to switch to: ").strip()
    try:
        choice_id = int(choice)
    except ValueError:
        print("Invalid input.")
        return

    # Verify user has access
    valid_ids = [ws[0] for ws in workspaces]
    if choice_id not in valid_ids:
        print("You don't have access to that workspace.")
        return

    workspace = database.get_workspace_by_id(choice_id)
    if workspace:
        current_workspace = workspace
        database.set_last_workspace(current_user, workspace[0])
        print(f"Switched to workspace: \"{workspace[1]}\" ({workspace[2]})")
    else:
        print("Workspace not found.")


def prompt_create_team_workspace():
    """Create a new team workspace."""
    global current_workspace
    name = input("Team workspace name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    ws_id = database.create_workspace(name, "team", current_user)
    workspace = database.get_workspace_by_id(ws_id)
    print(f"Team workspace \"{name}\" created!")

    switch = input("Switch to this workspace now? (y/n): ").strip().lower()
    if switch == "y":
        current_workspace = workspace
        database.set_last_workspace(current_user, workspace[0])
        print(f"Switched to workspace: \"{workspace[1]}\" (team)")


def prompt_invite_user():
    """Invite another user to the current team workspace."""
    if current_workspace[2] != "team":
        print("You can only invite users to team workspaces.")
        return

    username = input("Username to invite: ").strip()
    user = database.get_user(username)
    if user is None:
        print(f"User '{username}' does not exist.")
        return

    database.add_workspace_member(current_workspace[0], username)
    print(f"User '{username}' has been added to \"{current_workspace[1]}\".")


def prompt_view_workspaces():
    """Display all workspaces the user belongs to."""
    workspaces = database.get_user_workspaces(current_user)
    if not workspaces:
        print("You have no workspaces.")
        return

    print("\n--- Your Workspaces ---")
    for ws in workspaces:
        marker = " <-- current" if ws[0] == current_workspace[0] else ""
        print(f"  {ws[0]}) {ws[1]} ({ws[2]}){marker}")
    print()


# --- Main ---

print(welcome)
database.create_tables()

current_user = prompt_login()
current_workspace = resolve_workspace(current_user)

while (user_input := input(get_menu())) != "11":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_workspace_movies(current_workspace[0], upcoming=True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_workspace_movies(current_workspace[0])
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        movies = prompt_get_watched_movies()
        if movies:
            print_movie_list("Watched", movies)
        else:
            print("No watched movies in this workspace yet!")
    elif user_input == "6":
        movies = prompt_search_movies()
        if movies:
            print_movie_list("Movies found", movies)
        else:
            print("Found no movies for that search term!")
    elif user_input == "7":
        prompt_switch_workspace()
    elif user_input == "8":
        prompt_create_team_workspace()
    elif user_input == "9":
        prompt_invite_user()
    elif user_input == "10":
        prompt_view_workspaces()
    else:
        print("Invalid input, please try again!")

print("Goodbye!")
