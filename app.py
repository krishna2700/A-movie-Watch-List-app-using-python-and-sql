import datetime
import database

# ──────────────────────────────────────────────
# Menus
# ──────────────────────────────────────────────

main_menu = """
╔══════════════════════════════════════════╗
║        WATCHLIST & TASK MANAGER          ║
╠══════════════════════════════════════════╣
║  MOVIES                                  ║
║  1) Add new movie                        ║
║  2) View upcoming movies                 ║
║  3) View all movies                      ║
║  4) Add watched movie                    ║
║  5) View watched movies                  ║
║  6) Add user to the app                  ║
║  7) Search for a movie                   ║
║                                          ║
║  TASK MANAGEMENT                         ║
║  10) Create a new task                   ║
║  11) View all tasks                      ║
║  12) View task details                   ║
║  13) Start a task                        ║
║  14) Complete a task                     ║
║  15) Add follow-up task                  ║
║  16) Start follow-up task                ║
║  17) Complete follow-up task             ║
║                                          ║
║  AGENT MANAGEMENT                        ║
║  20) Add agent                           ║
║  21) View all agents                     ║
║  22) Assign agent to task                ║
║  23) Assign agent to follow-up task      ║
║  24) Pause (stop) selected agents        ║
║  25) Resume selected agents              ║
║                                          ║
║  0) Exit                                 ║
╚══════════════════════════════════════════╝

Your selection: """

welcome = "Welcome to the Watchlist & Task Manager!"


# ──────────────────────────────────────────────
# Movie Functions (existing)
# ──────────────────────────────────────────────

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    database.add_movie(title, release_timestamp)


def print_movie_list(heading, movies):
    print(f"\n-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"  {movie[0]}: {movie[1]} (on {human_date})")
    print("----\n")


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


# ──────────────────────────────────────────────
# Task Functions
# ──────────────────────────────────────────────

def prompt_create_task():
    title = input("Task title: ")
    description = input("Task description (optional): ")
    task_id = database.create_task(title, description)
    print(f"  ✅ Task #{task_id} created: '{title}' [Pending]")


def prompt_view_all_tasks():
    tasks = database.get_all_tasks()
    if not tasks:
        print("\n  No tasks found.")
        return
    print("\n╔══════════════════════════════════════════╗")
    print("║              ALL TASKS                   ║")
    print("╠══════════════════════════════════════════╣")
    for task in tasks:
        task_id = task[0]
        title = task[1]
        status_display = database.format_task_status_display(task_id, is_followup=False)
        print(f"  #{task_id}: {title}")
        print(f"         Status: {status_display}")

        # Show follow-up tasks inline
        followups = database.get_followup_tasks(task_id)
        if followups:
            for fu in followups:
                fu_id = fu[0]
                fu_title = fu[2]
                fu_status_display = database.format_task_status_display(fu_id, is_followup=True)
                print(f"         └─ Follow-up #{fu_id}: {fu_title}")
                print(f"            Status: {fu_status_display}")
    print("╚══════════════════════════════════════════╝\n")


def prompt_view_task_details():
    task_id = input("Task ID: ")
    try:
        task_id = int(task_id)
    except ValueError:
        print("  Invalid task ID.")
        return

    task = database.get_task_by_id(task_id)
    if not task:
        print("  Task not found.")
        return

    print(f"\n  ── Task #{task[0]} ──")
    print(f"  Title:       {task[1]}")
    print(f"  Description: {task[2] or '(none)'}")
    print(f"  Status:      {database.format_task_status_display(task_id, is_followup=False)}")

    # Show per-agent breakdown
    agents = database.get_task_agents(task_id)
    if agents:
        print(f"  Agents ({len(agents)}):")
        for a in agents:
            print(f"    {a[2]} {a[1]}: {a[3]}")
    else:
        print("  Agents: (none assigned)")

    # Show follow-up tasks
    followups = database.get_followup_tasks(task_id)
    if followups:
        print(f"\n  ── Follow-up Tasks ({len(followups)}) ──")
        for fu in followups:
            fu_id = fu[0]
            fu_title = fu[2]
            fu_status_display = database.format_task_status_display(fu_id, is_followup=True)
            print(f"  #{fu_id}: {fu_title}")
            print(f"    Status: {fu_status_display}")

            fu_agents = database.get_followup_agents(fu_id)
            if fu_agents:
                print(f"    Agents ({len(fu_agents)}):")
                for fa in fu_agents:
                    print(f"      {fa[2]} {fa[1]}: {fa[3]}")
            else:
                print(f"    Agents: (none assigned)")
    print()


def prompt_start_task():
    task_id = input("Task ID to start: ")
    try:
        task_id = int(task_id)
    except ValueError:
        print("  Invalid task ID.")
        return
    database.start_task(task_id)
    print(f"  ▶ Task #{task_id} started — status: In Progress")
    _print_task_agent_summary(task_id, is_followup=False)


def prompt_complete_task():
    task_id = input("Task ID to complete: ")
    try:
        task_id = int(task_id)
    except ValueError:
        print("  Invalid task ID.")
        return
    database.complete_task(task_id)
    print(f"  ✅ Task #{task_id} completed.")


# ──────────────────────────────────────────────
# Follow-up Task Functions
# ──────────────────────────────────────────────

def prompt_add_followup():
    parent_id = input("Parent task ID: ")
    try:
        parent_id = int(parent_id)
    except ValueError:
        print("  Invalid task ID.")
        return

    parent = database.get_task_by_id(parent_id)
    if not parent:
        print("  Parent task not found.")
        return

    title = input("Follow-up task title: ")
    description = input("Follow-up description (optional): ")
    fu_id = database.create_followup_task(parent_id, title, description)
    print(f"  ✅ Follow-up #{fu_id} created under Task #{parent_id}: '{title}' [Pending]")


def prompt_start_followup():
    """
    KEY FIX: Starting a follow-up task RESETS its status to 'In Progress'
    and resets all assigned agents to 'Running'.
    This fixes the bug where follow-up status stayed 'Completed'.
    """
    fu_id = input("Follow-up task ID to start: ")
    try:
        fu_id = int(fu_id)
    except ValueError:
        print("  Invalid follow-up ID.")
        return

    fu = database.get_followup_task_by_id(fu_id)
    if not fu:
        print("  Follow-up task not found.")
        return

    database.start_followup_task(fu_id)
    print(f"  ▶ Follow-up #{fu_id} started — status RESET to: In Progress")
    _print_task_agent_summary(fu_id, is_followup=True)


def prompt_complete_followup():
    fu_id = input("Follow-up task ID to complete: ")
    try:
        fu_id = int(fu_id)
    except ValueError:
        print("  Invalid follow-up ID.")
        return
    database.complete_followup_task(fu_id)
    print(f"  ✅ Follow-up #{fu_id} completed.")


# ──────────────────────────────────────────────
# Agent Functions
# ──────────────────────────────────────────────

def prompt_add_agent():
    name = input("Agent name: ")
    icon = input("Agent icon (default 🤖): ") or "🤖"
    database.add_agent(name, icon)
    print(f"  ✅ Agent '{name}' {icon} added.")


def prompt_view_agents():
    agents = database.get_all_agents()
    if not agents:
        print("\n  No agents registered.")
        return
    print("\n  ── Registered Agents ──")
    for a in agents:
        print(f"  #{a[0]}: {a[2]} {a[1]}")
    print()


def prompt_assign_agent_to_task():
    task_id = input("Task ID: ")
    agent_id = input("Agent ID: ")
    try:
        task_id, agent_id = int(task_id), int(agent_id)
    except ValueError:
        print("  Invalid ID.")
        return
    database.assign_agent_to_task(task_id, agent_id)
    print(f"  ✅ Agent #{agent_id} assigned to Task #{task_id}.")


def prompt_assign_agent_to_followup():
    fu_id = input("Follow-up task ID: ")
    agent_id = input("Agent ID: ")
    try:
        fu_id, agent_id = int(fu_id), int(agent_id)
    except ValueError:
        print("  Invalid ID.")
        return
    database.assign_agent_to_followup(fu_id, agent_id)
    print(f"  ✅ Agent #{agent_id} assigned to Follow-up #{fu_id}.")


def prompt_pause_agents():
    """
    KEY FEATURE: Pause SELECTED agents (not all).
    User picks which agents to stop on a specific task/follow-up.
    Shows 'Stopped' status with the stopped agent icons.
    """
    task_type = input("Pause on (t)ask or (f)ollow-up? [t/f]: ").strip().lower()
    is_followup = task_type == "f"

    task_id = input("Task/Follow-up ID: ")
    try:
        task_id = int(task_id)
    except ValueError:
        print("  Invalid ID.")
        return

    # Show current agents and their statuses
    if is_followup:
        agents = database.get_followup_agents(task_id)
    else:
        agents = database.get_task_agents(task_id)

    if not agents:
        print("  No agents assigned to this task.")
        return

    print("\n  Current agents:")
    for a in agents:
        print(f"    #{a[0]}: {a[2]} {a[1]} — {a[3]}")

    agent_ids_str = input("Enter agent IDs to STOP (comma-separated, e.g. 1,3): ")
    try:
        agent_ids = [int(x.strip()) for x in agent_ids_str.split(",") if x.strip()]
    except ValueError:
        print("  Invalid agent IDs.")
        return

    for aid in agent_ids:
        if is_followup:
            database.stop_agent_on_followup(task_id, aid)
        else:
            database.stop_agent_on_task(task_id, aid)
        agent = database.get_agent_by_id(aid)
        agent_name = agent[1] if agent else f"#{aid}"
        agent_icon = agent[2] if agent else "🤖"
        print(f"  ⏸  {agent_icon} {agent_name} → Stopped")

    # Show updated status with icons
    label = "Follow-up" if is_followup else "Task"
    status_display = database.format_task_status_display(task_id, is_followup=is_followup)
    print(f"\n  {label} #{task_id} status: {status_display}")


def prompt_resume_agents():
    """Resume selected agents on a task/follow-up."""
    task_type = input("Resume on (t)ask or (f)ollow-up? [t/f]: ").strip().lower()
    is_followup = task_type == "f"

    task_id = input("Task/Follow-up ID: ")
    try:
        task_id = int(task_id)
    except ValueError:
        print("  Invalid ID.")
        return

    if is_followup:
        agents = database.get_followup_agents(task_id)
    else:
        agents = database.get_task_agents(task_id)

    if not agents:
        print("  No agents assigned to this task.")
        return

    print("\n  Current agents:")
    for a in agents:
        print(f"    #{a[0]}: {a[2]} {a[1]} — {a[3]}")

    agent_ids_str = input("Enter agent IDs to RESUME (comma-separated, e.g. 1,3): ")
    try:
        agent_ids = [int(x.strip()) for x in agent_ids_str.split(",") if x.strip()]
    except ValueError:
        print("  Invalid agent IDs.")
        return

    for aid in agent_ids:
        if is_followup:
            database.resume_agent_on_followup(task_id, aid)
        else:
            database.resume_agent_on_task(task_id, aid)
        agent = database.get_agent_by_id(aid)
        agent_name = agent[1] if agent else f"#{aid}"
        agent_icon = agent[2] if agent else "🤖"
        print(f"  ▶ {agent_icon} {agent_name} → Running")

    label = "Follow-up" if is_followup else "Task"
    status_display = database.format_task_status_display(task_id, is_followup=is_followup)
    print(f"\n  {label} #{task_id} status: {status_display}")


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def _print_task_agent_summary(task_id, is_followup=False):
    """Print a quick agent summary after starting/modifying a task."""
    if is_followup:
        agents = database.get_followup_agents(task_id)
    else:
        agents = database.get_task_agents(task_id)

    if agents:
        running = [a for a in agents if a[3] == "Running"]
        stopped = [a for a in agents if a[3] == "Stopped"]

        if running:
            icons = "".join(a[2] for a in running)
            names = ", ".join(a[1] for a in running)
            print(f"    In Progress: {icons} [{names}]")
        if stopped:
            icons = "".join(a[2] for a in stopped)
            names = ", ".join(a[1] for a in stopped)
            print(f"    Stopped:     {icons} [{names}]")
    else:
        print("    (no agents assigned)")


# ──────────────────────────────────────────────
# Main Loop
# ──────────────────────────────────────────────

print(welcome)
database.create_tables()

while (user_input := input(main_menu)) != "0":
    # Movie options
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

    # Task options
    elif user_input == "10":
        prompt_create_task()
    elif user_input == "11":
        prompt_view_all_tasks()
    elif user_input == "12":
        prompt_view_task_details()
    elif user_input == "13":
        prompt_start_task()
    elif user_input == "14":
        prompt_complete_task()
    elif user_input == "15":
        prompt_add_followup()
    elif user_input == "16":
        prompt_start_followup()
    elif user_input == "17":
        prompt_complete_followup()

    # Agent options
    elif user_input == "20":
        prompt_add_agent()
    elif user_input == "21":
        prompt_view_agents()
    elif user_input == "22":
        prompt_assign_agent_to_task()
    elif user_input == "23":
        prompt_assign_agent_to_followup()
    elif user_input == "24":
        prompt_pause_agents()
    elif user_input == "25":
        prompt_resume_agents()

    else:
        print("Invalid input, please try again!")
