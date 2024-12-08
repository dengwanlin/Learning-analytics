from meteostat import Point, Daily
import pandas as pd
from datetime import datetime

# Define location and time frame
location = Point(51.43, 6.77)  # Duisburg's latitude and gratitude
start = datetime(2023, 1, 1)  # convert to datetime object
end = datetime(2023, 12, 31)  # convert to datetime object

# Get data
data = Daily(location, start, end)
data = data.fetch()

# Save to CSV
data.to_csv("Duisburg_Weather_2023.csv", index=True)  # index=True, keep the index
print("Weather data saved to Duisburg_Weather_2023.csv")
