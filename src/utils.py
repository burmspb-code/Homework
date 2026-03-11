import json
from pathlib import Path

from src.logger.config import setup_logger

# Создаем объект логера для utils
logger = setup_logger("utils")


def flatten_transaction(t: dict) -> dict:
    """Приводит транзакцию к плоскому виду, как в CSV."""
    # Если это уже плоский CSV-словать, вернет его же (или расширит)
    # Если это JSON, вытащит вложенные поля наружу
    return {
        "id": t.get("id"),
        "state": t.get("state"),
        "date": t.get("date"),
        "amount": t.get("amount") or t.get("operationAmount", {}).get("amount"),
        "currency_code": t.get("currency_code") or t.get("operationAmount", {}).get("currency", {}).get("code"),
        "from": t.get("from"),
        "to": t.get("to"),
        "description": t.get("description"),
    }


def get_json_data(path: str | Path) -> list[dict]:
    """Возвращает список плоских словарей из JSON-файла."""
    logger.debug(f"Чтение данных json из файла {path}")
    data = []

    try:
        with open(path, encoding="utf-8") as file:
            raw_data = json.load(file)
            if isinstance(raw_data, list):
                data = raw_data
                logger.info("Данные успешно загружены")
            else:
                logger.error("Файл должен содержать список объектов")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при чтении JSON: {e}")

    # Превращаем всё в плоский формат перед возвратом
    return [flatten_transaction(t) for t in data]
