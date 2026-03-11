from src.transaction_analyzer import process_bank_search, process_bank_operations


# Тесты для process_bank_search
def test_process_bank_search_found(sample_data):
    # Поиск по части слова (регистронезависимый)
    result = process_bank_search(sample_data, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"


def test_process_bank_search_multiple_words(sample_data):
    # Поиск по нескольким словам (порядок не важен)
    result = process_bank_search(sample_data, "услуг оплата")
    assert len(result) == 1
    assert "Интернет" in result[0]["description"]


def test_process_bank_search_empty_query(sample_data):
    # Если строка поиска пустая, возвращается весь список
    assert process_bank_search(sample_data, "") == sample_data


def test_process_bank_search_no_results(sample_data):
    assert process_bank_search(sample_data, "налоги") == []


# Тесты для process_bank_operations
def test_process_bank_operations_with_categories(sample_data):
    categories = ["Перевод организации", "Покупка продуктов", "Неизвестно"]
    result = process_bank_operations(sample_data, categories)

    assert result["Перевод организации"] == 1
    assert result["Покупка продуктов"] == 1
    assert result["Неизвестно"] == 0


def test_process_bank_operations_no_categories(sample_data):
    # Если список категорий не передан, считаем всё имеющееся
    result = process_bank_operations(sample_data)
    assert result["Перевод другу"] == 1
    assert len(result) == 4  # 4 уникальных описания


def test_process_bank_operations_missing_description():
    data = [{"amount": 100}]
    result = process_bank_operations(data, ["Оплата"])
    assert result == {"Оплата": 0}


def test_process_bank_operations_empty_list():
    assert process_bank_operations([], ["Категория"]) == {"Категория": 0}