"""
Minimal test for load_movies_from_csv function in data_handler.py

This test checks:
1. How the function handles missing genres
2. How it processes blank lines
"""

from data_handler import load_movies_from_csv

with open("test_extra_cases.csv", "w") as file:
    file.write("title,genres,year\n")
    file.write("No Genres,\n")  
    file.write("Valid Movie,Action|Adventure\n")
    file.write("\n")  

movies = load_movies_from_csv("test_extra_cases.csv")

print("\nLoaded Movies:")
for movie in movies:
    print(movie)

# Test 1: Confirms the number of non blank rows processed 
if len(movies) == 2:
    print("Test passed: Correct number of valid movie entries.")
else:
    print("Test failed: Expected 2 movies, got", len(movies))

# Test 2: Check if missing genres became an empty list
if movies[0]["genres"] == []:
    print("Test passed: Empty genres handled correctly.")
else:
    print("Test failed: Expected empty list for missing genres.")
