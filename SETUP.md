# Setup and Installation Guide

## Prerequisites

Before installing and running the Movie Watch List application, ensure you have the following:

- **Python 3.x** (Python 3.6 or higher recommended)
- **SQLite3** (usually included with Python installation)
- **Command-line terminal** (bash, cmd, PowerShell, etc.)

## Installation Steps

### 1. Verify Python Installation

Check if Python is installed on your system:

```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.x.x`

If Python is not installed:
- **Linux**: `sudo dnf install python3` (Amazon Linux 2023)
- **macOS**: Install via Homebrew or download from python.org
- **Windows**: Download from python.org

### 2. Verify SQLite3

SQLite3 is typically included with Python. Verify it's available:

```bash
python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

Expected output: SQLite version number (e.g., `3.42.0`)

### 3. Clone or Download the Project

If using git:
```bash
git clone <repository-url>
cd <project-directory>
```

Or download and extract the project files to a directory.

### 4. Project Structure

Ensure your project directory contains:
```
.
├── README.md
├── SETUP.md
├── app.py
├── database.py
├── database/
│   └── README.md
└── app/
    └── README.md
```

### 5. Run the Application

Navigate to the project directory and run:

```bash
python app.py
# or
python3 app.py
```

## First Run

On the first run, the application will:
1. Create the SQLite database file (`data.db`) automatically
2. Create all necessary tables (movies, users, watched)
3. Display the welcome message and menu

## Quick Start Example

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Add a user:**
   - Select option `6`
   - Enter username: `john`

3. **Add a movie:**
   - Select option `1`
   - Enter title: `Inception`
   - Enter release date: `16-07-2010` (or press Enter for today)

4. **View all movies:**
   - Select option `3`

5. **Mark movie as watched:**
   - Select option `4`
   - Enter username: `john`
   - Enter movie ID: `1`

6. **View watched movies:**
   - Select option `5`
   - Enter username: `john`

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'database'"

**Solution:** Ensure you're running the script from the project root directory where `database.py` is located.

```bash
cd /path/to/project
python app.py
```

### Issue: "Permission denied" on database file

**Solution:** Check file permissions and ensure the directory is writable:

```bash
chmod 755 /path/to/project
```

### Issue: "sqlite3.OperationalError: database is locked"

**Solution:** 
- Close any other instances of the application
- Ensure no other process is accessing `data.db`
- Check if database file permissions allow write access

### Issue: Date format errors

**Solution:** Use the exact format `dd-mm-YYYY` (e.g., `16-07-2010`). Leading zeros are required for single-digit days/months.

## Database File

The application creates a SQLite database file named `data.db` in the project root directory. This file stores:
- All movies
- All users
- Watch history (which users watched which movies)

**Note:** The database file is created automatically on first run. You can delete it to reset the database (all data will be lost).

## Environment-Specific Notes

### Amazon Linux 2023

```bash
# Install Python 3 if needed
sudo dnf install python3

# Verify installation
python3 --version

# Run application
python3 app.py
```

### macOS

```bash
# Python 3 is usually pre-installed
python3 app.py

# If not installed, use Homebrew
brew install python3
```

### Windows

```bash
# Use Python launcher
py app.py

# Or if Python is in PATH
python app.py
```

## Dependencies

This project has **no external dependencies** beyond Python standard library:
- `sqlite3` - Database operations
- `datetime` - Date/time handling

No `requirements.txt` or `pip install` needed!

## Verification

After installation, verify everything works:

1. Run the application: `python app.py`
2. You should see: "Welcome to the watchlist app!"
3. Menu should display correctly
4. Try adding a test user (option 6)
5. Try adding a test movie (option 1)
6. Verify it appears in "View all movies" (option 3)

## Next Steps

- Read [README.md](README.md) for project overview
- Check [database/README.md](database/README.md) for database documentation
- Review [app/README.md](app/README.md) for application logic details

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the module-specific README files
3. Verify Python and SQLite versions meet requirements
