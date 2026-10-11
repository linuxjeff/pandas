import pandas as pd

titanic = pd.read_csv("titanic.csv")

ages_sex = titanic[["Age", "Sex"]]

print(ages_sex.head())

print(type(ages_sex))

print(ages_sex.shape)
