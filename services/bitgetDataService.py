import requests
from time import sleep

# Update based on Bitget API documentation
symbol = "BTCUSDT_UMCBL"

while True:
    # Try using an alternative endpoint
    url = f"https://api.bitget.com/api/mix/v1/market/futures_mark_price?symbol={symbol}"
    response = requests.get(url)

    # Check response status and data
    if response.status_code == 200:
        try:
            data = response.json()
            funding_rate = data.get("fundingRate")  # Use get() to avoid potential KeyError
            if funding_rate:
                print(f"Funding Rate: {funding_rate}")
        except (KeyError, AttributeError):
            print("Error: 'fundingRate' key not found in response data.")
    else:
        print(f"Error: {response.status_code}")
        # Additional checks:
        print(f"Response content: {response.text}")  # Print the full response for debugging

    sleep(60)

