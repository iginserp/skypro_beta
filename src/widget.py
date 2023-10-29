def widget(data: str) -> str:
    from masks import mask_card, mask_account
    """Функция, которая возвращает замаскированный номер карты """

    splitted_data = data.rsplit(" ", 1)
    card_account_type = splitted_data[0]
    card_account_number = splitted_data[1]
    
    if len(card_account_number) == 16:
        hidden_number = mask_card(card_account_number)
        result = card_account_type + ' ' + hidden_number
    elif len(card_account_number) == 20:
        hidden_number = mask_account(card_account_number)
        result = card_account_type + ' ' + hidden_number
    else:
        print('Некорректный формат данных!')
        result = data

    return result

