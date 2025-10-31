import pandas as pd

# Loads the raw weather data
df = pd.read_csv("data/raw_weather_data.csv")
print("✅ Raw data loaded")
print(df.head())

# Converts the 'time' column to datetime
df['date'] = pd.to_datetime(df['date'])

df.rename(columns={
    'time': 'date',
    'temperature_2m_max': 'temp_max',
    'temperature_2m_min': 'temp_min',
    'precipitation_sum': 'rainfall_mm',
    'windspeed_10m_max': 'wind_max'
}, inplace=True)

# Adds a new column for temperature range
df['temp_range'] = df['temp_max'] - df['temp_min']

# sort by city and date
df.sort_values(by=['city', 'date'], inplace=True)

# Saving the cleaned data
df.to_csv("data/clean_weather_data.csv", index=False)
