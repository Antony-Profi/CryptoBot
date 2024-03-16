import ccxt


def fetchData():
    gateio = ccxt.gateio()

    gateio_funding_rates = gateio.fetch_funding_rates()
    # gateio_funding_rates = []

    for funding_rate_key in gateio_funding_rates.keys():
        try:
            gateio_funding_rate = gateio.fetch_funding_rate(funding_rate_key)
            gateio_funding_rates.append(gateio_funding_rate)
        except:
            continue
    return gateio_funding_rates
