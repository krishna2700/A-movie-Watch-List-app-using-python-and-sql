# Movie Watchlist App

A Python-based command-line application for managing your movie watchlist using SQLite database.

## Overview

This application allows users to track movies they want to watch, mark movies as watched, and search through their collection. It uses SQLite for data persistence and provides a simple menu-driven interface.

## Features

- Add new movies with release dates
- View upcoming movies (releases after today)
- View all movies in the database
- Track watched movies per user
- Multi-user support
- Search movies by partial title match
- Automatic database schema creation
- Indexed queries for performance

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. No additional dependencies required - the app uses Python standard library only.

## Quick Start

Run the application:
```bash
python app.py
```

## Project Structure

```
.
├── app.py          # Main application with menu interface
├── database.py     # Database operations and queries
├── data.db         # SQLite database file (created on first run)
└── README.md       # This file
```

## Database Schema

The application uses three main tables:

- **movies**: Stores movie information (id, title, release_timestamp)
- **users**: Stores user accounts (username)
- **watched**: Junction table linking users to watched movies

See [DATABASE.md](DATABASE.md) for detailed schema information.

## Usage

See [USAGE.md](USAGE.md) for detailed usage instructions and examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.