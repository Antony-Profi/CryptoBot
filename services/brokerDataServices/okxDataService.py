import ccxt
from constans import OKX
from helpers.dateHelper import getTimeDifference


def fetchData(brokerData):
    binance = ccxt.binance()
    okx = ccxt.okx()

    symbols = binance.fetch_funding_rates().keys()

    formatted_okx_funding_rates = []

    for symbol in symbols:
        try:
            okx_funding_rate = okx.fetch_funding_rate(symbol)
            formatted_okx_funding_rate = {
                "broker": OKX,
                "symbol": okx_funding_rate["symbol"],
                "fundingRate": okx_funding_rate["fundingRate"],
                "fundingDatetime": okx_funding_rate["fundingDatetime"],
                "hoursLeft": getTimeDifference(okx_funding_rate["fundingDatetime"])
            }
            formatted_okx_funding_rates.append(formatted_okx_funding_rate)
        except:
            continue
    brokerData.okxData = formatted_okx_funding_rates
