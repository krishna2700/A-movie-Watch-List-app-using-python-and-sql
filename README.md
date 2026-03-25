# Movie Watchlist App

A command-line movie watchlist application built with Python and SQLite that allows users to track movies they want to watch and movies they've already watched.

## Features

- **Add Movies**: Add new movies with title and release date
- **View Movies**: View all movies or filter by upcoming releases
- **Track Watched Movies**: Mark movies as watched by specific users
- **User Management**: Add and manage multiple users
- **Search Functionality**: Search for movies by partial title match
- **Database Persistence**: All data is stored in a SQLite database

## Technologies Used

- **Python 3**: Core programming language
- **SQLite3**: Database for storing movies, users, and watch history
- **datetime**: For handling movie release dates and timestamps

## Database Schema

The application uses three main tables:

### Movies Table
- `id` (INTEGER PRIMARY KEY): Unique movie identifier
- `title` (TEXT): Movie title
- `release_timestamp` (REAL): Release date stored as Unix timestamp

### Users Table
- `username` (TEXT PRIMARY KEY): Unique username

### Watched Table
- `user_username` (TEXT): Foreign key to users table
- `movie_id` (INTEGER): Foreign key to movies table

## Installation

1. Clone the repository:
```bash
git clone https://github.com/krishna2700/A-movie-Watch-List-app-using-python-and-sql.git
cd A-movie-Watch-List-app-using-python-and-sql
```

2. Ensure you have Python 3.8+ installed:
```bash
python --version
```

3. No additional dependencies required (uses Python standard library)

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
   - Enter a username

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
   - Enter the movie ID (from the movie list)

5. **View your watched movies**:
   - Select option `5`
   - Enter your username
   - See all movies you've marked as watched

6. **Search for movies**:
   - Select option `7`
   - Enter a partial movie title
   - See matching results

## File Structure

```
.
├── app.py          # Main application with CLI interface
├── database.py     # Database operations and SQL queries
├── data.db         # SQLite database file (created on first run)
├── logo.svg        # Application logo
└── README.md       # This file
```

## Code Structure

### app.py
Contains the main application logic:
- Interactive menu system
- User input handling
- Display formatting for movie lists
- Coordination between user interface and database operations

### database.py
Handles all database operations:
- Table creation and schema management
- CRUD operations for movies, users, and watch history
- Search functionality
- Database indexing for performance

## Features in Detail

### Date Handling
- Release dates are stored as Unix timestamps for easy comparison
- Dates are displayed in human-readable format (e.g., "Jan 15 2024")
- Default to today's date if no release date is provided

### Search
- Case-insensitive partial matching
- Uses SQL LIKE operator for flexible searching

### Performance
- Database index on release_timestamp for faster upcoming movie queries
- Connection reuse for efficient database operations

## Future Enhancements

Potential features to add:
- Movie ratings and reviews
- Genre categorization
- Movie recommendations
- Export watchlist to CSV/JSON
- Web interface
- Movie poster integration
- Sorting options (by date, title, etc.)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Author

Created by krishna2700

## Repository

https://github.com/krishna2700/A-movie-Watch-List-app-using-python-and-sql
