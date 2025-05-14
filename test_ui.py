"""
test_ui_extra.py

Covers:
- print_header output formatting
- display_recommendations with standard input
"""

from ui import print_header, display_recommendations

# Test 1: Header formatting
print("Test 1: Print header formatting")
print_header()
print("Check visually: Does it show the border and centered message correctly?")

# Test 2: Display with a list of movie titles
print("\nTest 2: Display with few movie titles")
sample_movies = ["Inception", "The Matrix", "Finding Nemo"]
display_recommendations(sample_movies)
print("Check visually: Are all 3 movies printed clearly as a list?")
