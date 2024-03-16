import ccxt


def fetchData():
    coinex = ccxt.coinex()

    coinex_funding_rates = coinex.fetch_funding_rates()
    # coinex_funding_rates = []

    for funding_rate_key in coinex_funding_rates.keys():
        try:
            coinex_funding_rate = coinex.fetch_funding_rate(funding_rate_key)
            coinex_funding_rates.append(coinex_funding_rate)
        except:
            continue
    return coinex_funding_rates
