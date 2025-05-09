"""
ui.py

This module handles the user interaction for the movie recommendation system.
It gathers user preferences (favorite genres) and displays recommended movies
based on those preferences.

Author: Kenia Aviles, Kirubel Mogese
"""

import os


def print_header():
    """
    Shows the application header with borders.
    """
    print()  # spacing 
    print('=' * 60)
    print('      🎬  Movie Recommendation System  🎬')
    print('=' * 60)
    print()  # spacing 


def get_user_preferences(movies):
    """
    Prompts the user to enter their favorite movie genres.

    Users can type 'random' or 'list' to view all available genres before choosing.
    Or type 'quiz' to take a short quiz that helps pick a genre.

    Args:
        movies (list): List of movie data to extract available genres.

    Returns:
        list: A list of genre strings entered by the user.
    """
    # spacing 
    print()  

    # Build a set of all genres from the movie data
    all_genres = set()
    for movie in movies:
        for g in movie.get("genres", []):
            all_genres.add(g)

    # Display options
    print('Options:')
    print('- Type comma-separated genres (e.g. Action, Comedy)')
    print("- Type 'random' for a surprise mix of movies!")
    print("- Type 'list' to see all available genres")
    print("- Type 'quiz' to take a short quiz that helps pick a genre")
    print('-' * 60)

    while True:
        choice = input('Your choice: ').strip().lower()
        if choice == "list":
            print('\nAvailable genres:')
            for genre in sorted(all_genres):
                print('  -', genre)
            print('-' * 60)
            continue

        if choice == "random":
            return ['Random']

        if choice == "quiz":
            return run_genre_quiz()

        # Parse manual genres
        parts = choice.split(',')
        genres = [p.strip().title() for p in parts if p.strip()]
        if genres:
            return genres

        print('Please enter at least one valid option.')
        print('-' * 60)


def run_genre_quiz():
    """
    Ask the user a few simple questions to suggest one or two genres.

    Returns:
        list: A list of genre names.
    """
    # Quiz prompt
    print('\nQuiz: What mood fits you today?')
    print('-' * 60)
    q1 = input('1) Do you prefer fast-paced action or slower, thoughtful stories? (action vs thoughtful) ').strip().lower()
    q2 = input('2) Funny and light-hearted or serious and dramatic? (funny vs serious) ').strip().lower()
    q3 = input('3) Real-world settings or imaginative worlds? (real vs imaginative) ').strip().lower()

    # mapping logic
    genres = []
    if q1.startswith('action'):
        genres.append('Action')
    else:
        genres.append('Drama')
    if q2.startswith('funny'):
        genres.append('Comedy')
    else:
        genres = ['Thriller']
    if q3.startswith('imagin'):
        genres.append('Sci-Fi')
    else:
        genres.append('Adventure')

    print('\nQuiz complete! We suggest:')
    print('-' * 60)
    for g in genres:
        print('  *', g)
    print('-' * 60)
    return genres


def display_recommendations(recommendations):
    """
    Displays a list of recommended movies to the user.

    Args:
        recommendations (list): A list of movie titles (strings).
    """
    print()  
    print('=' * 60)
    print('  🎉 Your Movie Recommendations 🎉')
    print('=' * 60)

    if not recommendations:
        print('Sorry, we couldn\'t find any matching movies.')
    else:
        for movie in recommendations:
            print(f"- {movie}")

    print('=' * 60)
    print()  


def get_number_of_recommendations():
    """
    Ask the user how many recommendations they want.

    Returns:
        int: The number of movie recommendations to show.
    """
    print_header()
    while True:
        try:
            num = int(input('How many movie recommendations would you like? '))
            if num > 0:
                return num
            else:
                print('Please enter a positive number.')
        except ValueError:
            print('Invalid input. Please enter a number.')

# Example test run if this file is run directly
if __name__ == "__main__":
    # Example movie data for testing
    sample_movies = [
        {"title": "Movie A", "genres": ["Action", "Comedy"]},
        {"title": "Movie B", "genres": ["Drama", "Romance"]}
    ]
    user_genres = get_user_preferences(sample_movies)

    # Example recommendations for testing purposes
    sample_recommendations = ["Spiderman: No Way Home", "The Matrix", "The Minecraft Movie"]

    display_recommendations(sample_recommendations)
    