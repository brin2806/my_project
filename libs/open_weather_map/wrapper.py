# libs/open_weather_map/wrapper.py
import requests


class OpenWeatherMap():

    def __init__(self):
        # This is the base URL for the API and will be common to all requests
        self.api_url = 'http://api.openweathermap.org/data/2.5/'

    def get_forecast(self, city='', country=''):
    # Append the "forecast" path to the base API URL
        url = '%sforecast' % self.api_url

        # URL parameters
        params = {}
        if city and country:
            params['q'] = '%s,%s' % (city, country)
        else:
            params['lat'] = -33.8650
            params['lon'] = 151.2094


        # Do a get request on the forecast url, with the lat/lon params
        response = requests.get(url, params=params)

        # It's always a good idea to initialize results to empty, and update if data received
        results = {}
        # If the request was successful
        if response.status_code == requests.codes.ok:
            # Get the response body in JSON format
            results = response.json()

        return results        
