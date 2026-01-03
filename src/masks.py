"""Наложение маски на номер банковской карты и номер банковского счета"""

from create_masks import get_mask


def get_mask_card_number(card_n: int) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    resalt = get_mask(str(card_n), 6, 11, "*", 4, " ")
    return str(resalt)


def get_mask_account(account_n: int) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    resalt = get_mask(str(account_n), 0, 15, "*", 0, "")[-6::]
    return str(resalt)


card_number = 7000792289606361
account_number = 73654108430135874305

print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
