import json
from typing import Any, Dict, List, Union

from logger import logger  # type: ignore

from src.external_api import get_exchange_rate


def load_transactions_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON-файла.
    :param file_path: Путь к файлу.
    :return: Список транзакций или пустой список в случае ошибки.
    """
    logger.info(f"Загружаем транзакции из файла: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Успешно загружены транзакции")
            return data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Ошибка при загрузке файла: {e}")
        return []


def convert_transaction_rub(transaction: Dict[str, Any]) -> Union[float, str, None]:
    """
    Конвертирует сумму транзакции в рубли.
    :param transaction: Одна транзакция (словарь).
    :return: Сумма в рублях или сообщение об ошибке.
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    logger.info(f"Конвертация транзакции: сумма={amount}, валюта={currency}")

    if not amount or not currency:
        logger.warning("Транзакция не содержит данных о сумме или валюте.")
        return None

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        result = get_exchange_rate(currency, float(amount))
        logger.info(f"Конвертированная сумма: {result}")
        return result
    else:
        logger.warning(f"Неизвестная валюта: {currency}")
        return f"Неизвестная валюта: {currency}"
