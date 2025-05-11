"""
recommender.py

This module contains the logic for recommending movies based on user preferences.
It uses a dataset of movies and filters it based on the genres the user likes.


Pair Programming Role Documentation

Farzan Khan
- Driver: recommend_movies()

Kirubel Mogese
- Navigator: recommend_movies()

Kenia Aviles
- Navigator: recommend_movies()
"""

def recommend_movies(preferred_genres, movie_list, limit):
    """
    Recommend a limited number of movies based on the user's preferred genres.

    Args:
        preferred_genres (list): A list of genres the user enjoys.
        movie_list (list): A list of movie dictionaries with 'title' and 'genres' keys.
        limit (int): The maximum number of movie recommendations to return.

    Returns:
        list: A list of movie titles that match the user's preferences,limited to the number specified.
    """
    recommendations = []
    for movie in movie_list:
        if len(recommendations) >= limit:
            break
        genres_data = movie.get("genres", "")
        if isinstance(genres_data, str):
            movie_genres = genres_data.split("|")
        else:
            movie_genres = genres_data
        if any(genre in preferred_genres for genre in movie_genres):
            recommendations.append(movie.get("title", "Untitled"))
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
    results = recommend_movies(user_genres, sample_movies,2)

    print("Recommended Movies:")
    for movie in results:
        print(f"- {movie}")
