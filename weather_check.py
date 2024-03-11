import requests

def get_weather(city):
    
    endpoint = 'https://api.openweathermap.org/data/2.5/weather/'
    api_key = '98beb11ab0ebdd51d1293f2ea44686fe'

    params_data = {
        "apiKey": api_key,
        "q": city,
        "units": "metric"
    }
    
    response = requests.get(f'{endpoint}', params=params_data).json()
    
    return response 