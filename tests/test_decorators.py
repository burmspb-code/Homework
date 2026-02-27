"""Тестирование декораторов"""

import os
from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log_to_console_success(capsys: CaptureFixture[str]) -> None:
    """Тестируем успешное выполнение функции с выводом в консоль."""

    @log(filename=None)
    def add(x: int, y: int) -> int:
        return x + y

    result: int = add(1, 2)

    # Проверяем результат функции
    assert result == 3

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем наличие ключевых фраз в stderr (logging по умолчанию пишет в stderr)
    assert "add: ок" in captured.err


def test_log_to_console_error(capsys: CaptureFixture[str]) -> None:
    """Тестируем логирование ошибки."""

    @log(filename=None)
    def divide(x: int, y: int) -> float:
        return x / y

    # Проверяем, что исключение пробрасывается выше
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    # Проверяем лог ошибки
    assert "divide error: division by zero" in captured.err
    assert "Inputs: (1, 0), {}" in captured.err


def test_log_to_file(tmp_path: Path) -> None:
    """Тестируем запись логов в файл с использованием временной директории pytest."""
    # tmp_path — встроенная «умная» фикстура в pytest, которая автоматически создает временную директорию для тестов.
    log_file_str = str(tmp_path / "test.log")

    @log(filename=log_file_str)
    def multiply(x: int, y: int) -> float:
        return x * y

    multiply(2, 3)

    # Проверяем, что файл создан
    assert os.path.exists(log_file_str)

    # Читаем содержимое файла
    with open(log_file_str, "r") as f:
        content = f.read()
        assert "multiply: ок" in content
