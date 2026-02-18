# Movie Watchlist App

A command-line application built with Python and SQLite for managing your movie watchlist. Track movies you want to watch, mark them as watched, and search through your collection.

## Features

- **Add Movies**: Add new movies to your watchlist with release dates
- **View Movies**: See all movies or filter by upcoming releases
- **Track Watched Movies**: Mark movies as watched and view your watch history
- **User Management**: Support for multiple users with individual watchlists
- **Search Functionality**: Search for movies by partial title match
- **Date Tracking**: Automatically tracks release dates and formats them in a human-readable format

## Project Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## Database Schema

The application uses SQLite with three main tables:

### Movies Table
- `id` (INTEGER PRIMARY KEY): Unique movie identifier
- `title` (TEXT): Movie title
- `release_timestamp` (REAL): Release date as Unix timestamp

### Users Table
- `username` (TEXT PRIMARY KEY): Unique username

### Watched Table
- `user_username` (TEXT): Foreign key to users table
- `movie_id` (INTEGER): Foreign key to movies table

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/krishna2700/A-movie-Watch-List-app-using-python-and-sql.git
cd A-movie-Watch-List-app-using-python-and-sql
```

2. No additional dependencies required - uses Python standard library only!

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

When you run the app, you'll see the following menu:

```
1) Add new movie
2) View upcoming movies
3) View all movies
4) Add watched movie
5) View watched movies
6) Add user to the app
7) Search for a movie
8) Exit
```

### Example Workflow

1. **Add a user**:
   - Select option `6`
   - Enter your username

2. **Add a movie**:
   - Select option `1`
   - Enter movie title
   - Enter release date in format `dd-mm-YYYY` (or press Enter for today's date)

3. **View upcoming movies**:
   - Select option `2`
   - See all movies with release dates in the future

4. **Mark a movie as watched**:
   - Select option `4`
   - Enter your username
   - Enter the movie ID (shown when viewing movies)

5. **View your watched movies**:
   - Select option `5`
   - Enter your username
   - See all movies you've marked as watched

6. **Search for movies**:
   - Select option `7`
   - Enter partial movie title
   - See matching results

## Code Structure

### app.py
Contains the main application logic:
- Menu-driven interface
- User input handling
- Movie list formatting and display
- Date formatting utilities

### database.py
Handles all database operations:
- Table creation and indexing
- CRUD operations for movies, users, and watched records
- SQL query definitions
- Database connection management

## Features in Detail

### Date Handling
- Accepts dates in `dd-mm-YYYY` format
- Stores dates as Unix timestamps for efficient querying
- Displays dates in human-readable format (`Mon DD YYYY`)
- Defaults to current date if no date is provided

### Search Functionality
- Case-insensitive partial matching
- Uses SQL LIKE operator for flexible searches
- Returns all matching movies

### Performance Optimization
- Includes database index on `release_timestamp` for faster queries
- Uses parameterized queries to prevent SQL injection
- Context managers for proper connection handling

## Database Operations

The application automatically:
- Creates necessary tables on first run
- Creates indexes for optimized queries
- Handles foreign key relationships
- Manages database connections safely

## Future Enhancements

Potential features to add:
- Movie ratings and reviews
- Genre categorization
- Export watchlist to CSV/JSON
- Movie recommendations
- Integration with movie APIs (TMDB, OMDB)
- Web interface
- Movie poster storage

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project to demonstrate Python and SQL integration.

## Troubleshooting

**Database locked error**: Make sure only one instance of the app is running at a time.

**Invalid date format**: Ensure dates are entered in `dd-mm-YYYY` format (e.g., `25-12-2024`).

**Movie ID not found**: Use option 3 to view all movies and their IDs before marking as watched.
