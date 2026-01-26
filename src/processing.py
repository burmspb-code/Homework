"""Функции обработки данных"""


def filter_by_state(list_dicts: list[dict], key: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей по ключу"""

    return [item for item in list_dicts if item["state"] == key]


def sort_by_date(list_dicts: list[dict], reverse: bool = True) -> list[dict]:
    """Возвращает новый список, отсортированный по дате
    reverse = True - по убыванию (по умолчанию)
    reverse = False - по возрастанию
    """

    return sorted(list_dicts, key=lambda x: x["date"], reverse=reverse)
