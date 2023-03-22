import requests


def get_weather(misto):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={misto}&appid={api_key}&units=metric"
    print(url)
    response_get = requests.get(url)
    response_json = response_get.json()


    weather = response_json['weather'][0]['description']
    temp = response_json['main']['temp']
    feels_like = response_json['main']['feels_like']
    city = response_json['name']

    weather_msg = f'the weather in {city}: {weather}'
    temp_msg = f'temperature is {temp}'
    feels_like_msg = f'feels like {feels_like}'

    print(response_get.url)

    return weather_msg, temp_msg, feels_like_msg


def get_forecast(misto, i):
    api_key = "c391c9305dfc0f78f2e9eb6516d65c87"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={misto}&appid={api_key}&units=metric"

    response_get = requests.get(url)
    response_json = response_get.json()



    weather = response_json['list'][i]['weather'][0]['description']
    temp = response_json['list'][i]['main']['temp']
    feels_like = response_json['list'][i]['main']['feels_like']
    city = response_json['city']['name']

    time = response_json['list'][i]['dt_txt']

    time_msg = f'forecast for {time}'
    weather_msg = f'the weather in {city}: {weather}'
    temp_msg = f'temperature is {temp}'
    feels_like_msg = f'feels like {feels_like}'


    return time_msg, weather_msg, temp_msg, feels_like_msg


if __name__ == "__main__":
    get_weather(misto="london")



