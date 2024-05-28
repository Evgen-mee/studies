# - compile()
#
# уменьшить количество кода, если одно регулярное выражение используется несколько раз
# увеличить производительность кода, если одно регулярное выражение используется несколько раз
#
# re.compile(pattern, flags=0)
# метод, который позволяет вручную компилировать регулярные выражения.
#
# pattern - регулярное выражение
# flags - флаги, пройдём позже
#
# Возвращаемое значение:
# Объект Pattern - скомпилированное регулярное выражение
#
#
# import re
# regex = re.compile(r'[a-zA-Z]{1,}') # Записали в регулярку
# print(regex)  # re.compile('[a-zA-Z]{1,}')
#
# # Теперь можно использовать методы:
# print(regex.findall('Some words.'))  # ['Some', 'words'] # Вызываем метод, регулярку не передаем т.к. она вшита
# print(regex.sub('deleted', 'Some words again.'))  # deleted deleted deleted.


# После компиляции регулярного выражения, функция re.compile() возвращает объект Pattern
# можно обратиться ко всем функция из модуля re
#
# Атрибуты
#  - pattern.flags
# Каждый флаг - хранится как какое-либо число. pattern.flags возвращает сумму этих чисел:
# print(pattern.flags) # 32
#
#  - pattern.groups
# Возвращает количество групп в регулярном выражении:
# print(pattern.groups) # 1
#
#  - pattern.groupindex
# Возвращает словарь, в котором ключи - именованные группы, а значения - номера этих групп:
# print(pattern.groupindex) # {'group1': 1}
#
#  - pattern.pattern
# Возвращает регулярное выражение:
# print(pattern.pattern) # (?P<group1>[a-zA-Z]{1,})
#
#
# Методы
# Благодаря объекту Pattern в методах
# search(), match(), fullmatch(), finditer(), findall()
# появляются дополнительные параметры:
#
# pos - позволяет указывать индекс в строке, с которого надо начать искать совпадение
# endpos - указывает, до какого индекса надо выполнять поиск
#
# import re
# pattern = re.compile(r'(?P<group1>[a-zA-Z]{1,})')
# match1 = pattern.match("Some words.", 4) # None
# match2 = pattern.match("Some words.", 5) # words


