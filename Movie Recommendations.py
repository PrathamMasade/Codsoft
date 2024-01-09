#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

# Load the MovieLens dataset
ratings_path = r"C:\Users\prath\Downloads\ml-25m\ml-25m\ratings.csv"
movies_path = r"C:\Users\prath\Downloads\ml-25m\ml-25m\movies.csv"
ratings = pd.read_csv(ratings_path)
movies = pd.read_csv(movies_path)

# Merge ratings and movies data
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Create a list of unique movie titles
unique_movies = movie_ratings['title'].unique()

# Take input from the user for a few movies
user_input_movies = input("Enter a few movie titles separated by commas: ").split(',')

# Remove leading and trailing whitespaces from each movie title
user_input_movies = [movie.strip() for movie in user_input_movies]

# Filter out movies that are not in the dataset
user_input_movies = [movie for movie in user_input_movies if movie in unique_movies]

# If none of the input movies are found in the dataset
if not user_input_movies:
    print("None of the input movies are found in the dataset.")
else:
    # Assume a hypothetical rating of 5 for the input movies
    input_ratings = {movie: 5 for movie in user_input_movies}

    # Filter the dataset for movies not in the user input
    remaining_movies = movie_ratings[~movie_ratings['title'].isin(user_input_movies)]

    # Group by movie title and calculate the mean rating
    movie_ratings_mean = remaining_movies.groupby('title')['rating'].mean().reset_index()

    # Sort movies by mean rating in descending order
    recommended_movies = movie_ratings_mean.sort_values(by='rating', ascending=False)['title'].tolist()

    # Exclude movies already in the input
    recommended_movies = [movie for movie in recommended_movies if movie not in user_input_movies]

    print("\nRecommended movies based on your input:")
    print(recommended_movies[:10])


# In[ ]:




