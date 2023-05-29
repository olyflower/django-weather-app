import os
import requests
from django.shortcuts import render


def index(request):
    api_key = os.environ.get("API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    if request.method == "POST":
        city = request.POST["city"]
        current_weather = get_weather(city, api_key, url)
        return render(request, "../templates/index.html", current_weather)
    else:
        return render(request, "../templates/index.html")


def get_weather(city, api_key, url):
    response = requests.get(url.format(city, api_key)).json()
    weather_data = {
        "city": city,
        "temperature": response["main"]["temp"],
        "feels_like": response["main"]["feels_like"],
        "pressure": response["main"]["pressure"],
        "wind": response["wind"]["speed"],
        "description": response["weather"][0]["main"],
        "icon": response["weather"][0]["icon"],
    }
    return weather_data
