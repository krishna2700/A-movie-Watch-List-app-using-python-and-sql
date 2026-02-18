# Application API Documentation

This document describes the application interface (`app.py`) and user interaction flow.

## Overview

The `app.py` module provides the main user interface for the Movie Watch List application. It implements a command-line menu system that allows users to interact with the database through various operations.

## Main Components

### Menu System

The application uses a continuous loop that displays a menu and processes user input until the user selects option 8 (Exit).

### Functions

#### `prompt_add_movie()`
Prompts the user to add a new movie to the database.

**User Input:**
- Movie title (required)
- Release date in format `dd-mm-YYYY` (optional, defaults to today)

**Example:**
```
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010
```

#### `print_movie_list(heading, movies)`
Formats and displays a list of movies.

**Parameters:**
- `heading` (str): Section heading (e.g., "Upcoming", "All", "Watched")
- `movies` (list): List of movie tuples `(id, title, release_timestamp)`

**Output Format:**
```
-- Upcoming movies --
1: The Matrix (on Mar 31 1999)
2: Inception (on Jul 16 2010)
---- 
```

#### `prompt_watch_movie()`
Prompts the user to mark a movie as watched.

**User Input:**
- Username
- Movie ID

**Example:**
```
Username: john_doe
Movie ID: 1
```

#### `prompt_get_watched_movies()`
Prompts for a username and retrieves their watched movies.

**User Input:**
- Username

**Returns:**
- List of watched movies or None if user has no watched movies

#### `prompt_add_user()`
Prompts the user to add a new user to the system.

**User Input:**
- Username

**Example:**
```
Username: jane_smith
```

#### `prompt_search_movies()`
Prompts the user to search for movies by partial title.

**User Input:**
- Partial movie title

**Returns:**
- List of matching movies or None if no matches found

**Example:**
```
Enter partial movie title: Matrix
```

## Menu Options

### 1. Add new movie
Calls `prompt_add_movie()` to add a movie to the database.

### 2. View upcoming movies
Retrieves and displays movies with release dates in the future using `database.get_movies(upcoming=True)`.

### 3. View all movies
Retrieves and displays all movies in the database using `database.get_movies()`.

### 4. Add watched movie
Calls `prompt_watch_movie()` to record that a user watched a movie.

### 5. View watched movies
Calls `prompt_get_watched_movies()` and displays the results. Shows a message if the user has no watched movies.

### 6. Add user to the app
Calls `prompt_add_user()` to register a new user.

### 7. Search for a movie
Calls `prompt_search_movies()` and displays matching movies. Shows a message if no movies are found.

### 8. Exit
Terminates the application loop.

## Application Flow

1. **Initialization:**
   - Displays welcome message
   - Creates database tables
   - Enters main menu loop

2. **Main Loop:**
   - Displays menu
   - Reads user input
   - Executes corresponding function
   - Repeats until user selects Exit

3. **Error Handling:**
   - Invalid menu selections display: "Invalid input, please try again!"
   - No error handling for database operations (may crash on invalid input)

## Date Format

The application uses the following date format:
- **Input:** `dd-mm-YYYY` (e.g., "31-03-1999")
- **Display:** `MMM DD YYYY` (e.g., "Mar 31 1999")
- **Storage:** Unix timestamp (float)

## Example Session

```
Welcome to the watchlist app!
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.

Your selection: 1
Movie title: The Matrix
Release date (dd-mm-YYYY): 31-03-1999
Please select one of the following options:
...
Your selection: 8
```

## Limitations

- No input validation for movie IDs (may cause errors)
- No duplicate username checking (may cause database errors)
- No error handling for invalid date formats
- No confirmation prompts for destructive operations
- Single database connection shared across all operations
