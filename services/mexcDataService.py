import ccxt


def fetchData():
    binance = ccxt.binance()
    mexc = ccxt.mexc()

    binance_funding_rates = binance.fetch_funding_rates()
    mexc_funding_rates = []

    print("BINANCE\n", binance_funding_rates.keys())

    for funding_rate_key in binance_funding_rates.keys():
        try:
            mexc_funding_rate = mexc.fetch_funding_rate(funding_rate_key)
            print("MEXC\n", mexc_funding_rate)
            mexc_funding_rates.append(mexc.fetch_funding_rate(funding_rate_key))
        except:
            continue
    return binance_funding_rates, mexc_funding_rates
