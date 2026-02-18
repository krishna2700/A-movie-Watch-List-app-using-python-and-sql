# Application Module Documentation

## Overview

The `app.py` module is the main entry point for the Movie Watch List application. It provides a command-line interface for users to interact with the movie database.

## File Location

`/app.py`

## Main Components

### Menu System

The application uses a simple text-based menu system with numbered options:

```
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.

Your selection: 
```

### Core Functions

#### `prompt_add_movie()`
Prompts the user to add a new movie to the database.

**User Input:**
- Movie title
- Release date (format: dd-mm-YYYY) or defaults to today's date

**Process:**
1. Gets movie title from user
2. Gets release date (optional, defaults to today)
3. Converts date to timestamp
4. Calls `database.add_movie()`

**Example:**
```
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010
```

---

#### `print_movie_list(heading, movies)`
Formats and displays a list of movies.

**Parameters:**
- `heading` (str): Section heading (e.g., "Upcoming", "All", "Watched")
- `movies` (list): List of movie tuples `[(id, title, timestamp), ...]`

**Output Format:**
```
-- Upcoming movies --
1: Inception (on Jul 16 2010)
2: The Matrix (on Mar 31 1999)
---- 
```

---

#### `prompt_watch_movie()`
Prompts user to mark a movie as watched.

**User Input:**
- Username
- Movie ID

**Process:**
1. Gets username
2. Gets movie ID
3. Calls `database.watch_movie()`

**Example:**
```
Username: john_doe
Movie ID: 1
```

---

#### `prompt_get_watched_movies()`
Retrieves and displays watched movies for a user.

**User Input:**
- Username

**Returns:**
- List of watched movies or None

**Process:**
1. Gets username
2. Calls `database.get_watched_movies()`
3. Returns movie list

---

#### `prompt_add_user()`
Adds a new user to the system.

**User Input:**
- Username

**Process:**
1. Gets username
2. Calls `database.add_user()`

**Example:**
```
Username: john_doe
```

---

#### `prompt_search_movies()`
Searches for movies by partial title.

**User Input:**
- Partial movie title

**Returns:**
- List of matching movies

**Process:**
1. Gets search term
2. Calls `database.search_movies()`
3. Returns results

**Example:**
```
Enter partial movie title: inception
```

---

## Main Application Loop

The application runs in a continuous loop until the user selects option 8:

```python
while (user_input := input(menu)) != "8":
    # Process user input
```

### Menu Option Handlers

1. **Option 1**: Add new movie
   - Calls `prompt_add_movie()`

2. **Option 2**: View upcoming movies
   - Gets upcoming movies from database
   - Displays formatted list

3. **Option 3**: View all movies
   - Gets all movies from database
   - Displays formatted list

4. **Option 4**: Add watched movie
   - Calls `prompt_watch_movie()`

5. **Option 5**: View watched movies
   - Gets watched movies for user
   - Displays formatted list or error message

6. **Option 6**: Add user
   - Calls `prompt_add_user()`

7. **Option 7**: Search movies
   - Searches and displays results or "no movies found" message

8. **Option 8**: Exit
   - Breaks the loop and exits

**Invalid Input:**
- Displays error message: "Invalid input, please try again!"

## Application Flow

1. **Initialization:**
   - Prints welcome message
   - Calls `database.create_tables()` to ensure database is set up

2. **Main Loop:**
   - Displays menu
   - Waits for user input
   - Processes selection
   - Returns to menu

3. **Exit:**
   - User selects option 8
   - Loop terminates
   - Application closes

## Date Formatting

The application uses the following date formats:

- **Input Format**: `dd-mm-YYYY` (e.g., "16-07-2010")
- **Display Format**: `MMM dd YYYY` (e.g., "Jul 16 2010")
- **Storage Format**: Unix timestamp (float)

## Dependencies

- `datetime`: For date parsing and formatting
- `database`: Custom module for database operations

## User Experience Features

- **Default Values**: Release date defaults to today if not provided
- **Error Messages**: Clear feedback for invalid input or empty results
- **Formatted Output**: Human-readable date formatting in movie lists
- **Case-Sensitive Search**: Movie search is case-sensitive

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

Your selection: 6
Username: alice

Your selection: 1
Movie title: The Matrix
Release date (dd-mm-YYYY): 31-03-1999

Your selection: 3
-- All movies --
1: The Matrix (on Mar 31 1999)
---- 

Your selection: 8
```

## Error Handling

- Invalid menu selections display error messages
- Empty search results show appropriate messages
- Database errors are not explicitly caught (may need enhancement)

## Future Enhancements

Potential improvements:
- Input validation for dates
- Error handling for database operations
- Case-insensitive search
- Movie deletion functionality
- User authentication
- Export/import functionality
