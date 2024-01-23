#  - loads() для строк
# Переводит строку json в код
# Для десериализации данных
# принимает аргумент строка с данными в формате json
#
# import json
# json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}' # строка json
# data = json.loads(json_data)       # преобразуем строку json в словарь пайтона
# print(type(data)) == <class 'dict'>
# print(data)       == {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
#
#
# - load() для файлов
# принимает файловый объект и возвращает его десериализованное содержимое
#
# data.json имеет следующее содержимое:
#
# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "cities": ["Abakan", "Almetyevsk", "Anadyr", "Anapa", "Arkhangelsk", "Astrakhan"],
#   "currency": "RUB"
# }
#
# читает содержимое data.json файла в словарь data и выводит его содержимое
# import json
# with open('data.json') as file:
#     data = json.load(file)                # передаем файловый объект который преобразовался в словарь
#     for key, value in data.items():       # получаем ключ значение из inema
#         if type(value) == list:           # есле значение list
#             print(f'{key}: {", ".join(value)}')  # то делаем из списка строку и выводим
#         else:
#             print(f'{key}: {value}')
#
# выведет:
# name: Russia
# phone_code: 7
# capital: Moscow
# cities: Abakan, Almetyevsk, Anadyr, Anapa, Arkhangelsk, Astrakhan
# currency: RUB