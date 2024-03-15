import ccxt


def fetchData():
    binance = ccxt.binance()
    okx = ccxt.okx()

    binance_funding_rates = binance.fetch_funding_rates()
    okx_funding_rates = []

    print("BINANCE\n", binance_funding_rates.keys())

    for funding_rate_key in binance_funding_rates.keys():
        try:
            okx_funding_rate = okx.fetch_funding_rate(funding_rate_key)
            print("OKX\n", okx_funding_rate)
            okx_funding_rates.append(okx.fetch_funding_rate(funding_rate_key))
        except:
            continue
    return binance_funding_rates, okx_funding_rates
