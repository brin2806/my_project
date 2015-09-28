from django.test import TestCase
from mock import patch
import requests 
import json


from libs.open_weather_map import OpenWeatherMap


class OpenWeatherMapTestCase(TestCase):
	def setUp(self):
		self.open_weather_map = OpenWeatherMap()

	@patch("requests.get")	
	def test_failure(self, mock_get):
		response = requests.Response()
		response.status_code = requests.codes.bad_request 
		mock_get.return_value = response

		forecast = self.open_weather_map.get_forecast()

		self.assertEqual({}, forecast)

	@patch("requests.get")	
	def test_success(self, mock_get):
		response = requests.Response()
		response.status_code = requests.codes.ok 
		response._content = b'{"city": {"name": "Sydney"}}'
		mock_get.return_value = response

		forecast = self.open_weather_map.get_forecast()

		self.assertEqual("Sydney", forecast['city']['name'])
