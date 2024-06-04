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


# - writerow() записывает КАЖДУЮ строку отдельно (нужно итерироваться)
# import csv формат
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
# with open('students.csv формат', 'w', encoding='utf-8', newline='') as file:
#     writer = csv формат.writer(file, delimiter=';', quoting=csv формат.QUOTE_NONNUMERIC)
#     writer.writerow(columns)  # записали заголовки столбцов в первую строку
#     for row in data:          # записали остальные данные в строки
#         writer.writerow(row)
#
#
# создает файл с содержимым:
# "first_name";"second_name";"class_number";"class_letter"
# "Тимур";"Гуев";11;"А"
# "Руслан";"Чаниев";9;"Б"
# "Роман";"Белых";10;"В"


# - writerowS() записывает всю коллекцию в файл
# каждый элемент списка должен быть коллекцией!!!!
# import csv формат
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
# with open('students.csv формат', 'w', encoding='utf-8', newline='') as file:
#     writer = csv формат.writer(file, delimiter=';', quoting=csv формат.QUOTE_NONNUMERIC)
#     writer.writerow(columns)  # записали заголовки столбцов в первую строку методом writerow
#     writer.writerows(data)    # записали содержимое коллекции data методом writerow
#
# создает файл students.csv формат с содержимым:
# "first_name";"second_name";"class_number";"class_letter"
# "Тимур";"Гуев";11;"А"
# "Руслан";"Чаниев";9;"Б"
# "Роман";"Белых";10;"В"