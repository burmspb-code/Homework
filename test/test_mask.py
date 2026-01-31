"""Тесторование функции mask.py"""

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для маскировки карты (XXXX XX** **** XXXX)
def test_get_mask_card_number_standard() -> None:
    # Стандартный 16-значный номер
    assert get_mask_card_number(1234567812343456) == "1234 56** **** 3456"


def test_get_mask_card_number_short() -> None:
    # Если номер короче 16 знаков
    assert get_mask_card_number(12345678) == "1234 56**"


# Тесты для маскировки счета (**XXXX)
def test_get_mask_account_standard() -> None:
    # Стандартный 20-значный номер счета, должны остаться последние 4 цифры и 2 звезды
    # Пример: 73654108430135874305 -> **4305
    assert get_mask_account(73654108430135874305) == "**4305"


def test_get_mask_account_short() -> None:
    # Если номер счета слишком короткий (меньше 6 символов)
    assert get_mask_account(1234) == "****"


def test_mask_card_TypeError() -> None:
    # Проверка передачи None
    with pytest.raises(TypeError):
        get_mask_card_number(None)


def test_get_mask_account_TypeError() -> None:
    # Проверка передачи None
    with pytest.raises(TypeError):
        get_mask_account("string")
