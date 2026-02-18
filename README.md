# A-movie-Watch-List-app-using-python-and-sql

## Multi-Agent Web Application

This is a movie watchlist application with both CLI and web interfaces.

### Features

- **Multi-Agent System**: Web interface with multiple agent buttons
- **Blue Button**: Logs "hello" to console when clicked
- **Movie Management**: Add, view, and search movies
- **User Management**: Add users and track watched movies
- **Interactive Console**: Visual console output in the web interface

### Running the Application

#### CLI Version
```bash
python3 app.py
```

#### Web Version
```bash
python3 web_app.py
```

Then open your browser to `http://localhost:5000`

### Requirements

- Python 3.9+
- Flask 3.0.0
- SQLite3

Install dependencies:
```bash
pip install -r requirements.txt
```

### Multi-Agent Features

The web interface includes:
- **Agent 1**: Movie Fetcher - Manages movie data
- **Agent 2**: User Manager - Handles user operations
- **Agent 3**: Search Engine - Performs movie searches
- **Agent 4**: Analytics - Provides insights

Each agent button logs "hello" to the console when clicked, along with the agent activation message.
