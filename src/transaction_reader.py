"""Модуль для чтения транзакций"""

import csv
from pathlib import Path

import pandas as pd

from src.logger.config import setup_logger

# Создаем объект логера для transaction_reader
logger = setup_logger("transaction_reader")


def reading_csv_data(file_path: str | Path) -> list[dict]:
    """Читает транзакции из csv файла и возвращает список словарей"""
    logger.info(f"Открытие файла {file_path}")
    try:
        with open(file_path) as file:
            reader = csv.DictReader(file, delimiter=";")
            logger.info("Чтение прошло успешно")
            return list(reader)
    except FileNotFoundError:
        logger.error(f"Ошибка - файл {file_path} не найден")
        return []
    except Exception as e:
        logger.error(f"Ошибка - {e}")
        return []


def reading_xlsx_data(file_path: str | Path) -> list[dict]:
    """Читает транзакции из xlsx файла и возвращает список словарей"""
    logger.info(f"Открытие файла {file_path}")
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        list_dict = df.to_dict(orient="records")
        logger.info("Чтение прошло успешно")
        return list_dict
    except FileNotFoundError:
        logger.error(f"Ошибка - файл {file_path} не найден")
        return []
    except Exception as e:
        logger.error(f"Ошибка - {e}")
        return []
