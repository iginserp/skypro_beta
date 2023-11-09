# from src.widget import widget, transform_data


# print("Задание 1")
# raw_data = input("Введите исходные данные карты/счета: \n")
# mask_data = widget(raw_data)
# print("Замаскированные данные карты/счета:", mask_data)

# print("Задание 2")
# raw_data = input("Введите исходные данные даты-времени: \n")
# result = transform_data(raw_data)
# print("Результат:", result)

from src.processing import filter_by_state, order_by_date


print("Урок  Продвинутй Git ДЗ Задание 1\n")
raw_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

result = filter_by_state(raw_data)
print("Список отфильтрованный со значением по умолчанию:\n", result)

state_value = input("Введите значению ключа STATE для фильтрации списка словарей:\n")
result2 = filter_by_state(raw_data, state_value)
print(result2)

print("\n Сортировка списка по ключу date, по умолчанию: \n")
result3 = order_by_date(raw_data)
print(result3)

order = input("\n Введите способ сортировки списка: по убыванию - True, по возрастанию - False :\n")
result4 = order_by_date(raw_data, order)
print(result4)
