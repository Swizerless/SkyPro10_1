from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.transaction_data import transactions


def test_filter_by_currency_correct_filtering() -> None:
    """Проверяем, что фильтр возвращает только транзакции с валютой USD"""

    result = filter_by_currency(transactions, "USD")
    """Все возвращённые транзакции должны иметь currency code 'USD'"""
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)
    """И при этом в исходных данных есть такие транзакции"""
    assert any(t["operationAmount"]["currency"]["code"] == "USD" for t in transactions)


def test_filter_by_currency_no_matches() -> None:
    """Проверяем случай, когда валюты нет в списке транзакций"""

    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []  # должно вернуть пустой список


def test_filter_by_currency_empty_list() -> None:
    """Передаём пустой список — генератор не должен выдавать ошибок"""
    empty_list: list = []
    result = list(filter_by_currency(empty_list, "USD"))
    assert result == []


def test_filter_by_currency_no_matching_transactions() -> None:
    """Создаём список без нужной валюты"""
    no_usd_transactions = [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"name": "EUR", "code": "EUR"}}},
        {"id": 2, "operationAmount": {"amount": "200", "currency": {"name": "JPY", "code": "JPY"}}},
    ]
    result = list(filter_by_currency(no_usd_transactions, "USD"))
    assert result == []


def test_transaction_descriptions_correct() -> None:
    """Получаем описания для транзакций"""
    descriptions = list(transaction_descriptions(transactions))
    """Проверяем, что возвращённый список совпадает с полями 'description' исходных данных"""
    expected_descriptions = [t["description"] for t in transactions]
    assert descriptions == expected_descriptions


def test_transaction_descriptions_empty() -> None:
    """Передаём пустой список — генератор должен вернуть пустой список"""
    result = list(transaction_descriptions([]))
    assert result == []


def test_transaction_descriptions_single() -> None:
    """Создаём список из 1 транзакции"""
    single_transaction = [{"id": 123, "description": "Тестовая транзакция"}]
    result = list(transaction_descriptions(single_transaction))
    assert result == ["Тестовая транзакция"]


def test_transaction_descriptions_multiple() -> None:
    """Несколько транзакций с разными описаниями"""
    sample_transactions = [{"description": "Оплата услуги"}, {"description": "Перевод"}, {"description": "Покупка"}]
    result = list(transaction_descriptions(sample_transactions))
    assert result == ["Оплата услуги", "Перевод", "Покупка"]


def test_card_number_generator_range() -> None:
    start = 1
    end = 3
    gen = card_number_generator(start, end)
    results = list(gen)

    """Проверяем, что количество номеров соответствует диапазону"""
    assert len(results) == (end - start + 1)

    """Проверяем, что номера в правильном диапазоне и формате"""
    for i, number in enumerate(results, start=start):
        expected = f"{i:016d}"
        expected_formatted = " ".join([expected[j : j + 4] for j in range(0, 16, 4)])
        assert number == expected_formatted


def test_card_number_format() -> None:
    start = 1234567890123456
    end = 1234567890123456
    gen = card_number_generator(start, end)
    result = next(gen)

    """Проверяем форматирование: должно быть 4 группы по 4 цифры"""
    parts = result.split(" ")
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()


def test_card_number_edge_cases() -> None:
    """Тест с диапазоном из одного числа."""
    start_end = 9999999999999999
    gen = card_number_generator(start_end, start_end)
    result = next(gen)

    expected_str = f"{start_end:016d}"
    expected_formatted = " ".join([expected_str[j : j + 4] for j in range(0, 16, 4)])

    assert result == expected_formatted


def test_card_number_generation_completes() -> None:
    """Проверка, что генератор завершает работу после последнего числа"""
    start = 10
    end = 12
    gen = card_number_generator(start, end)

    results = list(gen)

    """Количество должно быть равным диапазону +1"""
    assert len(results) == (end - start + 1)

    """Проверяем последовательность номеров"""
    for i, number in enumerate(results, start=start):
        expected_str = f"{i:016d}"
        expected_formatted = " ".join([expected_str[j : j + 4] for j in range(0, 16, 4)])
        assert number == expected_formatted
