#  - Ограничение по типам данных
# В формат JSON нельзя записать словарь, у которого ключи – кортежи.

# - skipkeys
# позволяет игнорировать кортежи при записи в json
# import json
# ДатаВремя = {
#         'beegeek': 2018,
#         ('Timur', 'Guev'): 29,
#         ('Arthur', 'Kharisov'): 20,
#         'stepik': 2013
#        }
# json_data = json.dumps(ДатаВремя, skipkeys=True)      # преобразуем dict в json пропуская кортежи
# print(json_data) == {"beegeek": 2018, "stepik": 2013} # записали без кортежей

# если в словаре Python использовались числа, булевы значения или None,
# то ошибки не будет, вместо этого они будут преобразованы в строки.
# import json
# ДатаВремя = {1: 'Timur', False: 'Arthur', None: 'Ruslan'}
# json_data = json.dumps(ДатаВремя)
# print(json_data) == {"1": "Timur", "false": "Arthur", "null": "Ruslan"}