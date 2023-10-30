def mask_card(data: str) -> str:
    """Функция, которая возвращает замаскированный номер карты"""
    return data[:4] + " " + data[4:6] + "** **** " + data[-4:]


def mask_account(data: str) -> str:
    """Функция, которая возвращает замаскированный номер счета"""
    return "**" + data[-4:]
