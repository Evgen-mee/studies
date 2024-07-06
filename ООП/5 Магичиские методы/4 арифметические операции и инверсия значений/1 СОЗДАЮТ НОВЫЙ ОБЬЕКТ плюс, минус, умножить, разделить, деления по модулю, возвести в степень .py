# ДЛЯ ТОГО ЧТО БЫ ОПЕРАТОР РАБОТАЛ В ОБЕ СТОРОНЫ x + obj или obj + x
# В КЛАССЕ ДОЛЖНЫ БЫТЬ РЕАЛИЗОВАННЫ ОБА МЕТОДА БЕЗ ПРЕФИКСА И С ПРЕФИКСОМ r
# В КАЖДОМ МЕТОДЕ МОЖЕТ БЫТЬ АБСОЛЮТНО РАЗНАЯ ЛОГИКА
# ДЛЯ ОДИНАКОВОЙ ЛОГИКИ В МЕТОДЕ С ПРЕФЕКСОМ ВЫЗЫВАЕМ МЕТОД БЕЗПРЕФИКСА
#
# ПОСЛЕ РЕАЛИЗАЦИИ МЕТОДА СЛОЖЕНИЯ МОЖНО ИСПОЛЬЗОВАТЬ sum()

# Чтобы разрешить выполнять с экземплярами нашего класса различные арифметические операции,
# нам требуется определить в классе соответствующие магические методы:
#
# __add__() —  +
# __sub__() — -
# __mul__() — *
# __truediv__() — /
# __floordiv__() — //
# __mod__() — %
# __pow__() - **

# class PiggyBank:
#     def __init__(self, coins):
#         self.coins = coins
#
#     def __repr__(self):
#         return f'PiggyBank({self.coins})'
#
#     def __add__(self, other):
#         if isinstance(other, int):                       # проверка на тип принимаемого обьекта
#             return PiggyBank(self.coins + other)         # вернем новый экземпляр класса
#         elif isinstance(other, PiggyBank):               # проверка на тип принимаемого обьекта
#             return PiggyBank(self.coins + other.coins)   # вернем новый экземпляр класса
#         return NotImplemented                            # вернем NotImplemented  если нет реализации под данный тип
#
#
# bank1 = PiggyBank(10)
# bank2 = bank1 + 5
# bank3 = bank1 + bank2
#
# print(bank1)  # PiggyBank(10)
# print(bank2)  # PiggyBank(15)
# print(bank3)  # PiggyBank(25)


# При любой арифметической операции сначала происходит попытка вызвать основную версию магического метода
# (без префикса r) у первого операнда, и если он не определен явно или при
# его вызове была возвращена константа NotImplemented,
# происходит попытка вызова отраженной версии магического метода (с префиксом r) у второго операнда.

# Для реализации арифметических операций, не учитывающих порядок операндов,
# в Python доступен дополнительный набор магических методов с префиксом r
# ПРЕФИКС r МЕНЯЕТ МЕСТАМИ ПРИНИМАЕМЫЕ АРГУМЕНТЫ
#
# __radd__() —  +
# __rsub__() — -
# __rmul__() — *
# __rtruediv__() — /
# __rfloordiv__() — //
# __rmod__() — %
# __rpow__() - **

# class PiggyBank:
#     def __init__(self, coins):
#         self.coins = coins
#
#     def __repr__(self):
#         return f'PiggyBank({self.coins})'
#
#     def __add__(self, other):
#         return PiggyBank(self.coins + other)   # вернем новый экземпляр класса
#
#     def __radd__(self, other):                 # поменял местами (5 + bank) на  (bank + 5)
#         print('Вызов метода __radd__()')
#         return self.__add__(other)             # вызвали метод без префикса r
#
#
# bank = PiggyBank(10)
# У int нет реализации сложения с PiggyBank
# print(5 + bank)   # Вызов метода __radd__()  # PiggyBank(15)


# class SuperString:
#
#     def __init__(self, string):
#         self.string = string
#
#     def __str__(self):
#         return self.string
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self.string + other.string)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return self.__class__(self.string * other)
#         return NotImplemented
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return self.__class__(self.string[:len(self.string) // other])
#         return NotImplemented
#
#     def __lshift__(self, other):
#         if isinstance(other, int):
#             if len(self.string) <= other: return self.__class__("")
#             return self.__class__(self.string[:len(self.string) - other])
#         return NotImplemented
#
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             if len(self.string) <= other: return self.__class__("")
#             return self.__class__(self.string[other:])
#         return NotImplemented













