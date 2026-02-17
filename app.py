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
8) Switch workspace
9) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


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


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    return database.search_movies(search_term)


def prompt_login():
    username = input("Enter your username (or press Enter to skip): ")
    if username:
        return username
    return None


def prompt_switch_workspace(username):
    if not username:
        print("You need to login first!")
        return None

    workspaces = database.get_user_workspaces(username)
    print("\n-- Available Workspaces --")
    print("0) Personal Workspace")
    for idx, workspace in enumerate(workspaces, 1):
        print(f"{idx}) {workspace[1]} ({workspace[2]})")
    print("-------------------------\n")

    selection = input("Select workspace number: ")
    try:
        selection_num = int(selection)
        if selection_num == 0:
            workspace_name = "personal"
        elif 1 <= selection_num <= len(workspaces):
            workspace_name = workspaces[selection_num - 1][1]
        else:
            print("Invalid selection!")
            return None

        database.update_last_workspace(username, workspace_name)
        return workspace_name
    except ValueError:
        print("Invalid input!")
        return None


def initialize_user_workspaces(username):
    workspaces = database.get_user_workspaces(username)
    if not workspaces:
        database.add_workspace("Team Workspace 1", "team", username)
        database.add_workspace("Team Workspace 2", "team", username)


print(welcome)
database.create_tables()

current_user = prompt_login()
current_workspace = "personal"

if current_user:
    initialize_user_workspaces(current_user)
    current_workspace = database.get_last_workspace(current_user)
    print(f"\nWelcome back, {current_user}!")
    print(f"Current workspace: {current_workspace}\n")
else:
    print("\nContinuing as guest user in personal workspace.\n")

while (user_input := input(menu)) != "9":
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
        new_workspace = prompt_switch_workspace(current_user)
        if new_workspace:
            current_workspace = new_workspace
            print(f"\nSwitched to workspace: {current_workspace}\n")
    else:
        print("Invalid input, please try again!")
