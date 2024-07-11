# В качестве первого аргумента мы должны указать имя класса перечисления
#
# в качестве второго — имена элементов перечисления
# может быть представлен любым итерируемым объектом,
#
# содержащим имена, или строкой, в которой имена разделены одним пробелом
#
# можем передать итерируемый объект, в котором представлены пары имя-значение dict или tuple

# По умолчанию элементы перечисления принимают последовательные целочисленные значения, начиная с 1
# поведение можно изменить, передав при создании необязательный аргумент start, который определяет начальное значение

# Задаем начальное значение
# from enum import Enum

# Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)
#
# print(repr(Weekday.MONDAY))    # <Weekday.MONDAY: 0>
# print(repr(Weekday.TUESDAY))   # <Weekday.TUESDAY: 1>
# print(repr(Weekday.WEDNESDAY)) # <Weekday.WEDNESDAY: 2>


# Передаем пары имя и значение
# from enum import Enum
#
# Size = Enum('Size', [('S', 'small'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large')])
#
# print(str(Size.S))      # Size.S
# print(repr(Size.S))     # <Size.S: 'small'>
# print(type(Size.S))     # <enum 'Size'>
# print(Size.S.name)      # S
# print(Size.S.value)     # small

