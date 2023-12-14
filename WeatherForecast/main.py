import requests

def get_data(city,unit,api_key):
    try: 
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&APPID={api_key}")
        response.raise_for_status()  # Check for errors in the HTTP request
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return None

def display_data(weather_data):
    if weather_data:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_condition = weather_data['weather'][0]['description']

        print(f"\nWeather in {weather_data['name']}:")
        if unit == 'c':
            print(f"Temperature: {temp}°C")
        else:
            print(f"Temperature: {temp}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} meter/sec")
        print(f"Weather Condition: {weather_condition.capitalize()}\n")
    else:
        print("Unable to fetch weather data. Please check your input or try again later.")

if __name__ == "__main__":
    api_key = '2f99076cd56980060d392dc64ecf8165'
    city = input("Enter city name: ")
    unit = input("Enter C for celsius and F for farenheit: ").lower()

    while unit not in ['c','f']:
        print("Invalid input. Please enter 'C' or 'F'")
        unit = input("Enter C for celsius and F for farenheit: ").lower()
    if unit == 'c':
        weather_data = get_data(city,'metric',api_key)
        display_data(weather_data)
    else:
        weather_data = get_data(city,'imperial',api_key)
        display_data(weather_data)