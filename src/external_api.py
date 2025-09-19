import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("external_api")


def get_exchange_rate(currency, amount):
    logger.info("Начинается выполнение функции запроса API")
    curr_to = "RUB"
    curr_from = currency

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={curr_to}&from={curr_from}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers, data={})
    return response.json().get("result")
