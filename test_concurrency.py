#!/usr/bin/env python3
"""Test concurrent database operations to verify performance improvements."""

import time
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import database

def add_test_movie(index):
    """Add a movie to the database."""
    start_time = time.time()
    title = f"Test Movie {index}"
    release_timestamp = datetime.datetime.today().timestamp()
    database.add_movie(title, release_timestamp)
    elapsed = time.time() - start_time
    return index, elapsed

def main():
    # Initialize database
    database.create_tables()

    # Test concurrent operations
    num_tasks = 20
    print(f"Testing {num_tasks} concurrent database operations...")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(add_test_movie, i) for i in range(num_tasks)]

        results = []
        for future in as_completed(futures):
            index, elapsed = future.result()
            results.append((index, elapsed))
            print(f"Task {index} completed in {elapsed:.4f} seconds")

    total_time = time.time() - start_time

    print(f"\nAll {num_tasks} tasks completed in {total_time:.4f} seconds")
    print(f"Average time per task: {total_time/num_tasks:.4f} seconds")

    # Verify all movies were added
    movies = database.get_movies()
    print(f"Total movies in database: {len(movies)}")

if __name__ == "__main__":
    main()
