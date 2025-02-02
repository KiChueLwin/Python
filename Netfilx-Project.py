# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv")

# Filter the data to remove TV shows
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Selecting only the required columns
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Filter movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Define colors based on genre groups
colors = []
for index, row in netflix_movies.iterrows():
    if 'Children' in row['genre']:
        colors.append('blue')
    elif 'Documentaries' in row['genre']:
        colors.append('green')
    elif 'Stand-Up' in row['genre']:
        colors.append('red')
    else:
        colors.append('orange')

# Initialize a matplotlib figure object
fig = plt.figure()

# Create a scatter plot
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Add labels and title
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')

# Based on the plot, assign "yes" or "no" to the variable answer
answer = "no"

