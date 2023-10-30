import datetime
from src.masks import mask_card, mask_account


def widget(data: str) -> str:
    """Функция, которая возвращает замаскированный номер карты/счета"""

    splitted_data = data.rsplit(" ", 1)
    card_account_type = splitted_data[0]
    card_account_number = splitted_data[1]

    if len(card_account_number) == 16:
        hidden_number = mask_card(card_account_number)
        result = card_account_type + " " + hidden_number
    elif len(card_account_number) == 20:
        hidden_number = mask_account(card_account_number)
        result = card_account_type + " " + hidden_number
    else:
        print("Некорректный формат данных!")
        result = data

    return str(result)


def transform_data(date: str) -> str:
    """Функция, которая преобразует банковский формат даты-времени в пользовательский формат даты"""
    date_before = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    date_after = date_before.strftime("%d.%m.%Y")
    return date_after