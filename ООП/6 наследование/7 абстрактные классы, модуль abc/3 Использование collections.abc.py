# Абстрактные базовые классы модуля  полезны при создании пользовательских классов,
# которые работают как последовательности (tuple, str, list), множества (set), отображения (dict) и т.д.

# Иногда вместо наследования от встроенных типов tuple, str, set, list, dict
# куда проще реализовать соответствующий интерфейс

# достаточно реализовать абстрактные методы
# методы мексины определяться самостоятельно!!!!
# СМОТРИ ТАБЛИЦУ!!!

# неизменяемое множество, основанное на списке
# from collections.abc import Set
# class ListBasedSet(Set):
#     def __init__(self, iterable):
#         lst = []
#         for value in iterable:
#             if value not in lst:
#                 lst.append(value)
#         self.elements = lst
#
#     def __iter__(self):
#         return iter(self.elements)
#
#     def __contains__(self, value):
#         return value in self.elements
#
#     def __len__(self):
#         return len(self.elements)
#
#     def __repr__(self):
#         return f'{type(self).__name__}({self.elements})'
#
# s1 = ListBasedSet('abcdef')
# s2 = ListBasedSet('defghi')
#
# print(s1 | s2)  # ListBasedSet(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
# print(s1 & s2)  # ListBasedSet(['d', 'e', 'f'])
# print(s1 - s2)  # ListBasedSet(['a', 'b', 'c'])

