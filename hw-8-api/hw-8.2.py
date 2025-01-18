import requests
import json
from os import getenv

appid = getenv("open_weather_appid")
if appid == None:
    exit()

city = input("Enter the city name: ")

geocoder_response = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={appid}"
)

geocoder = json.loads(geocoder_response.content)

lat = geocoder[0]["lat"]
lon = geocoder[0]["lon"]

weather_response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={appid}"
)
weather = json.loads(weather_response.content)
print(weather["main"]["temp"])
print(weather["weather"][0]["description"])
