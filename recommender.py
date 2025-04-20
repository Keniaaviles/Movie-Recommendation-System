"""
recommender.py

This module contains the logic for recommending movies based on user preferences.
It uses a dataset of movies and filters it based on the genres the user likes.

Author: Farzan Khan
"""

def recommend_movies(preferred_genres, movie_list):
    """
    Recommend movies that match the user's favorite genres.

    Args:
        preferred_genres (list): A list of genres the user enjoys.
        movie_list (list): A list of movie dictionaries with 'title' and 'genres' keys.

    Returns:
        list: A list of movie titles that match the user's preferences.
    """
    recommendations = []

    for movie in movie_list:
        # Check if any of the user's genres are in the movie's genres
        if any(genre in movie['genres'] for genre in preferred_genres):
            recommendations.append(movie['title'])

    return recommendations

# Example usage (used for testing only if you run this file directly)
if __name__ == "__main__":
    sample_movies = [
        {"title": "Spiderman: No Way Home", "genres": ["Action", "Adventure"]},
        {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
        {"title": "Minecraft: The Movie", "genres": ["Animation", "Adventure"]},
        {"title": "The Notebook", "genres": ["Romance", "Drama"]}
    ]

    user_genres = ["Action", "Animation"]
    results = recommend_movies(user_genres, sample_movies)

    print("Recommended Movies:")
    for movie in results:
        print(f"- {movie}")
