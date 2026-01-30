"""Создание масок для строк по заданным параметрам"""


def get_mask(
    string_input: str,
    index_start: int,
    index_final: int,
    symbol_replace: str,
    index_separator: int,
    symbol_separator: str,
) -> str:
    """
    string_input - входная строка
    index_start - начальный индекс маски (отсчет от 0)
    index_final - конечный индекс маски (отсчет от 0)
    symbol_replace - символ для маски
    index_separator - количество знаков, после которого будет поставлен разделитель
    symbol_separator - символ для разделителя
    """
    chars = list(string_input) # Переводим в список

    # Формируем маску
    mask_char = symbol_replace[0] if symbol_replace else ""
    if mask_char:
        # max(0, index_start) - защита от минусовых индексов
        # работа через срезы защищает от неверных диапазонов
        chars[max(0, index_start): index_final + 1] = mask_char * len(chars[max(0, index_start): index_final + 1])

    # Вставляем разделители
    if index_separator > 0 and symbol_separator:
        sep = symbol_separator[0]
        # Разбиваем на группы по index_separator и соединяем их разделителем
        result = []
        for i in range(0, len(chars), index_separator):
            result.append("".join(chars[i: i + index_separator]))
        return sep.join(result)

    return "".join(chars)
