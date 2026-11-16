import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt



latitude = -25.274399
longitude = 133.775131

today_date = datetime.now()
week_before_date = today_date - timedelta(days = 7)

start_date= week_before_date.strftime("%Y-%m-%d")
end_date= today_date.strftime("%Y-%m-%d")


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()

date_time = data["daily"]

daily_table = pd.DataFrame({"Date": date_time["time"],
                            "Minimum Temperature":date_time["temperature_2m_min"],
                            "Maximum_Temperature":date_time["temperature_2m_min"]})


figure = plt.figure(figsize=(10,6))
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Last 1 week Temperature in Australia")
plt.plot(date_time["time"], date_time["temperature_2m_min"],marker="o", label="Minimum Temperature")
plt.plot(date_time["time"], date_time["temperature_2m_max"],marker="o", label="Maximum Temperature")
plt.legend()
plt.savefig("Aus_weather.png")
plt.show()

if not os.path.exists("data_test"):
    os.makedirs("data_test")