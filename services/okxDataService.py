import ccxt


def fetchData():
    binance = ccxt.binance()
    okx = ccxt.okx()

    binance_funding_rates = binance.fetch_funding_rates()
    okx_funding_rates = []

    for funding_rate_key in binance_funding_rates.keys():
        try:
            okx_funding_rate = okx.fetch_funding_rate(funding_rate_key)
            okx_funding_rates.append(okx_funding_rate)
        except:
            continue
    return okx_funding_rates
