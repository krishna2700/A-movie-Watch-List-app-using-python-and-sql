# Movie Watch List App

A Python-based command-line application for managing your movie watchlist using SQLite database.

## Overview

This application allows users to:
- Add movies to their watchlist
- Track upcoming movies
- Mark movies as watched
- Search for movies
- Manage multiple users and their watched movies

## Features

- **Movie Management**: Add new movies with release dates
- **Upcoming Movies**: View movies that haven't been released yet
- **Watch Tracking**: Mark movies as watched for specific users
- **User Management**: Add and manage multiple users
- **Search Functionality**: Search movies by partial title match
- **SQLite Database**: Persistent data storage using SQLite

## Project Structure

```
.
├── README.md           # Main project documentation
├── app.py              # Main application entry point
├── database.py         # Database operations module
├── data.db             # SQLite database file
└── SETUP.md            # Installation and setup guide
```

## Quick Start

1. **Prerequisites**
   - Python 3.x
   - SQLite3 (usually included with Python)

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Follow the Menu**
   - Select options 1-7 to interact with the application
   - Select option 8 to exit

## Menu Options

1. **Add new movie** - Add a movie with title and release date
2. **View upcoming movies** - Show movies not yet released
3. **View all movies** - Display all movies in the database
4. **Add watched movie** - Mark a movie as watched for a user
5. **View watched movies** - Show movies watched by a specific user
6. **Add user to the app** - Register a new user
7. **Search for a movie** - Find movies by partial title match
8. **Exit** - Close the application

## Documentation

- [Database Module Documentation](database/README.md) - Database operations and schema
- [Application Module Documentation](app/README.md) - Application logic and user interface
- [Setup Guide](SETUP.md) - Detailed installation instructions

## Database Schema

The application uses three main tables:
- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Stores user information (username)
- **watched**: Tracks which users have watched which movies

## Example Usage

```bash
# Start the application
python app.py

# Add a user
Select option 6, enter username: "john"

# Add a movie
Select option 1, enter title: "Inception", release date: "16-07-2010"

# View all movies
Select option 3

# Mark movie as watched
Select option 4, enter username: "john", movie ID: 1

# View watched movies
Select option 5, enter username: "john"
```

## Technologies Used

- **Python 3**: Core programming language
- **SQLite3**: Database management
- **datetime**: Date and time handling

## License

This project is open source and available for educational purposes.
