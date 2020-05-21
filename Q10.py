#Write a Pandas program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame.
import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("The Original Dataframe is as follows:")
print(diamonds.head())
print("The number of rows and columns are:")
print(diamonds.shape)
print("After droping those rows where values are missing the remaining are:")
print(diamonds.dropna(how='any').shape)
