"""Тестирование функций filter_by_state, sort_by_date"""
import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize ("list_dict_data, key_status, expected_result", [
    ("list_dict_data", 'EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                            ]),
    ("list_dict_data", 'CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                                ]),
    ("list_dict_data", 'EXECUTED',  [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                                ])
], indirect=['list_dict_data'])
def test_filter_by_state(list_dict_data, key_status, expected_result):
    assert filter_by_state(list_dict_data, key_status) == expected_result

@pytest.mark.parametrize ("list_dict_data, reverse, expected_result", [
    ("list_dict_data", True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                                ]),
    ("list_dict_data", False,  [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
                                    ])
], indirect=['list_dict_data'])
def test_sort_by_date(list_dict_data, reverse, expected_result):
    assert sort_by_date(list_dict_data, reverse) == expected_result
