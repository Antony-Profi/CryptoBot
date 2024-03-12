from binance import Client


client = Client()


def fetchData():
    return client.futures_mark_price()

