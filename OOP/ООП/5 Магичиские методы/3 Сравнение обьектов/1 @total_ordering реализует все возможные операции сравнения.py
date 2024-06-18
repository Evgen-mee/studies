# позволяет определить в классе лишь метод __eq__()
# и один из методов __lt__(), __le__(), __gt__() или __ge__().
# Все недостающие методы декоратор определит и реализует самостоятельно.

# ПОСЛЕ ОПРЕДЕЛЕНИЯ НАЧИНАЕТ РАБОТАТЬ min() max() sort()

# from functools import total_ordering
#
#
# @total_ordering
# class Fruit:
#     def __init__(self, name, mass):
#         self.name = name
#         self.mass = mass
#
#     def __eq__(self, other):
#         if isinstance(other, Fruit):
#             return self.mass == other.mass
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Fruit):
#             return self.mass < other.mass
#         return NotImplemented
#

