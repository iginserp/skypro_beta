from masks import mask_card, mask_account
from widget import widget

raw_data = input("Введите реквизиты карты/счета: \n")
mask_data = widget(raw_data)
print("Результат:", mask_data)
