#  - re.search()
# ищет первое совпадение в строке
# re.search(pattern, string, flags=0)
#
# pattern - регулярное выражение
# string - строка, к которой нужно применить регулярное выражение
# flags - флаг
#
# Возвращаемое значение:
# Объект Match, если совпадение было найдено
# None, если нету совпадений
#
# import re
# pattern = r'\d{3}' # Поиск последовательности из трёх чисел в строке
# string = 'abc 123 def 456 fed 321 cba'
# result = re.search(pattern, string) # Ищет только одно вхождение, самое первое
# print(result) # <re.Match object; span=(4, 7), match='123'>