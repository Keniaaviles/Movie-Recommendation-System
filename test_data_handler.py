"""
Unit test for the load_movies_from_csv function in data_handler.py

This test checks:
1. If the function correctly reads a CSV file.
2. If it splits the genres into a list.
3. If it handles missing files gracefully.

"""

from data_handler import load_movies_from_csv

# We will have created a sample CSV file to test with

# This CSV file contains 3 movie entries, just like a real dataset.
with open("test_movies.csv", "w") as file:
    file.write("title,genres\n")  # CSV header
    file.write("Spiderman: No Way Home,Action|Adventure\n")
    file.write("The Matrix,Action|Sci-Fi\n")
    file.write("Minecraft: The Movie,Animation|Adventure\n")


# Step 2: Call the function we are testing
movies = load_movies_from_csv("test_movies.csv")


# Step 3: Print out the result
print("\nLoaded Movies:")
for movie in movies:
    print(movie)

# Step 4: Run simple checks (manual test using if-statements)


# Check if 3 movies were loaded
if len(movies) == 3:
    print("Test passed: 3 movies were loaded.")
else:
    print("Test failed: Expected 3 movies, got", len(movies))

# Check if genres were split into a list correctly for the first movie
if "Action" in movies[0]['genres'] and "Adventure" in movies[0]['genres']:
    print("Test passed: Genres were split into a list.")
else:
    print("Test failed: Genres not split correctly.")


# Step 5: Test what happens with a missing file
print("\nTesting with missing file:")
missing = load_movies_from_csv("does_not_exist.csv")  # This file doesn't exist

if missing == []:
    print("Test passed: Missing file handled correctly (empty list returned).")
else:
    print("Test failed: Expected empty list for missing file.")
