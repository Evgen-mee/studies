#  - findall()
# возвращает список всех найденных совпадений
# re.findall(pattern, string, flags=0)
# #
# pattern - регулярное выражение
# string - строка, к которой нужно применить регулярное выражение
# flags - флаги
#
# Возвращаемое значение:
# Список совпадений, если они есть
# Пустой список, если совпадений нет
#
# import re
# pattern = r'\d{3}'
# string = 'abc 123 def 456 fed 321 cba'
# result = re.findall(pattern, string)
# print(result) # ['123', '456', '321']