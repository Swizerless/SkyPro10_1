import logging
import logging.config

from logging_config import LOGGING_CONFIG
from src.masks import get_mask_account, get_mask_card_number
from src.utils import convert_transaction_rub, load_transactions_json

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("main")

logger.info("Вызываем функции конвертации валюты с единичной транзакцией, без файла")
first_operation = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}

print(convert_transaction_rub(first_operation))

logger.info("Вызываем запрос на считывание файла")
operations_json = load_transactions_json("data/operations.json")
# logger.info("Вызываем функции конвертации валюты с полученным списком словарей")
# for dic in operations_json:
#     convert_transaction_rub(dic)

print(get_mask_account("73654108430135874305"))

print(get_mask_card_number("5424997579391743"))
