import requests

def temp(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data

paris_weather = temp(48.85,2.35)
print(f"{paris_weather["current"]["temperature_2m"]} C")


