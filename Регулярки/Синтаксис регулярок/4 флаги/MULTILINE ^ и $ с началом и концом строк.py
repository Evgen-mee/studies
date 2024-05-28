#  - re.MULTILINE
# При использовании флага спецсимволы ^ и $
# будут совпадать не с началом и концом всего текста, а с началом и концом строк.
#
# ищет совпадение по строкам, строка за строкой, ОТ НАЧАЛА И ДО КОНЦА ЗНАКА ПЕРЕНОСА СТРОКИ
#
# Сокращённая версия:
# re.M
#
# Встроенный флаг:(?m)
#
# Числовое представление:8
#
#
# import re
# string = '''I like flags
# I like flags
# I like flags
# '''
# test1 = re.findall(r'^I like flags$', string, flags=re.MULTILINE) # ищет совпадение по строкам
# test2 = re.findall(r'^I like flags$', string, flags=re.M)
# test3 = re.findall(r'(?m)^I like flags$', string) # ищет совпадение со всем текстом
#
# print(test1)  # ['I like flags', 'I like flags', 'I like flags']
# print(test1 == test2 and test2 == test3)  # True