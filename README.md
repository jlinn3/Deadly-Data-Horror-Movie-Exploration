# Deadly-Data-Horror-Movie-Exploration
Explore the world of horror movies with my comprehensive analysis project. Join me as I delve into the dark and intriguing world of horror cinema!

## Data Source

The dataset used in this analysis was sourced from Kaggle's Horror Movie Dataset. 

- **Dataset Name:** [Horror Movies Dataset]([https://www.kaggle.com/example/horror-movie-dataset](https://www.kaggle.com/datasets/sujaykapadnis/horror-movies-dataset))
- **Original Authors:** [SUJAY KAPADNIS]([https://www.kaggle.com/example](https://www.kaggle.com/sujaykapadnis))
Please refer to the original dataset for any specific licensing terms and conditions.

## Overview

This project explores the world of horror movie series through data analysis and visualization. I conducted exploratory data analysis (EDA) and data preprocessing using Python, focusing on a dataset sourced from Kaggle's Horror Movie Dataset. My analysis aims to uncover insights into horror movie series trends, popular franchises, and audience preferences. Essentially, I started with these questions to tackle:

  1. What are the most common terms in a movie description?
  2. What are the most popular and least popular horror movie?
  3. What year were the most horror movies released?
  4. Is there a correlation between budget and popularity?

## Data Preprocessing

I started by preprocessing the dataset to prepare it for analysis. Here are some of the preprocessing steps  performed:

Converted the text in the 'overview' column to lowercase.
Filtered out common words and stopwords from the 'overview' column.
Removed movies with a budget less than 1000 and revenue of 0.
Converted the 'release_date' column to datetime format and extracted 'release_year' and 'release_month'.
Excluded movies with genres containing the word 'horror'.
Dropped unnecessary columns such as 'poster_path', 'vote_count', 'status', 'backdrop_path', and 'adult'.
Saved the preprocessed data to a new CSV file.

## Dashboard Visualization on PowerBI

I created an interactive dashboard to visualize our findings and insights from the analysis. The dashboard allows users to explore horror movie series data through various charts, graphs, and filters. Check it out [here](https://app.powerbi.com/links/6-TgLbWc17?ctid=e641f655-18d2-4998-92ee-2370a0982732&pbi_source=linkShare)
