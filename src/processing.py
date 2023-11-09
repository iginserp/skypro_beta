def filter_by_state(dict_list: list, rqrd_state="EXECUTED") -> list:
    """Функция, которая фильтрует список словарей по ключу state, по умолчанию значение ключа - EXECUTED"""

    filtered_list = list(filter(lambda x: x["state"] == rqrd_state, dict_list))
    return filtered_list


def order_by_date(dict_list: list, order=True) -> list:
    """Функция, которая сортирует список словарей по дате, сортировка по умолчанию - по убыванию"""

    sorted_list = sorted(dict_list, key=lambda x: x["date"], reverse=order)
    return sorted_list
