# Конструкция match/case
# cmd = "right"
# match cmd:
#     case "right":
#         print("Вправо")
#     case "left" | "Прямо": # | выступает или
#         print("Влево или прямо")
#     case _:
#         print("нет совпадений")
#
#
# match cmd:
#     # до case command можем писать case  с проверками case "Left":
#     case command: # если не было переменной ранее то в command присвоиться cmd
#         print(f"команда {command}")
#         # дальше смысла писать case нет тк первый блок перехватит все
#
#
# match cmd:
#     case str() as command: # проверка евляется ли cmd строкой command создается после проверки
#         # или можем написать так case str(command)
#         print(f"это строка{command}")
#     case int() | float() as command if 0 <= command <= 9: #добавили проверку на диапозон
#         print(f"это число в диапозоне от 0 до 9{command}")
#     case _:
#         print("нет совпадений")
#
#
#
# # Конструкция match/case с кортежами и списками
# cmd = ("Балакирев", "pyton", 2000.70)
# match cmd:
#     case tuple() as book: # проверка на кортеж
#         print(f"кортеж {book}")
#
# match cmd:
#     case author, title, price: # распаковали кортеж в 3 переменные СРАБОТАЕТ ТОЛЬКО ЕСЛЕ колличество переменных совпадает
#         # есле кортеж больше а нам нужно первые 3 значения author, title, price,*_ ЗВЕЗДОЧКА
#         print(f"книга {author}, {title}, {price}")
#
# match cmd: # скобки просто групируют для читаемости
#     case (str() as author, str() as title, float() | int() as price, *_ ) if len(cmd) < 6 :
#         # проверка на длину коллекции и типов при распаковке
#         print(f"книга {author}, {title}, {price}")
#
# # есле мы уверенны что может на вход прийти коллекция с 3 или 5 значениями
# # можем воспользоваться или | подстановка произайдет автоматически
# # НО название переменных должно быть одно и то же author, title, price
# match cmd:
#     case (author, title, price, ) | (_, author, title, price,_ ) :
#         # проверка на длину коллекции и типов при распаковке
#         print(f"книга {author}, {title}, {price}")
#



# Конструкция match/case со словарями и множествами
# request ={"ключ1":"значение 1", "ключ2" :"значение 2"," ключ2":"значение 2","ключ2":"значение 2"}
#
# match request: # при {} ожидает ключ значение
#     case {"url":url, "method": method}:# два ключа с произвольными значниями
#
# match request:  # при {} ожидает ключ значение
#     case {"url": str(url), "method": int(method)}:  # проверка на тип данных
#
# match request:  # при {} ожидает ключ значение
#     case {"url": str(url), "ключ2" :"значение 2" | "значение 3" }:  # сработает только если во втором параметре совпадет ключ значение
#
# match request:  #
#     case {"url": url, "method": method, **kwasrgs} if not kwargs:  # проверка на то что в словаре только 2 ключа
data = {'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}]}

match data:
    case {'access': access, 'data': [date, *_]} if type(access) is bool and type(data) is list:
        print(access, type(date))
    case _:
        print("NO")
