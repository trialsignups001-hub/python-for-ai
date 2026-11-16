import requests
from datetime import datetime, timedelta
import pandas as pd

latitude = 48.85
longitude = 2.35

today_date = datetime.now()
week_before_date = today_date - timedelta(days=7)
print(today_date)

start_date = week_before_date.strftime("%Y-%m-%d")
print(start_date)
end_date = today_date.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

data = requests.get(url)
data_json = data.json()

print(data_json)