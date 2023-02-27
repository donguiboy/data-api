
import sys
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    url = f'https://weather.lewagon.com/geo/1.0/direct?q={query}&limit=5'
    response = requests.get(url).json()
    if len(response) == 1:
        city = response[0]
        return city
    if len(response) == 0:
        print("The city doesn't exist")
        return None
    for index, value in enumerate(response):
        print (f"{index+1}. {value['name']}, {value['country']}")
    final_answer = int(input("Multiple matches found, which city did you mean?\n")) -1
    return response[final_answer]

def weather_forecast(lat, lon):
    url = f"https://weather.lewagon.com/data/2.5/forecast?lat={lat}&lon={lon}"
    response = requests.get(url).json()
    for i in range(0,len(response["list"]),8):
        forecasts = []
        forecasts.append(response["list"][i])
        return forecasts

def main():
    query = input("City?\n> ")
    city = search_city(query)
    weather_forecast(city["lat"],city["lon"])

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
