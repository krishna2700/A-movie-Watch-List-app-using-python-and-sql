# Movie Watchlist App

A command-line application for managing your movie watchlist using Python and SQLite.

## Features

- Add movies with release dates
- View all movies or filter upcoming releases
- Track watched movies per user
- Multi-user support
- Search movies by title
- Persistent SQLite database storage

## Prerequisites

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - uses Python standard library only.

## Usage

Run the application:
```bash
python app.py
```

### Menu Options

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - Display movies releasing after today
3. **View all movies** - Display complete movie list
4. **Add watched movie** - Mark a movie as watched by a user
5. **View watched movies** - See all movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

## Database Structure

The application uses three main tables:

- **movies** - Stores movie information (id, title, release_timestamp)
- **users** - Stores registered usernames
- **watched** - Junction table linking users to movies they've watched

## File Structure

```
.
├── app.py         # Main application with CLI interface
├── database.py    # Database operations and SQLite queries
├── data.db        # SQLite database file (auto-created)
└── README.md      # This file
```

## Example Workflow

1. Start the app and add a user
2. Add movies to your watchlist with release dates
3. View upcoming movies to see what's coming soon
4. Mark movies as watched when you've seen them
5. Search for specific movies in your collection

## License

This project is open source and available for educational purposes.
