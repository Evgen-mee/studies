# __lt__() отвечает за сравнение на меньше
# __gt__() отвечает за сравнение на больше

# МОЖНО ИСПОЛЬЗОВАТЬ ОДИН МЕТОД ВТОРОЙ РЕАЛИЗУЕТСЯ АВТОМАТИЧЕСКИ!!!!

# ПОСЛЕ ОПРЕДЕЛЕНИЯ МЕТОДОВ НАЧИНАЕТ РАБОТАТЬ min() max() sort()

# выражение obj1 < obj2 равносильно вызову obj1.__lt__(obj2)
# выражение obj1 < obj2 равносильно вызову obj1.__gt__(obj2)

# методы для сравнения на больше/меньше необходимо реализовывать самостоятельно, и если этого не сделать,
# при попытке сравнения двух объектов на больше/меньше будет возбуждено исключение.

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
#     def __lt__(self, other):                   # сравниваем на меньше
#         if isinstance(other, Fruit):
#             return self.mass < other.mass
#         return NotImplemented
#
#     def __gt__(self, other):                  # сравниваем на больше
#         if isinstance(other, Fruit):
#             return self.mass > other.mass
#         return NotImplemented
#
#
# fruit1 = Fruit('банан', 150)
# fruit2 = Fruit('яблоко', 180)
#
# print(fruit1 < fruit2)  # True
# print(fruit1 > fruit2)  # False
# print(fruit2 < fruit1)  # False
# print(fruit2 > fruit1)  # True