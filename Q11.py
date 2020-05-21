#.  Write a Pandas program to count the duplicate rows of diamonds DataFrame.
import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("The Original Dataframe is as follows:")
print(diamonds.shape)
print("\n so the duplicate rows of diamonds dataFrame areas follows:")
print(diamonds.duplicated().sum())
