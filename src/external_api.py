import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из файла .env в окружение
load_dotenv()

def get_rub_transaction(amount: float, currency: str) -> float:
    """Возвращает сумму транзакции в рублях"""
    if currency == 'RUB':
        return amount
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        payload = {
        "amount": amount,
        "from": currency,
        "to": 'RUB'
        }
        headers = {
        "apikey": api_key
        }
        try:
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()  # Проверка на ошибки HTTP
            return response.json()["result"]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return 0.0
