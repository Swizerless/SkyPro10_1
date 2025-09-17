import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(currency, amount):
    to_curr = "RUB"
    inlet_curr = currency

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_curr}&from={inlet_curr}&amount={amount}"
    headers = {"apikey": os.getenv('API_KEY')}

    response = requests.get(url, headers=headers, data={})
    return response.json().get("result")