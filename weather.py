import requests

API_KEY = '93057970572593c2857fabdbce2d22b8'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric' 
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            print(f"\nWeather in {city}, {country}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description.capitalize()}\n")
        else:
            print(f"\nError: {data['message'].capitalize()}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    location = input("Enter a city or ZIP code: ")
    get_weather(location)
