import json

from logger import logger
from src.external_api import get_exchange_rate


def load_transactions_json(file_path):
    logger.info(f"Загружаем транзакции из файла: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info("Успешно загружены транзакции")
            return data

    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Ошибка при загрузке файла: {e}")
        return []


def convert_transaction_rub(transaction):
    amount = transaction.get('operationAmount').get('amount')
    currency = transaction.get('operationAmount').get('currency').get("code")
    logger.info(f"Конвертация транзакции: сумма={amount}, валюта={currency}")

    if currency == 'RUB':
        return amount
    elif currency in ['USD', 'EUR']:
        result = get_exchange_rate(currency, amount)
        logger.info(f"Конвертированная сумма: {result}")
        return result
    else:
        logger.warning(f"Неизвестная валюта: {currency}")
        return f'Неизвестная валюта: {currency}'
