import requests

#Public api key
api_key = "783da1bd6901fc5682d61c95496c0ce0"
location = input("Enter the city name: ")

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}')
data = response.json()

if not data:
    raise ValueError("No data found. Please check the city name and try again.")


lat = data[0]['lat']
lon = data[0]['lon']


response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric')
data = response.json()

if not data:
    raise ValueError("Error while trying to get weather data. Please try again.")


print(
    f"Currently in {location} the weather is: {data['weather'][0]['description']} u// {data['main']['temp']} °C // h: {data['main']['temp_max']} °C // l: {data['main']['temp_min']} °C // humidty: {data['main']['humidity']} % // wind speed: {data['wind']['speed']} km/h"
    )