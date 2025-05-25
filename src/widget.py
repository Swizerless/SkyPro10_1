from typing import Union

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_details: Union[str, int]) -> Union[str, int]:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета, а возвращает строку с замаскированным номером"""
    card = False
    account = False
    if "Счет" in bank_details or "Счёт" in bank_details:
        card = False
        account = True
    else:
        card = True
        account = False
    split_parts = bank_details.split()
    if card:
        mask_card_number = get_mask_card_number(split_parts[-1])
        card_type = " ".join(split_parts[:-1])
        card_result = f"{card_type} {mask_card_number}"
        return card_result
    else:
        mask_account_number = get_mask_account(split_parts[-1])
        account_type = " ".join(split_parts[:-1])
        account_result = f"{account_type} {mask_account_number}"
        return account_result

print(mask_account_card("MasterCard 7158300734726758"))






    # card_first_six_visible_numbers = card_number[:6]
    # card_last_four_visible_numbers = card_number[-4:]
    # card_masked_numbers = "*" * (len(card_number) - 10)
    # card_masked = card_first_six_visible_numbers + card_masked_numbers + card_last_four_visible_numbers
    # blocks = []
    # for i in range(0, len(card_masked), 4):
    #     block = card_masked[i : i + 4]
    #     blocks.append(block)
    # mask_card_number = " ".join(blocks)
    # return mask_card_number