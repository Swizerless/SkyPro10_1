import pytest

# Фикстуры для тестирования номеров карт
@pytest.fixture
def base_card_number():
    return "5424997579391743"  # Базовый номер карты

@pytest.fixture
def masked_card_number():
    return "5424 99** **** 1743"  # Ожидаемая маска для базового номера карты

@pytest.fixture
def invalid_card_number():
    return "abc12345678901234"  # Некорректный номер карты

#----------------------------------------------------------------------------------------
# Фикстуры для тестирования номеров счетов
@pytest.fixture
def base_account_number():
    return "73654108430135874305"  # Базовый номер счета

@pytest.fixture
def masked_account():
    return "**4305"  # Ожидаемая маска для базового номера счета

@pytest.fixture
def invalid_account_number():
    return "abc12345678901234"  # Некорректный номер счета

import pytest

#----------------------------------------------------------------------------------------
# Фикстуры для тестирования mask_account_card
@pytest.fixture
def visa_card():
    return "Visa Classic 5424997579391743"

@pytest.fixture
def mastercard():
    return "MasterCard 1234567890123456"

@pytest.fixture
def account():
    return "Счет 73654108430135874305"

@pytest.fixture
def invalid_bank_details():
    return "Invalid Input"

#----------------------------------------------------------------------------------------
# Фикстуры для тестирования get_date
@pytest.fixture
def valid_date():
    return "2023-10-15T12:34:56"

@pytest.fixture
def invalid_date():
    return "Invalid Date String"