'''
Задание 1
'''
import requests

def getcontent():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        for i, post in enumerate(posts[:5], start=1):
            print(f"Post {i}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}\n")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    getcontent()

'''
Задание 2
'''

import requests

def get_coordinates(city_name, api_key):
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city_name,
        'limit': 1,
        'appid': api_key
    }
    
    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        results = response.json()
        if results:
            lat = results[0]['lat']
            lon = results[0]['lon']
            return lat, lon

def get_weather_data(lat, lon, api_key):
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }
    
    response = requests.get(weather_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Температура: {temperature}°C, Погодные условия: {description}.")

def main():
    city_name = input("Введите город: ")
    api_key = "ac349f5c6c18855921e22def65ecd696"

    lat, lon = get_coordinates(city_name, api_key)
    if lat is not None and lon is not None:
        get_weather_data(lat, lon, api_key)

if __name__ == "__main__":
    main()
