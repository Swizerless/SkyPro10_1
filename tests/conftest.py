import pytest
from typing import List, Dict


# Фикстуры для тестирования номеров карт
@pytest.fixture
def base_card_number() -> str:
    return "5424997579391743"  # Базовый номер карты


@pytest.fixture
def masked_card_number() -> str:
    return "5424 99** **** 1743"  # Ожидаемая маска для базового номера карты


@pytest.fixture
def invalid_card_number() -> str:
    return "abc12345678901234"  # Некорректный номер карты


# ----------------------------------------------------------------------------------------
# Фикстуры для тестирования номеров счетов
@pytest.fixture
def base_account_number() -> str:
    return "73654108430135874305"  # Базовый номер счета


@pytest.fixture
def masked_account() -> str:
    return "**4305"  # Ожидаемая маска для базового номера счета


@pytest.fixture
def invalid_account_number() -> str:
    return "abc12345678901234"  # Некорректный номер счета


# ----------------------------------------------------------------------------------------
# Фикстуры для тестирования mask_account_card
@pytest.fixture
def visa_card() -> str:
    return "Visa Classic 5424997579391743"


@pytest.fixture
def mastercard() -> str:
    return "MasterCard 1234567890123456"


@pytest.fixture
def account() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def invalid_bank_details() -> str:
    return "Invalid Input"


# ----------------------------------------------------------------------------------------
# Фикстуры для тестирования get_date
@pytest.fixture
def valid_date() -> str:
    return "2023-10-15T12:34:56"


@pytest.fixture
def invalid_date() -> str:
    return "Invalid Date String"


# ----------------------------------------------------------------------------------------
# Фикстуры для тестирования модуля processing.py
@pytest.fixture
def transactions_list() -> List[Dict]:
    """Фикстура с тестовыми данными для filter_by_state."""
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
    ]


@pytest.fixture
def transactions_list_no_state() -> List[Dict]:
    """Фикстура с тестовыми данными без ключа state."""
    return [
        {"id": 1, "other_key": "value1"},
        {"id": 2, "other_key": "value2"},
    ]


@pytest.fixture
def transactions_list_with_dates() -> List[Dict]:
    """Фикстура с тестовыми данными для sort_by_date."""
    return [
        {"id": 1, "date": "2023-08-15T12:34:56"},
        {"id": 2, "date": "2023-09-01T00:00:00"},
        {"id": 3, "date": "2023-10-15T12:34:56"},
    ]


@pytest.fixture
def transactions_list_same_dates() -> List[Dict]:
    """Фикстура с тестовыми данными для одинаковых дат."""
    return [
        {"id": 1, "date": "2023-10-15T12:34:56"},
        {"id": 2, "date": "2023-10-15T12:34:56"},
        {"id": 3, "date": "2023-10-15T12:34:56"},
    ]


@pytest.fixture
def transactions_list_invalid_date() -> List[Dict]:
    """Фикстура с тестовыми данными для некорректных дат."""
    return [
        {"id": 1, "date": "invalid-date"},
        {"id": 2, "date": "2023/10/15T12:34:56"},
    ]
