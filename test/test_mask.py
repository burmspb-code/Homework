"""Тесторование функции mask.py"""


import pytest

from src.masks import get_mask_card_number, get_mask_account


# Тесты для маскировки карты (XXXX XX** **** XXXX)
def test_get_mask_card_number_standard():
    # Стандартный 16-значный номер
    assert get_mask_card_number(1234567812343456) == "1234 56** **** 3456"

def test_get_mask_card_number_short():
    # Если номер короче 16 знаков
    assert get_mask_card_number(12345678) == "1234 56**"

def test_get_mask_card_number_one():
    # Если номер короче 16 знаков
    assert get_mask_card_number(0) == "*"


# Тесты для маскировки счета (**XXXX)
def test_get_mask_account_standard():
    # Стандартный 20-значный номер счета, должны остаться последние 4 цифры и 2 звезды
    # Пример: 73654108430135874305 -> **4305
    assert get_mask_account(73654108430135874305) == "**4305"

def test_get_mask_account_short():
    # Если номер счета слишком короткий (меньше 6 символов)
    # Код [-6::] вернет всё что есть, но замаскированное
    assert get_mask_account(1234) == "****"

def test_get_mask_account_zero():
    # Проверка на нулевой счет
    assert get_mask_account(0) == "*"

def test_mask_card_empty_string():
    """Проверка пустой строки на входе"""
    # Ожидаемое поведение зависит от логики get_mask.
    # Обычно возвращается пустая строка или ошибка.
    assert get_mask_card_number("") == ""

def test_mask_card_none():
    """Проверка передачи None"""
    with pytest.raises(TypeError):
        get_mask_card_number(None)

def test_mask_account_zero():
    """Проверка передачи нуля"""
    # Номер счета не может быть '0', но функция должна это обработать
    assert get_mask_account(0) == "**0" # или специфичная ошибка
