import datetime
import database


menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()

def prompt_add_movie():
    title = input("Movie title: ") # Get movie title from user
    release_date = input("Release date (dd-mm-yyyy): ") # Get release date from user
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y") # Parse the date string into a datetime object
    timestamp = parsed_date.timestamp() # Convert datetime object to a timestamp
    database.add_movie(title, timestamp) # Add movie to the database
    print(f"Added {title} to the watchlist.") # Confirm addition to user


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
            release_date = datetime.datetime.fromtimestamp(movie[1]) # Convert timestamp back to datetime object
            release_date = release_date.strftime("%d %b %Y") # Format datetime object into a readable string 
            print(f"{movie[0]} (on {release_date})") # Print movie title and release date 
    print("----\n")

def prompt_watch_movie():
    movies = database.get_movies() # Get all movies from the database
    print_movie_list("All", movies) # Print the list of all movies
    movie_title = input("Enter the title of the movie you have watched: ") # Get movie title from user
    database.watch_movie(movie_title) # Mark the movie as watched in the database
    print("Movie marked as watched.") # Confirm action to user

    
while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie() # Prompt user to add a new movie
    elif user_input == "2":
        movies = database.get_movies(True) # Get upcoming movies from the database
        print_movie_list("Upcoming", movies) # Print the list of upcoming movies
    elif user_input == "3":
         movies = database.get_movies() # Get all movies from the database
         print_movie_list("All", movies) # Print the list of all movies
    elif user_input == "4":
        prompt_watch_movie() # Prompt user to mark a movie as watched
    elif user_input == "5":
        movies = database.get_watched_movies() # Get watched movies from the database
        print_movie_list("Watched", movies) # Print the list of watched movies
    else:
        print("Invalid input, please try again!")