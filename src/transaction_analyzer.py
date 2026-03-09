import re

import pandas as pd


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска и 
    возвращает список словарей, у которых в описании есть данная строка"""

    # Разбиваем строку поиска по любому не буквенно-цифровому символу
    words = [re.escape(word) for word in re.split(r'[^a-zA-Zа-яА-Я0-9]+', search) if word]

    if not words:
        return []

    # Склеиваем паттерн в слова, разделенные любыми символами (.*)
    search_pattern = ".*".join(words)
    pattern = re.compile(search_pattern, re.IGNORECASE)

    filtered_list = [item for item in data if "description" in item and pattern.search(str(item["description"]))]

    return filtered_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    data_frame = pd.DataFrame(data)  # Загружаем список словарей в датафрейм

    # Проверка наличия колонки, чтобы не упасть с ошибкой
    if 'description' not in data_frame.columns:
        return {key: 0 for key in categories}

    result_frame = data_frame.description.value_counts()  # Создаем объект с уникальными значениями

    return {key: int(result_frame.get(key, 0)) if key in result_frame.keys() else 0 for key in categories}
