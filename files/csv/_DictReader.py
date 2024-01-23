# Чтение данных с помощью DictReader
# Поддерживает создание объекта-словаря на основе названий столбцов
# можем обращаться к полям не по индексу, а по названию
#
# значениями по умолчанию для аргументов delimiter и quotechar
# являются ',' (символ запятой)
# и '"' (символ двойной кавычки)
#
# названия столбцов  хранятся в атрибуте fieldnames
# к элементам строк мы обращаемся
# по их названиям (int(item['price'])
#
# keywords;price;product_name
# "Садовый стул, стул для дачи";1699;ВЭДДО
# Садовый стул;2999;ЭПЛАРО
# Садовый табурет;1699;ЭПЛАРО
# Садовый стол;1999;ТЭРНО
# "Складной стол, обеденный стол";7499;ЭПЛАРО
#
# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     for row in rows:                                            # переменная row имеет тип dict
#         print(row)
#
# Вывидит:
# {'keywords': 'Садовый стул, стул для дачи', 'price': '1699', 'product_name': 'ВЭДДО'}
# {'keywords': 'Садовый стул', 'price': '2999', 'product_name': 'ЭПЛАРО'}
# {'keywords': 'Садовый табурет', 'price': '1699', 'product_name': 'ЭПЛАРО'}
# {'keywords': 'Садовый стол', 'price': '1999', 'product_name': 'ТЭРНО'}
# {'keywords': 'Складной стол, обеденный стол', 'price': '7499', 'product_name': 'ЭПЛАРО'}
#
# # сортируем DictReader
# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     expensive = sorted(rows, key=lambda item: int(item['price']), reverse=True)
#     for record in expensive[:5]:
#         print(record)


# quoting
# writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
# QUOTE_ALL: указывает объектам записи указывать все поля
# QUOTE_MINIMAL: указывает объектам записи заключать в кавычки только те поля,
# которые содержат специальные символы, такие как разделитель delimiter,
# кавычка quotechar или любой из символов в lineterminator
# QUOTE_NONNUMERIC: указывает объектам записи указывать все нечисловые поля
# QUOTE_NONE: указывает объектам записи никогда не заключать в кавычки поля


# Запись данных с помощью DictWriter
# позволяет записывать содержимое словаря в файл.
#
# ключи словарей, которые записываются в файл, должны совпадать с названиями полей,
# которые переданы в качестве аргумента fieldnames, иначе будет возникать ошибка
# порядок ключей в словарях совершенно не важен, при записи они будут расположены так как расположены в fieldnames
#
