# Movie Watchlist Application

A command-line movie watchlist application built with Python and SQLite, allowing users to track movies they want to watch and movies they've already watched.

## Features

- **Add Movies**: Add new movies with title and release date
- **View Movies**: View all movies or filter by upcoming releases
- **User Management**: Create user accounts to track individual watchlists
- **Watch Tracking**: Mark movies as watched for specific users
- **Search**: Search for movies by partial title match
- **Database**: SQLite database with indexed queries for performance

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone this repository
2. No additional dependencies required - uses Python standard library only

## Usage

Run the application:

```bash
python app.py
```

### Menu Options

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - See movies releasing after today
3. **View all movies** - Display complete movie list
4. **Add watched movie** - Mark a movie as watched for a user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Create a new user account
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

### Date Format

When adding movies, use the date format: `dd-mm-YYYY` (e.g., 14-02-2026)

If no date is provided, today's date will be used.

## Database Schema

The application uses three main tables:

- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Stores user accounts (username)
- **watched**: Junction table linking users to watched movies

An index on `release_timestamp` optimizes upcoming movie queries.

## Project Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## Additional Files

This repository also contains "Hello World" examples in multiple programming languages:

- `hello_world.py` - Python
- `hello_world.js` - JavaScript (Node.js)
- `hello_world.c` - C
- `hello_world.rb` - Ruby
- `HelloWorld.java` - Java

### Running Hello World Examples

**Python:**
```bash
python hello_world.py
```

**JavaScript:**
```bash
node hello_world.js
```

**C:**
```bash
gcc hello_world.c -o hello_world
./hello_world
```

**Ruby:**
```bash
ruby hello_world.rb
```

**Java:**
```bash
javac HelloWorld.java
java HelloWorld
```

## Example Workflow

1. Start the application: `python app.py`
2. Add a user: Select option `6`, enter username
3. Add movies: Select option `1`, enter movie details
4. Mark movie as watched: Select option `4`, enter username and movie ID
5. View watched movies: Select option `5`, enter username
6. Search for movies: Select option `7`, enter search term

## License

This project is provided as-is for educational purposes.
