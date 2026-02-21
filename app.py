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
8) Create new task (multi-agent).
9) Create follow-up task (multi-agent).
10) View all tasks.
11) Exit.

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


def prompt_create_task():
    task_name = input("Task name: ")
    branch_name = input("Branch name: ")
    task_id = database.add_task(task_name, branch_name, parent_task_id=None, is_initial_task=True)
    print(f"Initial task created with ID: {task_id} on branch: {branch_name}")


def prompt_create_follow_up_task():
    # Show initial tasks to select base branch
    initial_tasks = database.get_initial_tasks()

    if not initial_tasks:
        print("No initial tasks found. Please create an initial task first.")
        return

    print("\n-- Available base branches from initial tasks --")
    for task in initial_tasks:
        task_id = task[0]
        task_name = task[1]
        branch_name = task[2]
        created_at = datetime.datetime.fromtimestamp(task[4])
        human_date = created_at.strftime("%b %d %Y %H:%M")
        print(f"Task ID {task_id}: {task_name} (Branch: {branch_name}, Created: {human_date})")
    print("----\n")

    base_task_id = input("Select base task ID: ")
    base_task = database.get_task_by_id(base_task_id)

    if not base_task:
        print("Invalid task ID!")
        return

    base_branch = base_task[2]
    print(f"\nCreating follow-up task based on branch: {base_branch}")

    task_name = input("Follow-up task name: ")
    new_branch_name = input("New branch name for follow-up task: ")

    task_id = database.add_task(task_name, new_branch_name, parent_task_id=base_task_id, is_initial_task=False)
    print(f"\nFollow-up task created!")
    print(f"  Task ID: {task_id}")
    print(f"  New branch: {new_branch_name}")
    print(f"  Base branch: {base_branch}")
    print(f"  Parent task ID: {base_task_id}")


def print_all_tasks():
    tasks = database.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\n-- All Tasks --")
    for task in tasks:
        task_id = task[0]
        task_name = task[1]
        branch_name = task[2]
        parent_task_id = task[3]
        created_at = datetime.datetime.fromtimestamp(task[4])
        is_initial = task[5]
        human_date = created_at.strftime("%b %d %Y %H:%M")

        task_type = "Initial" if is_initial else "Follow-up"
        parent_info = f", Parent: Task {parent_task_id}" if parent_task_id else ""

        print(f"[{task_type}] Task {task_id}: {task_name}")
        print(f"  Branch: {branch_name}{parent_info}")
        print(f"  Created: {human_date}")
        print()


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "11":
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
        prompt_create_task()
    elif user_input == "9":
        prompt_create_follow_up_task()
    elif user_input == "10":
        print_all_tasks()
    else:
        print("Invalid input, please try again!")
