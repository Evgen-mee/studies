# создает файл countries.json и сохраняет в него информацию из словаря data в json формате
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
#
# with open('countries.json', 'w') as file:
#     json.dump(data, file)


# ensure_ascii
# ДЛЯ РАБОТЫ С РУССКИМ ЯЗЫКОМ
# import json
# data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
# s = json.dumps(data, ensure_ascii=False)
# print(s)
# result = json.loads(s)
# print(result)
# выводит:
# {"firstName": "Тимур", "lastName": "Гуев"}
# {'firstName': 'Тимур', 'lastName': 'Гуев'}
#
# Если не использовать то получим:
# import json
# data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
# s = json.dumps(data)
# print(s)
# result = json.loads(s)
# print(result)
# выводит:
# {"firstName": "\u0422\u0438\u043c\u0443\u0440", "lastName": "\u0413\u0443\u0435\u0432"}
# {'firstName': 'Тимур', 'lastName': 'Гуев'}


# indent
# задает отступ от левого края
# По умолчанию имеет значение None
#Если значением indent является строка, то она используется в качестве отступа!!!!
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data1 = json.dumps(data, indent=2)
# json_data2 = json.dumps(data, indent='++++')
# print(json_data1)
# print(json_data2)
#
# выводит:
# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "currency": "RUB"
# }
# {
# ++++"name": "Russia",
# ++++"phone_code": 7,
# ++++"capital": "Moscow",
# ++++"currency": "RUB"
# }

# sort_keys
# задает сортировку ключей в результирующем json
# при установки True, ключи будут отсортированы в алфавитном порядке
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data1 = json.dumps(data, indent=3)
# json_data2 = json.dumps(data, indent=3, sort_keys=True)
# print(json_data1)
# print(json_data2)
# выводит:
# {
#    "name": "Russia",
#    "phone_code": 7,
#    "capital": "Moscow",
#    "currency": "RUB"
# }
# {
#    "capital": "Moscow",
#    "currency": "RUB",
#    "name": "Russia",
#    "phone_code": 7

# Аргумент separators
# меняет стандартные разделитили : ,
# задает кортеж, состоящий из двух элементов (item_separator, key_separator)
# которые представляют разделители для элементов и ключей
# По умолчанию аргумент имеет значение (', ', ': ')
# import json
# data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
# json_data = json.dumps(data, indent=3, separators=(';', ' = '))
# print(json_data)
# выводит:
# {
#    "name" = "Russia";
#    "phone_code" = 7;
#    "capital" = "Moscow";
#    "currency" = "RUB"
# }