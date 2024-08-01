# request = {'url': 'https://proproprogs.ru/', 'method': 'GET', 'timeout': 1000}
#
# match request:
#     # фигурные скобки означают что ждем словарь {}, если подать НЕ словарь то case не выполниться
#     # и распаковываем ключ значение 'url': url
#     # если нет ключей в словаре то данный case не выполниться
#     case {'url': str(url), 'method': str(method)}:             # проверяем ключи на тип
#         print(f"Запрос: url: {url}, method: {method}")         # выводим значения указанных ключей
#
#     # принимаем любое значение по ключу                          'url': url
#     # принимаем любое значение типа str                          'url': str(url)
#     # принимаем только конкретное значение по конкретному ключу  'timeout': 1000
#     # принимаем НЕСКОЛЬКО значений по конкретному ключу  'timeout': 1000 | 2000
#     case {'url': 'https://proproprogs.ru/', 'method': method}:
#         print(f"Запрос: url: {url}, method: {method}")         # выводим значения указанных ключей
#
#     # проверяем на то что словарь конкретной длины
#     case {'url': 'https://proproprogs.ru/', 'method': method} if len(request) > 4:
#         print(f"Запрос: url: {url}, method: {method}")         # выводим значения указанных ключей
#
#     # проверяем на то что словарь имеет еще 3 ключа кроме используемых
#     # записываем оставшиеся ключи в **kwarg
#     # и проверяем их длину
#     case {'url': 'https://proproprogs.ru/', 'method': method, **kwargs} if len(kwargs) > 4:
#         print(f"Запрос: url: {url}, method: {method}")         # выводим значения указанных ключей
#
#
#     case _:  # wildcard
#         print("неверный запрос")
#
#
# # МНОЖЕСТВО
# primary_keys = {1, 2, 3}
#
# match primary_keys:
#     case set() as keys:
#         print(f"Primary Keys: {keys}")
#     case _:  # wildcard
#         print("неверный запрос")