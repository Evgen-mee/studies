# возвращает итератор, который последовательно генерирует элементы всех переданных итерируемых объектов

# упрощает обработку нескольких итерируемых объектов,
# не требуя предварительного конструирования объединенного списка

# Аргументы функции:
# *iterables — итерируемые объекты

# from itertools import chain
# chain_iter1 = chain('ABC', 'DEF')
# print(*chain_iter1)
#
# chain_iter2 = chain(enumerate('ABC'))
# print(*chain_iter2)
#
# for i in chain([1, 2, 3], ['a', 'b', 'c'], ('Timur', 29, 'Male', 'Teacher')):
#     print(i, end=' ')
#
# выводит:
# A B C D E F
# (0, 'A') (1, 'B') (2, 'C')
# 1 2 3 a b c Timur 29 Male Teacher