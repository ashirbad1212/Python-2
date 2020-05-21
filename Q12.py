# Write a Pandas program to get sample 75% of the diamonds DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame
import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("The Original Dataframe is as follows:")
print(diamonds.shape)
print("\n The Sample of  75% of diamonds DataFrame's rows without replacement is as follows:")
result = diamonds.sample(frac=0.75, random_state=99)
print(result)
print("\nThe remaining 25% of the rows are:")
print(diamonds.loc[~diamonds.index.isin(result.index), :])
