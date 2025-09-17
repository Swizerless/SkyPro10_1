import os
import unittest
from unittest.mock import patch

from src.external_api import get_exchange_rate


class TestGetExchangeRate(unittest.TestCase):
    @patch('requests.get')
    def test_get_exchange_rate(self, mock_get):
        # Настраиваем мок, чтобы возвращал нужный json
        mock_get.return_value.json.return_value = {"result": 123.45}

        # Вызов функции
        rate = get_exchange_rate('USD', 100)

        # Проверка, что функция возвращает ожидаемый результат
        self.assertEqual(rate, 123.45)

        # Проверка, что requests.get вызван с правильными параметрами
        mock_get.assert_called_with(
            'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100',
            headers={"apikey": os.getenv('API')},
            data={}
        )


# if __name__ == '__main__':
#     unittest.main()