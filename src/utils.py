import json
from pathlib import Path

from src.logger.config import setup_logger

# Создаем объект логера для utils
logger = setup_logger("utils")


def get_json_data(path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях."""

    logger.debug(f"Чтение данных json из файла {path}")

    current_dir = Path(__file__).parent  # Получаем текущую директорию.
    file_path = current_dir.parent / path  # Поднимаемся на уровень выше и идем в path

    try:
        with open(file_path) as file:
            data = json.load(file)
        if not isinstance(data, list):
            logger.error("Файл должен содержать список объектов")
            data = []

    except FileNotFoundError:
        logger.error(f"Ошибка - файл {path} не найден")
        data = []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {path}")
        data = []

    if data:
        logger.info("Данные успешно загружены")

    return data
