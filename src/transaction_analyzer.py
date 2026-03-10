import re
from collections import Counter

from src.logger.config import setup_logger

# Создаем объект логера для transaction_analyzer
logger = setup_logger("transaction_analyzer")

def process_bank_search(data: list[dict], search_str: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска и 
    возвращает список словарей, у которых в описании есть данная строка"""

    logger.info("Поиск транзакций по описанию")
    if not search_str:
        return data

    # Экранируем спецсимволы и создаем паттерн, который ищет каждое слово
    # (?=.*слово) проверяет наличие слова в любой части строки
    words = search_str.split()
    pattern = "".join([f"(?=.*{re.escape(word.lower())})" for word in words])

    filtered_list = []
    for item in data:
        description = str(item.get("description", "")).lower()
        if re.search(pattern, description):
            filtered_list.append(item)

    logger.info("Поиск завершен")
    return filtered_list


def process_bank_operations(data: list[dict], categories: list = None) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    logger.info("Групировка по списку операций")

    # Извлекаем все описания из словарей (если ключа 'description' нет, пропускаем)
    descriptions = [operation.get('description') for operation in data if 'description' in operation]

    if not descriptions:
        logger.warning("Нет данных для группировки или отсутствует ключ 'description'")
        return {key: 0 for key in categories}

    # Подсчитываем количество вхождений каждого описания
    counts = Counter(descriptions)
    #print(type(counts))
    logger.info("Группировка завершена")

    # Формируем итоговый словарь только по запрашиваемым категориям
    if categories:
        return {category: counts[category] for category in categories}
    else:
        return dict(counts)
