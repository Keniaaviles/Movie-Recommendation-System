"""
test_recommender.py

Unit tests for the recommender.py module.
"""
import unittest
from recommender import recommend_movies

class TestRecommendMovies(unittest.TestCase):

    def setUp(self):
        self.sample_movies = [
            {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
            {"title": "Forrest Gump", "genres": ["Drama", "Romance"]},
            {"title": "The Hangover", "genres": ["Comedy"]},
        ]

    def test_recommend_by_single_genre(self):
        result = recommend_movies(["Action"], self.sample_movies, 2)
        self.assertIn("The Matrix", result)

    def test_limit_results(self):
        result = recommend_movies(["Action", "Drama"], self.sample_movies, 1)
        self.assertEqual(len(result), 1)

    def test_empty_genres(self):
        result = recommend_movies([], self.sample_movies, 3)
        self.assertEqual(result, [])

    def test_no_matching_genres(self):
        result = recommend_movies(["Horror"], self.sample_movies, 3)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
