# имеет структуру ключ-значение
# в формате JSON используются только двойные кавычки!!!!!!!

# ключи в json могут быть только строками, заключенными в двойные кавычки
# если в словаре Python использовались числа, булевы значения или None,
# то ошибки не будет, вместо этого они будут преобразованы в строки.

# Значениями в json могут быть числа, списки значений, литералы true/false/null,вложенные объекты
#
# {
#    "firstName": "Тимур",
#    "lastName": "Гуев",
#    "address": {
#        "streetAddress": "Часовая 25, кв. 127",
#        "city": "Москва",
#        "postalCode": 125315                           #значение = число
#    },
#    "phoneNumbers": ["+7 (919) 424-84-34", "+7 (916) 928-92-34"]
# }
#
# - сериализация в файл
# - десериализация из файла в код


#  - Типы данных в json
# модуль json автоматически определяет тип значения при десериализации
# НО данные не всегда будут того же типа, что исходные данные в Python!!!!

# Таблица конвертации типов данных Python в JSON:
# Python     |	JSON
# dict       | 	object
# list,tuple | 	array
# str 	     |  string
# int, float | 	number
# True 	     |  true
# False 	 |  false
# None 	     |  null
#
# Таблица конвертации JSON в типы данных Python:
# JSON 	      |    Python
# object 	  |    dict
# array 	  |    list
# string 	  |    str
# number(int) |    int
# number(real)|    float
# true 	      |    True
# false 	  |    False
# null 	      |    None


#  - Ограничение по типам данных
# В формат JSON нельзя записать словарь, у которого ключи – кортежи.
#
# - skipkeys
# позволяет игнорировать кортежи при записи в json
# import json
# data = {
#         'beegeek': 2018,
#         ('Timur', 'Guev'): 29,
#         ('Arthur', 'Kharisov'): 20,
#         'stepik': 2013
#        }
# json_data = json.dumps(data, skipkeys=True)        # преобразуем dict в json пропуская кортежи
# print(json_data) == {"beegeek": 2018, "stepik": 2013} # записали без кортежей
#
#
# если в словаре Python использовались числа, булевы значения или None,
# то ошибки не будет, вместо этого они будут преобразованы в строки.
# import json
# data = {1: 'Timur', False: 'Arthur', None: 'Ruslan'}
# json_data = json.dumps(data)
# print(json_data) == {"1": "Timur", "false": "Arthur", "null": "Ruslan"}


#  - Кириллические символы в json
# import json
# data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
# s = json.dumps(data)
# print(s)
# result = json.loads(s)
# print(result)
# выводит:
# {"firstName": "\u0422\u0438\u043c\u0443\u0440", "lastName": "\u0413\u0443\u0435\u0432"}
# {'firstName': 'Тимур', 'lastName': 'Гуев'}
#
# ensure_ascii функций dumps() и dump()
# import json
# data = {'firstName': 'Тимур', 'lastName': 'Гуев'}
# s = json.dumps(data, ensure_ascii=False)           # задали не обязательный аргумент для корректной работы с кирилицей
# print(s)
# result = json.loads(s)
# print(result)
# выводит:
# {"firstName": "Тимур", "lastName": "Гуев"}
# {'firstName': 'Тимур', 'lastName': 'Гуев'}
