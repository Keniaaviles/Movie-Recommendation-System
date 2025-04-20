"""
Main entry point for the Movie Recommendation System.

This script integrates all the modules in the system:
1. User Interface (`ui.py`): Collects user preferences.
2. Recommendation Engine (`recommender.py`): Processes preferences and provides recommendations.
3. Data Handler (`data_handler.py`): Loads and processes movie data.

This is the file that ties everything together and allows the user to interact with the system.

Author: Team Project (Kenia, Farzan, Kirubel)
"""

from ui import get_user_preferences
from recommender import recommend_movies
from data_handler import load_movies_from_csv

def main():
    """
    Main function to run the movie recommendation system.
    
    The flow of the program:
    1. Load the movie data from a CSV file.
    2. Get the user's preferences (genres they like).
    3. Recommend movies based on those preferences.
    4. Display the recommendations to the user.
    """
    # Load movie data from CSV
    print("Loading movie data...")
    movies = load_movies_from_csv("movies_data.csv")
    
    # Get user preferences (genres they like)
    user_preferences = get_user_preferences()
    
    # Recommend movies based on user preferences
    recommendations = recommend_movies(user_preferences, movies)
    
    # Display the recommendations to the user
    if recommendations:
        print("\nRecommended Movies:")
        for movie in recommendations:
            print(f"- {movie['title']} ({', '.join(movie['genres'])})")
    else:
        print("\nSorry, no movies match your preferences.")

if __name__ == "__main__":
    # Start the program
    main()

