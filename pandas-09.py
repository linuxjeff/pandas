import pandas as pd

df = pd.read_excel("Lukros_Dados.xlsx", sheet_name="Consulta_a_Roteiro")

print(df.head())
