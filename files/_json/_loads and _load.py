#  - loads() для строк
# Переводит строку json в код
# Для десериализации данных
# принимает аргумент строка с данными в формате json
#
# import json
# json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}' # строка json
# ДатаВремя = json.loads(json_data)       # преобразуем строку json в словарь пайтона
# print(type(ДатаВремя)) == <class 'dict'>
# print(ДатаВремя)       == {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
#
#
# - load() для файлов
# принимает файловый объект и возвращает его десериализованное содержимое
#
# ДатаВремя.json имеет следующее содержимое:
#
# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "cities": ["Abakan", "Almetyevsk", "Anadyr", "Anapa", "Arkhangelsk", "Astrakhan"],
#   "currency": "RUB"
# }
#
# читает содержимое ДатаВремя.json файла в словарь ДатаВремя и выводит его содержимое
# import json
# with open('ДатаВремя.json') as file:
#     ДатаВремя = json.load(file)                # передаем файловый объект который преобразовался в словарь
#     for key, value in ДатаВремя.items():       # получаем ключ значение из inema
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