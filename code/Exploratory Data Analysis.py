import numpy as np
import pandas as pd
import re

#df = pd.read_csv('/content/drive/MyDrive/Horror Data Exploration/horror_movies.csv')

print(df.dtypes)
print(df.head())

#Finding Common Terms in Movie Descriptions
#Converting to lowercase for case-insensitive counting
df['overview'] = df['overview'].str.lower()

#Split the column into individual words
words = df['overview'].str.split()

#Now here's the tricky part- how can we get rid of fillers? Think pronouns, the, etc.
#I adjusted the top three common terms count for the top 25 and got rid of words I considered filler.
#Generally, I eliminated any pronouns of sorts (his, hers, she, him, they, them).
#I was really looking for any action verbs or adjectives- so I tried eliminating nouns instead.
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
# Flatten the list of lists into a single list of words and filter out common words
filtered_words = [word for sublist in words.dropna() for word in sublist if word not in common_words_to_exclude]

# Count the occurrences of each word
word_counts = pd.Series(filtered_words).value_counts()

# Get the top three common terms
top_three_common_terms = word_counts.head(3)

print("Top Three Common Terms in Overview Column:")
print(top_three_common_terms)

#Most Popular vs Least Popular
# Find the most popular horror movie
most_popular_horror_movie = df.loc[df['popularity'].idxmax(), ['title','popularity']]

# Find the least popular horror movie
least_popular_horror_movie = df.loc[df['popularity'].idxmin(), ['title','popularity']]

print("Most Popular Horror Movie:")
print(most_popular_horror_movie)

print("\nLeast Popular Horror Movie:")
print(least_popular_horror_movie)

# Exclude horror genre from the dataset; we know these are all horror to some degree.
non_horror_movies = df[~df['genre_names'].str.lower().str.contains('horror')]

# Count occurrences of each genre
genre_counts = non_horror_movies['genre_names'].value_counts()

# Find the most popular genre aside from horror
most_popular_genre = genre_counts.idxmax()

print("Most Popular Genre (Aside from Horror):", most_popular_genre)

#More Sequels?
# In our dataset, we will either have a collection name or null, meaning there was no collection
# For example, Friday the 13th is a collection of horror movies like Halloween
# But some movies will not follow up with more movies, we want to analyze that number
movies_in_collections = df['collection_name'].notnull().sum()

# Count the number of standalone movies (movies not part of a collection)
standalone_movies = df['collection_name'].isnull().sum()

print("Movies Turned into Collections vs. Standalone Movies:")
print("Movies turned into collections:", movies_in_collections)
print("Standalone movies:", standalone_movies)

# That's interesting! With so many sequels/reboots/remakes/continuations, I imagined we would have more collections
# Let's find the most popular standalone

standalone_movies_df = df[df['collection_name'].isnull()]

# Find the most popular standalone movie
most_popular_standalone_movie = standalone_movies_df.loc[standalone_movies_df['popularity'].idxmax()]

print("Most Popular Standalone Movie:")
print(most_popular_standalone_movie[['title', 'popularity', 'overview']])

#Dates of Terror

# Let's start by finding the year with the most releases. Our dataset ranges from 1957 to 2022

df['release_date'] = pd.to_datetime(df['release_date'])

# Extract the year from the 'release_date' column. Let's not worry about the month or dates (for now)
df['release_year'] = df['release_date'].dt.year
year_counts = df['release_year'].value_counts()

# Find the year with the most releases and the corresponding number of releases
most_releases_year = year_counts.idxmax()
most_releases_count = year_counts.max()

print("Year with the Most Releases:", most_releases_year)
print("Number of Releases in the Most Active Year:", most_releases_count)

# Let's check what month for 2020 had the most releases
df_2020 = df[df['release_date'].dt.year == 2020].copy()

# Extract the month from the 'release_date' column
df_2020.loc[:, 'release_month'] = df_2020['release_date'].dt.month

# Count occurrences of each release month in 2020
month_counts_2020 = df_2020['release_month'].value_counts()

# Find the month in 2020 with the most releases
most_releases_month_2020 = month_counts_2020.idxmax()
most_releases_count_2020 = month_counts_2020.max()  # Number of releases in the most active month

print("Month of 2020 with the Most Releases:", most_releases_month_2020)
print("Number of Releases in the Most Active Month:", most_releases_count_2020)

# For fun, what movies were released on any Friday the 13th? Let's not do popularity, let's focus on voting average
# Convert 'release_date' column to datetime format
df['release_date'] = pd.to_datetime(df['release_date'])

# Filter the DataFrame to include only movies released on Friday the 13th
friday_13th_movies = df[df['release_date'].dt.day == 13]
friday_13th_movies = friday_13th_movies[friday_13th_movies['release_date'].dt.weekday == 4]  # 4 corresponds to Friday

# Find the movie with the highest vote average among Friday the 13th releases
movie_with_highest_vote_average = friday_13th_movies.loc[friday_13th_movies['vote_average'].idxmax()]

print("Movie Released on a Friday the 13th with the Highest Vote Average:")
print(movie_with_highest_vote_average[['title', 'vote_average']])

#What language does horror speak?
# Let's find what language was the most popular
# Group the DataFrame by 'original_language' and calculate the average popularity for each language
language_popularity = df.groupby('original_language')['popularity'].mean()

# Find the language with the highest average popularity
most_popular_language = language_popularity.idxmax()
highest_average_popularity = language_popularity.max()

# Let's find the least
least_popular_language = language_popularity.idxmin()
lowest_average_popularity = language_popularity.min()

print("Most Popular Language:", most_popular_language)
print("Average Popularity for the Most Popular Language:", highest_average_popularity)

print("Least Popular Language:", least_popular_language)
print("Average Popularity for the Least Popular Language:", lowest_average_popularity)

# Instead of popularity, let's focus on voting_average
# Group the DataFrame by 'original_language' and calculate the average voting average for each language
language_voting_average = df.groupby('original_language')['vote_average'].mean()

# Find the language with the highest average voting average
highest_voting_language = language_voting_average.idxmax()
highest_average_voting_average = language_voting_average.max()

# Find the language with the least average voting average
least_voting_language = language_voting_average.idxmin()
least_average_voting_average = language_voting_average.min()

print("Language with the Highest Voting Average:", highest_voting_language)
print("Average Voting Average for the Highest Voting Language:", highest_average_voting_average)

print("\nLanguage with the Least Voting Average:", least_voting_language)
print("Average Voting Average for the Least Voting Language:", least_average_voting_average)

#Slash Costs
# Now we can get into the money of it all
# Calculate the correlation between 'budget' and 'popularity'
correlation = df['budget'].corr(df['popularity'])

print("Correlation Between Budget and Audience Popularity:", correlation)

# Filter out movies with a budget greater than 1000
df_filtered = df[df['budget'] > 1000]

# Find the movie with the highest budget and its revenue, popularity, and title
highest_budget_movie = df_filtered.loc[df_filtered['budget'].idxmax()]
highest_budget = highest_budget_movie['budget']
highest_budget_revenue = highest_budget_movie['revenue']
highest_budget_popularity = highest_budget_movie['popularity']
highest_budget_title = highest_budget_movie['title']

# Find the movie with the lowest budget and its revenue, popularity, and title
lowest_budget_movie = df_filtered.loc[df_filtered['budget'].idxmin()]
lowest_budget = lowest_budget_movie['budget']
lowest_budget_revenue = lowest_budget_movie['revenue']
lowest_budget_popularity = lowest_budget_movie['popularity']
lowest_budget_title = lowest_budget_movie['title']

# Compare the revenue of the highest and lowest budget movies
if highest_budget_revenue > lowest_budget_revenue:
    higher_revenue_movie = 'highest budget'
elif highest_budget_revenue < lowest_budget_revenue:
    higher_revenue_movie = 'lowest budget'
else:
    higher_revenue_movie = 'both movies have the same revenue'

print("Highest Budget Movie:")
print("Title:", highest_budget_title)
print("Budget:", highest_budget)
print("Revenue:", highest_budget_revenue)
print("Popularity:", highest_budget_popularity)

print("\nLowest Budget Movie:")
print("Title:", lowest_budget_title)
print("Budget:", lowest_budget)
print("Revenue:", lowest_budget_revenue)
print("Popularity:", lowest_budget_popularity)

print("\nMovie with Higher Revenue:", higher_revenue_movie)

# Find the index of the movie with the highest revenue
highest_revenue_index = df['revenue'].idxmax()

# Retrieve the title, revenue, and budget of the movie with the highest revenue
highest_revenue_title = df.loc[highest_revenue_index, 'title']
highest_revenue = df.loc[highest_revenue_index, 'revenue']
highest_revenue_budget = df.loc[highest_revenue_index, 'budget']

print("Movie with the Highest Revenue:")
print("Title:", highest_revenue_title)
print("Revenue:", highest_revenue)
print("Budget:", highest_revenue_budget)

# Filter out movies with a revenue of 0
df_filtered = df[df['revenue'] > 0]

# Find the index of the movie with the highest voting average in the filtered DataFrame
highest_voting_index = df_filtered['vote_average'].idxmax()

# Retrieve the title, revenue, budget, and voting average of the movie with the highest voting average
highest_voting_title = df_filtered.loc[highest_voting_index, 'title']
highest_voting_revenue = df_filtered.loc[highest_voting_index, 'revenue']
highest_voting_budget = df_filtered.loc[highest_voting_index, 'budget']
highest_voting_average = df_filtered.loc[highest_voting_index, 'vote_average']

print("Movie with the Highest Voting Average (Excluding Movies with Revenue of 0):")
print("Title:", highest_voting_title)
print("Revenue:", highest_voting_revenue)
print("Budget:", highest_voting_budget)
print("Voting Average:", highest_voting_average)
