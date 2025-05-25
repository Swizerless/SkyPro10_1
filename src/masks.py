def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_first_six_visible_numbers = card_number[:6]
    card_last_four_visible_numbers = card_number[-4:]
    card_masked_numbers = "*" * (len(card_number) - 10)
    card_masked = card_first_six_visible_numbers + card_masked_numbers + card_last_four_visible_numbers
    blocks = []
    for i in range(0, len(card_masked), 4):
        block = card_masked[i : i + 4]
        blocks.append(block)
    mask_card_number = " ".join(blocks)
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_last_four_digits = account_number[-4:]
    account_masked_digits = "*" * (len(account_number) - 4)
    mask_account = account_masked_digits[-2:] + account_last_four_digits
    return mask_account
