import requests

def get_weather_forecast(api_key, city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] == 200:
        weather_info = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return weather_info, temperature, humidity, wind_speed
    else:
        return None

def main():
    api_key = '2608c4b53dfcef8c0774a3c76c410cb9'  # Replace with your actual API key
    city_name = 'dapitan city'  # Replace with your desired city

    weather_data = get_weather_forecast(api_key, city_name)
    if weather_data:
        weather_info, temperature, humidity, wind_speed = weather_data
        print(f"Weather Forecast for {city_name}:")
        print(f"- Weather: {weather_info}")
        print(f"- Temperature: {temperature}°C")
        print(f"- Humidity: {humidity}%")
        print(f"- Wind Speed: {wind_speed} m/s")
    else:
