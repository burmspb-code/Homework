from unittest.mock import MagicMock, patch

from src.logger.config import setup_logger


@patch("src.logger.config.os.path.exists")
@patch("src.logger.config.os.makedirs")
@patch("src.logger.config.logging.FileHandler")
def test_create_log_dir_if_not_exists(
    mock_file_handler: MagicMock, mock_makedirs: MagicMock, mock_exists: MagicMock
) -> None:
    # 1. Имитируем, что папки нет
    mock_exists.return_value = False

    # 2. Вызываем функцию
    setup_logger("test_name")

    # 3. ПРОВЕРКИ:
    # Проверяем, что путь проверялся
    mock_exists.assert_called_once()

    # Проверяем, что папка была создана
    mock_makedirs.assert_called_once()

    # ПРАВКА: Проверяем, что FileHandler БЫЛ создан (это правильно)
    mock_file_handler.assert_called_once()

    # Можно даже проверить, что лог-файл назван правильно
    args, kwargs = mock_file_handler.call_args
    assert "test_name.log" in args[0]


@patch("src.logger.config.os.path.exists")
@patch("src.logger.config.os.makedirs")
@patch("src.logger.config.logging.FileHandler")  # Мокаем, чтобы не создавался реальный .log файл
def test_setup_logger_does_not_create_dir_if_exists(
    mock_file_handler: MagicMock, mock_makedirs: MagicMock, mock_exists: MagicMock
) -> None:
    # Имитируем, что папка уже существует
    mock_exists.return_value = True

    # Вызываем функцию с обязательным аргументом name
    setup_logger("test_name")

    # Проверяем, что проверка была, а команда на создание НЕ вызывалась
    mock_exists.assert_called_once()
    mock_makedirs.assert_not_called()
    mock_file_handler.assert_not_called()
