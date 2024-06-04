# ключи словарей, которые записываются в файл, должны совпадать с названиями полей,
# которые переданы в качестве аргумента fieldnames, иначе будет возникать ошибка

# Аргумент newline функции open()
# отвечает за переводы строк при чтении или записи в текстовый файл
# По умолчанию None   # все разделители строк преобразуются в '\n'
# newline=''          # '\n' будет преобразован в пустую строку.

# Аргумент quoting обьекта writer
#  - QUOTE_ALL: указывает объектам записи указывать все поля
#
#  - QUOTE_MINIMAL: указывает объектам записи заключать в кавычки только те поля,
# которые содержат специальные символы, такие как разделитель delimiter,
# кавычка quotechar или любой из символов в lineterminator
#
#  - QUOTE_NONNUMERIC: указывает объектам записи указывать все нечисловые поля
#
#  - QUOTE_NONE: указывает объектам записи никогда не заключать в кавычки поля

# import csv формат
# data = [{'first_name': 'Тимур', 'second_name': 'Гуев', 'class_number': 11, 'class_letter': 'А'},
#         {'first_name': 'Руслан', 'second_name': 'Чаниев', 'class_number': 9, 'class_letter': 'Б'},
#         {'first_name': 'Роман', 'second_name': 'Белых', 'class_number': 10, 'class_letter': 'В'}]
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
#
# with open('students.csv формат', 'w', encoding='utf-8', newline='') as file:
#     writer = csv формат.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv формат.QUOTE_NONNUMERIC)
#     writer.writeheader()                 # запись заголовков
#     # writerow() построчная запись
#     for row in data:                     # запись строк
#         writer.writerow(row)
#
#     # использум writerows вместо writer (для примера)
#     # writerows() запись всей коллекции в обьект
#     # writer.writerows(data) запись всей коллекции в обьект
#
# создает файл students.csv формат с содержимым:
# "first_name";"second_name";"class_number";"class_letter"
# "Тимур";"Гуев";11;"А"
# "Руслан";"Чаниев";9;"Б"
# "Роман";"Белых";10;"В"