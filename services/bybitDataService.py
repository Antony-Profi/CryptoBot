import ccxt


def fetchData():
    bybit = ccxt.bybit()

    bybit_funding_rates = bybit.fetch_funding_rates()
    # bybit_funding_rates = []

    for funding_rate_key in bybit_funding_rates.keys():
        try:
            bybit_funding_rate = bybit.fetch_funding_rate(funding_rate_key)
            bybit_funding_rates.append(bybit_funding_rate)
        except:
            continue
    return bybit_funding_rates
