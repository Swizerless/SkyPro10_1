import pytest

from src.widget import get_date, mask_account_card

# ------------------------- Тесты для mask_account_card -------------------------


@pytest.mark.parametrize(
    "bank_details, expected",
    [
        ("Visa Classic 5424997579391743", "Visa Classic 5424 99** **** 1743"),  # Карта Visa
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),  # Карта MasterCard
        ("Счет 73654108430135874305", "Счет **4305"),  # Счет
        ("Счёт 12345678901234567890", "Счёт **7890"),  # Альтернативное написание "Счёт"
        ("Invalid Input", "Invalid Input"),  # Некорректные данные
        ("Random Text Without Numbers", "Invalid Input"),  # Некорректные данные
    ],
)
def test_mask_account_card(bank_details, expected):
    """Тестируем правильность маскирования номера карты или счета."""
    assert mask_account_card(bank_details) == expected


# ------------------------- Тесты для get_date -------------------------


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2023-10-15T12:34:56", "15.10.2023"),  # Стандартный формат даты
        ("2021-01-01T00:00:00", "01.01.2021"),  # Минимальная дата
        ("2099-12-31T23:59:59", "31.12.2099"),  # Максимальная дата
        ("2023-02-28T12:34:56", "28.02.2023"),  # Последний день февраля
    ],
)
def test_get_date(date, expected):
    """Тестируем правильность преобразования даты."""
    assert get_date(date) == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        "",  # Пустая строка
        "2023/10/15T12:34:56",  # Неправильный разделитель даты
        "Invalid Date String",  # Полностью некорректная строка
        "2023-13-01T12:34:56",  # Невалидный месяц (13)
        "2023-02-30T12:34:56",  # Невалидный день (30 февраля)
    ],
)
def test_get_date_invalid_data(invalid_date):
    """Тестируем обработку некорректных входных данных."""
    with pytest.raises(ValueError):
        get_date(invalid_date)
