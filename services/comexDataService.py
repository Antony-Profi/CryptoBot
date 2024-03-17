import requests
from datetime import datetime


def fetchData():
    url = "https://api.commex.com/fapi/v1/fundingRate?limit=1000"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        funding_rates = []

        for item in data:
            symbol = item['symbol']
            funding_rate = item['fundingRate']
            funding_time = item['fundingTime']

            funding_time_str = datetime.fromtimestamp(funding_time / 1000).isoformat()

            funding_rates.append((symbol, funding_rate, funding_time_str))

        return funding_rates
    else:
        print(f"Ошибка: {response.status_code}")


funding_rates = fetchData()

for symbol, funding_rate, funding_time in funding_rates:
    print(f"Символ: {symbol}")
    print(f"Funding Rate: {funding_rate}")
    print(f"Funding Time: {funding_time}")
    print()
