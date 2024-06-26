# Если методы __int__(), __float__() и __complex__() не определены,
# соответствующие функции будут обращаться к методу __index__()
# который указывает на то, что объект имеет целочисленный тип
# Этот метод должен возвращать целое число, которое и будет передаваться в эти функции.
# Наличие этого метода у класса так же позволяет применять к экземпляру этого класса функции преобразования
# в другую систему счисления, такие как bin(), oct() и hex()

# class Angle:
#     def __init__(self, value):
#         self.value = value
#
#     def __index__(self):   # __index__() отработает если вернуть только ЦЕЛОЕ число
#         print('Вызов метода __index__()')
#         return self.value
#
#
# angle = Angle(100)
#
# print(int(angle))     # 100
# print(float(angle))   # 100.0
# print(bin(angle))     # 0b1100100
# print(oct(angle))     # 0o144
# print(hex(angle))     # 0x64