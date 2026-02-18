# Setup Guide

This guide will help you set up and run the Movie Watch List application.

## Prerequisites

- **Python 3.x** (Python 3.6 or higher recommended)
- **SQLite3** (usually included with Python)
- **Command-line terminal**

## Installation Steps

### 1. Check Python Installation

Verify Python is installed:
```bash
python --version
# or
python3 --version
```

### 2. Clone or Download the Project

If using git:
```bash
git clone <repository-url>
cd <project-directory>
```

Or download and extract the project files.

### 3. Verify Project Files

Ensure you have the following files:
- `app.py` - Main application
- `database.py` - Database module
- `README.md` - Project documentation

### 4. Run the Application

Execute the main application:
```bash
python app.py
# or
python3 app.py
```

The database file (`data.db`) will be created automatically on first run.

## First Run

When you first run the application:

1. The welcome message will appear
2. Database tables will be created automatically
3. The main menu will be displayed

## Initial Setup Recommendations

### 1. Add Some Movies

Start by adding a few movies to test the application:
- Use option 1 to add movies
- Try different release dates (past and future)

### 2. Add Users

Create user accounts:
- Use option 6 to add users
- Choose unique usernames

### 3. Mark Movies as Watched

Test the watched functionality:
- Use option 4 to mark movies as watched
- Use option 5 to view watched movies

## Database File

The application creates a SQLite database file named `data.db` in the project directory. This file stores:
- All movies
- All users
- Watched movie records

**Note:** The database file persists between runs. To start fresh, delete `data.db` and it will be recreated.

## Troubleshooting

### Python Not Found
- Install Python from [python.org](https://www.python.org/downloads/)
- Ensure Python is added to your system PATH

### Permission Errors
- Ensure you have write permissions in the project directory
- On Linux/Mac, you may need to use `sudo` or change directory permissions

### Database Errors
- Delete `data.db` to reset the database
- Ensure you have write permissions in the project directory

### Import Errors
- Ensure `app.py` and `database.py` are in the same directory
- Run the application from the project root directory

## Development Setup

For development purposes:

1. **Create a virtual environment (optional):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **No additional packages required** - uses only Python standard library

3. **Run the application:**
```bash
python app.py
```

## File Structure After First Run

```
.
├── app.py
├── database.py
├── data.db          # Created automatically
├── README.md
└── docs/
    ├── DATABASE.md
    ├── API.md
    └── SETUP.md
```

## Next Steps

After setup:
1. Read the main [README.md](../README.md) for feature overview
2. Check [API.md](API.md) for usage details
3. Review [DATABASE.md](DATABASE.md) for database structure
4. Start using the application!
