# - dumps()
# Для сериализации данных в json
# преобразование данных в строку
# Все данные будут str
#
# в результирующую строку всегда попадают двойные кавычки
#
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data = json.dumps(data)                       # сериализуем словарь data в json строку
# print(type(json_data)) ==  <class 'str'>
# print(json_data)  == {"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}
#
#
# - dump()
# создает файл
# записывает переданный Python объект в файл
#
# Типы данных хроняться согласно переданным
# т.е. словарь data , будет иметь как значения int так и str
#
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# with open('countries.json', 'w') as file:
#     json.dump(data, file)
#
# создает файл countries.json и сохраняет в него информацию из словаря data в json формате.


# indent, sort_keys и separators ДЛЯ dumps() и dump()
#
# -Аргумент indent
# задает отступ от левого края
# По умолчанию имеет значение None
# В indent можно передать строку!!               # indent = "++++" 4 плюса с лева
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data1 = json.dumps(data, indent=2)         # указали 2 отступа от левого края
#
#
# - Аргумент sort_keys
# задает сортировку ключей в результирующем json
# сортирует ключи в алфавитном порядке
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data2 = json.dumps(data, indent=3, sort_keys=True)          # отсортировали ключи
#
#
# Аргумент separators
# меняет стандпртные разделитили : ,
# задает кортеж, состоящий из двух элементов (item_separator, key_separator)
# которые представляют разделители для элементов и ключей
# По умолчанию аргумент имеет значение (', ', ': ')
#
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data = json.dumps(data, indent=3, separators=(';', ' = '))     # заменили , на ; и : на =
# print(json_data) = {"name" = "Russia"; "phone_code" = 7; "capital" = "Moscow"; "currency" = "RUB"}
