import datetime
import sqlite3
import unittest
import os

# We test the database module by patching its connection to use an in-memory DB.
import database


class TestDatabase(unittest.TestCase):
    """Tests for the database module functions."""

    def setUp(self):
        """Create a fresh in-memory database for each test."""
        self.original_connection = database.connection
        database.connection = sqlite3.connect(":memory:")
        database.create_tables()

    def tearDown(self):
        """Restore the original connection after each test."""
        database.connection.close()
        database.connection = self.original_connection

    # --- create_tables ---

    def test_create_tables(self):
        """Tables movies, users, and watched should exist after creation."""
        cursor = database.connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tables = [row[0] for row in cursor.fetchall()]
        self.assertIn("movies", tables)
        self.assertIn("users", tables)
        self.assertIn("watched", tables)

    # --- add_movie / get_movies ---

    def test_add_movie(self):
        """Adding a movie should make it retrievable via get_movies."""
        ts = datetime.datetime(2025, 6, 15).timestamp()
        database.add_movie("Test Movie", ts)

        movies = database.get_movies()
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0][1], "Test Movie")
        self.assertEqual(movies[0][2], ts)

    def test_add_multiple_movies(self):
        """Multiple movies should all be stored and returned."""
        ts1 = datetime.datetime(2025, 1, 1).timestamp()
        ts2 = datetime.datetime(2025, 6, 1).timestamp()
        database.add_movie("Movie A", ts1)
        database.add_movie("Movie B", ts2)

        movies = database.get_movies()
        self.assertEqual(len(movies), 2)
        titles = {m[1] for m in movies}
        self.assertEqual(titles, {"Movie A", "Movie B"})

    def test_get_movies_upcoming(self):
        """get_movies(upcoming=True) should only return future movies."""
        past_ts = datetime.datetime(2000, 1, 1).timestamp()
        future_ts = (datetime.datetime.today() + datetime.timedelta(days=365)).timestamp()

        database.add_movie("Old Movie", past_ts)
        database.add_movie("Future Movie", future_ts)

        upcoming = database.get_movies(upcoming=True)
        self.assertEqual(len(upcoming), 1)
        self.assertEqual(upcoming[0][1], "Future Movie")

    def test_get_movies_all(self):
        """get_movies() without upcoming flag should return all movies."""
        past_ts = datetime.datetime(2000, 1, 1).timestamp()
        future_ts = (datetime.datetime.today() + datetime.timedelta(days=365)).timestamp()

        database.add_movie("Old Movie", past_ts)
        database.add_movie("Future Movie", future_ts)

        all_movies = database.get_movies(upcoming=False)
        self.assertEqual(len(all_movies), 2)

    # --- add_user ---

    def test_add_user(self):
        """Adding a user should store them in the users table."""
        database.add_user("alice")

        cursor = database.connection.cursor()
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], "alice")

    def test_add_duplicate_user_raises(self):
        """Adding a duplicate username should raise an IntegrityError."""
        database.add_user("alice")
        with self.assertRaises(sqlite3.IntegrityError):
            database.add_user("alice")

    # --- watch_movie / get_watched_movies ---

    def test_watch_movie_and_get_watched(self):
        """Watching a movie should link user to movie, retrievable via get_watched_movies."""
        ts = datetime.datetime(2025, 3, 1).timestamp()
        database.add_movie("Watched Film", ts)
        database.add_user("bob")

        movies = database.get_movies()
        movie_id = movies[0][0]

        database.watch_movie("bob", movie_id)

        watched = database.get_watched_movies("bob")
        self.assertEqual(len(watched), 1)
        self.assertEqual(watched[0][1], "Watched Film")

    def test_get_watched_movies_empty(self):
        """A user who hasn't watched anything should return an empty list."""
        database.add_user("carol")
        watched = database.get_watched_movies("carol")
        self.assertEqual(len(watched), 0)

    def test_watch_multiple_movies(self):
        """A user can watch multiple movies."""
        ts1 = datetime.datetime(2025, 1, 1).timestamp()
        ts2 = datetime.datetime(2025, 2, 1).timestamp()
        database.add_movie("Film A", ts1)
        database.add_movie("Film B", ts2)
        database.add_user("dave")

        movies = database.get_movies()
        for m in movies:
            database.watch_movie("dave", m[0])

        watched = database.get_watched_movies("dave")
        self.assertEqual(len(watched), 2)

    # --- search_movies ---

    def test_search_movies_found(self):
        """Searching with a partial title should return matching movies."""
        ts = datetime.datetime(2025, 5, 1).timestamp()
        database.add_movie("The Matrix", ts)
        database.add_movie("Matrix Reloaded", ts)
        database.add_movie("Inception", ts)

        results = database.search_movies("Matrix")
        self.assertEqual(len(results), 2)
        titles = {r[1] for r in results}
        self.assertEqual(titles, {"The Matrix", "Matrix Reloaded"})

    def test_search_movies_case_insensitive(self):
        """SQLite LIKE is case-insensitive for ASCII by default."""
        ts = datetime.datetime(2025, 5, 1).timestamp()
        database.add_movie("The Matrix", ts)

        results = database.search_movies("matrix")
        self.assertEqual(len(results), 1)

    def test_search_movies_no_results(self):
        """Searching for a non-existent title should return an empty list."""
        ts = datetime.datetime(2025, 5, 1).timestamp()
        database.add_movie("The Matrix", ts)

        results = database.search_movies("Godfather")
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
