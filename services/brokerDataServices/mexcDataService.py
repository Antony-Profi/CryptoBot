import ccxt
from enums import broker
from enums.broker import Broker
from constans import MEXC


def fetchData(mexcData):
    binance = ccxt.binance()
    mexc = ccxt.mexc()

    symbols = binance.fetch_funding_rates().keys()

    formatted_mexc_funding_rates = []

    for symbol in symbols:
        try:
            mexc_funding_rate = mexc.fetch_funding_rate(symbol)
            formatted_mexc_funding_rate = {
                broker: MEXC,
                "symbol": mexc_funding_rate["symbol"],
                "fundingRate": mexc_funding_rate["fundingRate"],
                "fundingDatetime": mexc_funding_rate["fundingDatetime"]
            }
            formatted_mexc_funding_rates.append(formatted_mexc_funding_rate)
        except:
            continue
    mexcData = formatted_mexc_funding_rates