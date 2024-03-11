import requests as requests

base = "https://fapi.binance.com"
path = "/fapi/v1/premiumIndex"
url = base + path
param = {"symbol": "ETHUSDT"}
r = requests.get(url, params=param)
if r.status_code == 200:
    data = r.json()
    print(data)

else:
    print("error")
