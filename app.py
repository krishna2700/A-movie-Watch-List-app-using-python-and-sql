import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Switch workspace.
9) Create workspace.
10) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

# Global variable to track current workspace
current_workspace = None
current_user = None


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    database.add_movie(title, release_timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("---- \n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def prompt_get_watched_movies():
    username = input("Username: ")
    return database.get_watched_movies(username)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)
    # Create default personal workspace for new user
    workspace_id = database.create_workspace(f"{username}'s Personal Workspace", "personal", username)
    database.update_user_last_workspace(username, "personal", str(workspace_id))
    print(f"User '{username}' created with a personal workspace!")


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    return database.search_movies(search_term)


def prompt_login():
    """Prompt user to login and restore their last workspace"""
    global current_user, current_workspace
    username = input("Enter your username to login: ")
    
    # Check if user exists
    workspaces = database.get_user_workspaces(username)
    if not workspaces:
        print(f"User '{username}' not found. Please create a user first (option 6).")
        return False
    
    current_user = username
    
    # Get user's last workspace
    last_workspace_type, last_workspace_id = database.get_user_last_workspace(username)
    
    if last_workspace_id:
        workspace = database.get_workspace_by_id(int(last_workspace_id))
        if workspace:
            current_workspace = workspace
            print(f"\nWelcome back, {username}!")
            print(f"Restored your last workspace: {workspace[1]} ({workspace[2]})")
        else:
            # Workspace not found, default to first available
            current_workspace = workspaces[0]
            print(f"\nWelcome back, {username}!")
            print(f"Current workspace: {current_workspace[1]} ({current_workspace[2]})")
    else:
        # No last workspace, use first available (should be personal)
        current_workspace = workspaces[0]
        print(f"\nWelcome, {username}!")
        print(f"Current workspace: {current_workspace[1]} ({current_workspace[2]})")
    
    return True


def prompt_switch_workspace():
    """Allow user to switch between their workspaces"""
    global current_workspace
    
    if not current_user:
        print("Please login first!")
        return
    
    workspaces = database.get_user_workspaces(current_user)
    
    if not workspaces:
        print("No workspaces available.")
        return
    
    print("\n-- Available Workspaces --")
    for ws in workspaces:
        workspace_type = "CURRENT" if current_workspace and ws[0] == current_workspace[0] else ""
        print(f"{ws[0]}: {ws[1]} ({ws[2]}) {workspace_type}")
    print("----\n")
    
    workspace_id = input("Enter workspace ID to switch to: ")
    
    try:
        workspace_id = int(workspace_id)
        workspace = database.get_workspace_by_id(workspace_id)
        
        if workspace and workspace in workspaces:
            current_workspace = workspace
            # Save this as the user's last workspace
            database.update_user_last_workspace(current_user, workspace[2], str(workspace_id))
            print(f"Switched to workspace: {workspace[1]} ({workspace[2]})")
        else:
            print("Invalid workspace ID or you don't have access to this workspace.")
    except ValueError:
        print("Invalid workspace ID.")


def prompt_create_workspace():
    """Create a new team workspace"""
    if not current_user:
        print("Please login first!")
        return
    
    workspace_name = input("Enter workspace name: ")
    workspace_type = input("Enter workspace type (personal/team): ").lower()
    
    if workspace_type not in ['personal', 'team']:
        print("Invalid workspace type. Must be 'personal' or 'team'.")
        return
    
    workspace_id = database.create_workspace(workspace_name, workspace_type, current_user)
    print(f"Workspace '{workspace_name}' created successfully! (ID: {workspace_id})")
    
    # Optionally switch to the new workspace
    switch = input("Switch to this workspace now? (y/n): ").lower()
    if switch == 'y':
        global current_workspace
        current_workspace = database.get_workspace_by_id(workspace_id)
        database.update_user_last_workspace(current_user, workspace_type, str(workspace_id))
        print(f"Switched to workspace: {workspace_name}")


print(welcome)
database.create_tables()

# Prompt user to login
print("\n--- Login Required ---")
while not prompt_login():
    create_new = input("Would you like to create a new user? (y/n): ").lower()
    if create_new == 'y':
        prompt_add_user()
    else:
        print("Login is required to use the app.")

while (user_input := input(menu)) != "10":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(upcoming=True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        movies = prompt_get_watched_movies()
        if movies:
            print_movie_list("Watched", movies)
        else:
            print("That user has watched no movies yet!")
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        movies = prompt_search_movies()
        if movies:
            print_movie_list("Movies found", movies)
        else:
            print("Found no movies for that search term!")
    elif user_input == "8":
        prompt_switch_workspace()
    elif user_input == "9":
        prompt_create_workspace()
    else:
        print("Invalid input, please try again!")
