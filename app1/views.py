
# app1/views.py
from django.shortcuts import render

from libs.open_weather_map import OpenWeatherMap


def index(request):
    open_weather_map = OpenWeatherMap()

    context = {
        'forecast': open_weather_map.get_forecast()
        }  # So far, we are not specifying any custom context
    return render(request, 'app1/index.html', context)