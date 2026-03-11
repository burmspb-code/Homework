import runpy
import sys

import pytest

from src.main import ask_yes_no, main, actions
from unittest.mock import patch, MagicMock


def test_ask_yes_no_positive(monkeypatch):
    # Имитируем ввод "Да"
    monkeypatch.setattr('builtins.input', lambda _: "Да")
    assert ask_yes_no("Вопрос", ["Да", "Нет"]) is True


def test_ask_yes_no_negative(monkeypatch):
    # Имитируем ввод "Нет"
    monkeypatch.setattr('builtins.input', lambda _: "Нет")
    assert ask_yes_no("Вопрос", ["Да", "Нет"]) is False


def test_ask_yes_no_retry(monkeypatch, capsys):
    # Имитируем сначала неверный ввод, затем верный
    inputs = iter(["ошибка", "Да"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert ask_yes_no("Вопрос", ["Да", "Нет"]) is True
    captured = capsys.readouterr()
    assert "Некорректный ввод, повторите попытку." in captured.out


@patch("src.main.get_json_data")
@patch("src.main.filter_by_state")
@patch("src.main.sort_by_date")
@patch("src.main.filter_by_currency")
@patch("src.main.mask_account_card")
@patch("src.main.get_date")
@patch("src.main.process_bank_search")
def test_main_full_scenario(
        mock_search, mock_date, mock_mask, mock_filter_curr,
        mock_sort, mock_filter_state, mock_get_json,
        monkeypatch, capsys
):
    # --- РЕШЕНИЕ ПРОБЛЕМЫ С ACTIONS ---
    # Принудительно подставляем моки в словарь actions,
    # чтобы main() вызывал их, а не реальные функции
    actions["1"]["func"] = mock_get_json
    # ----------------------------------

    fake_data = [{
        "date": "2023-01-01T12:00:00",
        "description": "Перевод",
        "amount": "100",
        "currency_code": "RUB",
        "to": "Счет 1",
        "from": "Карта 1"
    }]

    mock_get_json.return_value = fake_data
    mock_filter_state.return_value = fake_data
    mock_sort.return_value = fake_data
    mock_filter_curr.return_value = iter(fake_data)
    mock_search.return_value = fake_data
    mock_date.return_value = "01.01.2023"
    mock_mask.return_value = "**1234"

    # Ответы: 5 (ошибка), 1 (ок), test (ошибка), EXECUTED (ок), Да, по возрастанию, Да, Да, test
    inputs = iter(["5", "1", "test", "EXECUTED", "Да", "по возрастанию", "Да", "Да", "test"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr().out

    assert "Не корректный ввод, повторите попытку." in captured
    # Исправлено: в коде стоит .upper(), поэтому в выводе будет "TEST"
    assert "Статус операции TEST недоступен." in captured
    assert "Для опработки выбран JSON-файл." in captured
    assert "Всего банковских операций в выборке: 1" in captured
    assert "01.01.2023 Перевод" in captured
    assert "Сумма: 100 руб." in captured


def test_main_block_execution(monkeypatch):
    """Тестируем блок if __name__ == '__main__': через имитацию прерывания"""

    # Мы подменяем input так, чтобы он сразу вызывал исключение.
    # Это предотвратит попытку чтения из консоли и остановит выполнение main.
    def mock_exit(*args, **kwargs):
        raise SystemExit  # Имитируем выход из программы

    monkeypatch.setattr("builtins.input", mock_exit)

    # Очищаем кэш импортов, чтобы runpy не ругался на повторный импорт
    if "src.main" in sys.modules:
        del sys.modules["src.main"]

    # Запускаем модуль.
    # Когда выполнится main(), он вызовет input(), который выкинет SystemExit.
    # Тест перехватит это исключение и зачтет успешное прохождение строки.
    with pytest.raises(SystemExit):
        runpy.run_module("src.main", run_name="__main__")

