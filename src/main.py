from src.generators import filter_by_currency
from src.processing import sort_by_date, filter_by_state
from src.transaction_analyzer import process_bank_search
from src.transaction_reader import reading_csv_data, reading_xlsx_data
from src.utils import get_json_data
from src.widget import get_date, mask_account_card

# Составляем словарь функций для ввода пользователя
actions: dict = {"1": {"func": get_json_data, "disc": "JSON-файл.", "path": "../data/operations.json"},
           "2": {"func": reading_csv_data, "disc": "CSV-файл.", "path": "../data/transactions.csv"},
           "3": {"func": reading_xlsx_data, "disc": "XLSX-файл.", "path": "../data/transactions_excel.xlsx"}
           }
# Варианты ответов
answer_yes_no: list[str] = ["Да", "Нет"]
answer_sorted: list[str] = ["по возрастанию", "по убыванию"]

def ask_yes_no(question: str, answer_options: list[str]) -> bool:
    """Задает вопрос  question с вариантами ответа answer_options и
     возвращает True, если ответ = answer_options[0]"""
    while True:
        answer = input(f'{question} {"/".join(answer_options)}\n').strip().lower()
        if answer in [option.lower() for option in answer_options]:
            break
        else:
            print("Некорректный ввод, повторите попытку.")
    return True if answer == answer_options[0].lower() else False

def main():
    """Основная логика проекта"""

    # Выбор загрузки данных
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        menu_item = input(f"Выберите необходимый пункт меню:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла\n"
                "Пункт: ")
        if menu_item in ["1", "2", "3"]:
            print(f"Для опработки выбран {actions.get(menu_item).get('disc')}")
            # Загружаем данные
            list_data = actions.get(menu_item).get("func")(actions.get(menu_item).get("path"))
            break
        else:
            print("Не корректный ввод, повторите попытку.")

    # Выбор статуса для фильтрации
    while True:
        status_item = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                            "Статус: ").upper()
        if status_item.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {status_item}")
            # Фильтруем данные
            list_data = filter_by_state(list_data, status_item)
            break
        else:
            print(f"Статус операции {status_item} недоступен.")


    if ask_yes_no("Отсортировать операции по дате? ", answer_yes_no):
        # Если Да, то сортируем:
        if ask_yes_no("Отсортировать по возрастанию или по убыванию?", answer_sorted):
            reverse = False
            list_data = sort_by_date(list_data, reverse)  # Сортировка по убыванию
        else:
            list_data = sort_by_date(list_data) # Сортировка по возрастанию

    if ask_yes_no("Выводить только рублевые транзакции? ", answer_yes_no):
        # Если Да, то фильтруем:
        list_data = list(filter_by_currency(list_data, "RUB"))

    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании? ", answer_yes_no):
        # Если Да, то вводим описание:
        search_str = input("Введите описание: ")
        list_data = process_bank_search(list_data, search_str)

    print("Распечатываю итоговый список транзакций...\n")

    print(f"Всего банковских операций в выборке: {len(list_data)}")
    print()

    if list_data:
        for transaction in list_data:
            # Печатаем дату и время
            print(f'{get_date(transaction.get("date"))} {transaction.get("description")}')

            # Логика для счетов:
            from_info = transaction.get("from")
            to_info = transaction.get("to")
            if from_info:  # Если отправитель есть (не None и не пустая строка)
                print(f'{mask_account_card(from_info)} -> {mask_account_card(to_info)}')
            else:  # Если отправителя нет (например, открытие вклада)
                print(f'{mask_account_card(to_info)}')

            # Сумма и валюта
            currency = transaction.get("currency_code") if transaction.get("currency_code") != "RUB" else "руб."
            print(f'Сумма: {transaction.get("amount")} {currency}')
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
