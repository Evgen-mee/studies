# __le__() отвечает за сравнение на меньше
# __ge__() отвечает за сравнение на больше

# выражение obj1 <= obj2 равносильно вызову obj1.__le__(obj2)
# выражение obj1 >= obj2 равносильно вызову obj1.__ge__(obj2)

# МОЖНО ИСПОЛЬЗОВАТЬ ОДИН МЕТОД ВТОРОЙ РЕАЛИЗУЕТСЯ АВТОМАТИЧЕСКИ!!!!


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
#     def __le__(self, other):                # сравнение на больше или равно
#         if isinstance(other, Fruit):
#             return self.mass <= other.mass
#         return NotImplemented
#
#     def __ge__(self, other):              # сравнение на меньше или равно
#         if isinstance(other, Fruit):
#             return self.mass >= other.mass
#         return NotImplemented
#
#
# fruit1 = Fruit('банан', 150)
# fruit2 = Fruit('яблоко', 180)
# fruit3 = Fruit('груша', 150)
#
# print(fruit1 <= fruit2)       # True
# print(fruit1 >= fruit2)       # False
# print(fruit1 <= fruit3)       # True
# print(fruit1 >= fruit3)       # True