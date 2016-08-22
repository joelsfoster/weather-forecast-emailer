import requests

# Get the weather forecast for today
def get_weather_forecast():
    # Note to dev: add affordances for two-word names like "New York"
    zip_code = input("What is your ZIP code?")
    #
    country_code = "us"
    url ='http://api.openweathermap.org/data/2.5/weather?zip=' + zip_code + ',' + country_code + '&units=metric&appid=7477fad7ebe10ae26c2d45c57dc4e96f'
    weather_request = requests.get(url)

    # Take the returned data and convert it to JSON, then parse the info we need from it
    weather_json = weather_request.json()
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Create a readable sentance with our information
    forecast = "The forecast for today is "
    forecast += description + " with a high of " + str(int(temp_max)) + "C"
    forecast += " and a low of " + str(int(temp_min)) + "C."
    
    return forecast
