import ccxt
from constans import BITMART
from helpers.dateHelper import getTimeDifference


def fetchData(brokerData):
    binance = ccxt.binance()
    bitmart = ccxt.bitmart()

    symbols = binance.fetch_funding_rates().keys()

    formatted_bitmart_funding_rates = []

    for symbol in symbols:
        try:
            bitmart_funding_rate = bitmart.fetch_funding_rate(symbol)
            formatted_bitmart_funding_rate = {
                "broker": BITMART,
                "symbol": bitmart_funding_rate["symbol"],
                "fundingRate": bitmart_funding_rate["fundingRate"],
                "fundingDatetime": bitmart_funding_rate["fundingDatetime"],
                "timeLeft": getTimeDifference(bitmart_funding_rate["fundingDatetime"])
            }
            formatted_bitmart_funding_rates.append(formatted_bitmart_funding_rate)
        except:
            continue
    brokerData.bitmartData = formatted_bitmart_funding_rates
