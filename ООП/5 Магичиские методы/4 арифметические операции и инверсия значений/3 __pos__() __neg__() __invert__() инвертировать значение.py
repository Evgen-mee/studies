# __pos__() — определяет поведение для унарного плюса
# __neg__() — определяет поведение для унарного минуса
# __invert__() — определяет поведение для оператора инвертирования

# Из встроенных типов оператор инвертирования ~
# определен лишь для типов int и bool.
# Значение выражения ~x определяется как -(x + 1)

# class Angle:
#     def __init__(self, value):
#         self.value = value                       # градусная мера угла
#
#     def __repr__(self):
#         return f'Angle({self.value})'
#
#     def __pos__(self):
#         return Angle(self.value)
#
#     def __neg__(self):
#         return Angle(-self.value)
#
#     def __invert__(self):
#         if 0 <= self.value <= 180:
#             return Angle(180 - self.value)
#         return Angle(180 + self.value)
#
#
# angle = Angle(100)
#
# print(+angle)   # Angle(100)
# print(-angle)   # Angle(-100)
# print(~angle)   # Angle(80)


