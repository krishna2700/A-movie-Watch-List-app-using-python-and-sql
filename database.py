import datetime  # Importing the datetime module for working with dates and times
import sqlite3   # Importing the sqlite3 module to interact with SQLite databases

# SQL statement to create a table named 'movies' if it doesn’t already exist
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,                -- Column for movie title (string)
    release_timestamp REAL,    -- Column for movie release date stored as a timestamp (float)
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watchlist (
    watcher_name TEXT,           -- Column for the name of the person who watched the movie (string)
    title TEXT,             -- Column for the name of the person who watched the movie (string)
);"""

# SQL statement to insert a new movie into the movies table
# Default "watched" is set to 0 (meaning not watched yet)
INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?);"

# SQL statement to delete a movie from the table
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"

# SQL statement to select all movies from the table
SELECT_ALL_MOVIES = "SELECT * FROM movies;"

# SQL statement to select only movies that are upcoming (release date after today)
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"

# SQL statement to select only movies that have been watched
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"

# SQL statement to insert a new watched movie into the watchlist table
INSERT_MOVIE_WATCHED = "INSERT INTO watched (watcher_name, title) VALUES (?, ?);"

# SQL statement to update a movie's watched status to 1 (meaning watched)
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"



# Establish a connection to the database file "data.db"
# If the file does not exist, SQLite will create it
connection = sqlite3.connect("data.db")


# Function to create the movies table
def create_tables():
    with connection:  # Opens a transaction
        connection.execute(CREATE_MOVIES_TABLE)  # Executes the create table SQL
        connection.execute(CREATE_WATCHLIST_TABLE)  # Executes the create table SQL


# Function to add a new movie to the database
def add_movie(title, release_timestamp):
    with connection:  # Opens a transaction
        connection.execute(INSERT_MOVIE, (title, release_timestamp))  # Inserts movie into the table


# Function to retrieve movies from the database
# If upcoming=True, only upcoming movies are returned
def get_movies(upcoming=False):
    with connection:  # Opens a transaction
        cursor = connection.cursor()  # Creates a cursor to run queries
        if upcoming:  # If user wants upcoming movies
            today_timestamp = datetime.datetime.today().timestamp()  # Get today's date as timestamp
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))  # Query for upcoming movies
        else:  # Otherwise return all movies
            cursor.execute(SELECT_ALL_MOVIES)  # Query for all movies
        return cursor.fetchall()  # Return the list of movies fetched


def watch_movie(username,title):
    with connection:  # Opens a transaction
        connection.execute(DELETE_MOVIE, (title,))  # Deletes the movie from the table
        connection.execute(INSERT_MOVIE_WATCHED, (username,title,))  # Inserts movie into the watched table


# Function to retrieve all watched movies
def get_watched_movies(username):
    with connection:  # Opens a transaction
        cursor = connection.cursor()  # Creates a cursor to run queries
        cursor.execute(SELECT_WATCHED_MOVIES,(username))  # Query for watched movies
        return cursor.fetchall()  # Return the list of watched movies