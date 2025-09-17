from src.utils import convert_operations_dict
import os
from dotenv import load_dotenv
import requests

# Загружаем переменные окружения из файла .env
load_dotenv()

def get_exchange_rate(currency: str) -> float:
    """
    Получает курс валюты к рублю (RUB) через API.

    :param currency: Код валюты (например, 'USD', 'EUR').
    :return: Курс валюты к рублю (float) или None в случае ошибки.
    """
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")

    if not api_key or not base_url:
        print("API_KEY или BASE_URL не найдены в переменных окружения.")
        return None

    try:
        # Формируем параметры запроса
        params = {"symbols": "RUB", "base": currency}
        headers = {"apikey": api_key}

        # Выполняем запрос к API
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  # Проверяем статус ответа

        # Парсим JSON-ответ
        data = response.json()
        rate = data["rates"]["RUB"]
        return rate

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except KeyError:
        print("Некорректный ответ от API.")
        return None


def get_transaction_amount_in_rubles(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях.

    :param transaction: Словарь с данными транзакции (должен содержать 'operationAmount').
    :return: Сумма в рублях (float) или None в случае ошибки.
    """
    operation_amount = transaction.get("operationAmount")
    if not operation_amount:
        print("Транзакция не содержит поля 'operationAmount'.")
        return None

    amount_str = operation_amount.get("amount")
    currency_code = operation_amount.get("currency", {}).get("code")

    if not amount_str or not currency_code:
        print("Транзакция не содержит полей 'amount' или 'currency.code'.")
        return None

    # Преобразуем сумму в число
    try:
        amount = float(amount_str)
    except ValueError:
        print(f"Некорректное значение суммы: {amount_str}")
        return None

    # Если валюта — RUB, возвращаем сумму без конвертации
    if currency_code.upper() == "RUB":
        return amount

    # Если валюта — USD или EUR, выполняем конвертацию
    if currency_code.upper() in ["USD", "EUR"]:
        exchange_rate = get_exchange_rate(currency_code.upper())
        if exchange_rate is not None:
            return amount * exchange_rate
        else:
            print(f"Не удалось получить курс для валюты: {currency_code}")
            return None

    # Если валюта не поддерживается
    print(f"Валюта {currency_code} не поддерживается.")
    return None


if __name__ == "__main__":
    # Указываем путь к файлу operations.json
    file_path = "../data/operations.json"

    # Загружаем данные о транзакциях
    transactions = convert_operations_dict(file_path)

    # Обрабатываем каждую транзакцию
    if transactions:
        for transaction in transactions:
            rubles_amount = get_transaction_amount_in_rubles(transaction)
            print(f"ID транзакции: {transaction.get('id')}, Сумма в рублях: {rubles_amount}")
    else:
        print("Нет данных для обработки.")