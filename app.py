import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

database.create_tables()


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


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
            'release_timestamp': movie[2],
            'release_date': movie_date.strftime("%Y-%m-%d")
        })

    return jsonify({'movies': movies_list})


@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')
    release_date = data.get('release_date')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    if release_date:
        release_timestamp = datetime.datetime.strptime(release_date, "%Y-%m-%d").timestamp()
    else:
        release_timestamp = datetime.datetime.today().timestamp()

    database.add_movie(title, release_timestamp)
    return jsonify({'message': 'Movie added successfully'}), 201


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    database.delete_movie(movie_id)
    return jsonify({'message': 'Movie deleted successfully'})


@app.route('/api/movies/search', methods=['GET'])
def search_movies():
    search_term = request.args.get('q', '')
    movies = database.search_movies(search_term)

    movies_list = []
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        movies_list.append({
            'id': movie[0],
            'title': movie[1],
            'release_timestamp': movie[2],
            'release_date': movie_date.strftime("%Y-%m-%d")
        })

    return jsonify({'movies': movies_list})


@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    database.add_user(username)
    return jsonify({'message': 'User added successfully'}), 201


@app.route('/api/users/<username>/watched', methods=['GET'])
def get_watched_movies(username):
    movies = database.get_watched_movies(username)

    movies_list = []
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        movies_list.append({
            'id': movie[0],
            'title': movie[1],
            'release_timestamp': movie[2],
            'release_date': movie_date.strftime("%Y-%m-%d")
        })

    return jsonify({'movies': movies_list})


@app.route('/api/users/<username>/watched', methods=['POST'])
def watch_movie(username):
    data = request.get_json()
    movie_id = data.get('movie_id')

    if not movie_id:
        return jsonify({'error': 'Movie ID is required'}), 400

    database.watch_movie(username, movie_id)
    return jsonify({'message': 'Movie marked as watched'}), 201


@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats = database.get_statistics()
    return jsonify(stats)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
