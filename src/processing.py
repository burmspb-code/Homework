"""Функции обработки данных"""

def filter_by_state(list_dicts: list[dict], key: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей по ключу"""

    return [item for item in list_dicts if item["state"] == key]



def sort_by_date(list_dicts: list[dict], key_sort: bool = True) -> list[dict]:
    """Возвращает новый список, отсортированный по дате
    key_sort = True - по удыванию (по умолчанию)
    key_sort = False - по возрастанию
    """

    return sorted(list_dicts, key=lambda x: x["date"], reverse=key_sort)

# Проверка filter_by_state
# list_d = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# print(filter_by_state(list_d))
# print(filter_by_state(list_d, 'CANCELED'))

# Проверка sort_by_date
# list_d = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# #print(sort_by_date(list_d)
# print(sort_by_date(list_d, False))
