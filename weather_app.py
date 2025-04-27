import requests
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # for Celsius
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc.capitalize()}")
    else:
        print("\nError:", data.get("message", "Unable to fetch weather."))
def main():
    print("=== Weather App ===")
    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter city name or ZIP code: ")
    get_weather(api_key, location)
if __name__ == "__main__":
    main()
