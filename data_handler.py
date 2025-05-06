"""
data_handler.py

This module handles loading movie data from a CSV file.
Each row should contain a movie title and a list of genres.

Author: Kirubel Mogese
"""

import csv

def load_movies_from_csv(filename):
    """
    Loads movie data from a CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries with 'title' and 'genres' keys.
    """
    movies = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['title']
                genres = row['genres'].split('|')  # Genres separated by | in csv
                movies.append({'title': title, 'genres': genres})
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")

    return movies

# Test when run directly
if __name__ == "__main__":
    movie_list = load_movies_from_csv("movies_data.csv") 
    for movie in movie_list:
        print(movie)
