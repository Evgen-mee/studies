# CSV (от англ. Comma-Separated Values — значения, разделённые запятыми)
# — текстовый формат, предназначенный для представления табличных данных.
# Строка таблицы соответствует строке текста, которая содержит одно
# или несколько полей, разделенных запятыми.

# Формат данных csv, в котором разделителем является символ табуляции,
# называют tsv (англ. tab separated values — «значения, разделенные табуляцией»).
#
# tsv — текстовый формат для представления табличных данных.
# Каждая запись в таблице — строка текстового файла.
# Каждое поле записи отделяется от других символом табуляции,
# а точнее — горизонтальной табуляции.
#
# tsv и csv — формы более общего формата dsv
# (англ. delimiter separated values — «значения,
# разграниченные разделителем»).
#
# пробелов после запятой быть не должно!!!
# в формате csv будет выглядеть так:
#
# Rank,Language,Share
# 1,Python,31.17%
# 2,Java,17.75%
# 3,JavaScript,8%
# 4,C#,7.05%
# 5,PHP,6.09%

# Разделителем записей был выбран символ новой строки,
# а разделителем полей — символ запятой.
#
# with open('products.csv', encoding='utf-8') as file: #  вывидет csv строка = лист
#     data = file.read()
#     for line in data.splitlines():
#         print(line.split(','))
#
#
# with open('products.csv', encoding='utf-8') as file: #  вывидет  вложенный список (таблицу)
#     data = file.read()
#     table = [r.split(',') for r in data.splitlines()]
#
#
# with open('products.csv', encoding='utf-8') as file:
#     data = file.read()
#     table = [r.split(',') for r in data.splitlines()]
#     del table[0]                                        # удаляем заголовок
#     table.sort(key=lambda item: int(item[1]))
#     for line in table[:5]:
#         print(line)


# Модуль csv
# reader == список
# next(rows) пропустить заголовок!!!!
#
# keywords,price,product_name
# Садовый стул,1699,ВЭДДО
# Садовый стул,2999,ЭПЛАРО
# Садовый табурет,1699,ЭПЛАРО

# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.reader(file)                               # создаем reader объект
#     for row in rows:
#         print(row)
#
# вывидет:
# ['keywords', 'price', 'product_name']
# ['Садовый стул', '1699', 'ВЭДДО']
# ['Садовый стул', '2999', 'ЭПЛАРО']
# ['Садовый табурет', '1699', 'ЭПЛАРО']
#
# При создании reader объекта мы можем его настраивать, указывая:
# - аргумент delimiter — односимвольная строка, используемая для разделения полей,
# по умолчанию имеет значение ','
# - аргумент quotechar — односимвольная строка, используемая для кавычек в полях,
# содержащих специальные символы, по умолчанию имеет значение '"'.
#
# разделителя выбран символ ';'
#
# keywords;price;product_name
# "Садовый стул, стул для дачи";1699;ВЭДДО
# Садовый стул;2999;ЭПЛАРО
# Садовый табурет;1699;ЭПЛАРО
# Садовый стол;1999;ТЭРНО
#
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=';', quotechar='"') # задали аргументы delimiter quotechar
#     for index, row in enumerate(rows):                    # берем определенное колличество строк
#         if index > 5:
#             break
#         print(row)


#

# Запись данных с помощью writer
# создает файл students.csv
#
# параметр newline функции open()
# отвечает за переводы строк при чтении или записи в текстовый файл
# По умолчанию имеет значение None разделители строк == '\n'
# Если в файле оказывается лишний перевод строки,
# то следует использовать этот параметр в режиме newline='',
# тогда '\n' будет преобразован в пустую строку.
#
# import csv
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(columns)                 # запись заголовков
#     for row in data:                         # запись строк
#         writer.writerow(row)
#
#




