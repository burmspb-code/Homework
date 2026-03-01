"""Наложение маски на номер банковской карты и номер банковского счета"""

from src.create_masks import get_mask
from src.logger.config import setup_logger

# Создаем объект логера для masks
logger = setup_logger("masks")


def get_mask_card_number(card_n: int) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""

    logger.debug(f"Маскировка номера карты: {card_n}")

    if not isinstance(card_n, int):
        logger.error(f"Ошибка - номер карты {card_n} не целое число")

        raise TypeError("Номер карты должен быть целым числом")

    result = get_mask(str(card_n), 6, 11, "*", 4, " ")
    logger.info("Номер карты успешно замаскирован")

    return str(result)


def get_mask_account(account_n: int) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера счета по правилу
    **XXXX"""

    logger.debug(f"Маскиовка номера счета: {account_n}")

    if not isinstance(account_n, int):
        logger.error(f"Ошибка - номер счета {account_n} не целое число")

        raise TypeError("Номер счета должен быть целым числом")

    result = get_mask(str(account_n), 0, 15, "*", 0, "")[-6::]
    logger.info("Номер счета успешно замаскирован")

    return str(result)
