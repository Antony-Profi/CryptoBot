import ccxt


def fetchData():
    binance = ccxt.binance()
    bitget = ccxt.bitget()

    binance_funding_rates = binance.fetch_funding_rates()
    bitget_funding_rates = []

    print("BINANCE\n", binance_funding_rates.keys())

    for funding_rate_key in binance_funding_rates.keys():
        try:
            bitget_funding_rate = bitget.fetch_funding_rate(funding_rate_key)
            print("BITGET\n", bitget_funding_rate)
            bitget_funding_rates.append(bitget.fetch_funding_rate(funding_rate_key))
        except:
            continue
    return binance_funding_rates, bitget_funding_rates
