import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic.iloc[9:25, 2:5])
