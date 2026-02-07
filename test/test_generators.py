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

def test_transaction_descriptions_standard(test_transactions: list[dict], expected_descriptions: list[str]) -> None:
    """Проверяем стандартную работу функции"""
    result_descriptions = list(transaction_descriptions(test_transactions))
    assert result_descriptions == expected_descriptions

def test_transaction_descriptions_empty():
    """Проверка на пустой список транзакций"""
    with pytest.raises(ValueError):
        list(transaction_descriptions([]))

@pytest.mark.parametrize("input_data, expected_output", [
    # Случай с одной транзакцией
    (
        [{"description": "Перевод по номеру карты"}],
        ["Перевод по номеру карты"]
    ),
    # Случай с несколькими транзакциями
    (
        [
            {"description": "Оплата телефона"},
            {"description": "Перевод другу"},
            {"description": "Кешбэк"}
        ],
        ["Оплата телефона", "Перевод другу", "Кешбэк"]
    ),
    # Случай, когда в некоторых транзакциях нет ключа description
    (
        [
            {"description": "Покупка"},
            {"amount": 100},  # Ключ отсутствует
            {"description": "Ужин"}
        ],
        ["Покупка", "", "Ужин"]
    )
])
def test_transaction_descriptions_different_data(input_data, expected_output):
    assert list(transaction_descriptions(input_data)) == expected_output


def test_generator_returns_list():
    """Проверка, что функция возвращает список строк"""
    result = card_number_generator(1, 3)
    assert isinstance(result, list)
    assert all(isinstance(card, str) for card in result)


def test_generator_correct_range_length():
    """Проверка, что генерируется ровно столько карт, сколько в диапазоне [start, stop]"""
    start, stop = 5, 15
    result = card_number_generator(start, stop)
    # Диапазон inclusive: 15 - 5 + 1 = 11
    assert len(result) == 11


@pytest.mark.parametrize("start_val, expected_last_digits", [
    (1, "0001"),
    (10, "0010"),
    (9999, "9999"),
])
def test_card_padding_right_to_left(start_val, expected_last_digits):
    """Проверяет, что числа дополняются нулями слева (выравнивание вправо)"""
    result = card_number_generator(start_val, start_val)
    # Берем последнюю группу из 4 цифр
    last_group = result[0].split()[-1]
    assert last_group == expected_last_digits


def test_full_card_format():
    """Проверяет общую структуру номера: XXXX XXXX XXXX XXXX"""
    result = card_number_generator(12345678, 12345678)
    card = result[0]

    # Проверка общей длины (16 цифр + 3 пробела)
    assert len(card) == 19
    # Проверка позиций пробелов
    assert card[4] == " " and card[9] == " " and card[14] == " "
    # Проверка, что внутри только цифры и пробелы
    assert card.replace(" ", "").isdigit()


def test_boundary_values():
    """Проверка работы с крайними значениями (0 и 9999...)"""
    start = 0
    stop = 9999999999999999
    # Проверим только границы, чтобы не генерировать квадриллион строк
    res_start = card_number_generator(0, 0)
    assert res_start[0] == "0000 0000 0000 0000"

    res_stop = card_number_generator(stop, stop)
    assert res_stop[0] == "9999 9999 9999 9999"


def test_empty_result_if_start_greater_than_stop():
    """Если start > stop, должен вернуться пустой список"""
    assert card_number_generator(10, 5) == []
