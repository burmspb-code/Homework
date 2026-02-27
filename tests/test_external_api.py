from unittest.mock import patch, MagicMock
import requests
from src.external_api import get_rub_transaction

def test_get_rub_transaction_rub():
    """Тест: если валюта RUB, API не вызывается, возвращается та же сумма."""
    assert get_rub_transaction(100.0, "RUB") == 100.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_get_rub_transaction_usd_success(mock_get, mock_getenv):
    """Тест успешного запроса конвертации из USD в RUB."""
    # Настройка моков
    mock_getenv.return_value = "test_api_key"

    # Создаем фальшивый ответ от API
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 8500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Вызов функции
    result = get_rub_transaction(100.0, "USD")

    # Проверки
    assert result == 8500.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "test_api_key"},
        params={"amount": 100.0, "from": "USD", "to": "RUB"}
    )


@patch("src.external_api.requests.get")
def test_get_rub_transaction_error(mock_get):
    """Тест: возврат 0.0 при ошибке запроса к API."""
    # Настраиваем мок на генерацию исключения
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    result = get_rub_transaction(100.0, "EUR")

    assert result == 0.0
    mock_get.assert_called_once()
