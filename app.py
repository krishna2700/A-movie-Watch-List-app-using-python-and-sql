import datetime
import os
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Add image to a movie.
9) Export movie image.
10) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()

    image_path = input("Image file path (leave blank to skip): ").strip()
    image_data = None
    if image_path and os.path.isfile(image_path):
        with open(image_path, "rb") as f:
            image_data = f.read()
        print(f"Image loaded from '{image_path}' ({len(image_data)} bytes).")
    elif image_path:
        print(f"File '{image_path}' not found. Movie will be added without an image.")

    database.add_movie(title, release_timestamp, image_data)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_date.strftime("%b %d %Y")
        has_image = " [has image]" if (len(movie) > 3 and movie[3]) else ""
        print(f"{movie[0]}: {movie[1]} (on {human_date}){has_image}")
    print("---- \n")


def prompt_add_movie_image():
    movie_id = input("Movie ID: ").strip()
    image_path = input("Image file path: ").strip()

    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    with open(image_path, "rb") as f:
        image_data = f.read()

    database.add_movie_image(movie_id, image_data)
    print(f"Image ({len(image_data)} bytes) saved for movie ID {movie_id}.")


def prompt_export_movie_image():
    movie_id = input("Movie ID: ").strip()
    result = database.get_movie_image(movie_id)

    if result is None:
        print(f"No movie found with ID {movie_id}.")
        return

    movie_id_val, title, image_data = result

    if not image_data:
        print(f"Movie '{title}' (ID {movie_id_val}) has no image stored.")
        return

    default_name = f"movie_{movie_id_val}_image.png"
    output_path = input(f"Save image as (default: {default_name}): ").strip() or default_name

    with open(output_path, "wb") as f:
        f.write(image_data)

    print(f"Image for '{title}' exported to '{output_path}' ({len(image_data)} bytes).")


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


print(welcome)
database.create_tables()

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
        prompt_add_movie_image()
    elif user_input == "9":
        prompt_export_movie_image()
    else:
        print("Invalid input, please try again!")
