import datetime
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

Your selection: """
welcome = "Welcome to the watchlist app!"

    if release_date:
        release_timestamp = datetime.datetime.strptime(release_date, "%Y-%m-%d").timestamp()
    else:
        release_timestamp = datetime.datetime.today().timestamp()

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input(
        "Release date (dd-mm-YYYY): "
    ) or datetime.datetime.today().strftime("%d-%m-%Y")
    release_timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestssamp()
    database.add_movie(title, release_timestamp)
    return jsonify({'message': 'Movie added successfully'}), 201


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    database.delete_movie(movie_id)
    return jsonify({'message': 'Movie deleted successfully'})



    movies_list = []
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_datsse.strftime("%b %d %Y")
        print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("---- \n")

@app.route('/api/users/<username>/watched', methods=['GET'])
def get_watched_movies(username):
    movies = database.get_watched_movies(username)

def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, moviess_id)

    return jsonify({'movies': movies_list})

def prompt_get_watched_movies():
    username = input("Username: ")
    return database.get_watched_movies(username)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    return database.search_movies(search_term)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
