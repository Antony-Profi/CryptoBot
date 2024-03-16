import ccxt


def fetchData():
    binance = ccxt.binance()
    mexc = ccxt.mexc()

    binance_funding_rates = binance.fetch_funding_rates()
    mexc_funding_rates = []

    for funding_rate_key in binance_funding_rates.keys():
        try:
            mexc_funding_rate = mexc.fetch_funding_rate(funding_rate_key)
            mexc_funding_rates.append(mexc_funding_rate)
        except:
            continue
    return mexc_funding_rates
