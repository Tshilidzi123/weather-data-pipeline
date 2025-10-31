import pandas as pd
import mysql.connector
import json

# Loading database credentials
with open("config/db_config.json") as f:
    db_config = json.load(f)

# Connection to MySQL
connection = mysql.connector.connect(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
)
cursor = connection.cursor()

# Reads cleaned data
df = pd.read_csv("data/clean_weather_data.csv")

# Inserting data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO daily_weather (date, city, temp_max, temp_min, temp_range, rainfall_mm, wind_max)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['date'],
        row['city'],
        row['temp_max'],
        row['temp_min'],
        row['temp_range'],
        row['rainfall_mm'],
        row['wind_max']
    ))

# Commits and closes connection
connection.commit()
connection.close()

