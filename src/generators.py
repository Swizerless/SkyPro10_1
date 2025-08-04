from typing import Iterator, Generator


def filter_by_currency(transactions_list: list, currency_code: str) -> Iterator:
    """
    Фильтрует список транзакций по валюте.
    """
    return filter(
        lambda x: x.get("operationAmount", {}).get("currency", {}).get("code") == currency_code, transactions_list
    )


def transaction_descriptions(transactions_list: list[dict]) -> Iterator:
    """пример реализации генератора"""
    for t in transactions_list:
        yield t["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров банковских карт в диапазоне от start до end включительно.
    Номера формата XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_number = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_number
