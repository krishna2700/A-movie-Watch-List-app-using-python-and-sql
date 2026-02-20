import datetime
import database

# TODO: Add input validation for all user prompts (dates, movie IDs, usernames)
# TODO: Add error handling for database operations (e.g., duplicate users, invalid FKs)
# TODO: Add options to delete or edit movies and users

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Select user profile (follow-up view, up to 50 movies).
9) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    # TODO: Validate date format and catch ValueError for malformed input
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
    # TODO: Verify username and movie_id exist before inserting to avoid orphaned records
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


def prompt_select_user_profile():
    username = input("Username: ")
    if not database.user_exists(username):
        print(f"User '{username}' not found. Please add the user first (option 6).")
        return

    watched_count = database.get_watched_count(username)
    watched = database.get_watched_movies_limited(username, limit=50)
    unwatched = database.get_unwatched_movies(username, limit=50)

    print(f"\n== Profile for '{username}' ==")
    print(f"Total movies watched: {watched_count}")

    if watched:
        print(f"\n-- Watched movies (showing up to 50) --")
        for movie in watched:
            movie_date = datetime.datetime.fromtimestamp(movie[2])
            human_date = movie_date.strftime("%b %d %Y")
            print(f"  {movie[0]}: {movie[1]} (on {human_date})")
        if watched_count > 50:
            print(f"  ... and {watched_count - 50} more.")
    else:
        print("\nNo movies watched yet.")

    if unwatched:
        print(f"\n-- Suggestions: movies not yet watched (up to 50) --")
        for movie in unwatched:
            movie_date = datetime.datetime.fromtimestamp(movie[2])
            human_date = movie_date.strftime("%b %d %Y")
            print(f"  {movie[0]}: {movie[1]} (on {human_date})")
    else:
        print("\nYou've watched every movie in the catalog!")

    print("====\n")


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
        prompt_select_user_profile()
    else:
        print("Invalid input, please try again!")
