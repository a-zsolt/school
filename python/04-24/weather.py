import requests
import json

#Public api key
api_key = "783da1bd6901fc5682d61c95496c0ce0"
location = input("Enter the city name: ")

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}')
data = response.json()

lat = data[0]['lat']
lon = data[0]['lon']

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric')
data = response.json()


print(f"Currently in {location} the weather is: {data['weather'][0]['description']} // {data['main']['temp']} °C // h: {data['main']['temp_max']} °C // l: {data['main']['temp_min']} °C // humidty: {data['main']['humidity']} % // wind speed: {data['wind']['speed']} km/h")