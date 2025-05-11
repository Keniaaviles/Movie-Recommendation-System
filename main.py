"""
main.py

Main entry point for the Movie Recommendation System.

This script integrates all the modules in the system using a class-based structure:
1. User Interface (`ui.py`): Collects user preferences through prompts, quizzes, or genre selection.
2. Recommendation Engine (`recommender.py`): Matches user preferences with movies and selects the best fits.
3. Data Handler (`data_handler.py`): Loads and parses movie data from a CSV file, handling errors gracefully.

Execution Flow:
- A MovieRecommenderSystem class encapsulates the main workflow.
- The program begins by resolving the path to the movie data file.
- It loads and validates the dataset from a local CSV.
- Users are prompted to select how many movie recommendations they'd like.
- Then, they input their genre preferences, choose to take a quiz, or opt for a random selection.
- The system processes the input and displays relevant movie suggestions.
- The loop repeats until the user decides to exit.

This is the file that ties everything together and allows the user to interact with the system in a user-friendly loop.


Pair Programming Role Documentation

Kenia Aviles
- Driver: MovieRecommenderSystem.run()
- Navigator: MovieRecommenderSystem.__init__()

Kirubel Mogese
- Driver: MovieRecommenderSystem.__init__(), MovieRecommenderSystem.load_data()
- Navigator: MovieRecommenderSystem.run()

Farzan Khan
- Navigator: MovieRecommenderSystem.load_data()
- Driver: MovieRecommenderSystem.load_data()
"""


import os
import random
from ui import (
    get_user_preferences,
    display_recommendations, 
    get_number_of_recommendations, 
    print_header
)
from recommender import recommend_movies
from data_handler import load_movies_from_csv

class MovieRecommenderSystem:
    """
    This class runs the Movie Recommendation System.

    It handles reading the movie data, asking the user for their favorite genres,
    and showing recommended movies based on their choices.
    """

    def __init__(self, csv_filename):
        """
        Sets up the system by getting the full path to the movie data file.

        Args:
            csv_filename (str): The name of the CSV file that contains movie titles and genres.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(script_dir, csv_filename)
        self.movies = []

    def load_data(self):
        """
        Loads the list of movies from the CSV file.

        Returns:
            bool: True if movies were loaded successfully, False if there was a problem.
        """
        print("Loading movie data...")
        self.movies = load_movies_from_csv(self.csv_path)

        if not self.movies:
            print("Error: No movies loaded. Please check that 'movies_data.csv' exists and is correctly formatted.")
            return False
        return True

    def run(self):
        """
        Runs the main loop of the program.

        It asks the user how many movie suggestions they want,
        what types of movies they like, and then shows matching movies.
        The loop continues until the user says they want to quit.
        """
        if not self.load_data():
            return

        while True:
            print_header()

            num_recommendations = get_number_of_recommendations()
            user_preferences = get_user_preferences(self.movies)

            if len(user_preferences) == 1 and user_preferences[0].lower() == "random":
                available = list(self.movies)
                count = min(num_recommendations, len(available))
                recommendations = random.sample([movie["title"] for movie in available], count)
            else:
                recommendations = recommend_movies(user_preferences, self.movies, num_recommendations)

            display_recommendations(recommendations[:num_recommendations])

            again = input("Would you like to return to the main menu? (yes/no): ").strip().lower()
            if again not in ("yes", "y"):
                print("\n🎬 Thank you for using the Movie Recommendation System! Goodbye!")
                break

def main():
    """
    This is where the program starts running.

    It creates the MovieRecommenderSystem and starts it.
    """
    system = MovieRecommenderSystem("movies_data.csv")
    system.run()

if __name__ == "__main__":
    main()
