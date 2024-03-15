import ccxt


def fetchData():
    binance = ccxt.binance()
    bybit = ccxt.bybit()

    binance_funding_rates = binance.fetch_funding_rates()
    bybit_funding_rates = []

    print("BINANCE\n", binance_funding_rates.keys())

    for funding_rate_key in binance_funding_rates.keys():
        try:
            bybit_funding_rate = bybit.fetch_funding_rate(funding_rate_key)
            print("BYBIT\n", bybit_funding_rate)
            bybit_funding_rates.append(bybit.fetch_funding_rate(funding_rate_key))
        except:
            continue
    return binance_funding_rates, bybit_funding_rates
