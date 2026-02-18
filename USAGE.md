# Usage Guide

## Getting Started

### Running the Application

Start the application by running:

```bash
python app.py
```

You'll see the welcome message and main menu:

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

Your selection:
```

## Menu Options

### 1. Add New Movie

Add a movie to your watchlist.

**Steps:**
1. Select option `1`
2. Enter the movie title when prompted
3. Enter the release date in `dd-mm-YYYY` format (or press Enter for today's date)

**Example:**
```
Your selection: 1
Movie title: The Matrix Resurrections
Release date (dd-mm-YYYY): 22-12-2021
```

**Notes:**
- If you press Enter without typing a date, the current date is used
- The date format must be `dd-mm-YYYY` (e.g., `15-01-2025`)
- The movie is automatically assigned a unique ID

### 2. View Upcoming Movies

Display all movies with release dates after today.

**Steps:**
1. Select option `2`

**Example Output:**
```
-- Upcoming movies --
3: Dune Part Three (on Mar 15 2026)
5: Avatar 4 (on Dec 20 2026)
----
```

**Notes:**
- Only shows movies with release dates in the future
- Movies are listed with their ID, title, and formatted release date
- Uses an indexed query for fast performance

### 3. View All Movies

Display every movie in the database, regardless of release date.

**Steps:**
1. Select option `3`

**Example Output:**
```
-- All movies --
1: The Shawshank Redemption (on Sep 23 1994)
2: The Godfather (on Mar 24 1972)
3: Dune Part Three (on Mar 15 2026)
4: Inception (on Jul 16 2010)
----
```

### 4. Add Watched Movie

Mark a movie as watched by a specific user.

**Steps:**
1. Select option `4`
2. Enter the username
3. Enter the movie ID (from the movie list)

**Example:**
```
Your selection: 4
Username: john_doe
Movie ID: 2
```

**Prerequisites:**
- The user must exist in the database (add via option 6)
- The movie ID must exist (check via option 3)

**Notes:**
- Creates a relationship between the user and the movie
- A user can mark the same movie as watched multiple times (no duplicate prevention)

### 5. View Watched Movies

Display all movies watched by a specific user.

**Steps:**
1. Select option `5`
2. Enter the username

**Example Output:**
```
Your selection: 5
Username: john_doe
-- Watched movies --
2: The Godfather (on Mar 24 1972)
4: Inception (on Jul 16 2010)
----
```

**If No Movies Watched:**
```
Your selection: 5
Username: jane_doe
That user has watched no movies yet!
```

**Notes:**
- Only shows movies the specified user has marked as watched
- Uses a JOIN query to combine user, watched, and movie data

### 6. Add User to the App

Create a new user account.

**Steps:**
1. Select option `6`
2. Enter a unique username

**Example:**
```
Your selection: 6
Username: alice_smith
```

**Notes:**
- Username must be unique
- No password or additional information required
- Users must exist before they can mark movies as watched

### 7. Search for a Movie

Search for movies by partial title match (case-insensitive).

**Steps:**
1. Select option `7`
2. Enter any part of the movie title

**Example:**
```
Your selection: 7
Enter partial movie title: matrix
-- Movies found --
1: The Matrix (on Mar 31 1999)
2: The Matrix Reloaded (on May 15 2003)
3: The Matrix Resurrections (on Dec 22 2021)
----
```

**If No Results:**
```
Your selection: 7
Enter partial movie title: xyz123
Found no movies for that search term!
```

**Notes:**
- Search is case-insensitive
- Matches any part of the title (beginning, middle, or end)
- Uses SQL LIKE with wildcards (`%search_term%`)

### 8. Exit

Close the application.

**Steps:**
1. Select option `8`

The application will terminate gracefully.

## Common Workflows

### Adding and Tracking a New Movie

1. Add a user (option 6):
   ```
   Your selection: 6
   Username: moviefan
   ```

2. Add the movie (option 1):
   ```
   Your selection: 1
   Movie title: Oppenheimer
   Release date (dd-mm-YYYY): 21-07-2023
   ```

3. View all movies to get the ID (option 3):
   ```
   -- All movies --
   1: Oppenheimer (on Jul 21 2023)
   ----
   ```

4. Mark as watched (option 4):
   ```
   Your selection: 4
   Username: moviefan
   Movie ID: 1
   ```

5. Verify watched list (option 5):
   ```
   Your selection: 5
   Username: moviefan
   -- Watched movies --
   1: Oppenheimer (on Jul 21 2023)
   ----
   ```

### Planning Your Movie Calendar

1. View upcoming movies (option 2):
   ```
   -- Upcoming movies --
   5: Dune Part Three (on Mar 15 2026)
   7: The Batman Part II (on Oct 02 2026)
   ----
   ```

2. Search for a specific franchise (option 7):
   ```
   Enter partial movie title: dune
   -- Movies found --
   3: Dune (on Oct 22 2021)
   4: Dune Part Two (on Mar 01 2024)
   5: Dune Part Three (on Mar 15 2026)
   ----
   ```

### Managing Multiple Users

Each user can maintain their own watched list:

**User 1:**
```
Your selection: 5
Username: alice
-- Watched movies --
1: The Godfather (on Mar 24 1972)
----
```

**User 2:**
```
Your selection: 5
Username: bob
-- Watched movies --
2: Inception (on Jul 16 2010)
3: Interstellar (on Nov 07 2014)
----
```

## Date Format Reference

### Input Format

When adding movies, use: `dd-mm-YYYY`

**Examples:**
- `01-01-2025` → January 1st, 2025
- `15-06-2024` → June 15th, 2024
- `31-12-2023` → December 31st, 2023

### Display Format

Movies are displayed as: `Mon DD YYYY`

**Examples:**
- `Jan 01 2025`
- `Jun 15 2024`
- `Dec 31 2023`

### Default Date

Pressing Enter without entering a date uses today's date automatically.

## Error Handling

### Invalid Menu Selection

```
Your selection: 99
Invalid input, please try again!
```

### Non-existent User (when viewing watched movies)

```
That user has watched no movies yet!
```

### Non-existent Movie (when searching)

```
Found no movies for that search term!
```

## Tips and Best Practices

1. **Add Users First**: Create user accounts before trying to mark movies as watched

2. **Note Movie IDs**: When adding movies, use option 3 to view all movies and their IDs before marking them as watched

3. **Use Search**: If you have many movies, use option 7 to quickly find specific titles

4. **Track Release Dates**: Use option 2 regularly to see what's coming up soon

5. **Consistent Usernames**: Use the same username each time to maintain your personal watchlist

6. **Date Format**: Always use the `dd-mm-YYYY` format to avoid errors (e.g., `25-12-2025`, not `12/25/2025`)

## Database Location

All data is stored in `data.db` in the application directory. This file:
- Is created automatically on first run
- Persists between sessions
- Can be backed up by copying the file
- Can be reset by deleting it (the app will create a new empty database)

## Advanced Usage

### Backing Up Your Data

```bash
cp data.db data_backup_$(date +%Y%m%d).db
```

### Viewing the Database Directly

Using SQLite command-line tool:

```bash
sqlite3 data.db
```

Then run SQL queries:
```sql
SELECT * FROM movies;
SELECT * FROM users;
SELECT * FROM watched;
```

Exit with `.quit`

### Resetting the Database

```bash
rm data.db
python app.py  # Creates fresh database
```

## Troubleshooting

### Problem: "That user has watched no movies yet!"

**Solution**: Make sure the username exists. Add it using option 6 first.

### Problem: Movie not appearing in upcoming movies

**Solution**: Check if the release date is in the future. Use option 3 to view all movies and verify the date.

### Problem: Can't find a movie with search

**Solution**:
- Try a shorter search term
- Check spelling
- Use option 3 to view all movies

### Problem: Wrong date displayed

**Solution**: Verify you used `dd-mm-YYYY` format when adding the movie. If wrong, you'll need to add it again with the correct date.
