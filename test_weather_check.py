import unittest
from unittest import mock
from weather_check import get_weather

class TestGetWeather(unittest.TestCase):
    
    # Note: Mock is used for each test because we need to replace the real requests.get function with a fake one for testing.
    
    @mock.patch("weather_check.requests.get")
    def test_get_weather(self, mock_requests_get):
        
        # Define the data that our fake requests.get function will return when the city is valid
        data = {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 14.17, 'feels_like': 13.26, 'temp_min': 12.86, 'temp_max': 15.32, 'pressure': 1008, 'humidity': 62}, 'visibility': 10000, 'wind': {'speed': 7.2, 'deg': 250}, 'clouds':
                {'all': 75}, 'dt': 1649169046, 'sys': {'type': 2, 'id': 2019646, 'country': 'GB', 'sunrise': 1649136418, 'sunset': 1649183948}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
        
        # Set up fake response for the call to requests.get
        mock_requests_get.return_value = mock.Mock(
            name="mock response", **{"status_code": 200, "json.return_value": data})

        # Call the function with a valid city and check that it returns the correct data
        assert get_weather("London")['name'] == data['name']
        
        # Check that requests.get was called exactly once
        mock_requests_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()