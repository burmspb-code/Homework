"""Генераторы для обработки данных"""
from collections.abc import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    for transaction in transactions:
        yield transaction["description"]


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[int]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
     где X — цифра номера карты"""

    for num in range(start, end + 1):
        # :016d означает: целое число (d), дополнить нулями (0) до длины 16 знаков
        str_mum = f"{num:016d}"
        yield f"{str_mum[:4]} {str_mum[4:8]} {str_mum[8:12]} {str_mum[12:]}"
