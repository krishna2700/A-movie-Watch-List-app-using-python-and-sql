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
8) Add an agent.
9) Create a new task (initial).
10) Add a branch to a task.
11) Create follow-up task (select agent & base branch).
12) View tasks and branches.
13) Exit.

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


# --- Agent prompts ---

def prompt_add_agent():
    name = input("Agent name: ")
    description = input("Agent description: ")
    database.add_agent(name, description)
    print(f"Agent '{name}' added successfully!")


def print_agents_list(agents):
    if not agents:
        print("No agents found. Please add an agent first.")
        return
    print("\n-- Available Agents --")
    for agent in agents:
        print(f"  [{agent[0]}] {agent[1]} - {agent[2] or 'No description'}")
    print("----\n")


# --- Task prompts ---

def prompt_create_task():
    agents = database.get_agents()
    if not agents:
        print("No agents available. Please add an agent first (option 8).")
        return

    title = input("Task title: ")
    description = input("Task description: ")

    print_agents_list(agents)
    agent_id = input("Select agent ID for this task: ")

    agent = database.get_agent_by_id(agent_id)
    if not agent:
        print(f"Agent with ID {agent_id} not found.")
        return

    database.add_task(title, description, agent_id)
    print(f"\nTask '{title}' created successfully, assigned to agent '{agent[1]}'.")
    print("You can now add branches to this task (option 10).\n")


def prompt_add_branch():
    tasks = database.get_tasks()
    if not tasks:
        print("No tasks found. Please create a task first (option 9).")
        return

    print_tasks_list(tasks)
    task_id = input("Enter the Task ID to add a branch to: ")

    task = database.get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return

    name = input("Branch name: ")
    description = input("Branch description: ")
    database.add_branch(task_id, name, description)
    print(f"Branch '{name}' added to task '{task[1]}'.\n")


def prompt_create_follow_up_task():
    """Create a follow-up task with a different agent, selecting a base branch."""
    tasks = database.get_tasks()
    if not tasks:
        print("No tasks found. Please create an initial task first (option 9).")
        return

    print_tasks_list(tasks)
    parent_task_id = input("Enter the parent Task ID to follow up on: ")

    parent_task = database.get_task_by_id(parent_task_id)
    if not parent_task:
        print(f"Task with ID {parent_task_id} not found.")
        return

    # Show branches for the parent task so user can select the base branch
    branches = database.get_branches_for_task(parent_task_id)
    if not branches:
        print(f"\nTask '{parent_task[1]}' has no branches yet.")
        print("Please add branches to this task first (option 10).\n")
        return

    parent_agent = database.get_agent_by_id(parent_task[3])
    parent_agent_name = parent_agent[1] if parent_agent else "Unknown"

    print(f"\n{'='*60}")
    print(f"  Follow-up for Task: '{parent_task[1]}' (ID: {parent_task[0]})")
    print(f"  Original Agent: {parent_agent_name}")
    print(f"{'='*60}")
    print(f"\n  Available branches to base your follow-up on:\n")

    for i, branch in enumerate(branches, start=1):
        branch_date = datetime.datetime.fromtimestamp(branch[4])
        human_date = branch_date.strftime("%b %d %Y %H:%M")
        print(f"    {i}) [{branch[0]}] {branch[2]}")
        print(f"       Description: {branch[3] or 'No description'}")
        print(f"       Created: {human_date}")
        print()

    print(f"{'='*60}")
    branch_choice = input("Select a branch number (1, 2, ...) to base the follow-up on: ")

    try:
        branch_index = int(branch_choice) - 1
        if branch_index < 0 or branch_index >= len(branches):
            print("Invalid branch selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    selected_branch = branches[branch_index]
    selected_branch_id = selected_branch[0]
    selected_branch_name = selected_branch[2]

    print(f"\n  >> Base branch selected: '{selected_branch_name}' (ID: {selected_branch_id})")
    print()

    # Now select a different agent for the follow-up
    agents = database.get_agents()
    if not agents:
        print("No agents available. Please add an agent first (option 8).")
        return

    print("  Select a different agent for this follow-up task:\n")
    print_agents_list(agents)
    agent_id = input("Select agent ID: ")

    agent = database.get_agent_by_id(agent_id)
    if not agent:
        print(f"Agent with ID {agent_id} not found.")
        return

    title = input("Follow-up task title: ")
    description = input("Follow-up task description: ")

    database.add_task(title, description, agent_id, parent_task_id, selected_branch_id)

    print(f"\n{'='*60}")
    print(f"  Follow-up task created successfully!")
    print(f"  Title       : {title}")
    print(f"  Agent       : {agent[1]}")
    print(f"  Based on    : Branch '{selected_branch_name}' (ID: {selected_branch_id})")
    print(f"  Parent task : '{parent_task[1]}' (ID: {parent_task[0]})")
    print(f"{'='*60}\n")


def print_tasks_list(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n-- All Tasks --")
    for task in tasks:
        task_date = datetime.datetime.fromtimestamp(task[6])
        human_date = task_date.strftime("%b %d %Y %H:%M")
        agent = database.get_agent_by_id(task[3])
        agent_name = agent[1] if agent else "Unknown"

        parent_info = ""
        if task[4]:
            parent = database.get_task_by_id(task[4])
            parent_info = f" | Follow-up of Task '{parent[1]}' (ID: {parent[0]})" if parent else ""

        branch_info = ""
        if task[5]:
            branch = database.get_branch_by_id(task[5])
            branch_info = f" | Based on branch '{branch[2]}' (ID: {branch[0]})" if branch else ""

        print(f"  [{task[0]}] {task[1]} (Agent: {agent_name}, Created: {human_date}){parent_info}{branch_info}")
    print("----\n")


def prompt_view_tasks_and_branches():
    """View all tasks with their branches and follow-up lineage."""
    tasks = database.get_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print(f"\n{'='*60}")
    print("  TASKS & BRANCHES OVERVIEW")
    print(f"{'='*60}\n")

    for task in tasks:
        task_date = datetime.datetime.fromtimestamp(task[6])
        human_date = task_date.strftime("%b %d %Y %H:%M")
        agent = database.get_agent_by_id(task[3])
        agent_name = agent[1] if agent else "Unknown"

        is_follow_up = task[4] is not None
        task_type = "FOLLOW-UP" if is_follow_up else "INITIAL"

        print(f"  [{task_type}] Task ID: {task[0]}")
        print(f"    Title       : {task[1]}")
        print(f"    Description : {task[2] or 'No description'}")
        print(f"    Agent       : {agent_name} (ID: {task[3]})")
        print(f"    Created     : {human_date}")

        if is_follow_up:
            parent = database.get_task_by_id(task[4])
            parent_name = parent[1] if parent else "Unknown"
            print(f"    Parent Task : '{parent_name}' (ID: {task[4]})")

            if task[5]:
                branch = database.get_branch_by_id(task[5])
                if branch:
                    print(f"    Base Branch : '{branch[2]}' (ID: {branch[0]}) - {branch[3] or 'No description'}")
                else:
                    print(f"    Base Branch : Unknown (ID: {task[5]})")
            else:
                print(f"    Base Branch : None (no branch selected)")

        # Show branches created under this task
        branches = database.get_branches_for_task(task[0])
        if branches:
            print(f"    Branches ({len(branches)}):")
            for branch in branches:
                b_date = datetime.datetime.fromtimestamp(branch[4])
                b_human_date = b_date.strftime("%b %d %Y %H:%M")
                print(f"      - [{branch[0]}] {branch[2]}: {branch[3] or 'No description'} (Created: {b_human_date})")

        # Show follow-up tasks
        follow_ups = database.get_follow_up_tasks(task[0])
        if follow_ups:
            print(f"    Follow-ups ({len(follow_ups)}):")
            for fu in follow_ups:
                fu_agent = database.get_agent_by_id(fu[3])
                fu_agent_name = fu_agent[1] if fu_agent else "Unknown"
                fu_branch_info = ""
                if fu[5]:
                    fu_branch = database.get_branch_by_id(fu[5])
                    fu_branch_info = f" based on branch '{fu_branch[2]}'" if fu_branch else ""
                print(f"      - [{fu[0]}] {fu[1]} (Agent: {fu_agent_name}){fu_branch_info}")

        print(f"  {'-'*56}")

    print()


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "13":
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
        prompt_add_agent()
    elif user_input == "9":
        prompt_create_task()
    elif user_input == "10":
        prompt_add_branch()
    elif user_input == "11":
        prompt_create_follow_up_task()
    elif user_input == "12":
        prompt_view_tasks_and_branches()
    else:
        print("Invalid input, please try again!")
