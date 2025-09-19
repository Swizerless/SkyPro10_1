import logging
import logging.config
from logging_config import LOGGING_CONFIG
from src.utils import convert_transaction_rub, load_transactions_json

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('main')

logger.info(f'Вызываем функции конвертации валюты с единичной транзакцией, без файла')
first_operation = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

print(convert_transaction_rub(first_operation))

logger.info(f'Вызываем запрос на считывание файла')
operations_json = load_transactions_json('data/operations.json')
logger.info(f'Вызываем функции конвертации валюты с полученным списком словарей')
for dic in operations_json:
    convert_transaction_rub(dic)