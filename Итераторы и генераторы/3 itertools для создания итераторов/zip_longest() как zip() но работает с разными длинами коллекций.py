# Аргументы функции:
# *iterables — итерируемые объекты
# fillvalue — заполнитель, по умолчанию имеет значение None


# from itertools import zip_longest
# print(*zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))
# print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))                     # fillvalue=None
# print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue='*'))
# print(*zip_longest(['a', 'b', 'c', 'd', 'e'], [1, 2, 3], fillvalue=777))
# выводит:
#
# (1, 'a') (2, 'b') (3, 'c')
# (1, 'a') (2, 'b') (3, 'c') (None, 'd') (None, 'e')
# (1, 'a') (2, 'b') (3, 'c') ('*', 'd') ('*', 'e')
# ('a', 1) ('b', 2) ('c', 3) ('d', 777) ('e', 777)