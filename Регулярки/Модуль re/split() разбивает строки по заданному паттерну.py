#  - split()
# разбивает строки по заданному паттерну УКАЗЫВАЕМ РАЗДЕЛИТЕЛЬ
# re.split(pattern, string, maxsplit=0, flags=0)
#
# pattern - регулярное выражение
# string - строка, к которой нужно применить регулярное выражение
# maxsplit - максимальное количество делений строки
# flags - флаги
#
# Возвращаемое значение:
# Если совпадения есть - список частей разделённой строки.
# [string], если совпадений нет
#
#
# import re
# pattern = r'\s\d{3}\s'
# string = 'abc 123 def 456 fed 321 cba'
# result = re.split(pattern, string) # Если совпадения есть, то разделит строку на части
# print(result) # ['abc', 'def', 'fed', 'cba']
#
#
# import re
# pattern = r'\s\d{3}\s'
# string = 'abc 123 def 456 fed 321 cba'
# result = re.split(pattern, string, 2)
# передали число в maxsplit что бы разделить строку на нужное колличество
# после указанного деления дальше идет остаток строки
# print(result) # ['abc', 'def', 'fed 321 cba']
#
#
# import re
# pattern = r'123'
# string = '456'
# result = re.split(pattern, string) #Если совпадений нет, то функция вернёт [string]
# print(result) # ['456']