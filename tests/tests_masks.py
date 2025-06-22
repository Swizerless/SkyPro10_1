import pytest
from src.masks import get_mask_card_number, get_mask_account

# ------------------------- Тесты для get_mask_card_number -------------------------

@pytest.mark.parametrize(
    "extra_digits, expected",
    [
        ("", "5424 99** **** 1743"),  # Стандартная длина (16 цифр)
        ("12", "5424 99** **** **43 12"),  # Длинная длина (18 цифр)
    ],
)
def test_get_mask_card_number(base_card_number, extra_digits, expected):
    """Тестируем правильность маскирования номера карты."""
    card_number = base_card_number + extra_digits
    assert get_mask_card_number(card_number) == expected


def test_invalid_card_number(invalid_card_number):
    """Тестируем обработку некорректного номера карты."""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)


# ------------------------- Тесты для get_mask_account -------------------------

@pytest.mark.parametrize(
    "extra_digits, expected",
    [
        ("", "**4305"),  # Стандартная длина (20 цифр)
        ("12", "**0512"),  # Длинная длина (22 цифры)
    ],
)
def test_get_mask_account(base_account_number, extra_digits, expected):
    """Тестируем правильность маскирования номера счета."""
    account_number = base_account_number + extra_digits
    assert get_mask_account(account_number) == expected


def test_invalid_account_number(invalid_account_number):
    """Тестируем обработку некорректного номера счета."""
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)