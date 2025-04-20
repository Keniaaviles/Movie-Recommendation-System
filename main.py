"""
main.py

This is the main file for the Movie Recommendation System.
It coordinates the user interface, data handling, and recommendation engine modules.
"""

# Importing planned modules 
from ui import get_user_preferences
from recommender import recommend_movies
from data_handler import load_movie_data

def main():
    """
    The main function of the program.
    Gathers user preferences, loads movie data, and prints recommendations.
    """
    print("Welcome to the Movie Recommendation System!")

    # Get user input 
    preferences = get_user_preferences()

    # Load movie data 
    movies = load_movie_data("sample_data.csv")

    # Get recommendations 
    recommendations = recommend_movies(preferences, movies)

    # Show results 
    print("\nRecommended Movies:")
    for movie in recommendations:
        print("-", movie)

if __name__ == "__main__":
    main()
