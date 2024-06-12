# возвращает итератор, циклично генерирующий последовательность элементов переданного итерируемого объекта.

# Аргументы функции:
# iterable — итерируемый объект

# охраняет копию каждого элемента из iterable.
# Когда итерируемый объект iterable исчерпан, функция начинает возвращать элементы из сохраненной копии.

# from itertools import cycle
#
# for index, char in enumerate(cycle('abcd')):
#     if index < 7:
#         print(char)
#     else:
#         break
#
# cycle_iter = cycle([0, 1])
# print(next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter))
#
# for i in zip(range(7), cycle(['a', 'b', 'c'])):
#     print(i)
# выводит:
#
# a
# b
# c
# d
# a
# b
# c
# 0 1 0 1 0
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'a')
# (4, 'b')
# (5, 'c')
# (6, 'a')