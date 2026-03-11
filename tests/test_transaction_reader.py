from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.transaction_reader import reading_xlsx_data, reading_csv_data


@patch("builtins.open", new_callable=mock_open, read_data="amount,currency\n100,RUB")  # Мокаем open
@patch("csv.DictReader")
def test_reading_csv_data_success(mock_dict_reader: MagicMock, mock_file: MagicMock) -> None:
    """Корректная работы функции"""
    # Создаем mok для csv.DictReader
    mock_dict_reader.return_value = [{"amount": "100", "currency": "RUB"}]

    result = reading_csv_data("test.csv")

    assert result == [{"amount": "100", "currency": "RUB"}]
    mock_dict_reader.return_value = [{"amount": "100", "currency": "RUB"}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_reading_csv_data_not_found(mock_file: MagicMock) -> None:
    """Тест ошибки - файл не найден"""
    result = reading_csv_data("missing.csv")
    assert result == []
    mock_file.assert_called_once()


@patch("builtins.open", side_effect=Exception("Read error"))
def test_reading_csv_data_exception(mock_file: MagicMock) -> None:
    """Тест ошибки чтения"""
    result = reading_csv_data("error.csv")
    assert result == []
    mock_file.assert_called_once()


@patch("pandas.read_excel")
def test_reading_xlsx_data_success(mock_read_excel: MagicMock) -> None:
    # Имитируем возврат DataFrame
    mock_read_excel.return_value = pd.DataFrame([{"amount": 100}])

    file_path = "data/operations.xlsx"
    reading_xlsx_data(file_path)

    # Добавляем engine='openpyxl' в проверку, так как он есть в коде!
    mock_read_excel.assert_called_once_with(file_path, engine='openpyxl')


@patch("pandas.read_excel")
def test_reading_xlsx_data_file_not_found(mock_read_excel: MagicMock) -> None:
    """Тест ошибки - файл не найден"""
    mock_read_excel.side_effect = FileNotFoundError

    result = reading_xlsx_data("non_existent.xlsx")

    assert result == []


@patch("pandas.read_excel")
def test_reading_xlsx_data_error(mock_read_excel: MagicMock) -> None:
    """Тест ошибки чтения"""
    mock_read_excel.side_effect = Exception("Some error")

    result = reading_xlsx_data("error.xlsx")

    assert result == []
