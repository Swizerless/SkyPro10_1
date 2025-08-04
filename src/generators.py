from typing import Iterator


def filter_by_currency(transactions_list: list, currency_code: str) -> Iterator:
    """
    Фильтрует список транзакций по валюте.
    """
    return (
        filter(
            lambda x: x.get("operationAmount", {}).get("currency", {}).get("code") == currency_code, transactions_list
        )
    )

def transaction_descriptions(transactions_list: list[dict]) -> Iterator:
    """пример реализации генератора"""
    for t in transactions_list:
        yield t["description"]