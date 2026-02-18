from flask import Flask, render_template, jsonify, request
import datetime
import database

app = Flask(__name__)

# Initialize database
database.create_tables()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/movies', methods=['GET'])
def get_movies():
    upcoming = request.args.get('upcoming', 'false').lower() == 'true'
    movies = database.get_movies(upcoming=upcoming)
    
    movies_list = []
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        movies_list.append({
            'id': movie[0],
            'title': movie[1],
            'release_date': movie_date.strftime("%b %d %Y"),
            'timestamp': movie[2]
        })
    
    return jsonify(movies_list)


@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.json
    title = data.get('title')
    release_date = data.get('release_date', datetime.datetime.today().strftime("%d-%m-%Y"))
    
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    database.add_movie(title, release_timestamp)
    
    return jsonify({'status': 'success', 'message': 'Movie added successfully'})


@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    database.add_user(username)
    
    return jsonify({'status': 'success', 'message': 'User added successfully'})


@app.route('/api/watched', methods=['POST'])
def watch_movie():
    data = request.json
    username = data.get('username')
    movie_id = data.get('movie_id')
    database.watch_movie(username, movie_id)
    
    return jsonify({'status': 'success', 'message': 'Movie marked as watched'})


@app.route('/api/watched/<username>', methods=['GET'])
def get_watched_movies(username):
    movies = database.get_watched_movies(username)
    
    movies_list = []
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        movies_list.append({
            'id': movie[0],
            'title': movie[1],
            'release_date': movie_date.strftime("%b %d %Y"),
            'timestamp': movie[2]
        })
    
    return jsonify(movies_list)


@app.route('/api/search', methods=['GET'])
def search_movies():
    search_term = request.args.get('q', '')
    movies = database.search_movies(search_term)
    
    movies_list = []
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        movies_list.append({
            'id': movie[0],
            'title': movie[1],
            'release_date': movie_date.strftime("%b %d %Y"),
            'timestamp': movie[2]
        })
    
    return jsonify(movies_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
