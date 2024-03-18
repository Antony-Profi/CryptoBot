import ccxt
from enums import broker
from enums.broker import Broker
from constans import BITGET
from helpers.dateHelper import getHoursDifferenceWithCurrentDateTime


def fetchData(brokerData):
    binance = ccxt.binance()
    bitget = ccxt.bitget()

    symbols = binance.fetch_funding_rates().keys()

    formatted_bitget_funding_rates = []

    for symbol in symbols:
        try:
            bitget_funding_rate = bitget.fetch_funding_rate(symbol)
            formatted_bitget_funding_rate = {
                broker: BITGET,
                "symbol": bitget_funding_rate["symbol"],
                "fundingRate": bitget_funding_rate["fundingRate"],
                "fundingDatetime": bitget_funding_rate["fundingDatetime"],
                "hoursLeft": getHoursDifferenceWithCurrentDateTime(bitget_funding_rate["fundingDatetime"]),
                "fundingRatePerHourRatio":
                    bitget_funding_rate["fundingRate"] / getHoursDifferenceWithCurrentDateTime(
                        bitget_funding_rate["fundingDatetime"]
                    )
            }
            formatted_bitget_funding_rates.append(formatted_bitget_funding_rate)
        except:
            continue
    brokerData.bitgetData = formatted_bitget_funding_rates
