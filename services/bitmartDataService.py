import ccxt


def fetchData():
    binance = ccxt.binance()
    bitmart = ccxt.bitmart()

    binance_funding_rates = binance.fetch_funding_rates()
    bitmart_funding_rates = []

    print("BINANCE\n", binance_funding_rates.keys())

    for funding_rate_key in binance_funding_rates.keys():
        try:
            bitmart_funding_rate = bitmart.fetch_funding_rate(funding_rate_key)
            print("BITMART\n", bitmart_funding_rate)
            bitmart_funding_rates.append(bitmart.fetch_funding_rate(funding_rate_key))
        except:
            continue
    return binance_funding_rates, bitmart_funding_rates
