import ccxt
from enums import broker
from enums.broker import Broker
from constans import BITGET
from helpers.dateHelper import getHoursDifferenceWithCurrentDateTime


def fetchData():
    binance = ccxt.binance()
    bitget = ccxt.bitget()

    symbols = binance.fetch_funding_rates().keys()

    formatted_bitget_funding_rates = []

    for symbol in symbols:
        bitget_funding_rate = bitget.fetch_funding_rate(symbol)
        print(bitget_funding_rate)
        try:
            formatted_bitget_funding_rate = {
                "broker": BITGET,
                "symbol": bitget_funding_rate["symbol"],
                "fundingRate": bitget_funding_rate["fundingRate"],
                "fundingDatetime": bitget_funding_rate["fundingDatetime"],
                "hoursLeft": getHoursDifferenceWithCurrentDateTime(bitget_funding_rate["fundingDatetime"])
            }
            if formatted_bitget_funding_rate["hoursLeft"] >= 1:
                formatted_bitget_funding_rate["fundingRatePerHourRatio"] = formatted_bitget_funding_rate[
                                                                                "fundingRate"] / \
                                                                            formatted_bitget_funding_rate["hoursLeft"]
            else:
                formatted_bitget_funding_rate["fundingRatePerHourRatio"] = 0

                formatted_bitget_funding_rates.append(formatted_bitget_funding_rate)
                print(symbol)
        except Exception as e:
            print("Error processing symbol:", symbol, "Error:", e)

    bitgetData = formatted_bitget_funding_rates


data = fetchData()
print(data)
