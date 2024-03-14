import requests
import time


def get_contracts_data():
    """
    Функция для получения информации о фьючерсных контрактах с Gate.io.

    :return: Список с информацией о контрактах.
    """

    # URL запроса
    url = "https://api.gateio.ws/api/v4/futures/usdt/contracts?limit=100"

    # Заголовок с временной меткой
    headers = {
        "Timestamp": str(int(time.time() * 1000)),  # Временная метка в миллисекундах
    }

    # Отправка запроса
    response = requests.get(url, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Преобразование ответа в JSON
        data = response.json()

        # Список для хранения информации о контрактах
        contracts_info = []

        # Обработка данных
        for contract in data:
            # Создание списка с информацией о контракте
            contract_info = [
                contract['funding_rate'],
                contract['config_change_time'],
                contract['create_time'],
            ]

            # Добавление информации о контракте в список
            contracts_info.append(contract_info)

        # Возвращение списка с информацией о контрактах
        return contracts_info

    else:
        # Ошибка при получении данных
        print(f"Ошибка: {response.status_code}")
        return None