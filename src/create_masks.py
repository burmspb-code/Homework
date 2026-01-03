"""Создание масок для строк по заданным параметрам"""


def get_mask(
    string_input: str,
    index_start: int,
    index_final: int,
    simbol_replace: str,
    index_separator: int,
    symbol_separator: str,
) -> str:
    """
    string_input - входная строка
    index_start - начальный индекс маски (отсчет от 0)
    index_final - конечный индекс маски (отсчет от 0)
    simbol_replace - символ для маски
    index_separator - количество знаков, после которого будет поставлен разделитель
    symbol_separator - символ для разделителя
    """

    work_list = list(string_input)  # переводим в список
    new_list: list[str] = []  # формируем новый список

    if index_separator > 0:  # исключаем ZeroDivisionError
        # количество интервалов разделения
        separation_cycle = len(work_list) // index_separator
        # список индексов символов, после которых нужно делать разделение
        separator_list_number = [i * index_separator for i in range(1, separation_cycle + 1)]
    else:
        separator_list_number = []

    for i, item in enumerate(work_list):

        new_list += item

        if index_start <= i <= index_final:
            if simbol_replace:
                new_list[-1] = simbol_replace[0]

        if i + 1 in separator_list_number and i + 1 != len(work_list):
            if symbol_separator:
                new_list += symbol_separator[0]

    return "".join(new_list)
