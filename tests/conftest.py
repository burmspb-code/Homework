import logging
from typing import Generator

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture
def list_input_data() -> list[dict]:
    """
    Возвращает входные данные для тестирования
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def expected_result(request: FixtureRequest) -> list[dict]:
    """Возвращает ожидаемые дынне тестирования по значению параметризации"""
    expected_dict = {
        "list_expected_data_executed": [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        "list_expected_data_canceled": [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "list_expected_data_is_reverse": [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        "list_expected_data_is_not_reverse": [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ],
    }
    return expected_dict[request.param]


@pytest.fixture
def data_for_mask_account_card() -> list[dict[str, str]]:
    """
    Возвращает ожидаемые дынные для mask_account_card
    """
    list_data = [
        {"Visa Platinum 7000792289606361": "7000792289606361"},
        {"Счет 73654108430135874305": "73654108430135874305"},
        {"Maestro 1596837868705199": "1596837868705199"},
        {"Счет 64686473678894779589": "64686473678894779589"},
        {"MasterCard 7158300734726758": "7158300734726758"},
        {"Счет 35383033474447895560": "35383033474447895560"},
        {"Visa Classic 6831982476737658": "6831982476737658"},
        {"Visa Platinum 8990922113665229": "8990922113665229"},
        {"Visa Gold 5999414228426353": "5999414228426353"},
        {"Счет 73654108430135874305": "73654108430135874305"},
    ]
    return list_data


@pytest.fixture
def test_transactions() -> list[dict]:
    """Возвращает входные данные для тестирования генератора"""
    test_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return test_transactions


@pytest.fixture
def result_usd_1() -> dict:
    """Транзация 1 с валютой USD"""
    result_usd_1 = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    return result_usd_1


@pytest.fixture
def result_usd_2() -> dict:
    """Транзация 2 с валютой USD"""
    result_usd_2 = {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    return result_usd_2


@pytest.fixture
def result_usd_3() -> dict:
    """Транкзакция 3 с валютой USD"""
    result_usd_3 = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    return result_usd_3


@pytest.fixture
def result_rub_1() -> dict:
    """Транзация 1 с валютой RUB"""
    result_rub_1 = {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    return result_rub_1


@pytest.fixture
def result_rub_2() -> dict:
    """Транзация 2 с валютой RUB"""
    result_rub_2 = {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
    return result_rub_2


@pytest.fixture
def expected_descriptions() -> list[str]:
    """Ожидаемый результат  для transaction_descriptions"""
    transaction_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    return transaction_descriptions


@pytest.fixture(autouse=True)  # Фикстура для автоматического запуска перед каждым тестом на логированием
def reset_logging() -> Generator[None, None, None]:  # Фикстуры являются генераторами.
    """Сброс настройки логгера"""
    logger = logging.getLogger("src.decorators")  # Доступ к нужному логеру ("decorators").
    logger.handlers = []  # Обнуляем список хендлеров (способы вывода) для логера.
    yield  # Передаем управление тесту.


@pytest.fixture
def sample_data():
    return [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Оплата услуг: Интернет", "amount": 500},
        {"description": "Перевод другу", "amount": 1000},
        {"description": "Покупка продуктов", "amount": 200},
        {"amount": 50},  # Транзакция без описания
    ]
