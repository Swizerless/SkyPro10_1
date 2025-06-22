import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета,
    а возвращает строку с замаскированным номером"""
    try:
        split_parts = bank_details.split()
        if not split_parts:
            raise ValueError("Входная строка пуста или не содержит данных.")

        # Проверяем, что последняя часть содержит только цифры
        number = split_parts[-1]
        if not number.isdigit():
            return "Invalid Input"  # Возвращаем сообщение об ошибке для некорректных данных

        if "Счет" in bank_details or "Счёт" in bank_details:
            mask_account_number = get_mask_account(number)
            account_type = " ".join(split_parts[:-1])
            return f"{account_type} {mask_account_number}"
        else:
            mask_card_number = get_mask_card_number(number)
            card_type = " ".join(split_parts[:-1])
            return f"{card_type} {mask_card_number}"
    except Exception as e:
        raise ValueError(f"Ошибка при обработке данных: {e}")


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в странном формате
    и возвращает строку с датой в формате (ДД.ММ.ГГГГ)"""
    try:
        # Разбиваем строку на части
        split_date = re.split("[-T]", date)
        if len(split_date) < 3:
            raise ValueError("Некорректный формат даты.")

        # Проверяем, что все части являются числами
        year, month, day = map(int, split_date[:3])

        # Проверяем корректность даты с помощью datetime
        datetime(year=year, month=month, day=day)

        # Формируем результат
        date_list = [f"{day:02}", f"{month:02}", str(year)]
        return ".".join(date_list)
    except Exception as e:
        raise ValueError(f"Ошибка при обработке даты: {e}")