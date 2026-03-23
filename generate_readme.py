#!/usr/bin/env python3
"""
README Generator Script
This script generates a comprehensive README.md file for the Movie Watchlist application.
"""

def generate_readme():
    """Generate README.md content for the Movie Watchlist application."""

    readme_content = """# Movie Watchlist Application

A full-stack web application for managing movie watchlists built with Python, Flask, SQLite, and HTML/JavaScript.

## Overview

This application allows users to:
- Add movies to a watchlist with release dates
- View all movies or filter upcoming releases
- Mark movies as watched
- Track multiple users and their watched movies
- Search for movies by title
- Delete movies from the watchlist

## Features

- **Movie Management**: Add, view, search, and delete movies
- **User Tracking**: Support for multiple users with individual watchlists
- **Watched Movies**: Track which movies each user has watched
- **Upcoming Movies**: Filter to see only upcoming releases
- **RESTful API**: Clean API endpoints for all operations
- **Database**: SQLite database with indexed queries for performance
- **Web Interface**: User-friendly HTML/JavaScript frontend

## Technology Stack

- **Backend**: Python 3 with Flask framework
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **API**: RESTful endpoints with JSON responses
- **CORS**: Cross-Origin Resource Sharing enabled

## Project Structure

```
.
├── app.py              # Flask application with API endpoints
├── database.py         # Database operations and SQL queries
├── index.html          # Frontend web interface
├── data.db             # SQLite database file
└── README.md           # This file
```

## Database Schema

### Movies Table
- `id` (INTEGER PRIMARY KEY): Unique movie identifier
- `title` (TEXT): Movie title
- `release_timestamp` (REAL): Release date as Unix timestamp

### Users Table
- `username` (TEXT PRIMARY KEY): Unique username

### Watched Table
- `user_username` (TEXT): Foreign key to users table
- `movie_id` (INTEGER): Foreign key to movies table

## API Endpoints

### Get Movies
```
GET /api/movies
GET /api/movies?upcoming=true
```
Returns list of all movies or only upcoming movies.

### Add Movie
```
POST /api/movies
Content-Type: application/json

{
  "title": "Movie Title",
  "release_date": "2026-12-31"
}
```

### Delete Movie
```
DELETE /api/movies/<movie_id>
```

### Get Watched Movies
```
GET /api/users/<username>/watched
```
Returns list of movies watched by a specific user.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install required dependencies:
```bash
pip install flask flask-cors
```

3. Run the application:
```bash
python app.py
```

4. Access the application:
Open your browser and navigate to `http://localhost:5000`

## Usage

### Web Interface
1. Open `http://localhost:5000` in your web browser
2. Use the interface to add movies, view your watchlist, and manage watched movies

### API Usage Examples

**Add a movie:**
```bash
curl -X POST http://localhost:5000/api/movies \\
  -H "Content-Type: application/json" \\
  -d '{"title": "Inception", "release_date": "2026-07-16"}'
```

**Get all movies:**
```bash
curl http://localhost:5000/api/movies
```

**Get upcoming movies:**
```bash
curl http://localhost:5000/api/movies?upcoming=true
```

**Delete a movie:**
```bash
curl -X DELETE http://localhost:5000/api/movies/1
```

## Development

The application uses:
- Flask for the web server and routing
- SQLite for persistent data storage
- Datetime module for handling release dates
- CORS for cross-origin requests

### Database Initialization
The database tables are automatically created when the application starts via `database.create_tables()`.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for educational purposes.

## Author

Movie Watchlist Application - Python & SQL Project
"""

    return readme_content


def main():
    """Main function to generate and write README.md file."""
    print("Generating README.md...")

    readme_content = generate_readme()

    # Write to README.md file
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("✓ README.md has been successfully generated!")
    print(f"✓ Total lines: {len(readme_content.splitlines())}")
    print(f"✓ Total characters: {len(readme_content)}")


if __name__ == "__main__":
    main()
