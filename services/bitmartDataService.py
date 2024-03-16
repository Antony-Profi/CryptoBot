import ccxt


def fetchData():
    binance = ccxt.binance()
    bitmart = ccxt.bitmart()

    binance_funding_rates = binance.fetch_funding_rates()
    bitmart_funding_rates = []

    for funding_rate_key in binance_funding_rates.keys():
        try:
            bitmart_funding_rate = bitmart.fetch_funding_rate(funding_rate_key)
            bitmart_funding_rates.append(bitmart_funding_rate)
        except:
            continue
    return bitmart_funding_rates
