# - re.IGNORECASE
# При использовании флага регулярные выражения будут игнорировать регистр.
# Ищет все совпадения вне зависимости регистра ['привет', 'ПРИВЕТ', 'пРиВеТ']
# Сокращённая версия:
# re.I
#
# Встроенный флаг:
# (?i)
#
# Числовое представление: 2
#
# import re
# string = 'I like flags I LIKE FLAGS i like flags'
# test1 = re.findall(r'I like flags', string, flags=re.IGNORECASE)
# test2 = re.findall(r'I like flags', string, flags=re.I)
# test3 = re.findall(r'(?i)I like flags', string)
# print(test1)  # ['I like flags', 'I LIKE FLAGS', 'i like flags']
# print(test1 == test2 and test2 == test3)  # True
