import requests
import pandas as pd
from datetime import datetime, timedelta


#  cities 
cities = {
   "Johannesburg": (-26.2041, 28.0473),
    "Cape Town": (-33.9249, 18.4241),
    "Durban": (-29.8587, 31.0218),
    "Pretoria": (-25.7479, 28.2293),
    "Port Elizabeth": (-33.9608, 25.6022),
    "Bloemfontein": (-29.0852, 26.1596),
    "East London": (-33.0153, 27.9116),
    "Polokwane": (-23.8967, 29.4486),
    "Nelspruit": (-25.4658, 30.9853),
    "Kimberley": (-28.7294, 24.7595)
}

#  Calculates dynamic 7-day date range
end_date = datetime.today().date()
start_date = end_date - timedelta(days=7)

print(f"Fetching data from {start_date} to {end_date} ...")

all_data = []

for city, (lat, lon) in cities.items():
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max"
        f"&timezone=Africa/Johannesburg"
    )

    response = requests.get(url)
    data = response.json()

    if "daily" not in data:
        print(f"⚠️ No data available for {city}")
        continue

    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"],
        "rainfall_mm": data["daily"]["precipitation_sum"],
        "wind_max": data["daily"]["windspeed_10m_max"]
    })
    df["city"] = city
    all_data.append(df)

#  Combines all city data
final_df = pd.concat(all_data)
final_df.to_csv("data/raw_weather_data.csv", index=False)

print(f" Data extracted for {len(cities)} cities from {start_date} to {end_date}")


