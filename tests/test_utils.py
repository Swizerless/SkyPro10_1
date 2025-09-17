from unittest.mock import mock_open, patch

from src.utils import convert_transaction_rub, load_transactions_json


def test_load_transactions_json():
    with patch('builtins.open', mock_open(read_data='{"1": "2"}')):
        assert load_transactions_json('') == {"1": "2"}

    with patch('builtins.open', mock_open(read_data='{"1": "2"')):
        assert load_transactions_json('') == []


def test_convert_transaction_rub():
    with patch('requests.get') as r_mock:
        r_mock.return_value.json.return_value = {"result": 123}
        assert convert_transaction_rub({"operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}}) == 123

        assert convert_transaction_rub({"operationAmount": {"amount": "34114.93", "currency": {"code": "RUB"}}}) == '34114.93'

        assert convert_transaction_rub({"operationAmount": {"amount": "34114.93", "currency": {"code": "GBR"}}}) == 'Неизвестная валюта: GBR'