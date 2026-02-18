# Watchlist Web App - Multiagent Button

This project now includes a web interface with a multiagent button.

## Files Created

- `web_app.py` - Flask web server with REST API endpoints
- `templates/index.html` - Main web interface with multiagent button
- `static/style.css` - Styling for the web interface
- `multiagent_button.html` - Standalone HTML demo of the multiagent button
- `requirements.txt` - Python dependencies

## Multiagent Button Features

- **Blue Color**: Background color `#2563eb` (blue-600)
- **No onclick handler**: The button has no JavaScript onclick event
- **Hover effects**: Darker blue on hover (`#1d4ed8`)
- **Active state**: Even darker blue when clicked (`#1e40af`)
- **Modern styling**: Rounded corners, shadow, smooth transitions

## Running the Web App

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python web_app.py
   ```

3. Open browser to `http://localhost:5000`

## Viewing the Standalone Button

Simply open `multiagent_button.html` in any web browser to see the multiagent button.

## API Endpoints

- `GET /` - Main web interface
- `GET /api/movies` - Get all movies (add `?upcoming=true` for upcoming only)
- `POST /api/movies` - Add a new movie
- `POST /api/users` - Add a new user
- `POST /api/watched` - Mark a movie as watched
- `GET /api/watched/<username>` - Get watched movies for a user
- `GET /api/search?q=<term>` - Search for movies

## Button Specifications

- Class: `multiagent-button`
- Background: `#2563eb` (blue)
- No onclick attribute
- No JavaScript event listeners
- Padding: 15px 40px
- Font size: 18px
- Border radius: 8px
