"""Тестирование модуля generators.py"""
import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_standard(test_transactions: list[dict],
                            result_usd_1: dict, result_usd_2: dict, result_usd_3: dict,
                            result_rub_1: dict, result_rub_2: dict) -> None:
    """Проверяем стандартную работу функции"""
    result_usd = list(filter_by_currency(test_transactions, "USD"))
    result_rub = list(filter_by_currency(test_transactions, "RUB"))

    # Проверяем долларовые танзакции
    assert len(result_usd) == 3  # Проверяем что USD имеет 3 транзакции
    assert result_usd == [result_usd_1, result_usd_2, result_usd_3]


    # Проверяем рублевые танзакции
    assert len(result_rub) == 2  # Проверяем, что RUB имеет 2 транзакции
    assert result_rub == [result_rub_1, result_rub_2]

def test_filter_by_currency_incorrect_currency(test_transactions: list[dict],
                            result_usd_1: dict, result_usd_2: dict, result_usd_3: dict,
                            result_rub_1: dict, result_rub_2: dict) -> None:
    """Проверяем работу функции когда транзакции в заданной валюте отсутствуют"""

    with pytest.raises(ValueError):
        list(filter_by_currency(test_transactions, "EUR"))

def test_filter_by_currency_empty_list():
    """Проверка случая, когда на вход подан пустой список"""
    with pytest.raises(ValueError):
        # Пытаемся обработать пустой список
        list(filter_by_currency([], "USD"))

def test_no_currency_transaction():
    """Проверка случая, когда нет валютных операций"""
    transaction = {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
    with pytest.raises(ValueError):
        list(filter_by_currency([transaction], "USD"))

def test_transaction_descriptions(test_transactions: list[dict], expected_descriptions: list[str]) -> None:
    """Проверяем стандартную работу функции"""
    result_descriptions = list(transaction_descriptions(test_transactions))

    assert result_descriptions == expected_descriptions

