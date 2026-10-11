import pandas as pd

titanic = pd.read_csv("titanic.csv")

ages = titanic["Age"]

print(ages.head())

print(titanic["Age"])

print(titanic["Age"].shape)
