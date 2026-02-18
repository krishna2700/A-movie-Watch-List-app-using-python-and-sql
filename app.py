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
8) Task Management
9) Exit.

Your selection: """

task_menu = """Task Management:
1) Create new task
2) View all tasks
3) Add followup task
4) Start task/followup task
5) Complete task
6) Manage agents
7) Pause/Resume agents
8) View task status
9) Back to main menu

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


# Task management functions
def prompt_create_task():
    title = input("Task title: ")
    task_id = database.add_task(title)
    print(f"Task created with ID: {task_id}")
    
    # Ask if user wants to assign agents
    assign = input("Assign agents to this task? (y/n): ")
    if assign.lower() == 'y':
        assign_agents_to_task(task_id)


def prompt_create_followup_task():
    parent_id = input("Parent task ID: ")
    title = input("Followup task title: ")
    task_id = database.add_task(title, parent_task_id=int(parent_id))
    print(f"Followup task created with ID: {task_id}")
    
    # Ask if user wants to assign agents
    assign = input("Assign agents to this followup task? (y/n): ")
    if assign.lower() == 'y':
        assign_agents_to_task(task_id)


def view_all_tasks():
    tasks = database.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n=== All Tasks ===")
    for task in tasks:
        task_id = task[0]
        title = task[1]
        status_text, agent_icons, agent_count = database.get_task_status_display(task_id)
        
        # Display task with agent icons
        icon_display = ""
        if agent_count > 0:
            if len(agent_icons) <= 2:
                icon_display = " ".join(agent_icons)
            else:
                icon_display = f"{agent_icons[0]} {agent_icons[1]} +{agent_count - 2}"
        
        print(f"ID: {task_id} | {title} | Status: {status_text} {icon_display}")
        
        # Show followup tasks
        followup_tasks = database.get_followup_tasks(task_id)
        if followup_tasks:
            print("  Followup tasks:")
            for ft in followup_tasks:
                ft_id = ft[0]
                ft_title = ft[1]
                ft_status_text, ft_agent_icons, ft_agent_count = database.get_task_status_display(ft_id)
                
                ft_icon_display = ""
                if ft_agent_count > 0:
                    if len(ft_agent_icons) <= 2:
                        ft_icon_display = " ".join(ft_agent_icons)
                    else:
                        ft_icon_display = f"{ft_agent_icons[0]} {ft_agent_icons[1]} +{ft_agent_count - 2}"
                
                print(f"    ID: {ft_id} | {ft_title} | Status: {ft_status_text} {ft_icon_display}")
    print()


def prompt_start_task():
    task_id = input("Task ID to start: ")
    task = database.get_task(int(task_id))
    
    if not task:
        print("Task not found!")
        return
    
    parent_task_id = task[3]
    
    if parent_task_id is not None:
        # This is a followup task - use special start function
        database.start_followup_task(int(task_id))
        print(f"Followup task {task_id} started - status reset to 'in_progress'")
    else:
        # Regular task
        database.update_task_status(int(task_id), 'in_progress')
        print(f"Task {task_id} started")


def prompt_complete_task():
    task_id = input("Task ID to complete: ")
    database.update_task_status(int(task_id), 'completed')
    print(f"Task {task_id} marked as completed")


def manage_agents():
    print("\n=== Agent Management ===")
    print("1) Create new agent")
    print("2) View all agents")
    print("3) Assign agent to task")
    
    choice = input("Your selection: ")
    
    if choice == '1':
        name = input("Agent name: ")
        icon = input("Agent icon (emoji): ")
        agent_id = database.add_agent(name, icon)
        print(f"Agent created with ID: {agent_id}")
    elif choice == '2':
        agents = database.get_all_agents()
        if agents:
            print("\nAll Agents:")
            for agent in agents:
                print(f"ID: {agent[0]} | Name: {agent[1]} | Icon: {agent[2]}")
        else:
            print("No agents found.")
    elif choice == '3':
        task_id = input("Task ID: ")
        assign_agents_to_task(int(task_id))


def assign_agents_to_task(task_id):
    agents = database.get_all_agents()
    if not agents:
        print("No agents available. Create agents first.")
        return
    
    print("\nAvailable agents:")
    for agent in agents:
        print(f"ID: {agent[0]} | Name: {agent[1]} | Icon: {agent[2]}")
    
    agent_ids = input("Enter agent IDs to assign (comma-separated): ")
    for agent_id in agent_ids.split(','):
        database.assign_agent_to_task(task_id, int(agent_id.strip()))
    print("Agents assigned successfully")


def pause_resume_agents():
    task_id = input("Task ID: ")
    agents = database.get_task_agents(int(task_id))
    
    if not agents:
        print("No agents assigned to this task.")
        return
    
    print("\nAgents for this task:")
    for agent in agents:
        agent_id = agent[0]
        name = agent[1]
        icon = agent[2]
        status = agent[3]
        print(f"ID: {agent_id} | {icon} {name} | Status: {status}")
    
    print("\n1) Pause specific agents")
    print("2) Resume specific agents")
    
    choice = input("Your selection: ")
    
    if choice == '1':
        agent_ids = input("Enter agent IDs to pause (comma-separated): ")
        for agent_id in agent_ids.split(','):
            database.pause_agent(int(task_id), int(agent_id.strip()))
        print("Agents paused")
    elif choice == '2':
        agent_ids = input("Enter agent IDs to resume (comma-separated): ")
        for agent_id in agent_ids.split(','):
            database.resume_agent(int(task_id), int(agent_id.strip()))
        print("Agents resumed")


def view_task_status():
    task_id = input("Task ID: ")
    task = database.get_task(int(task_id))
    
    if not task:
        print("Task not found!")
        return
    
    status_text, agent_icons, agent_count = database.get_task_status_display(int(task_id))
    
    print(f"\nTask: {task[1]}")
    print(f"Status: {status_text}")
    
    if agent_count > 0:
        print(f"Agents ({agent_count}):")
        
        running = database.get_running_agents(int(task_id))
        stopped = database.get_stopped_agents(int(task_id))
        
        if running:
            print("  Running:")
            for agent in running:
                print(f"    {agent[2]} {agent[1]}")
        
        if stopped:
            print("  Stopped:")
            for agent in stopped:
                print(f"    {agent[2]} {agent[1]}")
    else:
        print("No agents assigned")
    print()


def task_management_menu():
    while (task_input := input(task_menu)) != "9":
        if task_input == "1":
            prompt_create_task()
        elif task_input == "2":
            view_all_tasks()
        elif task_input == "3":
            prompt_create_followup_task()
        elif task_input == "4":
            prompt_start_task()
        elif task_input == "5":
            prompt_complete_task()
        elif task_input == "6":
            manage_agents()
        elif task_input == "7":
            pause_resume_agents()
        elif task_input == "8":
            view_task_status()
        else:
            print("Invalid input, please try again!")


print(welcome)
database.create_tables()

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
        task_management_menu()
    else:
        print("Invalid input, please try again!")
