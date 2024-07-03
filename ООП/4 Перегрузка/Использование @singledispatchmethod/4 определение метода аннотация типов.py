# мы не можем использовать абстрактные типы из модуля typing


# from functools import singledispatchmethod
# class MyClass:
#     @singledispatchmethod
#     def base_implementation(self, arg):
#         print('Базовая реализация')
#
#     @base_implementation.register
#     def intfloat_implementation(self, arg: int | float):
#         print('Реализация для целочисленного и вещественного аргументов')
#
#
# obj = MyClass()
#
# obj.base_implementation(1)    # Реализация для целочисленного и вещественного аргументов
# obj.base_implementation(1.0)  # Реализация для целочисленного и вещественного аргументов