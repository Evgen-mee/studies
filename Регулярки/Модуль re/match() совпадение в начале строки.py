#  - re.match()
# ищет совпадение в начале строки
# re.match(pattern, string, flags=0)
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
# string = '123 abc 456 def 654 cba 321'
# result = re.match(pattern, string) # Ищет только одно вхождение в начале строки
# print(result) # <re.Match object; span=(0, 3), match='123'>