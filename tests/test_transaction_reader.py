from unittest.mock import MagicMock, mock_open, patch

from src.transaction_reader import readding_xlsx_data, reading_csv_data


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
def test_readding_xlsx_data_success(mock_read_excel: MagicMock) -> None:
    """Корректная работы функции"""
    # Создаем мок для DataFrame и его метода to_dict
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"amount": 100, "currency": "RUB"}]
    mock_read_excel.return_value = mock_df

    result = readding_xlsx_data("fake_path.xlsx")

    assert result == [{"amount": 100, "currency": "RUB"}]
    mock_read_excel.assert_called_once_with("fake_path.xlsx")
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("pandas.read_excel")
def test_readding_xlsx_data_file_not_found(mock_read_excel: MagicMock) -> None:
    """Тест ошибки - файл не найден"""
    mock_read_excel.side_effect = FileNotFoundError

    result = readding_xlsx_data("non_existent.xlsx")

    assert result == []


@patch("pandas.read_excel")
def test_readding_xlsx_data_error(mock_read_excel: MagicMock) -> None:
    """Тест ошибки чтения"""
    mock_read_excel.side_effect = Exception("Some error")

    result = readding_xlsx_data("error.xlsx")

    assert result == []
