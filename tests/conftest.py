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