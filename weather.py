import requests
import tkinter as tk
from tkinter import messagebox, font


def get_weather():
    city = city_entry.get()

    url = ('https://api.openweathermap.org/data/2.5/weather?q=' + city +
           '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

    weather_data = requests.get(url).json()

    if weather_data.get('main') is None:
        messagebox.showerror('Ошибка', 'Невозможно получить информацию о '
                             'погоде для данного города')
        return

    temperature = weather_data['main']['temp']
    temperature_feels = round(weather_data['main']['feels_like'])
    wind_speed = weather_data['wind']['speed']

    result_label['text'] = f'Сейчас в городе {city} {round(temperature)} ' \
                           f'градусов\n' \
                           f'Ощущается как {temperature_feels} градусов\n' \
                           f'Скорость ветра {wind_speed} м/с'


root = tk.Tk()
root.title("Приложение для прогноза погоды")

title_font = font.Font(size=14, weight='bold')
entry_font = font.Font(size=12)
button_font = font.Font(size=12)
result_font = font.Font(size=10)

title_label = tk.Label(root, text="Введите название города:", font=title_font)
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=entry_font)
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Получить погоду", font=button_font,
                               command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, height=4, font=result_font)
result_label.pack(pady=10)

root.mainloop()
