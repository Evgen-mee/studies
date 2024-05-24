#  - finditer()
# возвращает  в строке string
# re.finditer(pattern, string, flags=0)
#
# pattern - регулярное выражение
# string - строка, к которой нужно применить регулярное выражение
# flags - флаг
#
# Возвращаемое значение:
# Итератор Match объектов
#
# import re
# pattern = r'\d{3}'
# string = 'abc 123 def 456 fed 321 cba'
# result = re.finditer(pattern, string, 0)
# for i in result:
#     print(i)
# будет выведено:
# <re.Match object; span=(4, 7), match='123'>
# <re.Match object; span=(12, 15), match='456'>
# <re.Match object; span=(20, 23), match='321'>