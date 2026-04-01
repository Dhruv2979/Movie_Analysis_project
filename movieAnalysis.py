import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the DataSet
df = pd.read_csv(r"C:\Users\DHRUV SHAH\Python\project 3\MovieData.csv")
print(df.head(10))

# Data inspection
print(df.info())
print(df.describe())

# Data Cleaning
print(df.isnull().sum())
df['Year'] = df['Year'].astype(int)
df['Views'] = df['Views'].astype(int)
print(df.duplicated().sum())
print(df.info())

# Basic analysis
avg_movieRating = df['Rating'].mean()
max_HighestRating = df.loc[df['Rating'].idxmax(),'Rating']
min_LowestRating = df.loc[df['Rating'].idxmin(),'Rating']
HighestViews = df.loc[df['Views'].idxmax(),'Title']
HighestGenre = df.loc[df['Genre'].idxmax(),'Rating']
HighestYear = df.loc[df['Year'].idxmax(),'Rating']


print(f"Average Movie Rating is {avg_movieRating}\n")
print(f"Max Rating movie is {max_HighestRating}\n")
print(f"Min Rating movie is {min_LowestRating}\n")
print(f"Highest View is {HighestViews}\n")
print(f"Highest Genre is {HighestGenre}\n")
print(f"Highest Year is {HighestYear}\n")

# Advance Analysis
most_Viewed = df.nlargest(5,'Views')[['Title','Views']]
print(most_Viewed)

most_Rated = df.nlargest(5,'Rating')[['Title','Rating']]
print(most_Rated)

# Data visualization
sns.barplot(x="Genre", y="Rating", data=df, color="y")
plt.show()

sns.displot(df['Rating'], kde=True, color="r")
plt.show()

sns.scatterplot(x="Views", y="Rating", data=df, color="b")
plt.show()

sns.lineplot(x="Year", y="Rating", data = df, color="r")
plt.show()

sns.countplot(x="Genre",data=df, color="g", hue="Title")
plt.show()

# Average views per Genre
avg_views = df.groupby('Genre')['Views'].mean()
print(avg_views)

most_watchedGenre = df.loc[df['Genre'].idxmax(),'Genre']
print(f"Most Watched genre is {most_watchedGenre}")

# Find number of movies Relased each year
sns.barplot(x="Title", y="Year", data=df, color="y")
plt.show()

# Find Median rating of movies
Median_Rating = df['Rating'].median()
print(Median_Rating)

"""
1) Action and Sci-Fi movie have higher average ratings compared to other genres.
2) Recent movies (2021-2023) have higher average ratings compared to old movies.
3) Some genres like Horror or Comedy have lower average ratings.
4) A small number of movies are extremely popular.
"""