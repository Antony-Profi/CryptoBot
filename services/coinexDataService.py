import ccxt


def fetchData():
    binance = ccxt.binance()
    coinex = ccxt.coinex()

    binance_funding_rates = binance.fetch_funding_rates()
    coinex_funding_rates = []

    print("BINANCE\n", binance_funding_rates.keys())

    for funding_rate_key in binance_funding_rates.keys():
        try:
            coinex_funding_rate = coinex.fetch_funding_rate(funding_rate_key)
            print("COINEX\n", coinex_funding_rate)
            coinex_funding_rates.append(coinex.fetch_funding_rate(funding_rate_key))
        except:
            continue
    return binance_funding_rates, coinex_funding_rates
