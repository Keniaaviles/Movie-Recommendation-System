"""
test_ui.py

Unit tests for the ui.py module.
Written using Python's built-in unittest module.
"""

import unittest
from ui import display_recommendations

class TestUI(unittest.TestCase):
    def test_display_recommendations_output(self):
        # This test just ensures the function runs without errors
        sample_movies = ["Spiderman: No Way Home", "The Matrix", "Minecraft: The Movie"]
        try:
            display_recommendations(sample_movies)
        except Exception as e:
            self.fail(f"display_recommendations raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

