import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(currency, amount):
    curr_to = "RUB"
    curr_from = currency

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={curr_to}&from={curr_from}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers, data={})
    return response.json().get("result")
