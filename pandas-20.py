import pandas as pd

titanic = pd.read_csv("titanic.csv")

titanic.iloc[0:3, 3] = "anonymous"

print(titanic.iloc[:5, 3])
