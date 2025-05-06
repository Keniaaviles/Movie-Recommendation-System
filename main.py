"""
Main entry point for the Movie Recommendation System.

This script integrates all the modules in the system:
1. User Interface (`ui.py`): Collects user preferences.
2. Recommendation Engine (`recommender.py`): Processes preferences and provides recommendations.
3. Data Handler (`data_handler.py`): Loads and processes movie data.

This is the file that ties everything together and allows the user to interact with the system.

Author: Team Project (Kenia, Farzan, Kirubel)
"""
from ui import get_user_preferences, display_recommendations,get_number_of_recommendations
from recommender import recommend_movies
from data_handler import load_movies_from_csv

def main():
    """
    Main function to run the movie recommendation system.
    
    The flow of the program:
    1. Option of amount of Recommendations
    2. Load the movie data from a CSV file.
    3. Get the user's preferences (genres they like).
    4. Recommend movies based on those preferences.
    5. Display the recommendations to the user.
    """
    # Allows users to choose how many recommendations they would like 
    num_recommendations = get_number_of_recommendations()


    # Loads movie data from CSV
    print("Loading movie data...")
    movies = load_movies_from_csv("movies_data.csv")

    if not movies:
        print("Error: No movies loaded. Please check that 'movies_data.csv' exists and is correctly formatted.")
        return
    
    # Get user preferences (genres they like)
    user_preferences = get_user_preferences()
    
    # Recommend movies based on user preferences
    recommended_titles = recommend_movies(user_preferences, movies, num_recommendations)
    
    # Display the recommendations to the user
    display_recommendations(recommended_titles)

    # Limit to the number requested by user(error w/o it)
    limited_recommendations = recommended_titles[:num_recommendations]


if __name__ == "__main__":
    # Start the program
    main()



