import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "1972c4f524c2e8bfa2096a31e0fb7a8e"
city_name = input("Please enter the name of the city or country you want to know the weather for: ")

weather_params = {
    "q": city_name,
    "units": "metric",
    "appid": api_key
}

try:

    response = requests.get(OWM_Endpoint, params=weather_params)

    data = response.json()

    print(f"The weather in {city_name} is :{data['weather'][0]['description']}")
    print(f"The temperature is {data['main']['temp']}")
    print(f"The humidity is {data['main']['humidity']}")
    print(f"The wind speed is {data['wind']['speed']}")

except:
    print("The city name or country name you entered was not recognized.")
