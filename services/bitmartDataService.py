import ccxt


def fetchData():
    binance = ccxt.binance()
    bitmart = ccxt.bitmart()

    symbols = binance.fetch_funding_rates().keys()
    bitmart_funding_rates = []


    for symbol in symbols:
        try:
            bitmart_funding_rate = bitmart.fetch_funding_rate(symbol)
            

          
            bitmart_funding_rates.append()
        except:
            continue
    return bitmart_funding_rates
