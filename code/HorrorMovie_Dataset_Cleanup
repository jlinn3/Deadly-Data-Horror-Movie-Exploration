import numpy as np
import pandas as pd
import re

df = pd.read_csv('horror_movies.csv')
print("Data loaded successfully.")

print(df.dtypes)
print(df.head())

  df['overview'] = df['overview'].str.lower()

# List of common words to exclude
common_words_to_exclude = [
    'the', 'a', 'to', 'for', 'that',
    'of', 'and', 'in', 'is', 'her',
    'him', 'them', 'with', 'an', 'on',
    'when', 'are', 'into', 'but', 'his', 'he',
    'their', 'they', 'as', 'at','she','be','it',
    'will', 'was', 'by', ' this', 'have', 'has',
    'from', 'this', 'who', 'one', 'two', 'after',
    'next', 'up', 'down', 'out', 'man', 'woman'
]

# Replace missing values in 'overview' column with an empty string
df['overview'] = df['overview'].fillna('')

# Filter out common words from 'overview' column
df['overview'] = df['overview'].apply(lambda x: ' '.join([word for word in x.split() if word not in common_words_to_exclude]))


# Filter out movies with a budget less than 1000
df = df[df['budget'] >= 1000]

# Filter out movies with a revenue of 0
df = df[df['revenue'] > 0]

# Convert 'release_date' column to datetime
df['release_date'] = pd.to_datetime(df['release_date'])

# Extract 'release_year' from 'release_date'
df['release_year'] = df['release_date'].dt.year

# Extract 'release_month' from 'release_date'
df['release_month'] = df['release_date'].dt.month

# Exclude 'genre_names' containing 'horror'
df = df[~df['genre_names'].str.lower().str.contains('horror')]

# Drop unnecessary columns
columns_to_drop = ['poster_path', 'vote_count', 'status', 'backdrop_path', 'adult']
df = df.drop(columns=columns_to_drop)

# Save the preprocessed data to a new CSV file
#df.to_csv('', index=False)
