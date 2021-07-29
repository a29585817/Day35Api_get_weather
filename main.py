import requests

API_KEY = "Your API_KEY"

parameters = {
    "lat": 25.105497,
    "lon": 121.597366,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
weather_slice = data["hourly"][:12]
will_rain = False
for x in weather_slice:
    code = x["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    print("Please bring umbrela")
