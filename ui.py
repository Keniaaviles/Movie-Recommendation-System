"""
ui.py

Handles all user interactions for the Movie Recommendation System.
Specifically, it collects user preferences for movie genres.
"""

def get_user_preferences():
    """
    Prompt the user to enter preferred genres and return them as a list.

    This function collects a comma-separated list of genres from the user,
    strips any leading/trailing spaces, and converts them to a title-cased list.

    Returns:
        list of str: A cleaned list of user-preferred genres (e.g., ['Action', 'Comedy'])
    """
    raw_input = input("Enter your favorite genres, separated by commas: ")
    return [genre.strip().title() for genre in raw_input.split(",")]

def validate_genre_input(input_str):
    """
    Validates a single genre input.

    This function checks whether the input genre is a non-empty string.

    Args:
        input_str (str): The genre input to validate.

    Returns:
        True if the genre input is valid (non-empty), False otherwise.
    """
    if input_str.strip() != "":
        return True
    else:
        return False
