"""
recommender.py

This file has functions to help recommend movies based on the genres a user likes.
The functions take the user's preferences and match them to movies from a list.
"""

def process_user_preferences(user_genres):
    """
    This function fixes the way the user types their favorite genres.

    If the user writes extra spaces or uses different capital letters, this function 
    will clean that up so it looks neat.

    Args:
        user_genres (list of str): The genres the user likes, like 'action', 'comedy', etc.

    Returns:
        list of str: A list of genres that are cleaned up (capitalized and no extra spaces).
    """
    # Clean up genres by removing extra spaces and making each word start with a capital letter
    return [genre.strip().title() for genre in user_genres]


def get_movie_recommendations(user_genres, movie_dataset):
    """
    This function looks at the genres the user likes and finds movies that match those genres.

    It checks each movie in the dataset to see if it matches any of the genres the user likes.

    Args:
        user_genres (list of str): The genres the user prefers, like 'action', 'comedy', etc.
        movie_dataset (list of dict): A list of movies, where each movie has a title and genre.

    Returns:
        list of str: A list of movie titles that fit the genres the user likes.
    """
    recommended_movies = []
    
    # Go through each movie and check if its genre matches any of the user's genres
    for movie in movie_dataset:
        if any(genre in movie['genre'] for genre in user_genres):
            recommended_movies.append(movie['title'])
    
    return recommended_movies
