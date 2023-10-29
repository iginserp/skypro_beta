from widget import widget
from utils import transform_data

print("Задание 1")
raw_data = input("Введите исходные данные карты/счета: \n")
mask_data = widget(raw_data)
print("Замаскированные данные карты/счета:", mask_data)

print("Задание 2")
raw_data = input("Введите исходные данные даты-времени: \n")
result = transform_data(raw_data)
print("Результат:", result)

