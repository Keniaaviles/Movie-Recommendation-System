"""
ui.py

This module handles the user interaction for the movie recommendation system.
It gathers user preferences (favorite genres) and displays recommended movies
based on those preferences.

Author: Kenia Aviles
"""

def get_user_preferences():
    """
    Prompts the user to enter their favorite movie genres.

    Returns:
        list: A list of genre strings entered by the user.
    """
    print("Welcome to the Movie Recommendation System!")
    print("Tell us the kinds of movies you enjoy so we can recommend some for you.")
    print("Example genres: Action, Comedy, Sci-Fi, Adventure, Animation, Romance")
    user_input = input("Enter your favorite genres (separated by commas): ")
    
    # Clean up the input and return it as a list of genres
    genres = [genre.strip().title() for genre in user_input.split(",") if genre.strip()]
    return genres

def display_recommendations(recommendations):
    """
    Displays a list of recommended movies to the user.

    Args:
        recommendations (list): A list of movie titles (strings).
    """
    print("\n Here are some movies you might enjoy:")
    if not recommendations:
        print("Sorry, we couldn't find any matching movies.")
    else:
        for movie in recommendations:
            print(f"- {movie}")

def get_number_of_recommendations():
    """
    Ask the user how many recommendations they want.

    Returns:
        int: The number of movie recommendations to show.
    """
    while True:
        try:
            num = int(input("How many movie recommendations would you like? "))
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example test run if this file is run directly
if __name__ == "__main__":
    user_genres = get_user_preferences()

    # Example recommendations for testing purposes
    sample_recommendations = ["Spiderman: No Way Home", "The Matrix", "The Minecraft Movie"]

    display_recommendations(sample_recommendations)
