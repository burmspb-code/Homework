"""Обработка информации о картах и счетах"""
import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """Возвращает входную строку с маской номера карты или счета"""
    last_space = input_data.rfind(' ') # Индекс последнего пробела
    last_word = input_data[last_space+1:] # Считываем последнее слово (номер)
    if len(last_word) == 20: # Проверка на номер счета
        mask_word = get_mask_account(int(last_word))
    else:
        mask_word = get_mask_card_number(int(last_word))

    return input_data[:last_space + 1] + mask_word

def get_date(input_date: str) -> str:
    """Принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407
 и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1', input_date)[:10]


# Проверка работы функции mask_account_card
# list_data =["Visa Platinum 7000792289606361", "Счет 73654108430135874305", "Maestro 1596837868705199", "Счет 64686473678894779589", "MasterCard 7158300734726758", "Счет 35383033474447895560", "Visa Classic 6831982476737658", "Visa Platinum 8990922113665229", "Visa Gold 5999414228426353", "Счет 73654108430135874305"]
# for data in list_data:
#     print(mask_account_card(data))

# Проверка работы функции get_date
# list_date = ["2020-03-11T02:26:18.671407", "2024-10-05T02:26:18.671407"]
# for date in list_date:
#     print(get_date(date))
