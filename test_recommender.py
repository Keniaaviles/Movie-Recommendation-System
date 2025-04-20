"""
test_recommender.py

Unit tests for the recommender.py module.
"""

import unittest
from recommender import recommend_movies

class TestRecommender(unittest.TestCase):
    def setUp(self):
        self.sample_movies = [
            {"title": "Spiderman: No Way Home", "genres": ["Action", "Adventure"]},
            {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
            {"title": "Minecraft: The Movie", "genres": ["Animation", "Adventure"]},
            {"title": "The Notebook", "genres": ["Romance", "Drama"]}
        ]

    def test_recommend_action(self):
        user_input = ["Action"]
        expected = ["Spiderman: No Way Home", "The Matrix"]
        result = recommend_movies(user_input, self.sample_movies)
        self.assertEqual(result, expected)

    def test_recommend_none(self):
        user_input = ["Horror"]
        expected = []
        result = recommend_movies(user_input, self.sample_movies)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
