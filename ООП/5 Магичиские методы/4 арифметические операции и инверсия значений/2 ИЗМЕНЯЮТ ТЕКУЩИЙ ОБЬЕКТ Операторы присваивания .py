# Если в классе не определены магические методы с префиксом i, но определены их основные версии (без префикса i),
# то операторами составного присваивания пользоваться можно.
# Однако результатами таких арифметических операций всегда будут новые объекты.

# Неизменяемый класс всегда возвращает новый обьект во всех методах

# !!!методы, реализующие операции составного присваивания,
# должны возвращать свой результат с помощью инструкции return self.!!!
# если не указать в значение присвоется None

# происходит переприсваивание  с конкретного объекта на этот же,
# но с изменениями в атрибутах
# Поэтому id не меняется

# ЧТО БЫ += отработал с правой стороны нужно определить методЫ:
# 1) стандартный
# 2) с префиксом r
# 3) префиксом i

# Префикс i
# __iadd__() — +=
# __isub__() — -=
# __imul__() — *=
# __itruediv__() — /=
# __ifloordiv__() — //=
# __imod__() — %= определяет поведение для деления по модулю

# class PiggyBank:
#     def __init__(self, coins):
#         self.coins = coins
#
#     def __repr__(self):
#         return f'PiggyBank({self.coins})'
#
#     def __add__(self, other):
#         print('Вызов метода __add__()')
#         return PiggyBank(self.coins + other)
#
#     def __iadd__(self, other):
#         print('Вызов метода __iadd__()')
#         self.coins += other
#         return self
#
#
# bank = PiggyBank(10)
#
# bank += 10
#
# print(bank)   # Вызов метода __iadd__()  # PiggyBank(20)


# class Time:
#
#     def __sum_hours(self, other):
#         hours = ((self.hours + other.hours) % 24) + ((self.minutes + other.minutes) // 60)
#         minutes = (self.minutes + other.minutes) % 60
#         return hours, minutes
#
#     def __init__(self, hours=0, minutes=0):
#         self.hours = hours % 24 + minutes // 60
#         self.minutes = minutes % 60
#
#     def __str__(self):
#         return f'{self.hours:>02}:{self.minutes:>02}'
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(*self.__sum_hours(other))
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, self.__class__):
#             self.hours, self.minutes = self.__sum_hours(other)
#             return self
#         return NotImplemented
#
# # TEST_9:
# t1 = Time(15, 50)
# t2 = Time(2, 20)
# print(t1 + t2)
#
# t1 += Time(2, 20)
# print(t1)

