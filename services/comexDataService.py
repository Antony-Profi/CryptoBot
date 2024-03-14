# import threading
#
# import requests
#
#
# def fetch_funding_rates():
#     url = "https://api.commex.com/fapi/v1/fundingRate?limit=1000"
#
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#
#         funding_rates = []  # Создание пустого списка
#
#         for item in data:
#             symbol = item['symbol']
#             funding_rate = item['fundingRate']
#
#             funding_rates.append((symbol, funding_rate))  # Добавление элементов в список
#
#         return funding_rates
#     else:
#         print(f"Ошибка: {response.status_code}")


import requests
from datetime import datetime


def fetch_funding_rates():
    url = "https://api.commex.com/fapi/v1/fundingRate?limit=1000"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        funding_rates = []  # Создание пустого списка

        for item in data:
            symbol = item['symbol']
            funding_rate = item['fundingRate']
            funding_time = item['fundingTime']

            # Преобразование timestamp в читаемый формат
            funding_time_str = datetime.fromtimestamp(funding_time / 1000).isoformat()

            funding_rates.append((symbol, funding_rate, funding_time_str))  # Добавление элементов в список

        return funding_rates
    else:
        print(f"Ошибка: {response.status_code}")


# # Пример использования
# funding_rates = fetch_funding_rates()

# for symbol, funding_rate, funding_time in funding_rates:
#     print(f"Символ: {symbol}")
#     print(f"Funding Rate: {funding_rate}")
#     print(f"Funding Time: {funding_time}")
#     print()
