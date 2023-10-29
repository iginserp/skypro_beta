import datetime

def transform_data (date: str) -> str:

    ''' Функция, которая преобразует банковский формат даты-времени в пользовательский формат даты '''
    date_before = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    date_after = date_before.strftime('%d.%m.%Y')
    return date_after
