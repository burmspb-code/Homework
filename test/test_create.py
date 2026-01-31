"""Тестирование функции get_mask"""

import pytest

from src.create_masks import get_mask


def test_get_mask_basic() -> None:
    # Обычная маскировка части строки
    assert get_mask("12345678", 2, 5, "*", 0, "") == "12****78"


def test_get_mask_with_separator() -> None:
    # Маскировка с добавлением разделителей (например, для карт или телефонов)
    # 1234 5678 -> 12** *678 (если маска на 2-4 индексы и пробел каждые 4 символа)
    assert get_mask("12345678", 2, 4, "*", 4, " ") == "12** *678"


def test_get_mask_full_mask() -> None:
    # Маскировка всей строки
    assert get_mask("abc", 0, 2, "X", 0, "") == "XXX"


def test_get_mask_no_mask_symbol() -> None:
    # Если символ маски — пустая строка, символы не меняются, но разделители ставятся
    assert get_mask("123456", 0, 5, "", 2, "-") == "12-34-56"


def test_get_mask_zero_separator() -> None:
    # Проверка защиты от ZeroDivisionError (индекс разделителя 0)
    assert get_mask("1234", 0, 1, "*", 0, "-") == "**34"


def test_get_mask_separator_at_end() -> None:
    # Проверка, что разделитель не ставится в самый конец строки
    assert get_mask("1234", 0, 0, "*", 2, " ") == "*2 34"


def test_get_mask_long_separator_symbol() -> None:
    # Если передана строка в качестве символа, берется только первый знак
    assert get_mask("1234", 0, 1, "###", 2, "---") == "##-34"


def test_get_mask_negative_indices() -> None:
    # Проверка: как функция ведет себя с отрицательным стартом
    # В текущей логике (index_start <= i), -1 замаскирует всё с начала
    assert get_mask("1234", -5, 1, "*", 0, "") == "**34"


def test_get_mask_wrong_order() -> None:
    # Если конечный индекс меньше начального, маска не должна наложиться
    assert get_mask("1234", 3, 1, "*", 0, "") == "1234"


def test_get_mask_out_of_range() -> None:
    # Если индексы далеко за пределами строки
    assert get_mask("123", 0, 100, "X", 0, "") == "XXX"


def test_get_mask_empty_input() -> None:
    # Проверка пустой строки
    assert get_mask("", 0, 5, "*", 2, " ") == ""


def test_get_mask_type_exceptions() -> None:
    # Проверка: передача строки вместо числа для индексов
    with pytest.raises(TypeError):
        get_mask("12345", "start", 2, "*", 0, "")

    # Проверка: передача None вместо входной строки
    with pytest.raises(TypeError):
        get_mask(None, 0, 2, "*", 0, "")


def test_get_mask_negative_separator_step() -> None:
    # Проверка: при отрицательном шаге в range
    result = get_mask("12345", 0, 1, "*", -1, "-")
    assert result == "**345"  # Разделителей просто не должно быть
