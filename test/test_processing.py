"""Тестирование функций filter_by_state, sort_by_date"""

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "list_input_data, key_status, expected_result",
    [
        ("list_input_data", "EXECUTED", "list_expected_data_executed"),
        ("list_input_data", "CANCELED", "list_expected_data_canceled"),
    ],
    indirect=["list_input_data", "expected_result"],
)
def test_filter_by_state(list_input_data, key_status, expected_result):
    assert filter_by_state(list_input_data, key_status) == expected_result


@pytest.mark.parametrize(
    "list_input_data, reverse, expected_result",
    [
        ("list_input_data", True, "list_expected_data_is_reverse"),
        ("list_input_data", False, "list_expected_data_is_not_reverse"),
    ],
    indirect=["list_input_data", "expected_result"],
)
def test_sort_by_date(list_input_data, reverse, expected_result):
    assert sort_by_date(list_input_data, reverse) == expected_result



