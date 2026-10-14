import pandas as pd

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])

print(air_quality.head())
