import requests

from django.conf import settings
from django.shortcuts import render


def index(request):
    api_key = settings.API_KEY
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    if request.method == "POST":
        city = request.POST["city"]
        current_weather = get_weather(city, api_key, url)
        context = {"current_weather": current_weather, }
        return render(request, "../templates/index.html", context)
    else:
        return render(request, "../templates/index.html")


def get_weather(city, api_key, url):
    response = requests.get(url.format(city, api_key)).json()
    weather_data = {
        "city": city,
        "temperature": round(response["main"]["temp"] - 273.15),
        "feels_like": round(response["main"]["feels_like"] - 273.15),
        "pressure": response["main"]["pressure"],
        "wind": response["wind"]["speed"],
        "description": response["weather"][0]["main"],
        "icon": response["weather"][0]["icon"],
    }
    return weather_data
