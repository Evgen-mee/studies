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


#  - fullmatch()
# определяет соответствие строки переданному шаблону.
# Если вся строка соответствует шаблону - выводит объект Match, иначе - None
# re.fullmatch(pattern, string, flags=0)
#
# pattern - регулярное выражение
# string - строка, к которой нужно применить регулярное выражение
# flags - флаг
#
# Возвращаемое значение:
# Объект Match, если вся строка соответствует шаблону
# None, если строка не соответствует шаблону
#
# print(re.fullmatch('\d', '111')) # None
# print(re.fullmatch('\d', '1'))   # <re.Match object; span=(0, 1), match='1'>


#  - finditer()
# возвращает итератор Match объектов с вхождениями pattern в строке string
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

