import pandas as pd

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality_renamed = air_quality.rename(columns={
    "station_antwerp": "BETR801",
    "station_paris": "FR04014",
    "station_london": "London Westminster",    
})

print(air_quality_renamed.head())

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)

print(air_quality_renamed.head())
