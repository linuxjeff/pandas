import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality.head()

for metho_name in dir(air_quality.plot):
    if not metho_name.startswith("_"):
        print(metho_name)
