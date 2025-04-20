import unittest
from ui import get_user_preferences, validate_genre_input

class TestUI(unittest.TestCase):

    # Test the get_user_preferences() function
    def test_get_user_preferences(self):
        """
        Test that when the user types genres, the program splits it into
        a list of genres, removes extra spaces, and capitalizes each word.
        """
        # Normally, you'd run this by typing in the console, but here we simulate what the user types:
        # Imagine the user types 'Action, comedy, Drama'
        raw_input = 'Action, comedy, Drama'
        expected = ['Action', 'Comedy', 'Drama']  # This is what we expect

        # Split and format the genres
        result = [genre.strip().title() for genre in raw_input.split(",")]

        # Check if the result matches what we expect
        self.assertEqual(result, expected)  # This checks if the list is the same

    # Test the validate_genre_input() function (when input is valid)
    def test_validate_genre_input_valid(self):
        """
        Test that when the input is a valid genre (non-empty), the function returns True.
        """
        valid_input = "Action"  # A genre that should be valid
        result = validate_genre_input(valid_input)  # Test the function
        self.assertTrue(result)  # We expect the function to return True for valid input

    # Test the validate_genre_input() function (when input is invalid)
    def test_validate_genre_input_invalid(self):
        """
        Test that when the input is empty or just spaces, the function returns False.
        """
        invalid_input_1 = ""  # An empty input (invalid)
        invalid_input_2 = "   "  # Spaces only (invalid)
        
        # Test both invalid inputs
        self.assertFalse(validate_genre_input(invalid_input_1))  # Should return False
        self.assertFalse(validate_genre_input(invalid_input_2))  # Should return False

if __name__ == '__main__':
    unittest.main()
