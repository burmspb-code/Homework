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
