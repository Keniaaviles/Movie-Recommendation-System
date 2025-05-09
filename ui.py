"""
Taken from presentation:
The ui.py module handles user interaction,
prompting users to enter their favorite movie genres 
and displaying recommended movies based on those preferences.
"""

def get_user_preferences():
    """
    This prompts the user to input their favorite genres

    Returns:
        list of str: cleaned list of genres
    """
    print("Please enter your favorite movie genres: ")
    while True:
        response = input("Your favorite genres: ")
        if response.strip() != "":
            genres = response.split(",")
            cleaned_genres = []
            for genre in genres:
                cleaned_genres.append(genre.strip().capitalize())
            return cleaned_genres
        else:
            print("Sorry, you didn't enter any genres, please try again.")

def get_number_of_recommendations():
    """
    This function ask the user how many recommendations they want

    Returns:
        int: number of recommendations
    """
    while True:
        response = input("How many recommendations would you like? (Enter a number): ")
        try:
            number = int(response)
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Not a valid number. Please try again.")

def display_recommendations(recommendations):
    """
    Displays the recommended movies to the user

    Args:
        recommendations: list of movie dictionaries
    """
    if recommendations:
        print("\nRecommended Movies:")
        for movie in recommendations:
            print(f"- {movie['title']} ({', '.join(movie['genres'])})")
    else:
        print("\nSorry, no movies match your preferences.")
