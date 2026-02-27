import json
from pathlib import Path

def get_json_data(path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях."""
     
    current_dir = Path(__file__).parent # Получаем текущую директорию.
    file_path = current_dir.parent / path # Поднимаемся на уровень выше и идем в path

    try:
        with open(file_path) as file:
            data = json.load(file)
        if not isinstance(data, list):
            data = []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

if __name__ == '__main__':
    print(get_json_data("data/operations.json"))
