# data.json (пример файла)
# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "cities": ["Abakan", "Almetyevsk", "Anadyr", "Anapa", "Arkhangelsk", "Astrakhan"],
#   "currency": "RUB"
# }

# import json
# with open('data.json') as file:
#     data = json.load(file)                # передаем файловый объект
#     for key, value in data.items():       # получаем ключ значение
#         if type(value) == list:           # проверка на тип
#             print(f'{key}: {", ".join(value)}')
#         else:
#             print(f'{key}: {value}')
# выведит:
# name: Russia
# phone_code: 7
# capital: Moscow
# cities: Abakan, Almetyevsk, Anadyr, Anapa, Arkhangelsk, Astrakhan
# currency: RUB