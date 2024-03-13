# генераторные выражения подходят,
# когда код тела генераторной функции можно записать в одно выражение.
# в генераторных выражениях используются круглые скобки, а не квадратные.
#
# Генераторные выражения нельзя писать без скобок – это синтаксическая ошибка
#
# При передаче генераторного выражения в функцию в качестве единственного аргумента скобки можно опускать
#
# Нельзя распечатать элементы генераторного выражения с помощью функции print(), без предварительной распаковки.
#
#
# Python поддерживает четыре вида генераторов:
#
# генераторы списков (list comprehension)
# new_list = [выражение for элемент in последовательность if условие]
#
# генераторы множеств (set comprehension)
# new_set = {выражение for элемент in последовательность if условие}
#
# генераторы словарей (dict comprehension)
# new_dict = {ключ:значение for (ключ,значение) in dict.items() if условие}
#
# генераторные выражения (generator expressions, а не tuple comprehensions).
# new_gen = (выражение for элемент in последовательность if условие)
#
#
# from sys import getsizeof
# numbers = [1, 9, 8, 7, 90, -56, -34, 56, 100, 90, 2, 8]
# even_numbers = (num for num in numbers if num % 2 == 0)         # используем круглые скобки
# print(type(even_numbers))         # <class 'generator'>
# print(even_numbers)               # <generator object <genexpr> at 0x0000020E9C767300>
# print(getsizeof(even_numbers))    # 104
#
# squares = (i ** 2 for i in range(1, 7))         # создаем генератор с помощью генераторного выражения
# capitals = (s.upper() for s in 'abc')           # создаем генератор с помощью генераторного выражения
# stars = ('*' for i in range(5))                 # создаем генератор с помощью генераторного выражения
# for num in squares:
#     print(num)
# print(next(capitals))
# print(*stars, end=' ')
#
# выводит:
# 1
# 4
# 9
# 16
# 25
# 36
# A
# * * * * *
#
# В отличие от генераторных выражений,
# генераторные функции более универсальны не только из-за произвольного количества кода в их теле
# В них можно передавать разные значения аргументов
#
#
# Генераторные выражения нельзя писать без скобок – это синтаксическая ошибка
#
# При передаче генераторного выражения в функцию в качестве единственного аргумента скобки можно опускать
# print(sum(i*i for i in range(10)))          # передача без скобок
# print(sum((i*i for i in range(10))))        # передача со скобками
#
# Согласно PEP8 – то, что указано в скобках, можно переносить.
# Значит, генераторные выражения можно записывать так, чтобы их было удобно читать
# even_squares = (
#                 i ** 2
#                 for i in range(10)
#                 if i % 2 == 0
#                )
#
#
# #filter map
# Генераторные выражения занимают немного больше памяти,
# чем соответствующие аналоги map(), filter() с лямбда функциями.
# ВМЕСТО
# fruits = ['apple', 'apricot', 'avocado', 'pineapple', 'banana', 'bergamot', 'durian', 'grapefruit']
# fruits_filter = filter(lambda s: len(s) > 7, fruits)
# fruits_map = map(lambda s: s.upper(), fruits)
# fruits_filter_map = map(lambda s: s.upper(), filter(lambda s: len(s) > 7, fruits))
# МОЖНО
# fruits = ['apple', 'apricot', 'avocado', 'pineapple', 'banana', 'bergamot', 'durian', 'grapefruit']
# fruits_filter = (s for s in fruits if len(s) > 7)
# fruits_map = (s.upper() for s in fruits)
# fruits_filter_map = (s.upper() for s in fruits if len(s) > 7)
#
#
# Генераторные выражения и генераторные функции являются, как правило, взаимозаменяемыми.
# # Генераторная функция
# def do_something(elements):
#     for item in elements:
#         yield some_operation(item)
#
# может быть записана в виде функции,
# возвращающей генератор с помощью генераторного выражения:
# def do_something(elements):
#     return (some_operation(item) for item in elements)
#
# # генераторная функция
# def trim_line_endings(lines):     # принимает открытый текстовый файл
#     for line in lines:
#         yield line.rstrip('\n')   #  возвращает генератор строк переданного файла без символа \n
#
# # функции, возвращающей генератор с помощью генераторного выражения
# def trim_line_endings(lines):
#     return (line.rstrip('\n') for line in lines)


# def interleave(*args):
#    return (i for el in zip(*args) for i in el)
#
#
#
# numbers = [1, 2, 3]
# squares = [1, 4, 9]
# qubes = [1, 8, 27]
#
# print(*interleave(numbers, squares, qubes))

