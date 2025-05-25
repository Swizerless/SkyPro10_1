from typing import Union
import re
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_details: Union[str, int]) -> Union[str, int]:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета, а возвращает строку с замаскированным номером"""
    split_parts = bank_details.split()
    if "Счет" in bank_details or "Счёт" in bank_details:
        mask_account_number = get_mask_account(split_parts[-1])
        account_type = " ".join(split_parts[:-1])
        account_result = f"{account_type} {mask_account_number}"
        return account_result
    else:
        mask_card_number = get_mask_card_number(split_parts[-1])
        card_type = " ".join(split_parts[:-1])
        card_result = f"{card_type} {mask_card_number}"
        return card_result

def get_date(date: Union[str, int]) -> Union[str, int]:
    """Функция принимает на вход строку с датой в странном формате и возвращает строку с датой в формате (ДД.ММ.ГГГГ)"""
    split_date = re.split('[-T]', date)
    date_list = [split_date[2], split_date[1], split_date[0]]
    date_result = ".".join(date_list)
    return date_result

