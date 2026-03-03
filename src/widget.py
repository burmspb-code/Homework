"""Обработка информации о картах и счетах"""

import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """Возвращает входную строку с маской номера карты или счета"""
    last_space = input_data.rfind(" ")  # Индекс последнего пробела
    last_word = input_data[last_space + 1 :]  # Считываем последнее слово (номер)

    if len(last_word) == 20:  # Проверка на номер счета
        mask_word = get_mask_account(int(last_word))
    elif len(last_word) == 16:  # Проверка на номер кары
        mask_word = get_mask_card_number(int(last_word))
    else:
        return input_data
    return input_data[: last_space + 1] + mask_word


def get_date(input_date: str) -> str:
    """Принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407
    и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", input_date)[:10]
