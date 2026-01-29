"""Тесторование функций mask_account_card, get_date"""

import pytest

from src.widget import mask_account_card, get_date

# Входные дынные - список кортежей
card_data = [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
]


@pytest.mark.parametrize("description, expected_number", card_data)
def test_mask_account_card(description, expected_number):
    assert mask_account_card(description) == expected_number

def test_mask_account_card_number_is_not_decimal():
    assert mask_account_card("Visa Platinum qwdrtyu289606361") is None

def test_mask_account_card_is_not_correct_number():
    assert mask_account_card("Счет 736541") is None
