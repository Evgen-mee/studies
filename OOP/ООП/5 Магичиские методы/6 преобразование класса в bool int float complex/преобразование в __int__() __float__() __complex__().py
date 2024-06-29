#  - __int__() — определяет поведение экземпляра при передаче в функцию int().
# Метод должен возвращать значение, соответствующее преобразованию экземпляра в тип int

#  - __float__() — определяет поведение экземпляра при передаче в функцию float().
# Метод должен возвращать значение, соответствующее преобразованию экземпляра в тип float

#  - __complex__() — определяет поведение экземпляра при передаче в функцию complex().
# Метод должен возвращать значение, соответствующее преобразованию экземпляра в тип complex



# class Angle:
#     def __init__(self, value):
#         self.value = value
#
#     def __int__(self):
#         return int(self.value)
#
#     def __float__(self):
#         return float(self.value)
#
#
# angle1 = Angle(100)
# angle2 = Angle(100.1)
#
# print(int(angle1))     # 100
# print(int(angle2))     # 100
# print(float(angle1))   # 100.0
# print(float(angle2))   # 100.1
