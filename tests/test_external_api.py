from unittest.mock import MagicMock, patch

import requests

from src.external_api import get_rub_transaction


def test_get_rub_transaction_rub() -> None:
    """Тест: если валюта RUB, API не вызывается, возвращается та же сумма."""
    transaction = transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "RUB"}}}
    assert get_rub_transaction(transaction) == 100.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_get_rub_transaction_usd_success(mock_get: MagicMock, mock_getenv: MagicMock) -> None:
    """Тест успешного запроса конвертации из USD в RUB."""
    # Настройка моков
    mock_getenv.return_value = "test_api_key"

    # Создаем фальшивый ответ от API
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 8500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Вызов функции
    transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}
    result = get_rub_transaction(transaction)

    # Проверки
    assert result == 8500.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "test_api_key"},
        params={"amount": 100.0, "from": "USD", "to": "RUB"},
    )


@patch("src.external_api.requests.get")
def test_get_rub_transaction_error(mock_get: MagicMock) -> None:
    """Тест: возврат 0.0 при ошибке запроса к API."""
    # Настраиваем мок на генерацию исключения
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "EUR"}}}
    result = get_rub_transaction(transaction)

    assert result == 0.0
    mock_get.assert_called_once()


def test_get_rub_transaction_unsupported_currency() -> None:
    """Тест: возврат 0.0 для неподдерживаемой валюты (например, CNY)."""
    transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "CNY"}}}
    assert get_rub_transaction(transaction) == 0.0


def test_get_rub_transaction_empty_currency() -> None:
    """Тест: возврат 0.0, если валюта не указана."""
    transaction = {"amount": 100.0}  # Ключ 'currency' отсутствует
    assert get_rub_transaction(transaction) == 0.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_get_rub_transaction_currency_as_string(mock_get: MagicMock, mock_getenv: MagicMock) -> None:
    """Тест, когда currency в транзакции — это строка, а не словарь."""

    # Настраиваем моки
    mock_getenv.return_value = "test_api_key"
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Передаем "currency" как строку
    transaction = {
        "operationAmount": {"amount": 100.0, "currency": "usd"}  # Специально маленькими буквами для проверки .upper()
    }

    result = get_rub_transaction(transaction)

    # Проверяем результат
    assert result == 7500.0
