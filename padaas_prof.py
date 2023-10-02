import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv("nyc_weather.csv")
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="weather_data.html")