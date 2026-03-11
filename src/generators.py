"""Генераторы для обработки данных"""

from collections.abc import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""

    found = False  # Флаг поиска нужных данных

    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        currency_data = op_amount.get("currency", {})

        if currency_data.get("code") == currency:
            found = True  # Нунжная валюта присутствует в транзакциях
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if transactions:
        for transaction in transactions:
            yield transaction.get("description", "")
    else:
        raise ValueError("Данные отсутствуют")


def card_number_generator(start: int, stop: int) -> list[str]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты"""
    list_cards_number = []
    for num in range(start, stop + 1):
        number = f"{num:0>16}"
        card_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        list_cards_number.append(card_number)
    return list_cards_number
