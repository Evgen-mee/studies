# Содержимое файла(пример):
# keywords;price;product_name
# "Садовый стул, стул для дачи";1699;ВЭДДО
# Садовый стул;2999;ЭПЛАРО
# Садовый табурет;1699;ЭПЛАРО
# Садовый стол;1999;ТЭРНО
# "Складной стол, обеденный стол";7499;ЭПЛАРО
# Настил;1299;РУННЕН
# Стеллаж;1299;ХИЛЛИС
# "Кружка, сосуд, стакан с ручкой";39;СТЕЛЬНА
# Молочник;299;ВАРДАГЕН
# Термос для еды;699;ЭФТЕРФРОГАД
# Ситечко;59;ИДЕАЛИСК
# Чайник заварочный;499;РИКЛИГ
# Кофе-пресс;699;УПХЕТТА
# Чашка с блюдцем;249;ИКЕА
# "Кружка, стакан с ручкой";249;ЭМНТ
# Ситечко;199;САККУННИГ
# Кружка;199;ФИНСТИЛТ
# "Тарелка, блюдце";269;ЭВЕРЕНС

# для корректной обработки данных мы должны исключить первую строку из обработки, которая содержит названия столбцов.
# import csv формат
# with open('products.csv формат', encoding='utf-8') as file:           # открыли файл на чтение
#     rows = csv формат.reader(file, delimiter=';', quotechar='"')      # создали reader обьект с аргументами
#     del rows[0]                                                # удалили первую строку с названием столбцов

# rows = csv формат.reader(file)
# Объект reader дает доступ к построчному итератору
# После выполнения этой строки в переменную rows будет записан итератор,
# с помощью которого можно «пробежаться» циклом по файлу.
#
# В каждой итерации цикла при этом будет доступна соответствующая строка файла,
# уже разбитая по запятым и представляющая собой список.
# При этом автоматически будут учтены все нюансы с запятыми внутри кавычек и самими кавычками.
#
# каждая строка файла, полученная из итератора, является списком, к ней можно применять все способы работы со списками.


# Аргументы reader объекта
# - аргумент delimiter — односимвольная строка, используемая для разделения полей,
# по умолчанию имеет значение ','
# - аргумент quotechar — односимвольная строка, используемая для кавычек в полях, содержащих специальные символы,
# по умолчанию имеет значение '"'


# import csv формат
# with open('products.csv формат', encoding='utf-8') as file:           # открыли файл на чтение
#     rows = csv формат.reader(file, delimiter=';', quotechar='"')      # создали reader обьект с аргументами
#     for index, row in enumerate(rows):                         # итерируемся по первым 6 строкам включая заголовок файла
#         if index > 5:
#             break
#         print(row)
#
# выводит:
# ['keywords', 'price', 'product_name']
# ['Садовый стул, стул для дачи', '1699', 'ВЭДДО']
# ['Садовый стул', '2999', 'ЭПЛАРО']
# ['Садовый табурет', '1699', 'ЭПЛАРО']
# ['Садовый стол', '1999', 'ТЭРНО']
# ['Складной стол, обеденный стол', '7499', 'ЭПЛАРО']