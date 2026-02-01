"""Тестирование функции get_mask"""

from src.create_masks import get_mask


def test_get_mask_basic() -> None:
    """Обычная маска без разделителей"""
    assert get_mask("1234567890", 2, 5, "*", 0, "") == "12****7890"


def test_get_mask_with_separator() -> None:
    """Маскируем и разбиваем по 4 символа (как карту)"""
    # 1234 5678 1234 5678 -> 1234 **** **** 5678
    assert get_mask("1234567812345678", 4, 11, "*", 4, " ") == "1234 **** **** 5678"


def test_get_mask_full_range() -> None:
    """Маскируем всё строку"""
    assert get_mask("привет", 0, 5, "x", 0, "") == "xxxxxx"


def test_get_mask_out_of_range() -> None:
    """Индексы за пределами строки (слайсы в Python это переварят)"""
    assert get_mask("123", 0, 10, "#", 0, "") == "###"
    assert get_mask("123", -5, 1, "0", 0, "") == "003"


def test_get_mask_empty_input() -> None:
    """Пустая строка"""
    assert get_mask("", 0, 5, "*", 2, "-") == ""


def test_get_mask_no_replace_symbol() -> None:
    """Если символ замены — пустая строка"""
    assert get_mask("12345", 0, 2, "", 0, "") == "12345"


def test_get_mask_separator_logic() -> None:
    """Проверка разделителя в конце"""
    # "123456", разделитель каждые 2 символа
    assert get_mask("123456", 0, 0, "*", 2, "-") == "*2-34-56"
