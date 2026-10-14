import pandas as pd

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

print(air_quality.head())
