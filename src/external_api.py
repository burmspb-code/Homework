import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные из файла .env в окружение
load_dotenv()


def get_rub_transaction(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "").upper()

    if currency == "RUB":
        return float(amount)

    elif currency in ["USD", "EUR"]:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        payload: Dict[str, Any] = {"amount": amount, "from": currency, "to": "RUB"}
        headers = {"apikey": api_key}
        try:
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()
            result = data.get("result")
            return float(result) if result is not None else 0.0
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return 0.0
    else:
        return 0.0
