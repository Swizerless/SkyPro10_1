import pytest

from src.processing import filter_by_state, sort_by_date

# ------------------------- Тесты для filter_by_state -------------------------


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),  # Фильтрация по EXECUTED
        ("PENDING", [{"id": 2, "state": "PENDING"}]),  # Фильтрация по PENDING
        ("CANCELLED", []),  # Отсутствие совпадений
    ],
)
def test_filter_by_state(transactions_list, state, expected):
    """Тестируем фильтрацию списка словарей по заданному статусу state."""
    assert filter_by_state(transactions_list, state) == expected


def test_filter_by_state_no_state(transactions_list_no_state):
    """Тестируем работу функции при отсутствии ключа state в словарях."""
    assert filter_by_state(transactions_list_no_state, "EXECUTED") == []


# ------------------------- Тесты для sort_by_date -------------------------


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {"id": 3, "date": "2023-10-15T12:34:56"},
                {"id": 2, "date": "2023-09-01T00:00:00"},
                {"id": 1, "date": "2023-08-15T12:34:56"},
            ],
        ),  # Сортировка по убыванию
        (
            False,
            [
                {"id": 1, "date": "2023-08-15T12:34:56"},
                {"id": 2, "date": "2023-09-01T00:00:00"},
                {"id": 3, "date": "2023-10-15T12:34:56"},
            ],
        ),  # Сортировка по возрастанию
    ],
)
def test_sort_by_date(transactions_list_with_dates, reverse, expected):
    """Тестируем сортировку списка словарей по датам."""
    assert sort_by_date(transactions_list_with_dates, reverse) == expected


def test_sort_by_date_same_dates(transactions_list_same_dates):
    """Тестируем корректность сортировки при одинаковых датах."""
    sorted_list = sort_by_date(transactions_list_same_dates, reverse=True)
    assert sorted_list == transactions_list_same_dates  # Порядок сохраняется


def test_sort_by_date_invalid_format(transactions_list_invalid_date):
    """Тестируем работу функции с некорректными или нестандартными форматами дат."""
    with pytest.raises(ValueError):
        sort_by_date(transactions_list_invalid_date)
