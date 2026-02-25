"""Тестирование декораторов"""
import pytest
import os
from src.decorators import log


def test_log_to_console_success(capsys):
    """Тестируем успешное выполнение функции с выводом в консоль."""

    @log(filename=None)
    def add(x, y):
        return x + y

    result = add(1, 2)

    # Проверяем результат функции
    assert result == 3

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем наличие ключевых фраз в stderr (logging по умолчанию пишет в stderr)
    assert "add: ок" in captured.err


def test_log_to_console_error(capsys):
    """Тестируем логирование ошибки."""

    @log(filename=None)
    def divide(x, y):
        return x / y

    # Проверяем, что исключение пробрасывается выше
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    # Проверяем лог ошибки
    assert "divide error: division by zero" in captured.err
    assert "Inputs: (1, 0), {}" in captured.err

def test_log_to_file(tmp_path):
    """Тестируем запись логов в файл с использованием временной директории pytest."""
    # tmp_path — встроенная «умная» фикстура в pytest, которая автоматически создает временную директорию для тестов.
    log_file_str = str(tmp_path / "test.log")

    @log(filename=log_file_str)
    def multiply(x, y):
        return x * y

    multiply(2, 3)

    # Проверяем, что файл создан
    assert os.path.exists(log_file_str)

    # Читаем содержимое файла
    with open(log_file_str, "r") as f:
        content = f.read()
        assert "multiply: ок" in content
