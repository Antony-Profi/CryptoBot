import ccxt


def fetchData():
    binance = ccxt.binance()
    bitget = ccxt.bitget()

    binance_funding_rates = binance.fetch_funding_rates()
    bitget_funding_rates = []

    for funding_rate_key in binance_funding_rates.keys():
        try:
            bitget_funding_rate = bitget.fetch_funding_rate(funding_rate_key)
            bitget_funding_rates.append(bitget_funding_rate)
        except:
            continue
    return bitget_funding_rates
