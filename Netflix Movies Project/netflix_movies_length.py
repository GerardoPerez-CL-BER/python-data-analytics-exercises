# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')

# Filter the data to remove TV shows and store as netflix_subset
netflix_subset = netflix_df[netflix_df['type'] == 'Movie'].copy()

# Investigate and subset the Netflix movie data
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter netflix_movies to find the movies that are strictly shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]

# Using a for loop and if/elif statements, iterate through the rows of netflix_movies and assign colors of your choice to four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else).
# Define genre colors
genre_colors = {
    'Children': 'skyblue',
    'Documentaries': 'lightgreen',
    'Stand-Up': 'gold',
    'Other': 'lightcoral'  
}

# Initialize an empty list to store colors
colors = []

# Iterate through rows, assign colors based on genre
for genre in netflix_movies['genre']:
    if genre == 'Children':
        colors.append(genre_colors['Children'])
    elif genre == 'Documentaries':
        colors.append(genre_colors['Documentaries'])
    elif genre == 'Stand-Up':
        colors.append(genre_colors['Stand-Up'])
    else:
        colors.append(genre_colors['Other'])
        
# Create scatter plot
fig = plt.figure(figsize=(10, 6))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors, alpha=0.7)

plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Duration (min)', fontsize=12)
plt.title('Movie Duration by Year of Release', fontsize=14)

# Optionally, add a legend to explain the colors
for genre, color in genre_colors.items():
    plt.scatter([], [], c=color, label=genre, alpha=0.7)
plt.legend(loc='upper right')

# Show the plot
plt.grid(axis='y', alpha=0.4)
plt.show()
