"""Декораторы"""

import functools
import logging
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P") # Захватывает типы всех аргументов функции (*args, **kwargs).
R = TypeVar("R") # Захватывает возвращаемый тип функции.

# Создаем псевдоним для декоратора с параметрами
Decorator = Callable[[Callable[P, R]], Callable[P, R]]

def log(filename: str | None) -> Decorator[P, R]:
    """Декоратор логирует имя функции и успешный результат выполнения/описание возникшей ошибки"""
    # Настройка логгера
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Проверяем, чтобы не добавлять обработчики повторно
    if not logger.handlers:
    # Определяем куда выводить
        handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
        logger.addHandler(handler)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Логируем начало выполнения
            logger.info(f"Старт: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                # Логируем результат работы
                logger.info(f"{func.__name__}: ок")
                # Логируем завершение
                logger.info(f"Завершено: {func.__name__}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise e
        return wrapper
    return decorator
