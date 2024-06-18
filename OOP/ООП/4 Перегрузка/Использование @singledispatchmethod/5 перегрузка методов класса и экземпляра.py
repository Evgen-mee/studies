# можно перегружать любые методы в классе, будь то методы экземпляра,
# методы класса или статические методы.



# from functools import singledispatchmethod
# class MyClass:
#     @singledispatchmethod
#     def method(self, arg):
#         print('Базовая реализация метода экземпляра')
#
#     @method.register(int)                                     # перегружаем метод экземпляра
#     def _method(self, arg):
#         print('Реализация метода экземпляра для целочисленного аргумента')
#
#     @singledispatchmethod
#     @classmethod
#     def class_method(cls, arg):
#         print('Базовая реализация метода класса')
#
#     @class_method.register(str)                               # перегружаем метод класса
#     @classmethod
#     def _class_method(cls, arg):
#         print('Реализация метода класса для строкового аргумента')
#
#     @singledispatchmethod
#     @staticmethod
#     def static_method(arg):
#         print('Базовая реализация статического метода')
#
#     @static_method.register(list)                             # перегружаем статический метод
#     @staticmethod
#     def _static_method(arg):
#         print('Реализация статического метода для списочного аргумента')
#
#
# obj = MyClass()
#
# obj.method('bee')                      # Базовая реализация метода экземпляра
# obj.method(1)                          # Реализация метода экземпляра для целочисленного аргумента
# print()
#
# obj.class_method(1)                    # Базовая реализация метода класса
# obj.class_method('bee')                # Реализация метода класса для строкового аргумента
# print()
#
# obj.static_method(1)                   # Базовая реализация статического метода
# obj.static_method(['b', 'e', 'e'])     # Реализация статического метода для списочного аргумента
# выводит:
#
#
#
#
#
#
#
