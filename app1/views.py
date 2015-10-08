
# app1/views.py
from django.shortcuts import render

from libs.open_weather_map.wrapper import OpenWeatherMap
from app1 import forms as app1_forms


def index(request):
    context = {}
    # If request has GET parameters, this means it was created when the user clicked the submit
    # submit button on the form
    if request.GET:
         # Create a bound form based on the GET parameters to the request
        form = app1_forms.LocationForm(request.GET)
        if form.is_valid():
            # If the form parameters are valid, search for weather based on the form data
            # If the form parameters are invalid, the page will be loaded showing the errors
            open_weather_map = OpenWeatherMap()
            context['forecast'] = open_weather_map.get_forecast(
                    city=form.cleaned_data['city'], country=form.cleaned_data['country'])
    else:
        # This is an initial page load, so create an unbound form
        form = app1_forms.LocationForm()
    # Add the form to the page context so it is available to the template
    context['form'] = form
    return render(request, 'app1/index.html', context)    