from meteostat import Point, Daily
import pandas as pd
from datetime import datetime

# Define location and time frame
location = Point(51.43, 6.77)  # Duisburg 的经纬度
start = datetime(2023, 1, 1)  # 转换为 datetime 对象
end = datetime(2023, 12, 31)  # 转换为 datetime 对象

# Get data
data = Daily(location, start, end)
data = data.fetch()

# Save to CSV
data.to_csv("Duisburg_Weather_2023.csv", index=True)  # index=True 保留索引
print("Weather data saved to Duisburg_Weather_2023.csv")
