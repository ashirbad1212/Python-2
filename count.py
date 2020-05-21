#Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame.
import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("The Original Dataframe is:")
print(diamonds.head())
print("\nCount, minimum, maximum  price for each value cut of diamonds DataFrame is as follows:")
print(diamonds.groupby('cut').price.agg(['count', 'min', 'max']))
