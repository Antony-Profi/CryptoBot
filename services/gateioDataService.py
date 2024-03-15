import requests
import time


def get_contracts_data():
    url = "https://api.gateio.ws/api/v4/futures/usdt/contracts?limit=100"

    headers = {
        "Timestamp": str(int(time.time() * 1000)),  # Временная метка в миллисекундах
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contracts_info = []

        for contract in data:
            contract_info = [
                contract['funding_rate'],
                contract['config_change_time'],
                contract['create_time'],
            ]

            contracts_info.append(contract_info)
        return contracts_info

    else:
        print(f"Ошибка: {response.status_code}")
        return None
