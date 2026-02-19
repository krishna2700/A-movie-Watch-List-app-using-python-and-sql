from flask import Flask, render_template, request, redirect, url_for
import datetime
import database

app = Flask(__name__)

database.create_tables()


@app.template_filter('timestamp_to_date')
def timestamp_to_date(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%b %d, %Y")


@app.route('/')
def index():
    movies = database.get_movies()
    return render_template('index.html', movies=movies)


@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form.get('title')
    release_date = request.form.get('release_date') or datetime.datetime.today().strftime("%Y-%m-%d")
    release_timestamp = datetime.datetime.strptime(release_date, "%Y-%m-%d").timestamp()
    database.add_movie(title, release_timestamp)
    return redirect(url_for('index'))


@app.route('/upcoming')
def upcoming():
    movies = database.get_movies(upcoming=True)
    return render_template('index.html', movies=movies, page_title="Upcoming Movies")


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    database.add_user(username)
    return redirect(url_for('users'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
