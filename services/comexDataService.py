import threading

import requests


def fetch_funding_rates():
    url = "https://api.commex.com/fapi/v1/fundingRate?limit=1000"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        funding_rates = []  # Создание пустого списка

        for item in data:
            symbol = item['symbol']
            funding_rate = item['fundingRate']

            funding_rates.append((symbol, funding_rate))  # Добавление элементов в список

        print(funding_rates)
    else:
        print(f"Ошибка: {response.status_code}")


def update_data():
    global data

    # Получение данных с Comex
    data = fetch_funding_rates()

    # Обновление данных каждую минуту
    threading.Timer(10, update_data).start()

# Запуск обновления
update_data()
