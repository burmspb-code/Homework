from unittest.mock import MagicMock, mock_open, patch

from src.utils import get_json_data


@patch("src.utils.open", new_callable=mock_open, read_data='[{"amount": 100}]')
def test_get_json_data_success(mock_file: MagicMock) -> None:
    """Тест успешного чтения корректного JSON."""
    result = get_json_data("data/operations.json")
    assert result == [{"amount": 100}]
    mock_file.assert_called_once()


@patch("src.utils.open", side_effect=FileNotFoundError)
def test_get_json_data_file_not_found(mock_file: MagicMock) -> None:
    """Тест возврата пустого списка, если файл не найден."""
    result = get_json_data("wrong/path.json")
    assert result == []
    mock_file.assert_called_once()


@patch("src.utils.open", new_callable=mock_open, read_data="invalid json")
def test_get_json_data_invalid_json(mock_file: MagicMock) -> None:
    """Тест возврата пустого списка при битом JSON."""
    result = get_json_data("data/bad.json")
    assert result == []
    mock_file.assert_called_once()


@patch("src.utils.open", new_callable=mock_open, read_data='{"not_a": "list"}')
def test_get_json_data_not_a_list(mock_file: MagicMock) -> None:
    """Тест возврата пустого списка, если в JSON не список."""
    result = get_json_data("data/not_list.json")
    assert result == []
    mock_file.assert_called_once()
