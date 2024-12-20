import requests

#http://api.weatherapi.com/v1/current.json?key=3681f18eb0de4b66acc205019241612&q=Albuquerque&aqi=no



def get_weather(city):

    url = f'http://api.weatherapi.com/v1/current.json?key=3681f18eb0de4b66acc205019241612&q={city}&aqi=no'
    response = requests.get(url)
    weather = response.json()

    print(f'The current location is: {city}')

    temperature = weather.get('current').get('temp_f')
    print(f'The current temperature in F: {temperature}')
    condition = weather.get('current').get('condition').get('text')
    print(f'The current condition: {condition}')    

get_weather('Sedona')