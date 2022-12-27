import requests
from config import weather_token
import datetime
# print(weather_token)
def get_weather(city,weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        data = r.json()
        # print(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***"
              f"Погода нынче: {city}\n Температура: {cur_weather}C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}м/с\n"
              f"Восход Солнца: {sunrise}\nЗакат Солнца:{sunset}\nДлинна дня: {length_of_the_day}\n"
              f"Хорошего дня!")
    except Exception as ex:
        print(ex)
        print("Error! Try to enter the name of the city again!")

def main():
    city = input("Enter city: ")
    get_weather(city, weather_token)

if __name__ == '__main__':
    main()