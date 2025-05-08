"""
ui.py

This module handles the user interaction for the movie recommendation system.
It gathers user preferences (favorite genres) and displays recommended movies
based on those preferences.

Author: Kenia Aviles, Kirubel Mogese
"""

def get_user_preferences(movies):
    """
    Prompts the user to enter their favorite movie genres.

    Users can type 'random' or 'list' to view all available genres before choosing.

    Args:
        movies (list): List of movie data to extract available genres.

    Returns:
        list: A list of genre strings entered by the user.
    """
    # Build a set of all genres from the movie data
    all_genres = set()
    for movie in movies:
        for g in movie.get("genres", []):
            all_genres.add(g)

    print("Welcome to the Movie Recommendation System!")
    print("Tell us the kinds of movies you enjoy so we can recommend some for you.")
    print("Example genres: Action, Comedy, Sci-Fi, Adventure, Animation, Romance")
    print("Or type 'random' for a surprise mix of movies!")
    print("Type 'list' to see all available genres.")
    print("Type 'quiz' to take a short quiz that helps pick a genre.")
    
    while True:
        user_input = input("Enter your favorite genres (separated by commas), or 'quiz': ")
        choice = user_input.strip().lower()
        if choice == "list":
            print("\nAvailable genres:")
            for genre in sorted(all_genres):
                print(" - " + genre)
            print("")  
            continue
        if choice == "quiz":
            return run_genre_quiz()
        # Parse user-entered genres
        raw_parts = user_input.split(",")
        genres = []
        for part in raw_parts:
            cleaned = part.strip()
            if cleaned:
                genres.append(cleaned.title())
        return genres

def run_genre_quiz():
    """
    Ask the user a few simple questions to suggest one or two genres.

    Returns:
        list: A list of genre names.
    """
    print("\nLet's find a genre that fits your mood!")
    # Question 1
    q1 = input("Do you prefer fast-paced action or slower, thoughtful stories? (action vs thoughtful) ")
    # Question 2
    q2 = input("Do you like funny and light-hearted or serious and dramatic? (funny vs serious) ")
    # Question 3
    q3 = input("Do you enjoy real-world settings or imaginative worlds? (real vs imaginative) ")

    # mapping logic
    genres = []
    if q1.lower().startswith('action'):
        genres.append('Action')
    else:
        genres.append('Drama')  
    if q2.lower().startswith('funny'):
        genres.append('Comedy')
    else:
        genres = ['Thriller']
    if q3.lower().startswith('imagin'):
        genres.append('Sci-Fi')
    else:
        genres.append('Adventure')

    print(f"Based on your answers, we suggest: {', '.join(genres)}")
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
    # Example movie data for testing
    sample_movies = [
        {"title": "Movie A", "genres": ["Action", "Comedy"]},
        {"title": "Movie B", "genres": ["Drama", "Romance"]}
    ]
    user_genres = get_user_preferences(sample_movies)

    # Example recommendations for testing purposes
    sample_recommendations = ["Spiderman: No Way Home", "The Matrix", "The Minecraft Movie"]

    display_recommendations(sample_recommendations)


